from Home import st
from Home import helper
from streamlit_webrtc import webrtc_streamer
import av

db_key = helper.db_key

# st.set_page_config(page_title='Prediction', layout='wide')
st.subheader('Real-time Attendace System')

with st.spinner("Retrieving Data"):
    # retrieve data from database
    facial_data_df = helper.retrieve_data(db_key)
    st.dataframe(facial_data_df)
st.success("Data loaded successfully")


# Real Time Prediction

# callback function
def video_frame_callback(frame):
    img = frame.to_ndarray(format="bgr24")  # 3d numpy array
    # flipped = img[::-1, :, :]
    prediction_img = helper.name_prediction(img, facial_data_df)
    # print(prediction_img)
    print("Capturing prediction image")
    return av.VideoFrame.from_ndarray(prediction_img, format="bgr24")


webrtc_streamer(key="real_time_prediction", video_frame_callback=video_frame_callback)
