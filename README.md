# Input DP

Differential Privacy through input perturbation

## Description

Input DP app can be applied to mitigate risks of identity and membership disclosure from the data, as well as to protect local and global models in federated learning from inference attacks. Depending on the parameters like `epsilon` and `delta`, Input DP can result in central or local Differential Privacy. 

Input DP is applied individually by each client as a data-preprocessing step to prepare data for training models. 

This app contains two methods for achieving input DP:

1. **'input_dp'**: the method based on [1]. Use for achieving local differential privacy (stronger privacy, but more utility loss)
2. **input_dp_new_paradigm**: the method based on [2]. Use to achieve central differential privacy after federated learning (weaker privacy, less utility loss). Central DP results in a differentially private global model

Choose `delta` << 1/n, where n is the size of the dataset

The closer `epsilon` to 0, the higher the privacy of the noised_data

Too high values for `epsilon` and `delta` can result in gaining no meaningful privacy!

`sensitivity` and `iterations` parameters have to be specified only for the method  **input_dp_new_paradigm**

## Input

* **data.csv** containing the original dataset

Data to test the app is provided in the current repo **data/sample_data**

## Output

* **noised_data.csv** cointaining noised data produced by using differential privacy through input perturbation

## Workflows

* Pre: various pre-processing apps
* Post: various Analysis apps

## Config
```
fc_input_dp:
    data: data.csv                  # path to the input file 
    noised_data: noised_data.csv    # path to the output file
    target_attribute: label         # name of the target attribute or an empty string

    input_dp_method: input_dp       # one of two methods:  input_dp or input_dp_new_paradigm
    epsilon: epsilon                # float, has to be more than 0
    delta: delta                    # float, has to be more than 0 and less than 1

    sensitivity: sensitivity        # float, has to be more than 0. Sensitivity of the ML model used only with input_dp_new_paradigm
    iterations: iterations          # int, has to be more than 0. Number of iterations
                                    # when training ML model, used only with input_dp_new_paradigm
```

## References

[1] Fukuchi, K., Tran, Q.K., Sakuma, J. (2017).  Differentially Private  Empirical Risk Minimization with Input Perturbation.                       In: Yamamoto, A., Kida, T., Uno, T., Kuboyama, T.  (eds) Discovery Science. DS 2017. Lecture Notes in Computer Science(),  vol 10558. Springer, Cham. https://doi.org/10.1007/978-3-319-67786-6\_6

[2] Kang,  Yilin, Yong Liu, Ben Niu, Xin-Yi Tong, Likun Zhang and Weiping Wang.  “Input Perturbation: A New Paradigm between Central and Local  Differential Privacy.” *ArXiv* abs/2002.08570 (2020): n. pag.

