import streamlit

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.multiselect('Pick some fruits :',list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.header('Fruityvice Fruit Advice !')
streamlit.text(fruityvice_response.json())

#take json response and normalise it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#Output
streamlit.dataframe(fruityvice_normalized)
