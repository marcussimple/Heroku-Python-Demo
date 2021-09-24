import streamlit as st
#import plotly.express as px
import pandas as pd


#configuration
st.set_option("deprecation.showfileUploaderEncoding",False)

#title of app
st.title("Data visualisation App")

#Add sidebar
st.sidebar.subheader("Visualization settings")

#Setup file upload
# uploaded_file = st.sidebar.file_uploader(label="Upload your CSV or Excel file", 
#                                         type=['csv','xlsx','xls'])

# global df
# if uploaded_file is not None:
#     print("hello")
#     try:
#         df = pd.read_csv(uploaded_file)
#     except Exception as e:
#         print(e)
#         df = pd.read_excel(uploaded_file)
#     st.write(df)

#     st.text_input("to delete")