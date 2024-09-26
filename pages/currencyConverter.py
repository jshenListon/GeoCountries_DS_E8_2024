import streamlit as st
import requests
from constant import fetch_countries, countries_data, get_exchange_rate
import pydeck as pdk
from mainHub import selected_country, country_names

import requests
import streamlit as st
import pandas as pd
import numpy as np

st.header("Currency Converter App")
st.write("The purpose of this app is to measure the exchange rate between two selected countries")
col1,col2 = st.columns(2)
with col1:
    selected_country_1 = st.selectbox('Select the first country:', sorted(country_names))
with col2:
    selected_country_2 = st.selectbox('Select the second country:', sorted(country_names))

# Display selected country's details
def display_country_details(country_name):
    for country in countries_data:
        if country.get('name', {}).get('common') == country_name:
            st.subheader(f"Details for the currency of {country_name}")
            st.image(country.get('flags', {}).get('png'), width=200)
            currencies = country.get('currencies', {})
            currencies_formatted = ', '.join([f"{v.get('name')} ({k})" for k, v in currencies.items()])
            st.write(f"**Currencies:** {currencies_formatted}")
            return list(currencies.keys())[0] if currencies else None
        
        # Extract the first currency code for conversion
col3,col4 = st.columns(2)
with col3:
    currency_code_1 = display_country_details(selected_country_1)

# Display details for the second country
with col4:
    currency_code_2 = display_country_details(selected_country_2)

# Check if both countries have valid currencies
if currency_code_1 and currency_code_2:
    # Get the exchange rate between the two currencies
    exchange_rate = get_exchange_rate(currency_code_1, currency_code_2)
    
    if exchange_rate:
        st.write(f"**Exchange rate:** 1 {currency_code_1} = {exchange_rate} {currency_code_2}")
    
#Input for user to enter any amount of selected currency into the converter
    amount = st.number_input(f"Amount in {currency_code_1}:", min_value=0.0, step=0.01)
    converted_amount = amount * exchange_rate
    st.write(f"{amount} {currency_code_1} is equal to {converted_amount} {currency_code_2}")
else:
    st.write("Could not fetch currencies for one or both of the selected countries.")