import tkinter as tk
from pytube import YouTube
window=tk.Tk()
window.title("音樂")
window.geometry('1000x600')
window.iconbitmap("music.ico")
window.configure(bg='black')




yt=YouTube("https://www.youtube.com/watch?v=HK7SPnGSxLM")
stream=yt.streams.first()
stream.download("C:\\Users\\Administrator\\.spyder-py3","說好不哭")

stream=yt.streams.filter(res="720p",fps=30).first()
stream.download("C:\\Users\\Administrator\\.spyder-py3","說好不哭")


window.mainloop()
