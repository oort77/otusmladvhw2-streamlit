# -*- coding: utf-8 -*-
#  File: app.py
#  Project: 'Homework #2 OTUS.ML.Advanced'
#  Created by Gennady Matveev (gm@og.ly) on 02-01-2022.

# Import libraries
import os
import pandas as pd
import streamlit as st
import requests

st.set_page_config(page_title='OTUS.ML.ADV_HW2', page_icon='./car_at_night.ico',
                   layout='centered', initial_sidebar_state='expanded')

padding = 0
st.markdown(f""" <style>
    .reportview-container .main .block-container{{
        padding-top: {padding}rem;
        padding-right: {padding}rem;
        padding-left: {padding}rem;
        padding-bottom: {padding}rem;
    }} </style> """, unsafe_allow_html=True)
    
st.image('./sky.png')
st.subheader('Homework #2 OTUS.ML.Advanced')
st.write('Classification model for Heart Disease UCI: &nbsp;&nbsp;https://www.kaggle.com/ronitf/heart-disease-uci')
st.markdown("""---""")

# Import data, will need it for get requests
@st.cache(ttl=600)
def get_data():
    url = 'https://drive.google.com/uc?export=download&id=1wY3r2MwQoa-jiyzRoEM_eF_EU11vrCs0'
    return pd.read_csv(url, compression='zip')

df = get_data()

# Main interface
row_num = st.number_input('Please choose features vector 0-302 or set values in the left sidebar', 
                          min_value=0, max_value=302, value=42)
x17 =df.iloc[row_num,:-1].to_frame().T
st.write('Features, X')
st.write(x17)

# START Sidebar ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

with st.sidebar.expander("I want to choose my values", expanded=False):
    age = st.number_input('Age', min_value=25, max_value=80, value=57)
    sex = st.number_input('Sex', min_value=0, max_value=1, value=1)
    cp = st.number_input('cp', min_value=0, max_value=4, value=0)
    trestbps = st.number_input('trestbps', min_value=90, max_value=200, value=125)
    chol = st.number_input('chol', min_value=125, max_value=550, value=240)
    fbs = st.number_input('fbs', min_value=0, max_value=1, value=0)
    restecg = st.number_input('restecg', min_value=0, max_value=2, value=1)
    thalach = st.number_input('thalach', min_value=70, max_value=200, value=160)
    exang = st.number_input('exang', min_value=0, max_value=1, value=0)
    oldpeak = st.number_input('oldpeak', min_value=0, max_value=6, value=2)
    slope = st.number_input('slope', min_value=0, max_value=2, value=2)
    ca = st.number_input('ca', min_value=0, max_value=4, value=0)
    thal = st.number_input('thal', min_value=0, max_value=3, value=2)
    
    features = age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal
    send_req_sidebar = st.button('Get prediction')

# END Sidebar ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

send_req = st.button('Send get request')

# worker_port = int(os.getenv('WPORT'))
worker_port = 8080
worker_address = "http://localhost:" + str(worker_port) + "/predict/"

# Main page button
if send_req:
    prediction = requests.get(worker_address, 
                              params={"q": tuple(x17.values)})
    st.code(f'Parameters sent: {x17.values}')
    col1, col2 = st.columns(2)
    with col1:
        st.write('Model predicts')
        st.success(f'y = {prediction.text}')
    with col2:
        st.write('Ground truth')
        if int(prediction.text) == int(df.iloc[row_num]["target"]):
            st.success(f'y = {int(df.iloc[row_num]["target"])}')
        else:
            st.warning(f'y = {int(df.iloc[row_num]["target"])}')

# Sidebar button        

if send_req_sidebar:
    prediction = requests.get(worker_address, 
                              params={"q": features})
    st.code(f'Parameters sent: {features}')
    st.write('Model predicts')
    st.info(f'y = {prediction.text}')

