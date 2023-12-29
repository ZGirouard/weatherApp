#Weather_Interface.py
#Written by Zach Girouard
#03/03/2023

from Weather import Weather
import tkinter as tk
import time

#This makes a window appear
root = tk.Tk()
Frame_Width = 800
Frame_Height = 500
root.geometry(f'{Frame_Width}x{Frame_Height}')

canvas = tk.Canvas(root)
canvas.pack()
canvas.config(bg="skyblue", width=Frame_Width, height=Frame_Height)
root.title("Weather Interface")

class Weather_Interface():
    def __init__(self):
        self.city = input(str("Please enter the city you wish to search: "))
        self.weather = Weather(self.city)
        self.temp = self.weather.get_temp()
        self.time = self.weather.get_time()
        self.condition = self.weather.get_conditions()
    
    def draw(self):
        canvas.create_oval(370, 150, 420, 200, fill="yellow")
        canvas.create_text(400, 100, text=self.city, fill="black", font=('Calibri 32 bold'))
        canvas.create_text(250, 300, text=str("Temp: " + self.temp), fill="black", font=('Calibri 18'))
        canvas.create_text(550, 300, text=str("Time: " + self.time), fill="black", font=('Calibri 18'))
        canvas.create_text(375, 375, text=str(self.condition), fill="black", font=('Calibri 18'))

my_interface = Weather_Interface()

while True:
        canvas.delete("all")
        my_interface.draw()
        canvas.update()
        time.sleep(0.5)

