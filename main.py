# %%
import requests as Re
import json
import pandas as pd

headers = {'app':"REPORTS_API",
'tokenUuid':"##############",
'Content-Type':"application/json"}

response = Re.get('http://getblue.io/rest/report/api/campaigns', headers=headers)
response = response.json()
id = response[0]['CAMPANIGNID']
response2 = Re.get(f'http://getblue.io/rest/report/api/campaign/{id}', headers=headers)
response2= response2.json()

Data = []
mediaCost= []
Vendas = []
Clicks = []
Impressions = []
Sessions = []
for i in (response2):
    Data.append(i['DATE'])
    mediaCost.append(i['MEDIACOST'])
    Sessions.append(i['SESSIONS'])
    Vendas.append(i['SALES'])
    Impressions.append(i['IMPRESSIONS'])
    Clicks.append(i['CLICKS'])

DATA = pd.Series(Data)
MEDIACOST = pd.Series(mediaCost)
SESSIONS = pd.Series(Sessions)
IMPRESSIONS = pd.Series(Impressions)
CLICKS = pd.Series(Clicks)
VENDAS = pd.Series(Vendas)



dados = pd.DataFrame({'Data' : Data,'MediaCost' : mediaCost, 'Sessions' : SESSIONS, 'Impressions' : IMPRESSIONS, 'Clicks' : CLICKS, 'Vendas' : VENDAS})
