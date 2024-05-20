import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

@st.cache()
def load_data():
	# Load the Adult Income dataset into DataFrame.

	df = pd.read_csv('https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/whitehat-ds-datasets/adult.csv', header=None)
	df.head()

	# Rename the column names in the DataFrame using the list given above. 

	# Create the list
	column_name =['age', 'workclass', 'fnlwgt', 'education', 'education-years', 'marital-status', 'occupation', 'relationship', 'race','gender','capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'income']

	# Rename the columns using 'rename()'
	for i in range(df.shape[1]):
	  df.rename(columns={i:column_name[i]},inplace=True)

	# Print the first five rows of the DataFrame
	df.head()

	# Replace the invalid values ' ?' with 'np.nan'.

	df['native-country'] = df['native-country'].replace(' ?',np.nan)
	df['workclass'] = df['workclass'].replace(' ?',np.nan)
	df['occupation'] = df['occupation'].replace(' ?',np.nan)

	# Delete the rows with invalid values and the column not required 

	# Delete the rows with the 'dropna()' function
	df.dropna(inplace=True)

	# Delete the column with the 'drop()' function
	df.drop(columns='fnlwgt',axis=1,inplace=True)

	return df

census_df = load_data()

st.set_option('deprecation.showPyplotGlobalUse', False)

st.header('Census Data Visualisation Web App')
st.sidebar.header('Census Data Visualisation Web App')
# Using the 'if' statement, display raw data on the click of the checkbox.
if st.sidebar.checkbox("Show raw data"):
  st.subheader("Census Dataset")
  st.dataframe(census_df)

st.sidebar.subheader("Visualisation Selector")
plot_list = st.sidebar.multiselect('Select the charts/plot:', ('Income Group Distribution', 'Gender Distribution', 'Hours/Week by Income', 'Hours/Week by Gender', 'Work Class by Income'))

# Display pie plot using matplotlib module and 'st.pyplot()'
if "Income Group Distribution" in plot_list:
  st.subheader('Income Group Distribution')
  data = census_df['income'].value_counts()
  plt.figure(figsize=(20, 5))
  plt.pie(data, labels=data.index, autopct='%1.2f%%')
  st.pyplot()

if "Gender Distribution" in plot_list:
  st.subheader('Gender Distribution')
  data = census_df['gender'].value_counts()
  plt.figure(figsize=(20, 5))
  plt.pie(data, labels=data.index, autopct='%1.2f%%')
  st.pyplot()

# Display box plot using matplotlib module and 'st.pyplot()'
if "Hours/Week by Income" in plot_list:
  st.subheader('Hours/Week by Income')
  plt.figure(figsize=(20, 10))
  sns.boxplot(census_df['hours-per-week'], census_df['income'])
  st.pyplot()

if "Hours/Week by Gender" in plot_list:
  st.subheader('Hours/Week by Income')
  plt.figure(figsize=(20, 10))
  sns.boxplot(census_df['hours-per-week'], census_df['gender'])
  st.pyplot()

# Display count plot using seaborn module and 'st.pyplot()' 
if 'Work Class by Income' in plot_list:
  st.subheader('Work Class by Income')
  plt.figure(figsize=(20, 10))
  sns.countplot(census_df['workclass'], hue=census_df['income'])
  st.pyplot()