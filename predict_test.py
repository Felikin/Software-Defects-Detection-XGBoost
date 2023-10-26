#!/usr/bin/env python
# coding: utf-8

import requests


url = 'http://localhost:9696/predict'

software = {
    "loc" :33.0,
    "v(g)": 5.0,
    "ev(g)": 1.0,
    "iv(g)": 4.0,
    "n": 144.0,
    "v": 824.82,
    "l": 0.04,
    "d": 26.96,
    "i": 30.05,
    "e": 22636.74,
    "b": 0.27,
    "t": 1257.6,
    "lOCode": 30,
    "lOComment": 0,
    "lOBlank": 3,
    "locCodeAndComment": 0,
    "uniq_Op": 21.0,
    "uniq_Opnd": 23.0,
    "total_Op": 87.0,
    "total_Opnd": 57.0,
    "branchCount": 9.0
}


response = requests.post(url, json=software).json()
print(response)

if response['defects'] == True:
    print('Your software it is likely to have defects ')
else:
    print('Everything seems ok with your software')