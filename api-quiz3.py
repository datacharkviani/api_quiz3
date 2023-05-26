# დავალება N1
import requests
import json
import sqlite3

url = "https://hotels4.p.rapidapi.com/locations/v2/search"

key = "083ebb93f4msha5dfa7fcd7ae78ap1c89b7jsn83478efd4bf6"

city = "New York"

params = {"query": city,
          "locale":"en_US",
          "currency":"USD"}

headers = {"X-RapidAPI-Key": key}

response = requests.get(url, headers=headers, params=params)

res = json.loads(response.text)
res_structured = json.dumps(res, indent=4)

# print(res_structured)
# print(res)
print(response.status_code)
print(response.headers)



#  დავალება N2, json მონაცემებს ინახავს json ფაილში სტრუქტურულად
response1 = response.json()
with open('data.json', 'w') as file:
    json.dump(response1, file, indent=4)

# დავალება N3, წამოიღებს ინფორმაციას hotel API-დან.
hotel_name = res["suggestions"][1]['entities'][0]['name']
hotel_latitude = res["suggestions"][1]['entities'][0]['latitude']
landmark_name = res["suggestions"][2]['entities'][2]['name']
landmark_latitude = res["suggestions"][2]['entities'][2]['latitude']
transport_name = res["suggestions"][3]['entities'][2]['name']
transport_latitude = res["suggestions"][3]['entities'][2]['latitude']

print(hotel_latitude,"\n", hotel_name, "\n", landmark_latitude, "\n", landmark_name,
      "\n", transport_latitude,"\n", transport_name)

# დავალება N4, API-დან წამოღებულ ინფორმაციით ქმნის ცხრილს sqlite3 მოდულის საშუალებით
connection = sqlite3.connect('traveling_db')
cursor = connection.cursor()

cursor.execute(""" CREATE TABLE traveling_db (
            " " CHAR(50),
            Hotel CHAR(50) NOT NULL,
            Landmark CHAR(50) NOT NULL,
            Transport CHAR(50) NOT NULL
            )""" )


cursor.execute("""INSERT INTO traveling_db( " ", Hotel, Landmark, Transport) VALUES (?, ?, ?, ?)""",
               ( "Name ", hotel_name, landmark_name, transport_name))

cursor.execute("""INSERT INTO traveling_db( " " , Hotel, Landmark, Transport) VALUES (?, ?, ?, ?)""",
               ( "Latitude", hotel_latitude, landmark_latitude, transport_latitude))



connection.commit()
connection.close()







