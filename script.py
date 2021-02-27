import requests
import numpy

url = 'https://covid.ourworldindata.org/data/owid-covid-data.json'


if __name__ == "__main__":
   req = requests.get(url)
   if(req.status_code == 200):
       dataJSON = req.json()
       for countryCodes in dataJSON:
           print(countryCodes)