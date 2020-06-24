#!/usr/bin/env python3

import pyodbc
import urllib.request
import json

# tracking part
req = urllib.request.Request("http://api.open-notify.org/iss-now.json")
response = urllib.request.urlopen(req)

obj = json.loads(response.read())
timestamp = obj['timestamp']
latitude = obj['iss_position']['latitude']
longitude = obj['iss_position']['longitude']

# connection part
server = 'raivoclout.database.windows.net'
database = 'fromPS'
username = 'admraivo'
password = '$dmR4!v0'
driver= '{ODBC Driver 17 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)

# update db
cursor = cnxn.cursor()
cursor.execute("INSERT INTO dbo.f_iss_coordinates VALUES(?, ?, ?);", (timestamp, latitude, longitude))
cnxn.commit()
