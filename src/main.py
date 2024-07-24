import streamlit as st 
#from AiApi import llm
from CustomLLM import CustomLLM

llm = CustomLLM()


cuisine = st.sidebar.selectbox("Pick a cuisine" , ("Indian","Italian","Mexican","lebenese","French"))

resturant_name = llm(f"give me a fancy name of {cuisine} resturant give me only name as output and nothing else")
items = llm(f"give me names of menu items for a {cuisine} resturant as a comma seperated list and give me only that as output and nothing else")

st.title(f"Resturant name generator for {cuisine} resturant")
def generate_resturant_name_and_items(cuisine):
    return {
        "resturant_name" : cuisine,
        "menu_Items" : items
    }

if cuisine:
    response = generate_resturant_name_and_items(resturant_name)
    st.header(response["resturant_name"])
    menu_items = response["menu_Items"].split(',')
    st.write("**Menu Items**")
    for item in menu_items:
        st.write("-",item)




