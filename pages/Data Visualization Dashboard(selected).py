# streamlit_app.py

import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

# Set Streamlit page configuration
st.set_page_config(page_title="Data Visualization App", layout="wide")

# Title
st.title("📊 Data Visualization Dashboard")

# Upload CSV


file = st.file_uploader("Upload file ",type=["csv"])

if file is not None:
    df = pd.read_csv(file)
    
    n_rows = st.slider('choose the number of rows to display',
    min_value=5,max_value=len(df),step=1)
    columns_to_show=st.multiselect("select feautre to show >> " , df.columns.tolist())
    st.write(df[:n_rows][columns_to_show])

    tab1,tab2 = st.tabs(["Scatter plot ","Histogram"])
    
    
    numerical_columns = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
    with tab1:
      
        x_column = st.selectbox("Select feature:", numerical_columns)
        
        fig = px.scatter(df, x=x_column, y="Price")
        st.plotly_chart(fig)

    with tab2:
        
        x2_column = st.selectbox("Select feature", numerical_columns)
        fid2 = px.histogram(df,x=x2_column,y="Price")
        st.plotly_chart(fid2)