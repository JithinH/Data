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
from typing import Union, Dict
from io import BytesIO, StringIO
import json
import pandas as pd
import requests
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

def read_private_file_from_gdrive(
    file_url: str, file_format: str, google_auth: GoogleAuth, **kwargs
) -> Union[pd.DataFrame, Dict, str]:
    """Read private files from Google Drive.

    Parameters
    ----------
    file_url : str
        URL adress to file in Google Drive.

    file_format : str
        File format can be 'csv', 'xlsx', 'parquet', 'json' or 'txt'.

    google_auth: GoogleAuth
        Google Authentication object with access to target account. For more
        information on how to login using Auth2, please check the link below:
        https://docs.iterative.ai/PyDrive2/quickstart/#authentication

    Returns
    -------
    Union[pd.DataFrame, Dict, str].
        The specified object generate from target file.

    """
    drive = GoogleDrive(google_auth)

    # Parsing file URL
    file_id = file_url.split("/")[-2]

    file = drive.CreateFile({"id": file_id})

    content_io_buffer = file.GetContentIOBuffer()

    if file_format == "csv":
        return pd.read_csv(
            StringIO(content_io_buffer.read().decode()), **kwargs
        )

    elif file_format == "xlsx":
        return pd.read_excel(content_io_buffer.read(), **kwargs)

    elif file_format == "parquet":
        byte_stream = content_io_buffer.read()
        return pd.read_parquet(BytesIO(byte_stream), **kwargs)

    elif file_format == "json":
        return json.load(StringIO(content_io_buffer.read().decode()))

    elif file_format == "txt":
        byte_stream = content_io_buffer.read()
        return byte_stream.decode("utf-8", **kwargs)
# excel_file=pd.read_excel(r'C:\Users\Jithin H S\Downloads\final_data.xlsx')
sheet_name='Sheet1'

#data accessing from excel 

                
                 
# st.dataframe(df)
#search bar
to_find=st.text_input('Enter glass colour or type',label_visibility="visible")
makers=df.where((df['COLOUR']== to_find) | (df['TYPE']== to_find))

#display searched elements	
st.table(makers.dropna())


