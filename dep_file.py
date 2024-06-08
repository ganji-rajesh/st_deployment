import streamlit as st
import darts
from darts.models.forecasting.exponential_smoothing import ExponentialSmoothing

st.write('deploying_1st_model')

@st.cache_resource
def load_model():
    model = ExponentialSmoothing.load('hwes_m_model.pkl')
    return model

with st.spinner('loading model'):
    model = load_model()

st.write('prediction')
with st.spinner('predicting'):
    pred = model.predict(12).pd_dataframe()
    st.write(pred)

