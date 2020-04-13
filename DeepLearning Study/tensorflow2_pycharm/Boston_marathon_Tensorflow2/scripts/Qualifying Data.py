import pandas as pd
import numpy as np

marathon_qualifying_time = pd.read_csv('../source/marathon_qualifying.csv')

qualifying_time = pd.DataFrame(marathon_qualifying_time,columns =['F','M'])

qualifying_time['F'] = pd.to_timedelta(qualifying_time['F'])
qualifying_time['M'] = pd.to_timedelta(qualifying_time['M'])

qualifying_time['F'] = qualifying_time['F'].astype('m8[s]').astype(np.int64)
qualifying_time['M'] = qualifying_time['M'].astype('m8[s]').astype(np.int64)

marathon_2015_2017 = pd.read_csv('../source/marathon_2015_2017.csv')
marathon_2015_2017['M/F'] = marathon_2015_2017['M/F'].map({'M':1,'F':0})

qualifying_time_list = qualifying_time.values.tolist()
marathon_2015_2017_qualifying = pd.DataFrame(columns=['M/F','Age','Pace','Official Time','Year','qualifying'])
for index, record in marathon_2015_2017.iterrows():
    qualifying_standard = qualifying_time_list[record.Age-18][record['M/F']]
    qualifying_status = 1
    if record['Official Time'] > qualifying_standard:
        qualifying_status = 0
    marathon_2015_2017_qualifying = marathon_2015_2017_qualifying.append({'M/F':record['M/F'],
                                                                          "Age":record['Age'],
                                                                          'Pace':record['Pace'],
                                                                          'Official Time':record['Official Time'],
                                                                          'Year':record['Year'],
                                                                          'qualifying':qualifying_status},
                                                                         ignore_index=True)
marathon_2015_2017_qualifying.to_csv('../source/marathon_2015_2017_qualifying.csv',index=None,header=True)