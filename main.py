import streamlit as st
import joblib
import pandas as pd

# Load the saved model
model = joblib.load("laptop_price_predictor.pkl")

# Title
st.title("💻 Laptop Price Predictor")

# --- Input Features ---

# Company

company = st.selectbox("Company", ['Dell', 'Lenovo', 'HP', 'Asus', 'Acer', 'MSI', 'Toshiba',
                                   'Apple', 'Samsung', 'Mediacom', 'Microsoft', 'Others'])

# Type
typename = st.selectbox("Laptop Type", ['Notebook', 'Gaming', 'Ultrabook',
                                        '2 in 1 Convertible', 'Workstation', 'Netbook'])

# RAM
ram = st.selectbox("RAM (GB)", [2, 4, 6, 8, 12, 16, 24, 32, 64])

# OS
if company == "Apple" :
    os = st.selectbox("os",['macOS', 'Mac OS X'])

if company != "Apple" :
    
    os = st.selectbox("Operating System", ['Windows 10', 'Linux', 'Windows 7', 'Chrome OS',
                                       'Windows 10 S', 'Android'])

# Weight
weight_cat = st.selectbox("Weight Category", ['Light', 'Middle', 'Heavy'])

# Touchscreen and IPS
touchscreen = st.checkbox("Touchscreen")
ips = st.checkbox("IPS Display")

# Screen Resolution
res_options = {
    "HD (1366x768)": (1366, 768),
    "HD+ (1600x900)": (1600, 900),
    "Full HD (1920x1080)": (1920, 1080),
    "Full HD+ (1920x1200)": (1920, 1200),
    "Retina (2304x1440)": (2304, 1440),
    "Retina+ (2560x1440)": (2560, 1440),
    "Retina WQXGA (2560x1600)": (2560, 1600),
    "2K (2160x1440)": (2160, 1440),
    "2.5K Touch (2256x1504)": (2256, 1504),
    "Quad HD+ (3200x1800)": (3200, 1800),
    "2.7K Surface Pro (2736x1824)": (2736, 1824),
    "2.8K Retina (2880x1800)": (2880, 1800),
    "4K Ultra HD (3840x2160)": (3840, 2160),
    "WQXGA+ (2400x1600)": (2400, 1600)
}

screen_res = st.selectbox("Screen Resolution", list(res_options.keys()))
resolution_width, resolution_height = res_options[screen_res]

# Screen size is fixed at 15 inches (you can make it adjustable)
screen_size = 15
ppi = ((resolution_width**2 + resolution_height**2)**0.5) / screen_size

# CPU
cpu = st.selectbox("Processor", ['Intel Core i7', 'Intel Core i5', 'Intel Core i3',
                                 'AMD Processor', 'Other Intel Processor'])

# GPU
gpu = st.selectbox("GPU", ['Intel', 'Nvidia', 'AMD'])

# Storage options
ssd = st.selectbox("SSD Size", ['None', '16GB', '32GB', '64GB', '128GB', '256GB', '512GB', '1TB'])
hdd = st.selectbox("HDD Size", ['None', '32GB', '128GB', '512GB', '1TB', '2TB'])
hybrid = st.selectbox("Hybrid Storage", ['None', '1TB', '508GB'])
flash = st.selectbox("Flash Storage", ['None', '16GB', '32GB', '64GB', '128GB', '256GB', '512GB'])

# --- Data Preprocessing ---
def clean_storage(val):
    if val == 'None':
        return 0
    elif 'TB' in val:
        return int(val.replace('TB', '').strip()) * 1024
    else:
        return int(val.replace('GB', '').strip())

input_dict = {
    'Company': [company],
    'TypeName': [typename],
    'Ram': [ram],
    'OpSys': [os],
    'weight_category': [weight_cat],
    'Touchscreen': [int(touchscreen)],
    'IPS': [int(ips)],
    'PPI': [round(ppi, 2)],
    'Cpu_brand': [cpu],
    'Gpu_brand': [gpu],
    'SSD': [clean_storage(ssd)],
    'HDD': [clean_storage(hdd)],
    'Hybrid': [clean_storage(hybrid)],
    'Flash': [clean_storage(flash)]
}

input_df = pd.DataFrame(input_dict)

# --- Prediction ---
if st.button("Predict Price"):
    prediction = model.predict(input_df)
    st.success(f"💰 Estimated Laptop Price: {round(prediction[0], 2)} EGP")
