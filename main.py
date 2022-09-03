import streamlit as st
import pandas as pd
from geopy.geocoders import Nominatim

def geocoder(string):
    locator = Nominatim(user_agent="myGeocoder")
    return locator.geocode(string)

def geocoder_test(string):
    locator = Nominatim(user_agent="myGeocoder")
    location = locator.geocode(string)
    if not location:
        return('Add more Info (For example: Road, City, District)')
    else:
        return(location.address)
    
def st_ui():
    st.title("The Perfect Address 🌍")
    l = st.text_input("Enter a building or location")
    location = geocoder(l)
    b = st.button('Get Postal Address')
    if b:
        if not location:
            st.text('Add more Info (For example: Road, City, District)')
        else:
            st.subheader(location.address)
            data = [[location.latitude, location.longitude]]
            df = pd.DataFrame(data, columns=['lat', 'lon'])
            st.map(df)
            st.markdown(
                "<h4 style='text-align: center; color: black;'> Incorrect location? Give it a retry with more info </h4>",
                unsafe_allow_html=True)

if __name__ == '__main__':
    st_ui()
