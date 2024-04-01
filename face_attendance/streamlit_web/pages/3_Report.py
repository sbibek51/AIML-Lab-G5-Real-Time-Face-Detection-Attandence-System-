from Home import st
from Home import helper

# st.set_page_config(page_title='Reporting', layout='wide')
st.subheader('Report')

realTimePrediction = helper.RealTimePrediction()
key_name = 'attendance:logs'


# retrieve log data and show in report
def load_logs(key_name, end=-1):
    print("Key name is ", key_name)
    logs_list = helper.r.lrange(key_name, start=0, end=end)  # extract all data from redis database
    return logs_list


# tab to show information
tab1, tab2 = st.tabs(['Registered Data', 'Logs'])
with tab1:
    if st.button('Refresh Data'):
        with st.spinner('Retriving data from Redis database'):
            registration_data = realTimePrediction.retrieve_data()
            st.dataframe(registration_data[['Name','Role']])
with tab2:
    if st.button('Refresh Logs'):
        # retrieve data from redis database
        st.write(load_logs(key_name))
