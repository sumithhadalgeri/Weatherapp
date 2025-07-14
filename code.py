from tkinter import *
from tkinter import ttk
import requests



win=Tk()
win.title("Weather App")
win.config(bg="blue")
win.geometry("500x500")
name_label=Label(win,text="Weather App",
                font=("Time New Roman",40,"bold"))

name_label.place(x=25,y=50,height=45,width=450)
list_name=["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
#combox
com= ttk.Combobox(win,text="Weather App",values=list_name,
font=("Time New Roman",15,"bold"))

com.place(x=25,y=120,height=45,width=450)
#done button
done_button=Button(win,text="Done",
font=("Time New Roman",15,"bold"))
done_button.place(y=190,x=200,height=30,width=100)

w_label=Label(win,text="Weather Climate",
                 font=("Time New Roman",13))

w_label.place(x=25,y=260,height=40,width=150)
#111111
w_label1=Label(win,text="t",
                 font=("Time New Roman",13))

w_label1.place(x=220,y=260,height=40,width=150)

wd_label=Label(win,text="Weather Condition",
                 font=("Time New Roman",13))

wd_label.place(x=25,y=320,height=40,width=150)
#222
wd_label1=Label(win,text="wc",
                 font=("Time New Roman",13))

wd_label1.place(x=220,y=320,height=40,width=150)
#temp

t_label=Label(win,text="Temprature",
                 font=("Time New Roman",13))

t_label.place(x=25,y=380,height=40,width=150)
#333

t_label1=Label(win,text="Temp",
                 font=("Time New Roman",13))

t_label1.place(x=220,y=380,height=40,width=150)
#temp max
tm_label=Label(win,text="Max Temp",
                 font=("Time New Roman",13))

tm_label.place(x=25,y=440,height=40,width=150)
#44
tm_label1=Label(win,text="Mt",
                 font=("Time New Roman",13))

tm_label1.place(x=220,y=440,height=40,width=150)
#presurre
p_label=Label(win,text="Pressure",
                 font=("Time New Roman",13))

p_label.place(x=25,y=500,height=40,width=150)
#55
p1_label=Label(win,text="P",
                 font=("Time New Roman",13))

p1_label.place(x=220,y=500,height=40,width=150)











win.mainloop()