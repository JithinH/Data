#importing required libraries 

import pandas as pd 
import streamlit as st

#basic page setup and code for accessing required files
st.set_page_config(page_title='GLASS INVENTORY')
st.markdown('<h1 style="text-align: center; color: Red;">GLASSCRAFTERS</h1>', unsafe_allow_html=True)
st.markdown('<h2 style="text-align: center;color: yellow;">Glass Inventory</h2>', unsafe_allow_html=True)
excel_file='real_data.xlsx'
sheet_name='Sheet1'

#data accessing from excel 

df=pd.read_excel(excel_file,
                sheet_name=sheet_name,
                usecols='A:M',
                header=0)
                
                 

#search bar

to_find=st.text_input('Type to search',label_visibility="visible")
makers=df.where((df['COLOUR']==to_find) | (df['TYPE']==to_find) | (df['GLASSCRAFTERS CODE']==to_find) | (df['SHADE']==to_find) | (df['NAME']==to_find) | (df['SHELF NUMBER']==to_find))

#display searched elements	

st.table(makers.dropna())

# */ Project by CMRIT students
# 	Deekshita S
# 	Devyashree Menon	
# 	Jaynth R
# 	Jithin HS
# 	Madhushree L
# 	Meghana Singh  /*
