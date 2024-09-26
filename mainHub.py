import streamlit as st
import requests
from constant import countries_data, wiki_wiki
import pydeck as pdk
import wikipediaapi
import streamlit as st
import pandas as pd

    

# Create a list of country names
country_names = [country.get('name', {}).get('common', 'N/A') for country in countries_data]

# Streamlit selectbox for country selection
st.header("Facts about Countries and their capital!")
st.write("This website showcases facts about countries, such as their capital city  , land area and their population!")
selected_country = st.selectbox('Select a Country by adjusting the slider!', sorted(country_names))#This is where a user will select a country using st.selectbox

# Display selected country's details
for country in countries_data:#for loop of each country inside the dataset
    if country.get('name', {}).get('common') == selected_country:#If the country name matches the country the user has selected
        st.subheader(f"Details for {selected_country}")#St.subheader to display country name
        col1, col2 = st.columns(2)#Dividing up the data set into 2 columns
        with (col1):#Column 1
            st.image(country.get('flags', {}).get('png'), width=200)#Searches and displays for flag image of the country using the restcountries library
            st.write(f"**Official Name:** {country.get('name', {}).get('official', 'N/A')}")#Searches for and displays the name of the selected country, if the name cannot be found then display N/A
            st.write(f"**Capital:** {', '.join(country.get('capital', ['N/A']))}")
            st.write(f"**Area:** {country.get('area', 'N/A'):,} sq km")

        with(col2):
            st.write(f"**Subregion:** {country.get('subregion', 'N/A')}")   
            st.write(f"**Population:** {country.get('population', 'N/A'):,}")
            st.write(f"**Languages:** {', '.join(country.get('languages', {}).values())}")#Searches for and displays dataset of 'lanmguages via the restcountries dataset library
            st.write(f"**Time Zone:** {', '.join(country.get('timezones',{}))}")#Finds and displays the dataset for the codeword 'timezone' in the restcountries library
            currencies = country.get('currencies', {})#Gets the currency of a selected country from the library
            currencies_formatted = ', '.join([f"{v.get('name')} ({k})" for k, v in currencies.items()])#Searches for the name and type of currency to display
            st.write(f"**Currencies:** {currencies_formatted}")#displays the currency of the selectd country after searching for it

            break
st.divider()
for country in countries_data:#For loop of the collection of country data for each country
    if country.get('name', {}).get('common') == selected_country:#Finds the name of the selected country in the for loop
        country_lat = country.get('latlng', [0, 0])[0]#Gets the latitude and longitiude of the selected country
        country_lng = country.get('latlng', [0, 0])[1]#Gets the longitude of the selected country
        st.subheader(f"Map of {selected_country}")
        
        # Create a map centered on the selected country's coordinates
        st.pydeck_chart(pdk.Deck(
            map_style='mapbox://styles/mapbox/dark-v9',#THe map library used for the map
            initial_view_state=pdk.ViewState(
                latitude=country_lat,#The new variable of the latitude of the country equates to the variable calculated in the for loop
                longitude=country_lng,
                zoom=4,#How zoomed in the map appears at first
                pitch=1,#The angle at which the map is viewed
            ),
            layers=[
                pdk.Layer(
                    'ScatterplotLayer',
                    data=[{'name': selected_country, 'lat': country_lat, 'lon': country_lng}],#Determines the location of where the marker on the map should be placed, based on the users inputs.
                    get_position='[lon, lat]',#Gets the position of the country being selected based on it's latitude and longitude
                    get_radius=20000,  # Adjust size of marker
                    get_color=[200, 30, 0, 160],# Adjust the colour of the marker
                    pickable=True,
                ),
            ],
        ))
        break
#Function for collecting the information about the subdivisions of a country based on a wikipedia article
def get_subdivisions_wikipedia(country_name):#Defining the function to get the subdivision based on the country selected by the user
    page = wiki_wiki.page(f"Regions of {country_name}")#Defines the variabe of the regions page of the selected country's wikipedia page
    if page.exists():#If the page of the regions of the country does exist
        sentences = page.summary.split('. ')#States what character the extracted piece of text ends at.
        short_summary = '. '.join(sentences[:3]) + '.'#limits the number of sentenced extracted from wikipedia to only 3 sentences
        return short_summary
    else:
        return "No information available."#Returns if the country wikipedia page cannot be found
with st.sidebar:#Displays the following data on the sidebar
                st.header(f"Coat Of Arms of {selected_country}") 
                st.image(country.get('coatOfArms', {}).get('png', {}), width=200)
                st.subheader(f"Brief Overview of the Subdivisions of {selected_country}")
                summary_short = get_subdivisions_wikipedia(selected_country)#creates tge variable to Displays the summary from the subdivisions wikipedia function
                st.write(summary_short)#Displays the summary of the wikipedia page of the subdivisions of the country
                 
                





