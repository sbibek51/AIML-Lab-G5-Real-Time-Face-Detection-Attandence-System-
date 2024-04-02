import streamlit as st
import recognition_helper as helper
import cv2
import numpy as np
from streamlit_webrtc import webrtc_streamer
import av
import time

# st.set_page_config(page_title='Registration Form', layout='wide')
st.subheader("Registration Form")

registration_form = helper.RegistrationForm()

# Step 1: Collect person name and role
person_name = st.text_input(label='Name', placeholder='First and Last name')
role = st.selectbox(label='Select your role', options=('Student', 'Teacher'))

# realTimePrediction = helper.RealTimePrediction()
# facial_data_df = realTimePrediction.retrieve_data()
# st.dataframe(facial_data_df)


# step 2: Collect Facial embedding of the person
# def video_callback_func(frame):
#     img = frame.to_ndarray(format='bgr24')
#     print("Video calback function registration form")
#     image, embeddings = registration_form.get_embedding(img)
#     print('Image ', image)
#     print('Embeddings ', embeddings)
#     return av.VideoFrame.from_ndarray(image, format='bgr24')
#
#
# realTimePrediction = helper.RealTimePrediction()

# time
wait_time = 30
start_time = time.time()

realTimePrediction = helper.RealTimePrediction()


# callback function
def video_frame_callback(frame):
    global start_time
    img = frame.to_ndarray(format="bgr24")  # 3d numpy array
    prediction_img, embeddings = registration_form.get_embeddings(img)
    print("Capturing prediction image")
    return av.VideoFrame.from_ndarray(prediction_img, format="bgr24")


webrtc_streamer(key="real_time_prediction", video_frame_callback=video_frame_callback)

# step 3: save data in redis database

if st.button('Submit'):
    st.write(f'Person name : ', person_name)
    st.write(f'Role : ', role)
