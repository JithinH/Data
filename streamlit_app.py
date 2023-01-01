#importing required libraries 

import pandas as pd 
import streamlit as st

#from PIL import Image
#import pip
#pip.main(["install", "openpyxl"])
#above three codes can be used if pictures are required

#basic page setup and code for accessing required files
st.set_page_config(page_title='COMPANY NAME')
st.markdown('<div style="text-align: center;">GLASSCRAFTERS</div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: center;">Glass Inventory</div>', unsafe_allow_html=True)
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
makers=df.style.format(precision=0)

#display searched elements	
# st.table(makers.dropna())


