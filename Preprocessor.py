import numpy as np
import streamlit as st


@st.cache_data
def preprocess(df):
    df = df[['Car Name', 'Year', 'Distance', 'Owner', 'Fuel', 'Location', 'Drive', 'Type', 'Price']]
    df.rename({'Car Name': 'Car_Name'}, axis=1, inplace=True)
    df.drop('Location', axis=1, inplace=True)
    df.dropna(inplace=True)
    df['Year'] = df['Year'].astype(np.int64)


    return df
