# Protein Function Prediction
This study investigates the use of neural networks for predicting protein functions from amino acid sequences, as part of the CAFA5 competition. We utilized [encoder only ProtT5-XL-UniRef50, half-precision model](https://huggingface.co/Rostlab/prot_t5_xl_half_uniref50-enc) to embed protein sequences into dense vectors, creating a robust dataset for training. Two neural network architectures were developed: a single aspect model and a multiple aspect model.

## Data
The repository doesn't collect any new dataset. Instead, we have decided to leverage the already existing one, which can be found in Kaggle's CAFA 5 [Protein Function Prediction](https://www.kaggle.com/competitions/cafa-5-protein-function-prediction/data) competition. 
We have preprocessed by embedding the protein sequences and converted them to csv files, which we uploaded on a huggingface [repository](https://huggingface.co/datasets/nikolayvV/protein-function-prediction-preprocessed). This repository contains different csv files so we could easily load it as pandas dataframe and use it for different purposes:
- the whole data, which we can use to analyse our data, visualize it and get additional information about it
- features, which go into the model for training and testing
- labels, which are also prepared to go into the model for training

## Models

We train 2 different models. They both have similar architectures, but the first model is trained on all 1500 GO terms and doesn’t consider the subontologies. The second model on the other hand is a combination of 3 submodels - one for each of the subontologies (Molecular Function, Biological Process, and Cellular Component). The models can be accessed on [huggingface](https://huggingface.co/nikolayvV/protein_function_prediction).

### Model Evaluation

#### Training and Validation Scores

We used Cross-Entropy and Accuracy to evaluate both models. The results on the training and validation sets of the single aspect model are shown in the following table:

|     Data      |     Loss    | Accuracy |
| ------------- | ----------- | -------- |
| Training      | 0.0821      | 97.87 %  |
| Validation    | 0.0628      | 98.49 %  |

The results on the training and validation sets of the multi aspect model are shown in the following table:

|       Data       |     Loss    | Accuracy |
| ---------------- | ----------- | -------- |
| Training BP      | 0.0784      | 98.11 %  |
| Validation BP    | 0.0611      | 98.67 %  |
| Training CC      | 0.1040      | 96.63 %  |
| Validation CC    | 0.0851      | 97.29 %  |
| Training MF      | 0.0775      | 97.95 %  |
| Validation MF    | 0.0483      | 98.83 %  |
| Training Multi   | 0.0866      | 97.56 %  |
| Validation Multi | 0.0648      | 98.26 %  |

#### Test Scores

We submitted the predictions on the test data from both models to Kaggle (maximum score 0.5 in leaderboard) in order to get the test scores in the following table:

|     Model     |    Score    |
| ------------- | ----------- |
| Single Aspect | 0.30124     |
| Mutli Aspect  | 0.30043     |

## Authors
- Žan Pižmoht
- Nikolay Vasilev
