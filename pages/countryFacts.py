import streamlit as st
import requests
from constant import fetch_countries, countries_data, wiki_wiki
import pydeck as pdk
from mainHub import selected_country, country_names
import streamlit as st
import requests
import wikipediaapi

st.header("Cultural Info App")

# Select country
selected_country = st.selectbox('Select your country:', sorted(country_names))#Selectbox for user to select country
for country in countries_data:#For loop of country to be selected in the country dataset
    if country.get('name', {}).get('common') == selected_country:#Variable for what the selected country is
        st.subheader(f"Details for {selected_country}")
        col1, col2 = st.columns(2)#Divides the for loop into 2 columns
        with (col1):
            st.image(country.get('flags', {}).get('png'), width=200)
            st.write(f"**Official Name:** {country.get('name', {}).get('official', 'N/A')}")

# Function to fetch Wikipedia article on selected country using data from constant.py
def get_wikipedia_summary_short(country_name):
    page = wiki_wiki.page(country_name)#finds wikipedia page of the country based on it's name
    if page.exists():
        sentences = page.summary.split('. ')
        short_summary = '. '.join(sentences[:4]) + '.'
        return short_summary
    else:
        return "No information available."
def get_cuisine_wikipedia(country_name):
    page = wiki_wiki.page(f"Cuisine of {country_name}")
    if page.exists():
        sentences = page.summary.split('. ')
        short_summary = '. '.join(sentences[:3]) + '.'
        return short_summary
    else:
        return "No information available."
# Function to fetch cultural practices using Wikipedia
def get_cultural_practices_wikipedia(country_name):
    page = wiki_wiki.page(f"Culture of {country_name}")
    if page.exists():
        sentences = page.summary.split('. ')
        short_summary = '. '.join(sentences[:3]) + '.'
        return short_summary
    else:
        return "No information available."
def get_tourist_attractions_wikipedia(country_name):
    page = wiki_wiki.page(f"Tourism in {country_name}")
    if page.exists():
        sentences = page.summary.split('. ')
        short_summary = '. '.join(sentences[:3]) + '.'
        return short_summary
    else:
        return "No information available."

# Display information in the app
st.subheader(f"Brief Overview of {selected_country}")
summary_short = get_wikipedia_summary_short(selected_country)
st.write(summary_short)
st.divider()
st.subheader(f"Traditional Cuisine of {selected_country}")
cuisine = get_cuisine_wikipedia(selected_country)
st.write(cuisine)
st.divider()

st.subheader(f"Cultural Practices and Traditions in {selected_country}")
practices = get_cultural_practices_wikipedia(selected_country)
st.write(practices)
with st.sidebar:
    st.subheader(f"Top Tourist Attractions in {selected_country}")
    tourist_attractions = get_tourist_attractions_wikipedia(selected_country)
    st.write(tourist_attractions)
