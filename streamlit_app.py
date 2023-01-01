#importing required libraries 

import pandas as pd 
import streamlit as st

#basic page setup and code for accessing required files

st.set_page_config(page_title='GLASS INVENTORY')
x=st.markdown('GLASSCRAFTERS')
y=st.markdown('Glass Inventory')
name_1=x.center(60)
name_2=y.center(60)
excel_file='final_data_1.xlsx'
sheet_name='Sheet1'

#data accessing from excel 

df=pd.read_excel(excel_file,
                sheet_name=sheet_name,
                usecols='A:M',
                header=0)
                
                 

#search bar

to_find=st.text_input('Type to search',label_visibility="visible")
makers=df.where((df['COLOUR']==to_find) | (df['TYPE']==to_find) | (df['SPECTRUM CODE']==to_find) | (df['GLASSCRAFTERS CODE']==to_find) | (df['SHADE']==to_find) | (df['NAME']==to_find) | (df['SHELF']==to_find))

#display searched elements	

st.table(makers.dropna())

# */ Project by CMRIT students
# 	Deekshita S
# 	Devyashree Menon	
# 	Jaynth R
# 	Jithin HS
# 	Madhushree L
# 	Meghana Singh  /*
