import streamlit as st
import requests
import wikipediaapi
@st.cache_data
def fetch_countries():
    response = requests.get('https://restcountries.com/v3.1/all')
    if response.status_code == 200:
        return response.json()
    else:
        st.error('Failed to fetch countries data')
        return []

countries_data = fetch_countries()

def get_exchange_rate(currency_code, target_currency="NZD"):
    url = f"https://api.exchangerate-api.com/v4/latest/{currency_code}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        # Extract exchange rate for target currency
        exchange_rate = data.get('rates', {}).get(target_currency)
        return exchange_rate
    else:
        st.error("Error fetching exchange rate")
        return None
wiki_wiki = wikipediaapi.Wikipedia('english')

