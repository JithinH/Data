#importing required libraries 

import pandas as pd 
import streamlit as st
import csv

#from PIL import Image
#import pip
#pip.main(["install", "openpyxl"])
#above three codes can be used if pictures are required

#basic page setup and code for accessing required files
st.set_page_config(page_title='COMPANY NAME')
st.header('GLASS CRAFTERS')
st.subheader('Glass Inventory')
excel_file=open(r"C:/Users/Jithin H S/final_data.csv")
sheet_name='Sheet1'

#data accessing from excel 
df=pd.read_excel(excel_file,
                sheet_name=sheet_name,
                usecols='A:E',
                header=0)
                
                 
# st.dataframe(df)
#search bar
to_find=st.text_input('Enter glass colour or type',label_visibility="visible")
makers=df.where((df['COLOUR']== to_find) | (df['TYPE']== to_find))

#display searched elements	
st.table(makers.dropna())


