#importing required libraries 

import pandas as pd 
import streamlit as st


# from PIL import Image
# import pip
# pip.main(["install", "openpyxl"])
#above three codes can be used if pictures are required

#basic page setup and code for accessing required files
st.set_page_config(page_title='COMPANY NAME')
st.header('GLASS CRAFTERS')
st.subheader('Glass Inventory')
excel_file=pd.read_excel(r'https://drive.google.com/drive/folders/16XQ1urBhPzrf54ldBMMmPJyJ4_z0NiQB?usp=sharing')
sheet_name='Sheet1'

#data accessing from excel 

                
                 
# st.dataframe(df)
#search bar
to_find=st.text_input('Enter glass colour or type',label_visibility="visible")
makers=df.where((df['COLOUR']== to_find) | (df['TYPE']== to_find))

#display searched elements	
st.table(makers.dropna())


