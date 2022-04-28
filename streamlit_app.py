import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.multiselect('Pick some fruits :',list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)

#import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.header('Fruityvice Fruit Advice !')
#streamlit.text(fruityvice_response.json())

#take json response and normalise it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#Output
streamlit.dataframe(fruityvice_normalized)



streamlit.header('Fruityvice Fruit Advice !')
try:
    fruit_choice = streamlit.text_input('what food would you like information about ?')
    if not fruit_choice:
        streamlit.error('Please select a fruit to get a information')
    else:
        fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
        fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
        streamlit.dataframe(fruityvice_normalized) 

except URLError as e:
    streamlit.error()         
    
    
    
streamlit.header('Fruityvice Fruit Advice Using function')
def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized
'''
streamlit.header('Fruityvice Fruit Advice function!')
try:
    fruity_choice = streamlit.text_input('what food would you like information about ?')
    if not fruity_choice:
        streamlit.error('Please select a fruit to get a information')
    else:
        back_from_function = get_fruityvice_data(fruity_choice)
        streamlit.dataframe(back_from_function)

except URLError as e:
    streamlit.error()         
'''
                                        
#streamlit.stop()

streamlit.header('Fruityvice Fruit Advice !')
fruit_choice = streamlit.text_input('what food would you like information about ?','kiwi')
streamlit.write('The user entered', fruit_choice)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)


#streamlit.stop()

#import pandas
#import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)




my_cur.execute("insert into garder_plants.veggies.vegetable_details values('from streamlit','D')")
