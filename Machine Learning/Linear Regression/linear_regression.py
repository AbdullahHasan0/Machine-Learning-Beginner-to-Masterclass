import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

df = pd.read_csv("canada_per_capita_income.csv")

df_year = df

model = linear_model.LinearRegression()
print(model)