import streamlit as st
import pandas as pd
from geopy.geocoders import Nominatim


def geocoder(string):
    """
    .
    This function takes in a string and returns the raw location. That is every possible detail of the location.
    For example: The coordinates, the type and elevation.

    :param str string: The string containing a vague address

    :return: Returns a geopy.location dictionary
    """
    locator = Nominatim(user_agent="myGeocoder")
    return locator.geocode(string)


def geocoder_test(string):
    """
  .
  This function does the same as above but reserved for API calls and Testing(Without Streamlit UI involved)
  """

    locator = Nominatim(user_agent="myGeocoder")
    location = locator.geocode(string)
    if not location:
        return 'Add more Info (For example: Road, City, District)'
    else:
        return location.address


def st_ui():
    """
    .
    This function creates a Streamlit UI and performs the task of getting in the string and having a button that triggers the above the function. If found
    this also visualises the location through Streamlit's map function.
    """
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
                "<h4 style='text-align: center; color: black;'> Incorrect location? Give it a retry with more info "
                "</h4>",
                unsafe_allow_html=True)


if __name__ == '__main__':
    st_ui()
