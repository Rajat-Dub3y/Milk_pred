import sklearn
import pickle
import streamlit as st
model=pickle.load(open("dtmodel3.pkl",'rb'))
st.title("Milk Quality")
ph=st.number_input("ph")
temp=st.number_input("Temperature")
taste=st.number_input("Taste")
odor=st.number_input("Odor")
fat=st.number_input("Fat")
turbidity=st.number_input("Turbidity")
color=st.number_input("Colour")
def prediction(ph,temp,taste,odor,fat,turbidity,color):
    output = model.predict([[ph,temp,taste,odor,fat,turbidity,color]])
    if output[0]==0:
        st.write(f"Grade is Low")
    elif output[0]==1:
        st.write(f"Grade is Medium")
    else:
        st.write(f"Grade is High")
if st.button("submit"):
    prediction(ph,temp,taste,odor,fat,turbidity,color)