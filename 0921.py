import tkinter as tk
import tkinter.messagebox as messagebox

window=tk.Tk()
window.title("螢幕視窗")
window.geometry('500x300')


label=tk.Label(window,
               text="??????",
               font=('Segoe UI Black',22),
               bg='black',
               fg='#abedca'
               )

label.pack()

def do_job():
    messagebox.showinfo(title='prompt',message='Open File')
def do_select():
    label.config(text=appearance.get())



menuBar=tk.Menu(window)



filemenu=tk.Menu(menuBar,tearoff=False)


filemenu.add_command(label='New',command=do_job)
filemenu.add_command(label='Open',command=do_job)
filemenu.add_command(label='Save',command=do_job)
filemenu.add_separator()
filemenu.add_command(label='Exit',command=window.destroy)



menuBar.add_cascade(label='File',menu=filemenu)

window.config(menu=menuBar)

appearance=tk.StringVar()
appearance.set("NULL")

rA=tk.Radiobutton(window,text='我好帥',variable=appearance,value='100分',command=do_select)
rB=tk.Radiobutton(window,text='我好醜',variable=appearance,value='0分',command=do_select)

rA.pack()
rB.pack()










window.mainloop()