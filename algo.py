import numpy as np
from sklearn.preprocessing import StandardScaler

def input_DP(data, epsilon, delta): # delta_input << 1/n, where n is the number of instances in 

    if epsilon <= 0:
        raise ValueError("Wrong epsilon value. Epsilon should be more than zero: epsilon > 0")
    if delta <= 0:
        raise ValueError("Wrong delta value. Delta should be more than zero: delta > 0")
    
    X = np.array(data)
    n = X.shape[0]
    X = StandardScaler().fit_transform(X)
    
    loss_function = 3 * np.log(n)
    sigma = (loss_function ** 2) * (8 * np.log(2 / delta) + 4 * epsilon)/(n * epsilon ** 2)
    noise = np.random.normal(loc=0.0, scale=sigma, size=X.shape)
    noised_data = X + noise
   
    return noised_data

def input_DP_new_paradigm(data, epsilon, delta, sensitivity, iterations): # delta_input << 1/n
    
    if epsilon <= 0:
        raise ValueError("Wrong epsilon value. Epsilon should be more than zero: epsilon > 0")
    if delta <= 0:
        raise ValueError("Wrong delta value. Delta should be more than zero: delta > 0")
    
    X = np.array(data)
    n = X.shape[0]
    X = StandardScaler().fit_transform(X)
    
    loss_function = 3 * np.log(n)
    sigma = (loss_function**2) * iterations * np.log(1/delta)/(n * (n-1) * 
(epsilon**2)*np.sqrt(sensitivity))
    noise = np.random.normal(loc=0.0, scale=sigma, size=X.shape)
    noised_data = X + noise
   
    return noised_data

