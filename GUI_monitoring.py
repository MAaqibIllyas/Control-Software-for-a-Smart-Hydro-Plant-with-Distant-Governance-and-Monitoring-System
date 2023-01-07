import tkinter as tk
from tkinter import *
from PIL import Image
import time

def mainSwitch_function():
    print("---")


root.configure(bg='black') #for previous grey, coloroot=tk.Tk()

root.title("CONTROL & OVERVIEW OF HYDRO POWER PLANT")
#root.configure(width=1000,height=550,bg='#4d4d4d')ur code is #4d4d4d
root.geometry('1350x689+0+0')
root.resizable(height=False,width=False)

#def count():
#global counter
freq=tk.IntVar()
freq.set(50)
#print(counter)


#var = StringVar()
l1=tk.Label(root,text="Frequency in Hz",bg='#004466',fg="#ccccb3",relief=RAISED,font='Times 15 bold',width=13)
l1.place(x=0,y=5)
freqLabel=tk.Label(root, textvariable=freq, relief=RAISED,font='Times 20 ',bg='#004466',fg="#66ff33",width=11)
#var.set("a")
freqLabel.place(x=0,y=36)


vol=tk.IntVar()
vol.set(12)
l2=tk.Label(root,text="Voltage in Volts",bg='#004466',fg="#ccccb3",relief=RAISED,font='Times 15 bold',width=13)
l2.place(x=156,y=5)
volLabel=tk.Label(root, textvariable=vol, relief=RAISED,font='Times 20',bg='#004466',fg="#66ff33",width=10)
volLabel.place(x=156,y=36)


excitation=tk.IntVar()
excitation.set(123)
l3=tk.Label(root,text="Excitation in Amps",bg='#004466',fg="#ccccb3",relief=RAISED,font='Times 15 bold',width=15)
l3.place(x=309,y=5)
excitationLabel=tk.Label(root, textvariable=excitation, relief=RAISED,font='Times 20',bg='#004466',fg="#66ff33",width=12)
excitationLabel.place(x=309,y=36)


waterFlow=tk.IntVar()
waterFlow.set(123)
l4=tk.Label(root,text="Water Flow in liter/sec",bg='#004466',fg="#ccccb3",relief=RAISED,font='Times 15 bold',padx=4,width=17)
l4.place(x=490,y=5)
waterFlowLabel=tk.Label(root, textvariable=waterFlow, relief=RAISED,font='Times 20',bg='#004466',fg="#66ff33",width=14)
waterFlowLabel.place(x=490,y=36)


activePow=tk.IntVar()
activePow.set(123)
l5=tk.Label(root,text="Active Power in Watts",bg='#004466',fg="#ccccb3",relief=RAISED,font='Times 15 bold',width=17)
l5.place(x=700,y=5)
activePowLabel=tk.Label(root, textvariable=activePow, relief=RAISED,font='Times 20',bg='#004466',fg="#66ff33",width=14)
activePowLabel.place(x=700,y=36)


pf=tk.DoubleVar()
pf.set(0.989)
l6=tk.Label(root,text="Power Factor",bg='#004466',fg="#ccccb3",relief=RAISED,font='Times 15 bold',width=14)
l6.place(x=910,y=5)
pfLabel=tk.Label(root, textvariable=pf, relief=RAISED,font='Times 20',bg='#004466',fg="#66ff33",width=14)
pfLabel.place(x=910,y=36)


rpm=tk.DoubleVar()
rpm.set(166.7)
l7=tk.Label(root,text="RPMs",bg='#004466',fg="#ccccb3",relief=RAISED,font='Times 15 bold',width=5)
l7.place(x=1070,y=5)
rpmLabel=tk.Label(root, textvariable=rpm, relief=RAISED,font='Times 20',bg='#004466',fg="#66ff33",width=4)
rpmLabel.place(x=1070,y=36)


load=tk.DoubleVar()
load.set(166.7)
l8=tk.Label(root,text="Load in Watts",bg='#004466',fg="#ccccb3",relief=RAISED,font='Times 15 bold',width=18)
l8.place(x=1136,y=5)
loadLabel=tk.Label(root, textvariable=load, relief=RAISED,font='Times 20',bg='#004466',fg="#66ff33",width=15)
loadLabel.place(x=1136,y=36)

# photo=PhotoImage(file="adder subtractor.png")
# l9=tk.Label(root, image=photo)
# l9.place(x=309,y=200)

# photo1=PhotoImage(file="arrow-right.png")
# l10=tk.Label(root, image=photo1)
# l10.place(x=378,y=215)

