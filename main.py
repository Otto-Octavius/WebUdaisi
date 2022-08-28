import streamlit as st
import pandas as pd
from geopy.geocoders import Nominatim

locator = Nominatim(user_agent="myGeocoder")

def st_ui():
    st.title("The Perfect Address 🌍")
    l = st.text_input("Enter your location")
    location = locator.geocode(l)
    b = st.button('Get Postal Address')
    if b:
        if not location:
            st.text('Add more Info (For example: City,District)')
        else:
            st.subheader(location.address)
            data = [[location.latitude, location.longitude]]
            df = pd.DataFrame(data, columns=['lat', 'lon'])
            st.map(df)
            st.markdown(
                "<h4 style='text-align: center; color: white;'> Incorrect location? Give it a retry with more info </h4>",
                unsafe_allow_html=True)

if __name__ == '__main__':
    st_ui()
