import streamlit as st
import pandas as pd
from streamlit_tags import st_tags
from streamlit_super_slider import st_slider

from utils.utils import display_list, create_global_vars


create_global_vars()

#  STREAMLIT APP
st.title('Data labelling')
list_images = st.file_uploader(label="Please upload your images",
                               type=['png', 'jpg'],
                               accept_multiple_files=True)

# CREATE LABELS LIST
st.session_state.user_list = st_tags(
    label="Enter labels", text="Please enter the different possible labels for your images")
display_list(st.session_state.user_list)


if list_images != []:
    st.session_state.index = st_slider(0, len(list_images)-1)

    st.image(image=list_images[st.session_state.index])
    try:
        st.write(
            f"You have labelled this image as {st.session_state.labels[list_images[st.session_state.index].name]}")
    except KeyError:
        st.write("This image has not been labelled yet")
    st.session_state.label_selection = None

    st.session_state.label_selection = st.selectbox(
        "Select an option",
        [""] + [el for el in st.session_state.user_list],
        index=0,
        key=st.session_state.key_selector,
    )
    if st.session_state.label_selection == "":
        pass
    else:
        st.session_state.labels[list_images[st.session_state.index]
                                .name] = st.session_state.label_selection
        st.session_state.key_selector += 1


else:
    st.write("No more images to label, please upload some images")


# REVIEW LABELS AND DOWNLOAD RESULTS
if st.button("Review labelling"):
    results_df = pd.DataFrame.from_dict(st.session_state.labels, orient='index').reset_index(
    ).rename(columns={'index': 'image', 0: 'label'})
    st.write(results_df)
    st.download_button(label='Download labels', data=results_df.to_csv().encode(
        "utf-8"), file_name='labels.csv', mime='text/csv')
