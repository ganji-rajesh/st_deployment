import streamlit as st
import streamlit as st
import pandas as pd 


st.set_page_config(
    page_title="TGSNPDCL ecletricity prediction",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="auto",
)

st.title('Welcome to TGSNPDCL electircity prediction using timesereis analysis')
st.divider()
tgsnpdcl_des, tgsnpdcl_image = st.columns([0.7,0.3])

with tgsnpdcl_des:
    st.write('The Nothern Power Distribution Company of Telangana, abbreviated as TGSNPDCL, is a state electric power distribution company owned by the Government of Telangana. The Company caters to supply of electricity in districts of Mancherial, Nirmal, Kumram Bheem Asifabad, Kamareddy, Peddapalli, Jagtial, Rajanna, Hanamakonda, Warangal, Mahabubabad, Prof Jayashankar, Jangaon, Bhadradri Kothagudem, Adilabad, Nizamabad, Karimnagar and Khammam Districts.')
with tgsnpdcl_image:
    st.write('tgsnpdcl image')

st.write('TGSPDCL has x circles, x divisions, x sub-divisions, x sections, x areas.')
st.divider()
st.subheader(body='Objective: predict electricity demand')
st.write('Data source: Monthly commercial electricity consumption data was collected from January 2019 to May 2024 at each level of TGSPDCL from data.telangana.gov.in' )
st.write('data view & I have preprocessed and aggregated this at TGSNPDCL level for each month from Jan 2019 to May 2024.')
st.write(' timeseries analysis')
st.write('I have implemented SEM, HW , AR, MA, ARIMA models. HW model emerged as best model.')
st.write('Find predictions for June 2024 to Auguest 2024, June 2024 to November 2024, June 2024 to June 2025.')

# st.sidebar.success("Select a page above.")