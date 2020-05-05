import numpy as np

import pandas as pd

from datetime import date

def doTheCalculation(data):

	data['dayofyear']=(data['ANALYSIS_DATE']-

    	data['ANALYSIS_DATE'].apply(lambda x: date(x.year,1,1))

    	.astype('datetime64[ns]')).apply(lambda x: x.days)

	X = np.array(data[['TM','AM','VOLTMAT','VOLTMATDRY','ASHCONFNL','ASHCONADRY','ASHCONDRY',
                    'BFASHCNADR','BFASHCNDRY','BFFXCAADRY','BFFXCARDRY','ST_FEO','ST_AL2O3', 
                    'ST_AL2O3_BY_SIO','ST_CAO_SIO2','CARBON', 'MN','PHOSPORUS','TI','AL2O3',
                    'CB_FLOW','O2_PRESS', 'O2_FLOW','O2_PER','PCI','CB_TEMP','ATM_HUMID',
                    'HB_TEMP','HB_PRESS','TOP_TEMP1','TOP_TEMP2','TOP_TEMP3','TOP_TEMP4',
                    'TOP_PRESS','STP','ORE','TOT_FE','LIME','TOT_FLUX','COKE_PROC','NUT','TOT_FUEL'
                    
                    ]])

	return X
