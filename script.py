import requests
import json
import numpy as np

url = 'https://covid.ourworldindata.org/data/owid-covid-data.json'
newCasesList = []

if __name__ == "__main__":
   inputPercentile = input('Введите перцентиль: ')
   inputCountryCode = input('Введите код страны, по которому нужно собрать статистику: ')
   req = requests.get(url)
   if(req.status_code == 200):
       dataJSON = req.json()
       for countryCode in dataJSON:
           if(inputCountryCode == countryCode):
               countryData = dataJSON[inputCountryCode]['data']
               for eachData in countryData:
                   newCasesList.append(eachData['new_cases'])
   percentileNewCases = np.percentile(newCasesList, float(inputPercentile))
   print(percentileNewCases)