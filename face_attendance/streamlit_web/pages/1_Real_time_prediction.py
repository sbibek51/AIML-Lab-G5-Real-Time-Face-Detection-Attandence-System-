from Home import st
from Home import helper

db_key = helper.db_key

# st.set_page_config(page_title='Prediction', layout='wide')
st.subheader('Real-time Attendace System')

with st.spinner("Retrieving Data"):
    # retrieve data from database
    facial_data = helper.retrieve_data(db_key)
    st.dataframe(facial_data)
st.success("Data loaded successfully")
