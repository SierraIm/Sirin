import requests

def weather(city):
    city = "110000";
    url = "https://restapi.amap.com/v3/weather/weatherInfo?key=80c6ed9f9d558da85f26459bcc0c8339&city=" + city;
    response = requests.get(url);
    print (response.text);