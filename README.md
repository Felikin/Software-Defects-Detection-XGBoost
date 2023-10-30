# Midterm Project for Zoomcamp Machine Learning Course

This repository contains the code and materials for the midterm project of the Zoomcamp Machine Learning course. The project focuses on predict defects in C programs given various attributes about the code.

## Table of Contents

- [Project Description](#project-description)
- [Dataset](#dataset)
- [Dependencies](#dependencies)
- [Installation](#installation)
- [Usage](#usage)
- [Sample Output](#sampleoutput)

## Project Description

In this project, I have worked on a Kaggle binary classification contest from the [2023 edition of Kaggle's Playground Series](https://www.kaggle.com/competitions/playground-series-s3e23/overview). The main goal is predict defects in C programs given various attributes about the code.

## Dataset

### Find
Data is available in the /data folder, you can find it in the [contest url](https://www.kaggle.com/competitions/playground-series-s3e23/overview) also.

### Data Explanation
Data comes from McCabe and Halstead features extractors of
source code.  These features were defined in the 70s in an attempt to objectively characterize code features that are associated with software quality.  The nature of association is under dispute. Datasets are synthetically generated from real-world data

- Number of attributes: 22 (5 different lines of code measure, 
- 3 McCabe metrics, 4 base Halstead measures, 8 derived Halstead measures, a branch-count, and 1 goal field)

### Attribute Information
- 1. loc             : numeric - McCabe's line count of code
- 2. v(g)            : numeric - McCabe "cyclomatic complexity"
- 3. ev(g)           : numeric - McCabe "essential complexity"
- 4. iv(g)           : numeric - McCabe "design complexity"
- 5. n               : numeric - Halstead total operators + operands
- 6. v               : numeric - Halstead "volume"
- 7. l               : numeric - Halstead "program length"
- 8. d               : numeric - Halstead "difficulty"
- 9. i               : numeric - Halstead "intelligence"
- 10. e               : numeric - Halstead "effort"
- 11. b               : numeric - Halstead 
- 12. t               : numeric - Halstead's time estimator
- 13. lOCode          : numeric - Halstead's line count
- 14. lOComment       : numeric - Halstead's count of lines of comments
- 15. lOBlank         : numeric - Halstead's count of blank lines
- 16. lOCodeAndComment: numeric
- 17. uniq_Op         : numeric - unique operators
- 18. uniq_Opnd       : numeric - unique operands
- 19. total_Op        : numeric - total operators
- 20. total_Opnd      : numeric - total operands
- 21: branchCount     : numeric - of the flow graph
- 22. defects         : {false,true} - module has/has not one or more reported defects

## Dependencies

Pipfile.lock has listed all the dependencies and libraries used in this project. Here are some of the python libraries used.
- Python 3.9+
- NumPy
- Pandas
- Scikit-Learn
- XGBoost

## Installation
First of all clone this repo 
```
git clone https://github.com/Felikin/midterm-ML-zoomcamp.git
```
### Run with Docker
Once you have cloned the repo, you need to have Docker installed on your machine and just build and run the docker image.

To build the image run
```
docker build -t {build-tag} .
```
`{build-tag}`: Specifies any user-defined tag for docker image. eg. `project-test`

## Usage

To run the image run
```
docker run -it --rm -p 9696:9696 {build-tag}
```
then in another terminal run python ```python predict-test.py```. If you want to use other data you can find it in at ```"data/test.csv"``` file and replace the values of the attributes.

## Sample Output
![Sample of the project running locally](/data/sample_output.png)
