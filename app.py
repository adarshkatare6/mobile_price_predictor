import math
import streamlit as st
import pickle
import pandas as pd
import  numpy as np
#importing model
pipe=pickle.load(open('pipe.pkl','rb'))
df=pickle.load(open('df.pkl','rb'))

st.title("Mobile Price Predictor")

#brand
Brand = st.selectbox("Brand",df['Brand'].unique())

#Ram
RAM = st.selectbox("Ram(in gb)",df['RAM'].unique())
#Rom
ROM = st.selectbox("Rom(in gb)",df['ROM'].unique())
# type
Extendable_Upto = st.selectbox("Expandable upto",df['Extendable_Upto'].unique())
#processor
Processor = st.selectbox("Processor",df['Processor'].unique())
#Front camera
Front_Camera = st.selectbox("Front Camera(in MP)",df['Front_Camera'].unique())
#Rear camera
Rear_Camera = st.selectbox("Rear Camera(in MP)",df['Rear_Camera'].unique())
#screen size
Screen_Size = st.selectbox("Screen Size",df['Screen_Size'].unique())
#battery
Battery = st.selectbox("Battery(mAh)",df['Battery'].unique())
#Colour
Colour = st.selectbox("Colour",df['Colour'].unique())
#Display
Display = st.selectbox("Display",df['Display'].unique())
#is lithium
Lithium_ion_Battery = st.selectbox("Battery(lithium ion or not?)",["yes","no"])
Avg_Rating = st.selectbox("Aaverage rating",df['Avg_Rating'].unique())
# Price=20000
if st.button('Predict Price'):
    #query
    if Lithium_ion_Battery=="yes":
        Lithium_ion_Battery=1
    else:
        Lithium_ion_Battery=0
    # query=np.array([Brand,int(RAM),int(ROM),int(Extendable_Upto),Processor,int(Front_Camera),int(Rear_Camera),int(Screen_Size),int(Battery),Colour,Display,int(Lithium_ion_Battery),int(Avg_rating)])

    query_dict = {
        "Brand": [Brand],
        "RAM": [RAM],
        "ROM": [ROM],
        "Extendable_Upto": [Extendable_Upto],
        "Processor": [Processor],
        "Front_Camera": [Front_Camera],
        "Rear_Camera": [Rear_Camera],
        "Screen_Size": [Screen_Size],
        "Battery": [Battery],
        "Colour": [Colour],
        "Display": [Display],
        "Lithium_ion_Battery": [Lithium_ion_Battery],
        "Avg_Rating": [Avg_Rating]
    }
    # query = pd.DataFrame(query_dict)
    query = pd.DataFrame(query_dict)
    print(query)
    # query = query.reshape(1,13)
    prediction = pipe.predict(query)
    # st.title("The price of Mobile is " + str(prediction))
    st.title("Price of Phone is " + str(int(prediction)))