import http.client

conn = http.client.HTTPSConnection("apigw1.bot.or.th")

key = "29cd2bfc-8018-4480-9569-bb457e2081ef"
year = "2021"


headers = {
    'x-ibm-client-id': key,
    'accept': "application/json"
    }

conn.request("GET", f"/bot/public/financial-institutions-holidays/?year={year}", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))