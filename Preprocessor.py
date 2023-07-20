import numpy as np
import streamlit as st
import pandas as pd
from datetime import datetime


@st.cache_data
def preprocess(df):
    df = df[['Car Name', 'Year', 'Distance', 'Owner', 'Fuel', 'Location', 'Drive', 'Type', 'Price']]
    df.rename({'Car Name': 'Car_Name'}, axis=1, inplace=True)
    df.drop('Location', axis=1, inplace=True)
    df.dropna(inplace=True)
    df['Year'] = pd.to_datetime(df['Year'], format='%Y', errors='coerce')
    df['Year'] = df['Year'].dt.strftime('%Y')

    return df
