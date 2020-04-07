import tkinter as tk
import pyautogui
win=tk.Tk()
win.title('Take Screenshot')
win.geometry('300x300')
def takescreenshot():
    screenshot=pyautogui.screenshot()
    screenshot.save('Desktop\\screenshot.png')


button=tk.Button(win,text='Capture Screenshot',command=takescreenshot)
button.pack()

win.mainloop()
