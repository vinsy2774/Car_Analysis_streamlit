import pandas as pd
import streamlit as st
from PIL import Image
import Preprocessor
import helper

df = pd.read_csv('cars_24_combined.csv')
df = Preprocessor.preprocess(df)


st.sidebar.subheader('Used Cars Analysis')
user_menu = st.sidebar.radio(
    'Select an Option',
    ('Home', 'Overall Analysis', 'Fuel wise Analysis', 'Prices Wise Analysis', 'Distance wise analysis')
)

if user_menu == 'Home':
    st.title('Analysis of Used Cars')
    st.header('Welcome to my :red[**CAR**] Analysis Application')

    image = Image.open('Used_cars.png')
    st.image(image, width=300)

    st.divider()

    st.markdown("Here is Some information about used cars in India")
    st.markdown('''> As of 19 Jul 2023, there are over 102206 second-hand cars available for purchase in India, with popular 
                brands such as Maruti Suzuki, Hyundai, Mahindra, Honda, Tata, Toyota, and Ford.''')
    st.markdown('''> Popular cities to buy a second-hand car in India include Mumbai, Bangalore, Delhi, Pune, Navi Mumbai,
                Hyderabad, Ahmedabad, Chennai, and Kolkata.''')

    st.divider()
    st.write('Basic Overview of Used Cars')
    st.markdown(df.head(20).style.hide(axis="index").to_html(), unsafe_allow_html=True)


if user_menu == 'Overall Analysis':
    st.header('Overall Analysis')

    st.subheader('Top :red[5] Highest Priced Cars')
    top_priced_cars = helper.show_top_cars(df)
    st.markdown(top_priced_cars.style.hide(axis="index").to_html(), unsafe_allow_html=True)

    st.divider()
    st.subheader('Top :red[5] Lowest Priced Cars')
    bottom_priced_cars = helper.show_bottom_cars(df)
    st.markdown(bottom_priced_cars.style.hide(axis="index").to_html(), unsafe_allow_html=True)

    st.divider()
    st.subheader('Cars over Fuel type')
    cars_fuel = helper.total_cars_over_car_type(df, 'Fuel')
    st.bar_chart(cars_fuel)

    st.divider()
    st.subheader('Cars over Drive type')
    drive_type = helper.total_cars_over_drive_type(df, 'Drive')
    st.bar_chart(drive_type)

    st.divider()
    st.subheader('Cars over car type')
    car_type = helper.total_cars_over_car_type(df, 'Type')
    st.bar_chart(car_type)

    st.divider()
    st.subheader('Cars over Owner type')
    owner_type = helper.total_cars_over_owner_type(df, 'Owner')
    st.bar_chart(owner_type)

if user_menu == 'Fuel wise Analysis':
    st.header('Fuel wise Analysis')
    type_fuel = helper.fuel_type_bar(df)
    selected_fuel = st.selectbox('Choose the fuel type', type_fuel)
    res = helper.fetch_fuel_data(df, selected_fuel)
    st.dataframe(res)


