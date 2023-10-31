# File Explanation

## Table of Files
 - [data](#data)
    - [sample_output.png](#sample_output)
    - [train.csv](#train.csv)
    - [test.csv](#test.csv)
 - [Dockerfile](#dockerfile)
 - [Pipfile](#pipfile)
 - [Pipfile.lock](#pipfile.lock)
 - [notebook.ipynb](#notebook)
 - [predict.py](#predict)
 - [predict_test.py](#predict_test)
 - [train.py](#train)
 - [xgb_model.bin](#xgb_model)

## Data
[Folder](/data) where it is saved train and test dataset, there is a sample output also.
### Sample output
[Sample output](/sample_output.png) is a screenshot of model running output.
### Train dataset
[Train](/train.csv) dataset used in the model.
### Test dataset
[Test](/test.csv) dataset if you want change model output or test different values, also used for the contest submission.

## Dockerfile
[Dockerfile](/Dockerfile) is atext document that contains all the commands a user will call on the command line to assemble the image of the project.

## Pipfile
[Pipfile](/Pipfile) contains the specification for the project top-level requirements and any desired specifiers.

## Pipfile.lock
[Pipfile.lock](/Pipfile.lock) replaces the ```requirements.txt``` file used in most Python projects

## Notebook
A [notebook](/notebook.ipynb) where EDA, parameter tunning, cross-validation and model selection was done.

## predict.py
Python [script](/predict.py) where we charge the model and implement ```Flask``` for web app service

## predict_test.py
Python [script](/predict_test.py) that you should run to test the model. see [README.md](/README.md)

## train.py
Python [script](/train.py) where choosen model was trained and saved with ```pickle```.

## xgb_model.bin
binary [file](/xgb.bin) saved by ```pickle``` in [train](/train.py) script
