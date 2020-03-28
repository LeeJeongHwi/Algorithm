# Import pandas as a alias 'pd'
import pandas as pd

# Load the CSV files "marathon_qualifying_time.csv" under "data" folder
marathon_qualifying_time = pd.read_csv("./data/marathon_qualifying_time.csv")

# Drop unnecessary columns 
qualifying_time = pd.DataFrame(marathon_qualifying_time,columns=['F',  'M'])
# Import Numpy Library and call it as np
import numpy as np

# Convert using pandas to_timedelta method
qualifying_time['F'] = pd.to_timedelta(qualifying_time['F'])
qualifying_time['M'] = pd.to_timedelta(qualifying_time['M'])

# Convert time to seconds value using astype method
qualifying_time['F'] = qualifying_time['F'].astype('m8[s]').astype(np.int64)
qualifying_time['M'] = qualifying_time['M'].astype('m8[s]').astype(np.int64)

# Load the CSV
# files "marathon_results_2015 ~ 2017.csv" under "data" folder
marathon_2015_2017 = pd._______("./data/marathon_2015_2017.csv")
marathon_2015_2017['M/F'] = marathon_2015_2017['M/F'].map({'M': 1, ___: _})

# Add qualifying column with fixed string 2017
qualifying_time_list = qualifying_time.values.tolist()
# Define function name to_seconds
marathon_2015_2017_qualifying = pd.DataFrame(columns=['M/F',  'Age',  'Pace',  'Official Time', 'Year', 'qualifying'])
for index, record in marathon_2015_2017.__________:
    qualifying_standard = qualifying_time_list[record.Age-__][record['M/F']]
    qualifying_status = 1
    if (record['Official Time'] > ______________): 
        qualifying_status = 0
    marathon_2015_2017_qualifying = marathon_2015_2017_qualifying.append({'M/F' : record['M/F'],
                                                                          'Age' : record['Age'],
                                                                          'Pace' : record['Pace'],
                                                                          'Official Time' : record['Official Time'],
                                                                          'Year' : record['Year'],
                                                                          'qualifying' : _____________
                                                                          },
                                                                        ignore_index=True)
# Save to CSV file "marathon_2015_2017.csv"
marathon_2015_2017_qualifying.______("./data/marathon_2015_2017_qualifying.csv", index = None, header=True)
