import pandas as pd
from wordcloud_generator import generate_wordclouds

# let’s explore our dataset

data = pd.read_csv('training.csv', encoding='ISO-8859-1', header=None)
column_names = ['target', 'ids', 'date', 'flag', 'user', 'text']
data.columns = column_names
head = data.head()
info = data.info()
describe = data.describe()
head, info, describe

# Visualise the Dataset:
generate_wordclouds(data)