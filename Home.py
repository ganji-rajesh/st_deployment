import streamlit as st
import pandas as pd 


st.set_page_config(
    page_title="TGSNPDCL ecletricity prediction",
    page_icon="⚡⚡",
    layout="wide",
    initial_sidebar_state="auto",
)

st.title('Welcome to TGSNPDCL electircity prediction using timesereis analysis')
st.divider()
tgsnpdcl_des, tgsnpdcl_image = st.columns([0.7,0.3])

with tgsnpdcl_des:
    st.write('The Nothern Power Distribution Company of Telangana, abbreviated as TGSNPDCL, is a state electric power distribution company owned by the Government of Telangana. The Company caters to supply of electricity in districts of Mancherial, Nirmal, Kumram Bheem Asifabad, Kamareddy, Peddapalli, Jagtial, Rajanna, Hanamakonda, Warangal, Mahabubabad, Prof Jayashankar, Jangaon, Bhadradri Kothagudem, Adilabad, Nizamabad, Karimnagar and Khammam Districts.')
with tgsnpdcl_image:
    st.image('assets/tgsnpdcl_image.jpeg')

st.write('TGSPDCL has commercial electricity consumption data at circles,  division,  sub-division,  section, area level.')
st.divider()
st.subheader(body='Objective: predict electricity demand')
st.write('Data source: Monthly commercial electricity consumption data was collected from January 2019 to May 2024 at each level of TGSPDCL from data.telangana.gov.in' )
st.write('I have preprocessed and aggregated this at TGSNPDCL level for each month from Jan 2019 to May 2024.')
@st.cache_data
def pre_data():
    prep_data = pd.read_excel('assets/prep_data_final.xlsx')
    return prep_data
prep_data = pre_data()
st.dataframe(prep_data)
st.markdown('**timeseries analysis**')
st.write('I have implemented SEM, HW , AR, MA, ARIMA models. HW model emerged as best model.')
st.write('Find predictions for next one year(June 2024 to June 2025) in predictions webpage')
st.divider()
st.subheader('what can be done further...')
st.markdown('* Electricity demand can predicted at circle, division, sub-division level as well.' )
st.markdown(' * Latest ML techiniques can be used in prediction ')
st.divider()
st.subheader('limitations')
st.markdown('* HW model has MAPE of 5.4%, there is possibility of giving inaccurate predictions ')

