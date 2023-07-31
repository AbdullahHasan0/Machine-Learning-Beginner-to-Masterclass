import pandas as pd
from matplotlib import pyplot as plt

df =pd.read_csv('HR_comma_sep.csv')
pd.crosstab(df.salary,df.left).plot(kind='bar')

