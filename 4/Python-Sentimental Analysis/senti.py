import matplotlib.pyplot as plt
import pandas as pd

twitter_data=pd.read_csv("results_olympics5.csv")
print(twitter_data.corr())

twitter_data_subjective=twitter_data[twitter_data['subjectivity']>0.5]
plt.scatter(twitter_data_subjective.retwc,twitter_data_subjective.subjectivity)
plt.show()
