#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  5 13:37:06 2020

@author: hduser
"""
import numpy as np

import pandas as pd

from datetime import date

from flask import Flask, request, redirect, url_for, flash, jsonify

from bf_bike_features_calculation import doTheCalculation

import json, pickle


app = Flask(__name__)

@app.route('/makecalc/', methods=['POST'])
def makecalc():
    """
     Function run at each API call
    """
    jsonfile = request.get_json()

    data = pd.read_json(json.dumps(jsonfile),orient='index',convert_dates=['ANALYSIS_DATE'])

    print(data)

    res = dict()

    ypred = model.predict(doTheCalculation(data))

    for i in range(len(ypred)):

        res[i] = ypred[i] 

    return jsonify(res) 

if __name__ == '__main__':

    modelfile = '/home/hduser/Desktop/BF_Tuyeres_ML_Project/models_saved_dir/bf_bike-sharing.pickle'

    model = pickle.load(open(modelfile, 'rb'))

    print("BF SI Pickle Model is Loaded: OK")

def main():
    """Run the app."""
    app.run(host='0.0.0.0', port=8000, debug=True)  # nosec

if __name__ == '__main__':
    main()


