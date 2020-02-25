import tkinter
from time import strftime 


class ClockClass(tkinter.Label):
    def __init__(self, parent, **kw):
        tkinter.Label.__init__(self, parent, **kw)
        self.after_idle(self.time)
        self.pack()


    def time(self):
        # lists for ordinators
        dayslistones = [1,21,31]
        dayslisttwos = [2,22]
        dayslistthrees = [3,23]
        self.day = int(strftime('%d'))
        if self.day in dayslistones:
            ordinator = 'st'
        elif self.day in dayslisttwos:
            ordinator = 'nd'
        elif self.day in dayslistthrees:
            ordinator = 'rd'
        else:
            ordinator = 'th'

        self.text = strftime('%A, %B %d' + ordinator + ', %I:%M:%S %p') 
        self.config(text = self.text)
        self.after(1000, self.time)
    
# test clause for making changes
if __name__ == '__main__':
    root = tkinter.Tk()
    clock = ClockClass(root, bg='black', fg='white', font=("arial", 20), bd=0)
    clock.pack(side='top', fill='x')
    root.mainloop()
