import json
from config.database import *

with open('./app/holiday.json', 'r', encoding='utf-8') as h:
    holiday = json.loads(h.read())
    
    data_holiday = holiday['result']['data']

    try:
        for i in range(len(data_holiday)):
            date_holiday = data_holiday[i]['Date']
            date_date_thai = data_holiday[i]['DateThai']
            date_holiday_description = str(data_holiday[i]['HolidayDescription']).replace("'", "''")
            date_holiday_description_thai = str(data_holiday[i]['HolidayDescriptionThai']).replace("'", "''")
            
            database.commit(
                """

                INSERT INTO FCN_Holiday
                (
                    Date, DateThai, HolidayDescription, HolidayDescriptionThai
                )

                VALUES
                (
                    '""" + date_holiday + """', '"""+ date_date_thai + """', '"""+ date_holiday_description + """', 
                    '"""+ date_holiday_description_thai + """'
                )

                """
            )
            
            print(date_holiday + '|' + date_holiday_description_thai)
            
    except Exception as e:
        print(e)