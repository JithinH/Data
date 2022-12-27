import pandas as pd 
import streamlit as st
from PIL import Image
import pip
pip.main(["install", "openpyxl"])


st.set_page_config(page_title='COMPANY NAME')
st.header('GLASS CRAFTERS')
st.subheader('Glass Inventory')
excel_file='Test.xlsx'
sheet_name='test'

df=pd.read_excel(excel_file,
                sheet_name=sheet_name,
                usecols='A:D',
                header=0)
                
                 
# st.dataframe(df)
state=st.text_input('Enter glass colour',label_visibility="visible")


makers=df.where(df['State[c]']== state,)


#st.dataframe(makers)
st.table(makers.dropna())


