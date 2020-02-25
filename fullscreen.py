from tkinter import Tk, Frame, Label, TOP, BOTH, BOTTOM, YES, LEFT
from rssslider import RSSTicker
from clockclass import ClockClass
from imageclass import ImageLabel
from weatherclass import WeatherClass

class FullscreenWindow:

    def __init__(self):
        self.tk = Tk()
        self.tk.configure(background='red', highlightbackground='black', cursor='none')
        self.topFrame = Frame(self.tk, background = 'black', highlightbackground='black')
        self.topFrame.pack(side = TOP, fill=BOTH, expand = YES)
        self.midFrame = Frame(self.tk, background = 'black')
        self.midFrame.pack(fill=BOTH, expand = YES)
        self.bottomFrame = Frame(self.tk, background = 'black')
        self.bottomFrame.pack(side = BOTTOM, fill=BOTH, expand = YES)
        self.state = False
        self.tk.bind("<Return>", self.toggle_fullscreen)
        self.tk.bind("<Escape>", self.end_fullscreen)
        self.weather = WeatherClass(self.topFrame, 'http://api.openweathermap.org/data/2.5/weather?appid=c24a72fa13c5723fe9a0224b4f62a829&q=san%20diego',
            bg='black', fg='white', font=('arial', 15), bd=0, highlightbackground='black')
        #RSSfeed the first
        self.anime = RSSTicker(self.bottomFrame, 'https://www.reddit.com/r/anime/search.rss?q=flair_name%3A%22Episode%22&restrict_sr=1&sort=new', 'discussion', 
            bg='black', fg='white', font=("arial", 20), bd=0, highlightbackground='black')
        self.anime.pack(side=LEFT, fill=BOTH, expand=YES)
        self.anime2 = RSSTicker(self.tk, 'https://www.reddit.com/r/worldnews/hot.rss', '', 
            bg='black', fg='white', font=("arial", 20), bd=0, highlightbackground='black')
        self.anime2.pack(side=LEFT, fill=BOTH, expand=YES)
        #Load clock for Top
        self.clock = ClockClass(self.topFrame, bg='black', fg='white', font=("arial", 20), bd=0, pady=50)
        self.clock.pack()
        #Load image for center
        self.giffy = ImageLabel(self.midFrame, border = 0)
        self.giffy.pack()
        self.giffy.load('icon2.gif')
    



    def toggle_fullscreen(self, event=None):
        self.state = not self.state  # Just toggling the boolean
        self.tk.attributes("-fullscreen", self.state)
        return "break"

    def end_fullscreen(self, event=None):
        self.state = False
        self.tk.attributes("-fullscreen", False)
        return "break"

if __name__ == '__main__':
    root = FullscreenWindow()
    root.tk.mainloop()