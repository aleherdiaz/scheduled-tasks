import requests
import smtplib
import os

api_key = os.environ.get("OWM_API_KEY")
url = r"https://api.openweathermap.org/data/2.5/weather"
endpoint = r"https://api.openweathermap.org/data/2.5/forecast"
my_email = os.environ.get("MY_EMAIL")
password = os.environ.get("MY_PASSWORD")

weather_parameters = {
    "lat"   : 43.826601,
    "lon"   : -72.849672,
    "appid" : api_key,
    "cnt"   : 4

}

response = requests.get(url=endpoint, params=weather_parameters)
response.raise_for_status()
if response.status_code == 200:
    print("Success!")
elif response.status_code == 404:
    print("Not Found.")
weather_data = response.json()
#print(weather_data)

will_rain = False
ids = []
for i in range(4):
    ids.append(int(weather_data["list"][i]["weather"][0]["id"]))
    if ids[i] < 700:
        will_rain = True
if will_rain:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # Encripted
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="alejandro26hd.backup@gmail.com",
            msg="Subject: It's going to rain \n\n Bring an umbrella")
