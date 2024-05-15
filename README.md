# Protein Function Prediction
**TODO** Intoduction

## Data
The repository doesn't collect any new dataset. Instead, we have decided to leverage the already existing one, which can be found in Kaggle's CAFA 5 [Protein Function Prediction](https://www.kaggle.com/competitions/cafa-5-protein-function-prediction/data) competition. 
We have preprocessed by embedding the protein sequences and converted them to csv files, which we uploaded on a huggingface [repository](https://huggingface.co/datasets/nikolayvV/protein-function-prediction-preprocessed/tree/main/Train). This repository contains different csv files so we could easily load it as pandas dataframe and use it for different purposes:
- the whole data, which we can use to analyse our data, visualize it and get additional information about it
- features, which go into the model for training and testing
- labels, which are also prepared to go into the model for training

## Models

## Authors
- Žan Pižmoht
- Nikolay Vasilev
