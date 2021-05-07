# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def get_sheet_data():
    import gspread
    import pandas as pd
    from oauth2client.service_account import ServiceAccountCredentials
    
    # use creds to create a client to interact with the Google Drive API
    scope =["https://spreadsheets.google.com/feeds",
            'https://www.googleapis.com/auth/spreadsheets',
            "https://www.googleapis.com/auth/drive.file",
            "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)
    
    # Find a workbook by name and open the first sheet
    # Make sure you use the right name here.
    sheet = client.open("WSP_Test_Data").sheet1
    data = pd.DataFrame(sheet.get_all_records())
    return(data)