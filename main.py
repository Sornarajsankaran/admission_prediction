import pickle
import streamlit as st

import sklearn

st.write("""
 # Admission Prediction
 """)
st.write("""
### GRE Score""")
gre=st.number_input("Enter Gre Score",min_value=290,max_value=340)

st.write("""
### TOEFL Score""")
toefl=st.number_input("Enter Toefl Score",min_value=90,max_value=120)

st.write("""
### University Rating""")

univer_rating=st.selectbox("Enter your University Ranking",[1,2,3,4,5])


st.write("""
### SOP""")

sop=st.selectbox("Enter your SOP Ranking",[1,2,3,4,5])


st.write("""
### LOP""")

lop=st.selectbox("Enter your LOP Ranking",[1,2,3,4,5])

st.write("""
### CGPA""")

cgpa=st.number_input("Enter Your CGPA",min_value=0.0,max_value=10.0,step=0.1,value=10.0)

st.write("""
### Research Details""")

research=st.radio("No of Research Paper Published ",options=[0,1,2,3])

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://images.pexels.com/photos/1931141/pexels-photo-1931141.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()
model=pickle.load(open("admission_model.pkl","rb"))

if st.button("Predict"):
    predicted_value=model.predict([[gre,toefl,univer_rating,sop,lop,cgpa,research]])

    if predicted_value>0.5:
        st.success("#### You are selected ")
    else:
        st.success("#### You are not selected ")