# Show this code
with st.expander("Show code", expanded=False):
    show_me = st.checkbox('Show code of this program')
    if show_me:
        st.code("""
    # -*- coding: utf-8 -*-
#  File: app.py
#  Project: 'Homework #2 OTUS.ML.Advanced'
#  Created by Gennady Matveev (gm@og.ly) on 02-01-2022.

# Import libraries
import pandas as pd
import streamlit as st
import requests

st.set_page_config(page_title='OTUS.ML.ADV_HW2', page_icon='./car_at_night.ico',
                   layout='centered', initial_sidebar_state='expanded')

padding = 0
st.markdown(f''' <style>
    .reportview-container .main .block-container{{
        padding-top: {padding}rem;
        padding-right: {padding}rem;
        padding-left: {padding}rem;
        padding-bottom: {padding}rem;
    }} </style> ''', unsafe_allow_html=True)
    
st.image('./sky.png')
st.subheader('Homework #2 OTUS.ML.Advanced')
st.write('Classification model for Heart Disease UCI: &nbsp;&nbsp;https://www.kaggle.com/ronitf/heart-disease-uci')
st.markdown('''---''')

# Import data, will need it for get requests
@st.cache(ttl=600)
def get_data():
    url = 'https://drive.google.com/uc?export=download&id=1wY3r2MwQoa-jiyzRoEM_eF_EU11vrCs0'
    return pd.read_csv(url, compression='zip')

df = get_data()

# Main interface
row_num = st.number_input('Please choose features vector 0-302 or set values in the left sidebar', 
                          min_value=0, max_value=302, value=42)
x17 =df.iloc[row_num,:-1].to_frame().T
st.write('Features, X')
st.write(x17)

# START Sidebar ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

with st.sidebar.expander("I want to choose my values", expanded=False):
    age = st.number_input('Age', min_value=25, max_value=80, value=57)
    sex = st.number_input('Sex', min_value=0, max_value=1, value=1)
    cp = st.number_input('cp', min_value=0, max_value=4, value=0)
    trestbps = st.number_input('trestbps', min_value=90, max_value=200, value=125)
    chol = st.number_input('chol', min_value=125, max_value=550, value=240)
    fbs = st.number_input('fbs', min_value=0, max_value=1, value=0)
    restecg = st.number_input('restecg', min_value=0, max_value=2, value=1)
    thalach = st.number_input('thalach', min_value=70, max_value=200, value=160)
    exang = st.number_input('exang', min_value=0, max_value=1, value=0)
    oldpeak = st.number_input('oldpeak', min_value=0, max_value=6, value=2)
    slope = st.number_input('slope', min_value=0, max_value=2, value=2)
    ca = st.number_input('ca', min_value=0, max_value=4, value=0)
    thal = st.number_input('thal', min_value=0, max_value=3, value=2)
    
    features = age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal
    send_req_sidebar = st.button('Get prediction')

# END Sidebar ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

ssend_req = st.button('Send get request')

worker_port = int(os.environ.get("PORT", 8080))
worker_address = "http://worker:" + worker_port + "/predict/"

# Main page button
if send_req:
    prediction = requests.get(worker_address, 
                              params={"q": tuple(x17.values)})
    st.code(f'Parameters sent: {x17.values}')
    col1, col2 = st.columns(2)
    with col1:
        st.write('Model predicts')
        st.success(f'y = {prediction.text}')
    with col2:
        st.write('Ground truth')
        if int(prediction.text) == int(df.iloc[row_num]["target"]):
            st.success(f'y = {int(df.iloc[row_num]["target"])}')
        else:
            st.warning(f'y = {int(df.iloc[row_num]["target"])}')

# Sidebar button        

if send_req_sidebar:
    prediction = requests.get(worker_address, 
                              params={"q": features})
    st.code(f'Parameters sent: {features}')
    st.write('Model predicts')
    st.info(f'y = {prediction.text}')
    """
    )
    
    show_api = st.checkbox('Show code of FastAPI backend')
    if show_api:
        st.code("""
        # -*- coding: utf-8 -*-
#  File: main.py
#  Project: 'Homework #2 OTUS.ML.Advanced'
#  Created by Gennady Matveev (gm@og.ly) on 04-01-2022.
#  Copyright 2022. All rights reserved.

# Import libraries
import uvicorn
from atom import ATOMLoader
from fastapi import FastAPI, Query
import pandas as pd
from typing import List, Optional

cols = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach',
       'exang', 'oldpeak', 'slope', 'ca', 'thal']

atom = ATOMLoader("./models/atom20220104-32256", verbose=0)

# Initialize app
app = FastAPI()

# Routes
@app.get('/')
async def index():
    return {"text": "Hello, fellow ML students"}


@app.get('/predict/')
async def predict(q: Optional[List[float]] = Query(None)):
    dfx = pd.DataFrame([q], columns = cols)
    prediction = atom.predict(dfx)
    return int(prediction[0])


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8080)        
"""
)

    st.markdown("And, finally, classification model itself on [Colab](https://colab.research.google.com/github/oort77/OTUS_ADV_HW2/blob/main/notebooks/otus_adv_hw2.ipynb)")