import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm 
youtube_data=pd.read_csv('federer.csv')

plt.figure()

print(youtube_data.corr())

y=youtube_data.likeCount
X=youtube_data.viewCount
X=sm.add_constant(X)
lr_model=sm.OLS(y,X).fit()

print(lr_model.summary())
