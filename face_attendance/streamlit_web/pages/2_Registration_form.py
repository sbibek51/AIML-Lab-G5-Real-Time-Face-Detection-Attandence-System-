from Home import st
import cv2
import numpy as np
from streamlit_webrtc import webrtc_streamer
import av

# st.set_page_config(page_title='Registration Form', layout='wide')
st.subheader("Registration Form")

# Step 1: Collect person name and role
person_name = st.text_input(label='Name', placeholder='First and Last name')
role = st.selectbox(label='Select your role', options=('Student', 'Teacher'))


# step 2: Collect Facial embedding of the person
def video_callback_func(frames):
    img = frames.to_ndarray(format='bgr24')
    return av.VideoFrame.from_ndarray(img, format='bgr24')


webrtc_streamer(key='registration', video_frame_callback=video_callback_func)

# step 3: save data in redis database

if st.button('Submit'):
    st.write(f'Person name : ', person_name)
    st.write(f'Role : ', role)
