# The Perfect Address
A very minimlistic yet useful application using just 2 libraries: Pydaisi and Geopy. This aims to return the Postal address of any building/location, also performing a Map visualisation if found.

## Target Users
* Target audience could be students and job applicants who send their applications through the post to their head offices/Universities.
* Regular letter writers and logistics firms that seek to replace a disorganized or an improper address given by their sender/customers with a right one.

## Requirements

Both the Daisi App and the API  the API calls from notebooks/Py-scripts doesn't require any libraries.

PyDaisi package to connect the corresponding Daisi.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install PIL

```bash
pip install pydaisi
```

## Calling
Get a string containing a vague address consisting of the building, location or the city which it's present in.

```python
import pydaisi as pyd
i = input("Enter the location/building: ")
Daisi = pyd.Daisi("sam-dj/The Perfect Address")
```

## Passing and Rendering
We simply pass the string to the Daisi and finally print the result

```python
result = Daisi.geocoder_test(i).value
print(result)
```

## Running the Daisi App

As mentioned earlier, this can be automated just by [Running the Daisi App](https://app.daisi.io/daisies/sam-dj/The%20Perfect%20Address/info)

## References
My notebook which attempts to implement these ideas [Sam DJ's Notebook](https://colab.research.google.com/drive/1H94iwc7vW3G_NKt4khX_o39_UIZlFS4g?usp=sharing)

The official documentation of [GeoPy](https://geopy.readthedocs.io/en/stable/)

The official documentation of [Streamlit Map](https://docs.streamlit.io/library/api-reference/charts/st.map)
