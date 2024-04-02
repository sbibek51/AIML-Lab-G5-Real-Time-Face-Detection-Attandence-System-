import streamlit as st
import recognition_helper as helper
from streamlit_webrtc import webrtc_streamer
import av
import time

db_key = helper.db_key
realTimePrediction = helper.RealTimePrediction()

# st.set_page_config(page_title='Prediction', layout='wide')
st.subheader('Real-time Attendance System')

with st.spinner("Retrieving Data"):
    # retrieve data from database
    facial_data_df = realTimePrediction.retrieve_data()
    st.dataframe(facial_data_df)
st.success("Data loaded successfully")

# Real Time Prediction

# time
wait_time = 30
start_time = time.time()


# callback function
def video_frame_callback(frame):
    global start_time
    img = frame.to_ndarray(format="bgr24")  # 3d numpy array
    prediction_img = realTimePrediction.name_prediction(img, facial_data_df)
    print("Capturing prediction image")

    time_now = time.time()
    time_difference = time_now - start_time
    print(time_difference)
    if time_difference >= wait_time:
        realTimePrediction.save_logs_redis()
        start_time = time.time()  # reset time
        print("Save data to redis database")
    return av.VideoFrame.from_ndarray(prediction_img, format="bgr24")


webrtc_streamer(key="real_time_prediction", video_frame_callback=video_frame_callback)
