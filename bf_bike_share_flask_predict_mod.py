#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  5 13:43:42 2020

@author: hduser
"""

import requests, json

# url = '[http://localhost:8000/makecalc/](http://localhost:8000/makecalc/)'

url = 'http://localhost:8000/makecalc/' 

# =============================================================================

text = json.dumps(
    
    
    {"0":{
    
    "ANALYSIS_DATE":   "01/09/19",
    "TM":               9.367,                     
    "AM":               1.5,
    "VOLTMAT":          25.297,
    "VOLTMATDRY":       25.682,
    "ASHCONFNL":        21.901,
    "ASHCONADRY":       10.207,
    "ASHCONDRY":        10.362,
    "BFASHCNADR":       14.293,
    "BFASHCNDRY":       14.366,
    "BFFXCAADRY":       84.56,
    "BFFXCARDRY":       84.991,
    "ST_FEO":           9.396,
    "ST_AL2O3":         2.187,
    "ST_AL2O3_BY_SIO":  0.388,
    "ST_CAO_SIO2":      3.38,
    "CARBON":           4.305,
    "MN":               0.054,
    "PHOSPORUS":        0.091,
    "TI":               0.056,
    "AL2O3":            17.885,
    "CB_FLOW":          310152,
    "O2_PRESS":         3.87,
    "O2_FLOW":          18005,
    "O2_PER":           26.5,  
    "PCI":              68,
    "CB_TEMP":          131,
    "ATM_HUMID":        24,
    "HB_TEMP":          1098,
    "HB_PRESS":         3.65,
    "TOP_TEMP1":        150,
    "TOP_TEMP2":        146,
    "TOP_TEMP3":        146,
    "TOP_TEMP4":        160,
    "TOP_PRESS":        2,
    "STP":              8703,
    "ORE":              2437,
    "TOT_FE":           11140,
    "LIME":             376,
    "TOT_FLUX":         395,
    "COKE_PROC":        2582,   
    "NUT":              122,
    "TOT_FUEL":         2704 
    },
    
   "1":{
    
    "ANALYSIS_DATE":   "10/09/19",
    "TM":               9.933,                     
    "AM":               1.513,
    "VOLTMAT":          25.277,
    "VOLTMATDRY":       25.665,
    "ASHCONFNL":        20.192,
    "ASHCONADRY":       10.593,
    "ASHCONDRY":        10.756,
    "BFASHCNADR":       14.57,
    "BFASHCNDRY":       14.643,
    "BFFXCAADRY":       84.313,
    "BFFXCARDRY":       84.737,
    "ST_FEO":           9.268,
    "ST_AL2O3":         1.422,
    "ST_AL2O3_BY_SIO":  0.252,
    "ST_CAO_SIO2":      4.123,
    "CARBON":           4.286,
    "MN":               0.07,
    "PHOSPORUS":        0.097,
    "TI":               0.037,
    "AL2O3":            16.114,
    "CB_FLOW":          305208,
    "O2_PRESS":         3.79,
    "O2_FLOW":          21278,
    "O2_PER":           27.61,  
    "PCI":              64,
    "CB_TEMP":          124,
    "ATM_HUMID":        25.3,
    "HB_TEMP":          1108,
    "HB_PRESS":         3.57,
    "TOP_TEMP1":        170,
    "TOP_TEMP2":        179,
    "TOP_TEMP3":        181,
    "TOP_TEMP4":        187,
    "TOP_PRESS":        1.9,
    "STP":              7790,
    "ORE":              2679,
    "TOT_FE":           10469,
    "LIME":             351,
    "TOT_FLUX":         351,
    "COKE_PROC":        2552,   
    "NUT":              118,
    "TOT_FUEL":         2670
    },
    
    
    "2":{
    
    "ANALYSIS_DATE":   "24/09/19",
    "TM":               9.867,                     
    "AM":               1.503,
    "VOLTMAT":          25.233,
    "VOLTMATDRY":       25.618,
    "ASHCONFNL":        21.056,
    "ASHCONADRY":       10.413,
    "ASHCONDRY":        10.573,
    "BFASHCNADR":       14.357,
    "BFASHCNDRY":       14.429,
    "BFFXCAADRY":       84.533,
    "BFFXCARDRY":       84.958,
    "ST_FEO":           9.193,
    "ST_AL2O3":         1.705,
    "ST_AL2O3_BY_SIO":  0.335,
    "ST_CAO_SIO2":      3.984,
    "CARBON":           4.194,
    "MN":               0.115,
    "PHOSPORUS":        0.124,
    "TI":               0.078,
    "AL2O3":            16.262,
    "CB_FLOW":          306832,
    "O2_PRESS":         3.84,
    "O2_FLOW":          15647,
    "O2_PER":           25.86,  
    "PCI":              52,
    "CB_TEMP":          128,
    "ATM_HUMID":        24.4,
    "HB_TEMP":          1071,
    "HB_PRESS":         3.63,
    "TOP_TEMP1":        159,
    "TOP_TEMP2":        156,
    "TOP_TEMP3":        160,
    "TOP_TEMP4":        180,
    "TOP_PRESS":        2,
    "STP":              7363,
    "ORE":              3420,
    "TOT_FE":           10783,
    "LIME":             0,
    "TOT_FLUX":         31,
    "COKE_PROC":        2454,   
    "NUT":              144,
    "TOT_FUEL":         2599 
    }
    
    
        
        
           
        
        
        
        
    
    
    
    
    
    })

headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
r = requests.post(url, data=text, headers=headers)
print('\nPredicted Values for SI in BF Hot Metal are:')
print('\n')

print(r,r.text)

