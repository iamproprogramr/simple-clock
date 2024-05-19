from tkinter import *

from time import strftime

screen=Tk()
screen.geometry('350x150')
screen.configure(bg="black")
screen.title("ALARAM CLOCK BY YOUSAF")



#FRAMES

frame_line= Frame(screen,width=400,height=5,background="blue")
frame_line.grid(row=0,column=0)

frame_body= Frame(screen,width=400,height=290,background="gray")
frame_body.grid(row=78,column=0)






label = Label(frame_body, font=("arial", 20),bg='gray')
label.place(x=160,y=26)

def time():
    
    time1 = strftime("%I:%M:%S %p \n %A \n %d,%m,%Y")  
    label.config(text=time1,)
    label.after(1000, time)  

time()  

yousafabel = Label(frame_body,text="This watch is created by muhammad yousaf", font=("arial", 8,"bold"),bg='gray')
yousafabel.place(x=100,y=120)



screen.mainloop()
