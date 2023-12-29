#Weather.py
#Written by Zach Girouard
#03/02/2023

#import libraries
import requests
from bs4 import BeautifulSoup

#Weather class
class Weather():
    #Ask user for city input as a string
    def __init__(self, city):
        self.city = city
        print()
        Weather.fetch_data(self)
    
    #Fetch data for specific city using a google search
    def fetch_data(self):
        search = "https://www.google.com/search?q=" + "google weather" + self.city
        
        #Request data from the page
        html = requests.get(search).content

        #Get raw html data
        self.raw_data = BeautifulSoup(html, 'html.parser')

        #Get specific, readable data
        Weather.get_time(self)
        Weather.get_temp(self)
        Weather.get_conditions(self)
        Weather.get_additional_data(self)
    
    #Gets temperature of the city
    #NOTE due to National Weather Service alerts inferering with the html, a "special case" has been implemented to only grab the temp
    def get_temp(self):
        temp = self.raw_data.find('div', attrs = {'class': 'BNeawe iBp4i AP7Wnd'}).text
        special_case = []

        #Get only the numeric data
        if temp[0].isnumeric() and temp[1].isnumeric():
            return temp
        
        #Append temp to special case
        else:
            for i in range(len(temp)):
                if temp[i].isnumeric():
                    special_case.append(temp[i])
                else:
                    pass
            
            #Print out special case and degrees at the end
            temp = str(special_case[0] + special_case[1] + temp[-2] + temp[-1])
            return temp
    
    #Get the current time of the city
    def get_time(self):
        self.time = self.raw_data.find('div', attrs = {'class': 'BNeawe tAd8D AP7Wnd'}).text
        self.time = self.time.split('\n')
        return self.time[0]
    
    #Get the current conditions, found when we found the time in get_time
    def get_conditions(self):
        return self.time[1]

    #Get additional data from the city
    def get_additional_data(self):
        data_list = self.raw_data.find_all('div', attrs = {'class': 'BNeawe s3v9rd AP7Wnd'})
        selective_list = data_list[4].text

        #Will only print news if it corresponds to the selective_list
        #NOTE: Sometimes this section just includes extra data and not news
        if ';' or ',' in selective_list:
            pass
        else:
            return selective_list