import requests

payload = '''{
  "considerIp": "false",
  "wifiAccessPoints": [
    {
        "macAddress": "00:25:9c:cf:1c:ac",
        "signalStrength": -43,
        "signalToNoiseRatio": 0
    },
    {
        "macAddress": "00:25:9c:cf:1c:ad",
        "signalStrength": -55,
        "signalToNoiseRatio": 0
    }
  ],
}'''

r = requests.post('https://www.googleapis.com/geolocation/v1/geolocate?key=', 
params=payload)
print(r.text)
