import streamlit as st
import pandas as pd, numpy as np, matplotlib.pyplot as plt, seaborn as sns

# 1. Title and Subheader

st.title("Data analysis : Case study 7")
st.subheader("Data analysis using python and streamlit")

# 2. Upload Dataset

upload = st.file_uploader("Please upload your file (in CSV format)")
if upload is not None:
    data = pd.read_csv(upload)


# show dataset
if upload is not None:
    if st.checkbox("Preview dataset"):
        if st.button("head"):
            st.write(data.head())
        if st.button("Tail"):
            st.write(data.tail())
            
# 4. Check DataType of Each Column
if upload is not None:
    if st.checkbox("datatypes"):
        st.write(data.dtypes)   
             
# 5. Find Shape of Our Dataset (Number of Rows And Number of Columns)

if upload is not None:
    data_shape = st.radio("What Dimension Do You Want To Check?",('Row','Columns'))
    if data_shape=='Row':
        st.text("Number of rows")
        st.write(data.shape[0])
    if data_shape=='Columns':
        st.text("Number of rows")
        st.write(data.shape[1])
        
# 6. Find Null Values in The Dataset

if upload is not None:
    test = data.isnull().values.any()
    if test==True:
        if st.checkbox("Null values in datasets"):
            sns.heatmap(data.isnull())
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.pyplot()
    else:
        st.success("Congratulations! No null values")
        
# 7. Find Duplicate Values in the dataset

if upload is not None:
     test = data.duplicated().any()
     if test==True:
        st.warning("Warning: your data contain some duplicate values")
        dup = st.selectbox("Want to remove duplicates?",("Yes","No"))
        if dup =="Yes":
            data = data.drop_duplicates()
            st.text("Duplicates are removed")
        if dup =='No':
            st.text("No problem")

# 8. Get Overall Statistics

if upload is not None:
    if st.checkbox("Get overall statistics"):
        st.write(data.describe(include="all"))


        