import tkinter as tk
import threading
from pytube import YouTube

def showProgress(stream,chunk,file_handle,bytesRemain):
    size=stream.filesize
    currentProgress=((size-bytesRemain)/size)*100
    scale.set(currentProgress)
    window.update()
    print("Progress:"+str(currentProgress))
        
def do_download():
    thread1=threading.Thread(target=do_job1)
    thread1.start()
    
    
      
    
def do_job1():
    global strUrl
    global onlyMusic
    strUrl.set(entryUrl.get())
    print(strUrl.get())
    #https://www.youtube.com/watch?v=iKUwMUjavP4
        
    
    
    
    try:
        yt=YouTube(strUrl.get(),on_progress_callback=showProgress)
        
        if onlyMusic.get():
            stream=yt.streams.filter(only_audio=True).first()
        else:
            stream=yt.streams.first()
            
        stream.download()    
        print(stream)
    except:
        print("fail")    
def onCheckBoxClick():
    global checkMusic
    if onlyMusic.get():
        onlyMusic.set(0)
        window.update()
    else:
        onlyMusic.set(1)
        window.update()






window=tk.Tk()
window.title("音樂")
window.geometry('1000x600')
#window.iconbitmap("music.ico")
window.configure(bg='black')

label=tk.Label(window,text="URL",font=('aaaaaaaa',22))
label.pack()

onlyMusic=tk.IntVar()
onlyMusic.set(0)

checkMusic=tk.Checkbutton(window,text="only Music",variable=onlyMusic,onvalue=1,offvalue=0,command=onCheckBoxClick)
checkMusic.pack()



strUrl=tk.StringVar()
entryUrl=tk.Entry(window,width=50)
entryUrl.pack()

button=tk.Button(window,text="Download",command=do_download)
button.pack()

scale=tk.Scale(window,label="Progress",
               orient=tk.HORIZONTAL,
               from_=0,
               to=100)
scale.pack()




window.mainloop()