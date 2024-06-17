#importing libraries
import streamlit as st
import darts
from darts.timeseries import TimeSeries as Ts
import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots

from darts.models import ExponentialSmoothing
# titile
st.title('Predicting electricity demand for TSNPDCL region using Timeseries')
# defining functions for loading model,data and caching them
@st.cache_resource
def load_model():
    model = ExponentialSmoothing.load('hwes_best.pkl')
    return model
@st.cache_data
def loading_prep_data():
    p_data = pd.read_excel('assets/prep_data_final.xlsx')
    return p_data
# loading data and model
past_data = loading_prep_data()

with st.spinner('loading model'):
    model = load_model()



predictions, chart = st.columns([0.4,0.6])

# Add a slider for selecting prediction period
num_periods = st.slider('Select number of months for prediction, starting from June 2024 ', 1, 12)
with predictions:
    with st.spinner('predicting'):
            pred = model.predict(num_periods).pd_dataframe()
            st.write(pred)

# Create traces
trace_past = go.Scatter(x=past_data['Period'], y=past_data['Units'], mode='lines', name='Past Data')
trace_pred = go.Scatter(x=pred.index, y=pred['Units'], mode='lines', name='Predictions')
# Create a figure
fig = make_subplots(])

# Add traces
fig.add_trace(trace_past, secondary_y=False)
fig.add_trace(trace_pred, secondary_y=False)

# Customize layout
fig.update_layout(title='Past  vs Predicted demad',
                  xaxis_title='Months',
                  yaxis_title='Units(Kw)',
                 )

with chart:
    st.plotly_chart(fig)

st.write('want to know how i built this?...') 
st.markdown('[checkout github repo](http://www.example.com)')