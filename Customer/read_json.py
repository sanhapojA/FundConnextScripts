import json
from datetime import date, datetime, timedelta

for d in range(0, 386):
    textTime = date(2021, 5, 18) - timedelta(days = d) # 20200428
    textTime = str(textTime.strftime('%Y%m%d'))
    
    try:
    # Opening JSON file
        f = open('P:/FundConnext/FundConnext-PRD/Download Files/SA_Customers/'+textTime+'_IAM_CustomerProfile/'+textTime+'_IAMSA_INDIVIDUAL.json', 'r', encoding='UTF-8')

        # returns JSON object as
        # a dictionary
        data = json.load(f)
        
        # Iterating through the json
        
        for i in range(len(data)):
            thFirstName = data[i]['thFirstName']
            thLastName = data[i]['thLastName']
            cardNumber = data[i]['cardNumber']
            cddScore = data[i]['cddScore']
            print(textTime+'|'+str(cardNumber+'|'+str(cddScore)+'|'+str(thFirstName)+'|'+str(thLastName)))
    
    except:
        pass
