from tkinter import*
import random
from tkinter import messagebox
import tkinter

root=Tk()
root.title("Memory Matching Game!")
# root.geometry("500*550")

global winner,matches
# set winner counter to 0
winner=0

# create our matches
matches=[1,1,2,2,3,3,4,4,5,5,6,6]
# matches[0]
# suffle our matches
random.shuffle(matches)
# create button frame
my_frame=Frame(root)
my_frame.pack(pady=10)
# define some variables
count=0
answer_list=[]
answer_dict={}

# reset the game
def reset():
    global matches,winner
    winner=0
    matches=[1,1,2,2,3,3,4,4,5,5,6,6]
    # shuffle our matches
    random.shuffle(matches)
    # reset label
    my_label.config(text=" ")
    # reset our title
    button_list=[b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11]
    # loop the change button colors
    for button in button_list:
        button.config(text=" ",bg="SystemButtonFace",state="normal")
 
     
# create winner function
def win():
    my_label.config(text="congratulation! you won!!!",font=("Arial Bold",50))
    button_list=[b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11]
    # loop the change button colors
    for button in button_list:
        button.config(bg="blue")
 
# function for clicking button
def button_click(b,number):
    global count,answer_list,answer_dict,winner
    
    if b["text"]==" " and count<2:
        b["text"]=matches[number]
        # add number to answer list
        answer_list.append(number)
        # add button and number to answer dictionary
        answer_dict[b]=matches[number]
        # increment our counter
        count+=1
        # print(answer_dict)
    
    # start to determine correct or not
    if len(answer_list)==2:
        if matches[answer_list[0]]==matches[answer_list[1]]:
            my_label.config(text="match!")
            for key in answer_dict:
                key["state"]="disabled"
            count=0
            answer_list=[]
            answer_dict={}
            # increment our winner counter
            winner+=1
            if winner ==6:
                win()
        else:
            my_label.config(text="Sorry!")
            count=0
            answer_list=[]
            # pop up box
            messagebox.showinfo("Incorrect!","Incorrect")
            # reset the button
            for key in answer_dict:
                key["text"]=" "
            answer_dict={}

# define our button
b0=Button(my_frame,text=" ",font=("Helvetica",20),height=3,width=6,command=lambda:button_click(b0,0),relief="groove")
b1=Button(my_frame,text=" ",font=("Helvetica",20),height=3,width=6,command=lambda:button_click(b1,1),relief="groove")
b2=Button(my_frame,text=" ",font=("Helvetica",20),height=3,width=6,command=lambda:button_click(b2,2),relief="groove")
b3=Button(my_frame,text=" ",font=("Helvetica",20),height=3,width=6,command=lambda:button_click(b3,3),relief="groove")
b4=Button(my_frame,text=" ",font=("Helvetica",20),height=3,width=6,command=lambda:button_click(b4,4),relief="groove")
b5=Button(my_frame,text=" ",font=("Helvetica",20),height=3,width=6,command=lambda:button_click(b5,5),relief="groove")
b6=Button(my_frame,text=" ",font=("Helvetica",20),height=3,width=6,command=lambda:button_click(b6,6),relief="groove")
b7=Button(my_frame,text=" ",font=("Helvetica",20),height=3,width=6,command=lambda:button_click(b7,7),relief="groove")
b8=Button(my_frame,text=" ",font=("Helvetica",20),height=3,width=6,command=lambda:button_click(b8,8),relief="groove")
b9=Button(my_frame,text=" ",font=("Helvetica",20),height=3,width=6,command=lambda:button_click(b9,9),relief="groove")
b10=Button(my_frame,text=" ",font=("Helvetica",20),height=3,width=6,command=lambda:button_click(b10,10),relief="groove")
b11=Button(my_frame,text=" ",font=("Helvetica",20),height=3,width=6,command=lambda:button_click(b11,11),relief="groove")

# gride our button
b0.grid(row=0,column=0)
b1.grid(row=0,column=1)
b2.grid(row=0,column=2)
b3.grid(row=0,column=3)

b4.grid(row=1,column=0)
b5.grid(row=1,column=1)
b6.grid(row=1,column=2)
b7.grid(row=1,column=3)

b8.grid(row=2,column=0)
b9.grid(row=2,column=1)
b10.grid(row=2,column=2)
b11.grid(row=2,column=3)

my_label=Label(root,text=" ")
my_label.pack(pady=20)

# create a menu
my_menu=Menu(root)
root.config(menu=my_menu)

# create an option dropdown menu
# option_menu=Menu(my_menu,tearoff=False)
# my_menu.add_cascade(Label="Options",menu=option_menu)
# option_menu.add_command(Label="Reset_Game",command=reset)
# option_menu.add_separator()
# option_menu.add_command(Label="Exit_Game",command=root.quit)
root.mainloop()