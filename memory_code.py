import tkinter as tk
# import 
# from tkinter.constants import BOTTOM
window = tk.Tk()

# to rename the title of the window 
window.title("GUI")

# pack is used to show the object in the window 

# label=tk.Label(window,text="Hello world").pack()
# window.mainloop()

# for title name 
var=tk.Label(window,text="Memory_Game",font=("Arial Bold",50))
window.geometry('350x200')
var.grid(column=0,row=8)

# for button of numbers
bt=tk.Button(window,text="Enter",bg="skyblue",fg="black")
bt.grid(column=5,row=9)

# toop_frame=tk.Frame(window).pack()
# bottom_frame=tk.Frame(window).pack(side="bottom")

# bt1=tk.Button(toop_frame,text="Button 1",fg="grey").pack()
#bt2=tkinter.Button(toop_frame,text="Button 2",fg="grey").pack()
# bt3=tkinter.Button(toop_frame,text="Button 3",fg="grey").pack()
# bt4=tkinter.Button(toop_frame,text="Button 4",fg="grey").pack()
# bt5=tkinter.Button(toop_frame,text="Button 5",fg="grey").pack()
# bt6=tkinter.Button(toop_frame,text="Button 6",fg="grey").pack()
# bt7=tkinter.Button(toop_frame,text="Button 7",fg="grey").pack()
# bt8=tkinter.Button(toop_frame,text="Button 8",fg="grey").pack()
# bt9=tkinter.Button(toop_frame,text="Button 9",fg="grey").pack()
window.mainloop()