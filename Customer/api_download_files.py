import requests
import os
import json
from datetime import date, datetime, timedelta
from zipfile import ZipFile

# dates = datetime.today()
# dates = date.strftime('%Y%m%d')

#date = '20210215'

def make_folder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Create Disrectory. ' + directory)

def api_auth():
    url = "https://www.fundconnext.com/api/auth?username=API_IAM01&password=Yc7#%+Ex79//9F+d"
    payload = '{"username": "API_IAMSA01","password": "@bhjKz7Aj6E*&PoB\"}'
    headers = {'Content-Type': 'application/json'}
    response = requests.request("POST", url, headers=headers, data=payload)

    token = json.loads(response.text)
    return token['access_token']

def api_download_files():

    file_name = 'CustomerProfile'


    # for i in range(0,386): #386
        
        # textTime = date(2021, 5, 18) - timedelta(days = i)
        # textTime = str(textTime.strftime('%Y%m%d'))
    textTime = '20210619'

    url = 'https://www.fundconnext.com/api/files/' + textTime + '/' + file_name + '.zip' # --- ระบุวันที่ต้องการดึงไฟล์
    payload = '{"username": "API_IAMSA01","password": "@bhjKz7Aj6E*&PoB\"}'
    headers = {
        'X-Auth-Token': api_auth(),
        'Content-Type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    make_folder(r'P:/FundConnext/FundConnext-PRD/Download Files/' + 'SA_Customers' + '/' + textTime + '_IAM_' + file_name)

    try:
        with open(r'P:/FundConnext/FundConnext-PRD/Download Files/' + 'SA_Customers' +'/'+ textTime + '_IAM_' + file_name + '.zip', 'wb') as zip_file:
            zip_file.write(response.content) ## --- ใช้ content ในการดึงไฟล์
        file_extract = ZipFile(r'P:/FundConnext/FundConnext-PRD/Download Files/' + 'SA_Customers' +'/'+ textTime + '_IAM_'+ file_name +'.zip', 'r') # --- ไฟล์ที่ต้องการแตก.zip
        file_extract.extractall('P:/FundConnext/FundConnext-PRD/Download Files/' + 'SA_Customers' +'/'+ textTime + '_IAM_'+ file_name) # --- แตกไปไว้ที่ไหน?
    except:
        pass
    
    print('Download: ' + textTime)


api_download_files()