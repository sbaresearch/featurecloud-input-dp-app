from FeatureCloud.app.engine.app import AppState, app_state
import bios
import pandas as pd
import algo

INPUT_DIR = 'mnt/input'
OUTPUT_DIR = 'mnt/output'

INITIAL_STATE = 'initial'
WRITE_STATE = 'write'
TERMINAL_STATE = 'terminal'
# FeatureCloud requires that apps define the at least the 'initial' state.
# This state is executed after the app instance is started.

@app_state(INITIAL_STATE)
class InitialState(AppState):

    def register(self):
        self.register_transition(WRITE_STATE)  
        
    def run(self):
        self.log('Update')
        self.log('Reding config file')
        config = bios.read(f'{INPUT_DIR}/config.yml')
        config = config["fc_input_dp"]
        input_file = config['data']
        target_attribute = config['target_attribute']
        input_dp_method = config['input_dp_method']
        epsilon = config['epsilon']
        delta = config['delta']
        noised_data_file = config['noised_data']
        
        self.store('noised_data_file', noised_data_file)
        
        self.log(f'Reading data ...') 
        self.log(f'data file: {INPUT_DIR}/{input_file}')
        df = pd.read_csv(f'{INPUT_DIR}/{input_file}')
        if target_attribute!='':
            X = df.drop(target_attribute, axis=1) #drop the target label
        else:
            X = df
        self.store('dataframe', X)
        self.log(f'data size:{X.shape}')

        if input_dp_method == 'input_dp':
            noised_data = algo.input_DP(X, epsilon, delta)
            self.log(f'Method input_dp, noised data size :{noised_data.shape}')
            self.store('noised_data', noised_data)
        elif input_dp_method == 'input_dp_new_paradigm':
            sensitivity = config['sensitivity']
            iterations = config['iterations']
            noised_data = algo.input_DP_new_paradigm(X, epsilon, delta, sensitivity, iterations)
            self.log(f'Method input_dp_new_paradigm, noised data size  :{noised_data.shape}')
            self.store('noised_data', noised_data)
        else:
            raise ValueError("Wrong input_dp_method in config.yml, possible values:[input_dp, input_dp_new_paradigm]")
        
        return WRITE_STATE
                

@app_state(WRITE_STATE)
class WriteState(AppState):

    def register(self):
        self.register_transition(TERMINAL_STATE)  
        
    def run(self):
        self.log('Writing noised data...')
        noised_data = self.load('noised_data')
        df = self.load('dataframe')
        noised_df = pd.DataFrame(noised_data)
        noised_df.columns = list(df.columns)
        noised_df.to_csv(f'{OUTPUT_DIR}/noised_data_file')

        return TERMINAL_STATE
        