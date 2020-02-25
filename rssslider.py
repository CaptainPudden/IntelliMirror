import feedparser
import tkinter

feed = feedparser.parse('https://www.reddit.com/r/anime/search.rss?q=flair_name%3A%22Episode%22&restrict_sr=1&sort=new')
feedShow = {'entries': [{feed['entries'][0]['title']}]}

class RSSTicker(tkinter.Text):
    def __init__(self, parent, feedname, removeword, **kw):
        super().__init__(parent, height=1, wrap="none", state='disabled', **kw)
        self.feedname = feedname
        self.removeword = removeword
        self.headlineIndex = 0
        self.text = ''
        self.pos = 0
        self.after_idle(self.updateHeadline)
        self.after_idle(self.tick)
        self.after_idle(self.updatefeed)
        self.feed = feedparser.parse(self.feedname)

    def updatefeed(self):
        self.feed = feedparser.parse(self.feedname)
        self.after(60000, self.updatefeed)

    def updateHeadline(self):
        try:
            self.text += '.....' + self.feed['entries'][self.headlineIndex]['title'].replace(self.removeword, "")
        except IndexError:
            self.headlineIndex = 0
            self.text = self.feed['entries'][self.headlineIndex]['title']

        self.headlineIndex += 1
        if self.headlineIndex > 12:
            self.headlineIndex = 0
        self.after(500, self.updateHeadline)

    def tick(self):
        if self.pos < len(self.text):
            self.config(state='normal')
            self.insert('end', self.text[self.pos])
            self.pos += 1
            self.see('end')
            self.config(state='disabled')
        self.after(150, self.tick)

if __name__ == '__main__':
    root = tkinter.Tk()
    ticker = RSSTicker(root, 'https://www.reddit.com/r/anime/search.rss?q=flair_name%3A%22Episode%22&restrict_sr=1&sort=new', 'discussion', bg='black', fg='white', font=("arial", 20))
    ticker.pack(side='top', fill='x')
    root.mainloop()