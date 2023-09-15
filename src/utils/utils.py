import streamlit as st


def display_list(user_list):
    st.write(user_list)


# new_item = st.text_input("Add an item to the list:", st.session_state.text_input_value)
# if st.button("Add") and new_item is not None:
#     st.session_state.user_list = add_new_item(st.session_state.user_list, new_item)
#     st.session_state.text_input_value = ""

def modify_label(list_images, label):
    st.session_state.labels[list_images[st.session_state.index].name] =  label
    st.write(f"You have labelled this image as {st.session_state.labels[list_images[st.session_state.index].name]}")


# # Allow users to remove items
# item_to_remove = st.text_input("Enter the item number to remove (e.g.0, 1, 2):")
# if st.button("Remove"):
#     st.session_state.user_list = pop_item(st.session_state.user_list, int(item_to_remove))