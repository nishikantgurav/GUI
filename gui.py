'''import tkinter as tk
r = tk.Tk()
r.title('Counting Seconds')
button = tk.Button(r, text='Stop', width=25, command=r.destroy)
button.pack()
r.mainloop()'''
#from tkinter import *
import tkinter as tk
root = tk.Tk()
user=input("Enter your name: ")
password=input("Enter your password: ")
if user== "demo":
    win=tk.Tk()
    win.title("Hello")
    lb=tk.Label(win,text="Hello")
    lb.pack()
    win.mainloop()
else:
    print("Nohing")
