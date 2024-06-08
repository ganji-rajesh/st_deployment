import streamlit as st
from darts.models import ExponentialSmoothing

st.write('deploying_1st_model')

@st.cache_resource
def load_model():
    model = ExponentialSmoothing.load('hwes_m_model.pkl')
    return model

with st.spinner('loading model'):
    model = load_model()

st.write('prediction')
with st.spinner('predicting'):
    pred = model.predict(12)
    st.write(pred)

