#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  5 13:24:56 2020

@author: hduser
"""

import pandas as pd
import numpy as np
from datetime import date
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import pickle


## Convert Analysis_Date into YYYYMMDD (YMD) format in excel

data = pd.read_csv('aiml_bf_application_model_act_dataset1_mod3.csv', parse_dates=['ANALYSIS_DATE'])

data.head()
data.info()

# data['dayofyear']=(data['dteday']-data['dteday'].apply(lambda x: date(x.year,1,1)).astype('datetime64[ns]')).apply(lambda x: x.days)

offset = int(len(data)*0.8)

X = np.array(data.drop(['ANALYSIS_DATE','SI'],axis=1))
Y = np.array(data['SI'])

X_train, X_test = X[:offset], X[offset:]
Y_train, Y_test = Y[:offset], Y[offset:]

RF = RandomForestRegressor()

RF.fit(X_train,Y_train)

print('\nMean Squared Error:')

print(mean_squared_error(Y_test,RF.predict(X_test)))

print('\nMean Squared Error:Median')

print(mean_squared_error(Y_test,np.median(Y_train)*np.ones(len(Y_test))))

print('\nCheck predictions with ground truth:')

np.vstack((RF.predict(X_test),Y_test)).T

print('\nTest Set Expected Distribution:')

pd.DataFrame(Y_test).plot(kind='hist',bins=20)

print('\nTest Set Predicted Distribution:')

pd.DataFrame(RF.predict(X_test)).plot(kind='hist',bins=20)

print('\nTest Set Error Distribution:')

pd.DataFrame(Y_test-RF.predict(X_test)).plot(kind='hist',bins=20)

print('\nDump ML Model to a pickle object:')

with open("bf_bike-sharing.pickle", 'wb') as handle:
    pickle.dump(RF, handle, protocol=pickle.HIGHEST_PROTOCOL)


print('\nBF-SI Dataset Used: /home/hduser/Desktop/BF_Tuyeres_ML_Project/Datasets/aiml_bf_application_model_act_dataset1_mod3.csv')

print('\nSaved bf_bike-sharing.pickle model successfully to location: /home/hduser/Desktop/BF_Tuyeres_ML_Project/models_saved_dir/bf_bike-sharing.pickle')
