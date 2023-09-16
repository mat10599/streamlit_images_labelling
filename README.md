# streamlit_data_labelling


## Name
Data labelling app with streamlit.

## Description
The goal of this app is to allow the user to label unlabelled images manually.


## Installation
First clone the repository on your computer.
Then in your terminal either:
1. install the required dependencies running `pip install -r requirements.txt` (in terminal) or otherwise.
2. run `streamlit run labelling_app.py --server.port 8080` (in terminal). 

- **or**
1. run `docker build -t name_of_image .` (in terminal)
2. run `docker run name_of_image` (in terminal)
3. type http://0.0.0.0:8502 or http://localhost:8502 in your favourite browser to use the app!


## Usage
The app is meant to be used to label images. 
User should first upload the different images it wants to label.
Then, he should state what are the possible labels for the app.Finally, the user can label the different images, review and modify the labels if a mistake was made and download the image names with their labelling.

[streamlit-labelling_app-2023-09-16-18-09-55.webm](https://github.com/mat10599/streamlit_images_labelling/assets/78880807/299c0a15-aeb4-44b4-a53e-1f375be9965c)

## Roadmap
Future improvements to the app include:
- possibility to connect to a database and to directly "query" unlabelled images from it instead of manually uploading the images.
- "force" the images to be resized in a certain box: bigger images will take a bigger place in the app, shifting elements dynamically at the cost of user experience.


## Feedback 
Any comment/remark on how I could improve code quality or the app is much appreciated!