# l11=tk.Label(root,text="DC",bg="#bfbfbf",fg="black",width=4,height=3,font="Times 16 bold")
# l11.place(x=415,y=200)
#
# l12=tk.Label(root, image=photo1)
# l12.place(x=470,y=215)
#
# l13=tk.Label(root,text="AC Motor",bg="#bfbfbf",fg="black",width=8,height=3,font="Times 16 bold")
# l13.place(x=507,y=200)
#
# l14=tk.Label(root, image=photo1)
# l14.place(x=610,y=215)
#
# # photo2=PhotoImage(file="long-down-arrow.png")
# # l15=tk.Label(root, image=photo2)
# # l15.place(x=540,y=165)
#
# l16=tk.Label(root,text="Field Control",bg="#bfbfbf",fg="black",font="Times 16 bold")
# l16.place(x=499,y=135)
#
# l17=tk.Label(root,text="Frequency & Voltage Sensing Modules",bg="#bfbfbf",fg="black",height=3,font="Times 16 bold")
# l17.place(x=647,y=200)
#
# photo3=PhotoImage(file="long-down-arrow-128pi.png")
# l18=tk.Label(root, image=photo3)
# l18.place(x=740,y=278)
#
# l19=tk.Label(root,text="PID Based Control",bg="#bfbfbf",fg="black",height=3,font="Times 20 bold")
# l19.place(x=655,y=411)
#
# photo4=PhotoImage(file="horizontalLine.png")
# l20=tk.Label(root, image=photo4)
# l20.place(x=410,y=444)
#
# photo5=PhotoImage(file="odVA7.png")
# l21=tk.Label(root, image=photo4)
# l21.place(x=340,y=444)
#
# photo6=PhotoImage(file="up-arrow.png")
# l22=tk.Label(root, image=photo6)
# l22.place(x=340,y=410)
#
# l23=tk.Label(root, image=photo6)
# l23.place(x=340,y=373)
#
# l24=tk.Label(root, image=photo6)
# l24.place(x=340,y=336)
#
# l25=tk.Label(root, image=photo6)
# l25.place(x=340,y=299)
#
# l26=tk.Label(root, image=photo6)
# l26.place(x=340,y=262)
#
# l27=tk.Label(root, image=photo1)
# l27.place(x=272,y=215)
#
# l28=tk.Label(root,text="Input Voltage",bg="#bfbfbf",fg="black",font="Times 20 bold")
# l28.place(x=105,y=215)
#
# l27=tk.Label(root, image=photo1)
# l27.place(x=885,y=444)
#
# photo7=PhotoImage(file="contact-symbols.png")
# l28=tk.Label(root, image=photo7)
# l28.place(x=920,y=411)
#
# l29=tk.Label(root, image=photo1)
# l29.place(x=990,y=444)
#
# l30=tk.Label(root,text="LOAD",bg="#bfbfbf",fg="black",font="Times 20 bold")
# l30.place(x=1027,y=444)
#

clock = Label(root, font=('times', 20,'bold'), bg='#004466', fg="#66ff33")
clock.place(x=1136, y=610)
time1 = ''
def tick():
    global time1
    # get the current local time from the PC
    time2 = time.strftime('%H:%M:%S')
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    # calls itself every 200 milliseconds
    # to update the time display as needed
    # could use >200 ms, but display gets jerky
    clock.after(200, tick)
tick()

dateVariable= time.strftime('%A %d/%m/%y',time.localtime())
#print(dateVariable)
dateLable =tk.Label(root, font=('times', 20,'bold'), bg='#004466',fg="#66ff33",text=dateVariable)
dateLable.place(x=1136,y=647)

mainSwitch=tk.Button(root,bd=4,fg="#004466",bg='red',font="Times 20",text="SHUT DOWN",activebackground="#66ff33"
                     ,padx=10,pady=10,relief=SUNKEN,command=mainSwitch_function)
mainSwitch.place(x=1,y=100)




#=======================================================================================================================
def intakeFlowButton_function():
    print("set intake flow of water")
intakeFlowButton=tk.Button(root,bd=2,fg="#004466",bg='#66ff33',font="Times 16 bold",text="Intake Flow",
                           activebackground="#ff0000",relief=SUNKEN,command=intakeFlowButton_function)
intakeFlowButton.place(x=1,y=640)


def spillwayControlButton_function():
    print("set spillway Control")
spillwayControlButton=tk.Button(root,bd=2,fg="#004466",bg='#66ff33',font="Times 16 bold",text="Spillway Control",
                           activebackground="#ff0000",relief=SUNKEN,command=spillwayControlButton_function)
spillwayControlButton.place(x=120,y=640)


def penstockPressureButton_function():
    print("set penstock pressure")
penstockPressureButton=tk.Button(root,bd=2,fg="#004466",bg='#66ff33',font="Times 16 bold",text="Penstock Pressure",
                           activebackground="#ff0000",relief=SUNKEN,command=penstockPressureButton_function)
penstockPressureButton.place(x=280,y=640)


def valveControlButton_function():
    print("set Valve Control")
valveControlButton=tk.Button(root,bd=2,fg="#004466",bg='#66ff33',font="Times 16 bold",text="Valve Control",
                           activebackground="#ff0000",relief=SUNKEN,command=valveControlButton_function)
valveControlButton.place(x=460,y=640)

def excitationControlButton_function():
    print("set excitation")
excitationControlButton=tk.Button(root,bd=2,fg="#004466",bg='#66ff33',font="Times 16 bold",text="Excitation Control",
                           activebackground="#ff0000",relief=SUNKEN,command=excitationControlButton_function)
excitationControlButton.place(x=598,y=640)


def freqControlButton_function():
    print("set frequency")
freqControlButton=tk.Button(root,bd=2,fg="#004466",bg='#66ff33',font="Times 16 bold",text="Frequency Control",
                           activebackground="#ff0000",relief=SUNKEN,command=freqControlButton_function)
freqControlButton.place(x=700,y=640)


def powControlButton_function():
    print("set power")
powControlButton=tk.Button(root,bd=2,fg="#004466",bg='#66ff33',font="Times 16 bold",text="Power Control",
                           activebackground="#ff0000",relief=SUNKEN,command=powControlButton_function)
powControlButton.place(x=810,y=640)


def speedControlButton_function():
    print("set speed")
speedControlButton=tk.Button(root,bd=2,fg="#004466",bg='#66ff33',font="Times 16 bold",text="Speed Control",
                           activebackground="#ff0000",relief=SUNKEN,command=speedControlButton_function)
speedControlButton.place(x=1,y=598)


def pfControlButton_function():
    print("set power factor")
pfControlButton=tk.Button(root,bd=2,fg="#004466",bg='#66ff33',font="Times 16 bold",text="Power Factor Control",
                           activebackground="#ff0000",relief=SUNKEN,command=pfControlButton_function)
pfControlButton.place(x=140,y=598)

root.mainloop()


