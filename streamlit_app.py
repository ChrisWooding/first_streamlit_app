import streamlit
import pandas

streamlit.title('My Mum\'s New Healthy Cafe')

streamlit.header('Breakfast Menu')

streamlit.text('🥣 Omega 3 and blueberry oatmeal 🥣')
streamlit.text('🥗 Kale, spinach & rocket smoothie 🥗')
streamlit.text('🐔 Hard-boiled free-range egg 🐔')
streamlit.text('🥑🍞 Avocado toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
