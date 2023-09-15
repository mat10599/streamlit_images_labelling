import streamlit as st
import pandas as pd 
import numpy as np 
from streamlit_tags import st_tags
from streamlit_extras.no_default_selectbox import selectbox

from utils.utils import display_list, modify_label


# define the different global variables for the app

# dict {image_name: label}
if "labels" not in st.session_state:
    st.session_state.labels = {}
# list that will hold the different labels
if 'user_list' not in st.session_state:
    st.session_state.user_list = []
# index of the image to display
if 'index' not in st.session_state:
    st.session_state.index = 0

# text input value of the label to add to user_list
if 'text_input_value' not in st.session_state:
    st.session_state.text_input_value = ""

if "label_selection" not in st.session_state:
    st.session_state.label_selection = None

if "step_label_list_construction" not in st.session_state:
    st.session_state.step_label_list_construction = True

if "step_labelling" not in st.session_state:
    st.session_state.step_labelling = False

st.title('Data labelling')

list_images = st.file_uploader(label="Please upload your images",
                 type=['png', 'jpg'],
                 accept_multiple_files=True)

if st.session_state.step_label_list_construction:
    st.session_state.user_list = st_tags(label="Enter labels", text="Please enter the different possible labels for your images")
    display_list(st.session_state.user_list)
# def add_new_item(user_list, item_to_add):

#     if item_to_add == "":
#         st.warning("You must enter an item to add.")
#         return user_list
#     elif item_to_add in user_list:
#         st.warning("Item already in the list.")
#         return user_list
#     else:
#         user_list.append(item_to_add)
#         return user_list


# def pop_item(user_list, index_to_pop):
#     if 0 <= index_to_pop < len(user_list):
#         removed_item = user_list.pop(index_to_pop)
#         st.success(f"Removed '{removed_item}' from the list.")
#         return user_list
#     else:
#         st.warning("Invalid item number.")
#         return user_list







if list_images != []:
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button('Previous Image'):
            if st.session_state.index > 0:
                st.session_state.index -= 1 
            else:
                st.session_state.index = 0
    with col2:
        if st.button('Next Image'):
            if st.session_state.index < len(list_images)-1:
                st.session_state.index +=1
            else:
                st.session_state.index = len(list_images)-1
    
    st.image(image=list_images[st.session_state.index])
    st.session_state.label_selection = None
    
    st.session_state.label_selection = st.selectbox("Select an option", [el for el in st.session_state.user_list], on_change=modify_label)

    
    

    if st.session_state.label_selection!= None:
        if st.session_state.index < len(list_images)-1:
            st.session_state.index +=1
        else:
            st.warning("No more images to label, please review labelling")
    
   
    
else: 
    st.write("No more images to label, please upload some images")

if st.button("Review labelling"):
    results_df = pd.DataFrame.from_dict(st.session_state.labels, orient='index').reset_index().rename(columns={'index':'image', 0:'label'})
    st.write(results_df)

if st.session_state.labels != {} and st.button('Download labels'):
    st.download_button(label='Download labels', data=pd.DataFrame.from_dict(st.session_state.labels, orient='index').reset_index().rename(columns={'index':'image', 0:'label'}), file_name='labels.csv', mime='text/csv')