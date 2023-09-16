import streamlit as st


def display_list(user_list):
    st.write(user_list)


def create_global_vars():
    """creates all the global variables for the app
    """
    if "key_selector" not in st.session_state:
        st.session_state.key_selector = 0
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

# new_item = st.text_input("Add an item to the list:", st.session_state.text_input_value)
# if st.button("Add") and new_item is not None:
#     st.session_state.user_list = add_new_item(st.session_state.user_list, new_item)
#     st.session_state.text_input_value = ""



# # Allow users to remove items
# item_to_remove = st.text_input("Enter the item number to remove (e.g.0, 1, 2):")
# if st.button("Remove"):
#     st.session_state.user_list = pop_item(st.session_state.user_list, int(item_to_remove))