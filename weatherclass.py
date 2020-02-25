import tkinter
import requests, json 
  

# api_key = "c24a72fa13c5723fe9a0224b4f62a829"
# base_url/w apikey = "http://api.openweathermap.org/data/2.5/weather?appid=c24a72fa13c5723fe9a0224b4f62a829&q="
# city = 'san%20diego' 

class WeatherClass(tkinter.Label):
    def __init__(self, parent, weatherurl, **kw):
        tkinter.Label.__init__(self, parent, **kw)
        self.weatherurl = weatherurl
        self.after_idle(self.weatherupdate)
        self.pack()

    def weatherupdate(self):
        response = requests.get(self.weatherurl)
        self.weatherjson = response.json()
        a = self.weatherjson['main']
        temp = int((a['temp']-273.15)*9/5 + 32)
        b = self.weatherjson['weather']
        self.text = 'Temp: ' + str(temp) + '°F Weather: ' + b[0]["description"]
        self.config(text=self.text)
        self.after(60000, self.weatherupdate)



if __name__ == '__main__':
    root = tkinter.Tk()
    clock = WeatherClass(root, 'http://api.openweathermap.org/data/2.5/weather?appid=c24a72fa13c5723fe9a0224b4f62a829&q=san%20diego', 
        bg='black', fg='white', font=("arial", 20), bd=0)
    clock.pack(side='top', fill='x')
    root.mainloop()