#importing required libraries 

import pandas as pd 
import streamlit as st

#from PIL import Image
#import pip
#pip.main(["install", "openpyxl"])
#above three codes can be used if pictures are required

#basic page setup and code for accessing required files
st.set_page_config(page_title='COMPANY NAME')
st.markdown('<h1 style="text-align: center; color: Red;">GLASSCRAFTERS</h1>', unsafe_allow_html=True)
st.markdown('<h2 style="text-align: center;color: blue;">Glass Inventory</h2>', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)

with col1:
    st.write(' ')

with col2:
    st.image("https://st2.depositphotos.com/1025323/11461/i/950/depositphotos_114615432-stock-photo-digital-life-of-stained-glass.jpg")

with col3:
    st.write(' ')
excel_file='final_data_2.xlsx'
sheet_name='Sheet1'

#data accessing from excel 
df=pd.read_excel(excel_file,
                sheet_name=sheet_name,
                usecols='A:M',
                header=0)
                
                 
# st.dataframe(df)
#search bar
to_find=st.text_input('Enter glass colour or type',label_visibility="visible")
makers=(df.where((df['COLOUR']==to_find) | (df['TYPE']==to_find) | (df['SPECTRUM CODE']==to_find) | (df['GLASSCRAFTERS CODE']==to_find) | (df['SHADE']==to_find) | (df['SHELF']==to_find)))

#display searched elements	
st.table(makers.dropna())


