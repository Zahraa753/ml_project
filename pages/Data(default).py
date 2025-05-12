import streamlit as st
import pandas as pd
import plotly.express as px

st.title("DATA📉")

df = pd.read_csv("D:\downlode\df.csv")
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