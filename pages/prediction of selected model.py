import streamlit as st
import pickle
import numpy as np
import pandas as pd

df = pd.read_csv("D:\downlode\df.csv")
tab1,tab2,tab3,tab4 = st.tabs(["The Best Model","modle 1","Model2","Model3"])
with tab1:
    #load the model and dataframe

    pipe = pickle.load(open("D:\downlode\pipe.pkl", "rb"))

    st.title("💻Laptop Price Predictor")
    st.write("the best model")
    #Now we will take user input one by one as per our dataframe

    #Brand
    #company = st.selectbox('Brand', df['Company'].unique())
    company = st.selectbox('Brand', df['Company'].unique())
    #Type of laptop
    lap_type = st.selectbox("Type", df['TypeName'].unique())

    #Ram
    ram = st.selectbox("Ram(in GB)", [2,4,6,8,12,16,24,32,64])
    #weight
    weight = st.number_input("Weight of the Laptop",min_value = 0.69,max_value= 4.7)
    #Touch screen
    touchscreen = st.selectbox("TouchScreen", ['No', 'Yes'])
    #IPS
    ips = st.selectbox("IPS", ['No', 'Yes'])
    #screen size
    screen_size = st.number_input('Screen Size')

    # resolution
    resolution = st.selectbox('Screen Resolution',['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])

    #cpu
    cpu = st.selectbox('CPU',df['Cpu_brand'].unique())
    hdd = st.selectbox('HDD(in GB)',[0,128,256,512,1024,2048])
    ssd = st.selectbox('SSD(in GB)',[0,8,128,256,512,1024])
    gpu = st.selectbox('GPU',df['Gpu_brand'].unique())
    if company == "Apple" :
        os = st.selectbox("os",["Mac"])

    if company != "Apple" :
        os = st.selectbox('OS',["Windows","Others/No OS/Linux"])

    #Prediction
    if st.button('Price Prediction'):
        ppi = None
        if touchscreen == "Yes":
            touchscreen = 1
        else:
            touchscreen = 0
            
        if ips == "Yes":
            ips = 1
        else:
            ips = 0
        
        X_res = int(resolution.split('x')[0])
        Y_res = int(resolution.split('x')[1])
        ppi = ((X_res ** 2) + (Y_res**2)) ** 0.5 / screen_size

        # making prediction 
        query = np.array([company,lap_type,ram,weight,touchscreen,ips,ppi,cpu,hdd,ssd,gpu,os])
        query = query.reshape(1, 12)
        prediction = str(int(np.exp(pipe.predict(query)[0])))
        st.title("The predicted price of this configuration is " + prediction)

with tab2:
    st.write("modle1 predic")
with tab3:
    
    st.write("modle2 predic")


with tab4:
    st.write("modle3 predic")
