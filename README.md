# purple-air-analysis
A Quest project.

The purpose of this project was to determine microclimates around the Bay Area during major pollution events by analyzing air pollution data from 8/1/20 to 9/30/20. However, the programs and data sets created as a result of this project have far greater utility. 

# Things in this repo:
1. csvingest.py
 - Takes the raw data from purpleair.com and converts it to one CVS file that measures PM2.5 over time for each sensor (represented as coordinates). Missing datapoints have been given the meausurement '0.0'. T1, T2, T3, ..., etc. represent 30 minute time intervals.  
2. final_data_set.zip
 - The raw data downloaded from Purple Air. For each sensor, there is a primary and secondary dataset, which both record seperate measurements taken every 30 minutes. There are ~6700 csv files in this zip file. 
3. finaldataset2.csv
 - The final and most refined csv file that records pollution over time. Sensors that did not record during the pollution event have been removed. 
4. Screenshot of microclimates around the Bay Area
 - Each different cluster represents a distinguishable microclimate around the Bay Area. This map also represents the approximate location of the sensors I downloaded. 

# IMPORTANT!
I could not add the raw data file to github as the file size was too large. Please use this Google Drive link to access the dataset: https://drive.google.com/file/d/1lvv8bY8fTSJU4d0SmUthNGDCWW3AtLT1/view?usp=sharing
