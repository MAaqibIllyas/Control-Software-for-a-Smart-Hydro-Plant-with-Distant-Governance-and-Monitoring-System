import tkinter as tk
from tkinter import *
from PIL import Image
import time
import RPi.GPIO as GPIO
import time, sys


#count for current
#count1 for active power
#count2 for frequency
#count3 for vibration from Pizzo Electric Sensor
#count4 for rpm
GPIO.setmode(GPIO.BOARD)
def mainSwitch_function():
    print("mainSwitch_function")
def spillwayControlButton_function():
    print("set spillway Control")
def gateControlButton_function():
    print("set gate Control")
def loadControlButton_function():
    print("set load")
    

#============================================for MAX6675 Thermocoupl===============================
class MAX6675(object):
    '''Python driver for [MAX6675 Cold-Junction Compensated Thermocouple-to-Digital Converter](http://www.adafruit.com/datasheets/MAX6675.pdf)
     Requires:
     - The [GPIO Library](https://code.google.com/p/raspberry-gpio-python/) (Already on most Raspberry Pi OS builds)
     - A [Raspberry Pi](http://www.raspberrypi.org/)
    '''
    def __init__(self, cs_pin, clock_pin, data_pin, units = "c", board = GPIO.BOARD):
        '''Initialize Soft (Bitbang) SPI bus
        Parameters:
        - cs_pin:    Chip Select (CS) / Slave Select (SS) pin (Any GPIO)  
        - clock_pin: Clock (SCLK / SCK) pin (Any GPIO)
        - data_pin:  Data input (SO / MOSI) pin (Any GPIO)
        - units:     (optional) unit of measurement to return. ("c" (default) | "k" | "f")
        - board:     (optional) pin numbering method as per RPi.GPIO library (GPIO.BCM (default) | GPIO.BOARD)
        '''
        self.cs_pin = cs_pin
        self.clock_pin = clock_pin
        self.data_pin = data_pin
        self.units = units
        self.data = None
        self.board = board

        # Initialize needed GPIO
        #GPIO.setmode(self.board)
        GPIO.setup(self.cs_pin, GPIO.OUT)
        GPIO.setup(self.clock_pin, GPIO.OUT)
        GPIO.setup(self.data_pin, GPIO.IN)

        # Pull chip select high to make chip inactive
        GPIO.output(self.cs_pin, GPIO.HIGH)

    def get(self):
        '''Reads SPI bus and returns current value of thermocouple.'''
        self.read()
        
        return getattr(self, "to_" + self.units)(self.data_to_tc_temperature())

    def read(self):
        '''Reads 16 bits of the SPI bus & stores as an integer in self.data.'''
        bytesin = 0
        # Select the chip
        GPIO.output(self.cs_pin, GPIO.LOW)
        # Read in 16 bits
        for i in range(16):
            GPIO.output(self.clock_pin, GPIO.LOW)
            time.sleep(0.0000001)
            bytesin = bytesin << 1
            if (GPIO.input(self.data_pin)):
                bytesin = bytesin | 1
            GPIO.output(self.clock_pin, GPIO.HIGH)
        time.sleep(0.0000001)
        # Unselect the chip
        GPIO.output(self.cs_pin, GPIO.HIGH)
        # Save data
        self.data = bytesin



    def data_to_tc_temperature(self, data_16 = None):
        '''Takes an integer and returns a thermocouple temperature in celsius.'''
        if data_16 is None:
            data_16 = self.data
        # Remove bits D0-3
        tc_data = ((data_16 >> 3) & 0xFFF)
        # 12-bit resolution
        return (tc_data * 0.25)

    def to_c(self, celsius):
        '''Celsius passthrough for generic to_* method.'''
        return celsius


    def cleanup(self):
        '''Selective GPIO cleanup'''
        GPIO.setup(self.cs_pin, GPIO.IN)
        GPIO.setup(self.clock_pin, GPIO.IN)

class MAX6675Error(Exception):
     def __init__(self, value):
         self.value = value
     def __str__(self):
         return repr(self.value)



    # default example
cs_pin = 24
clock_pin = 23
data_pin = 29
units = "c"
thermocouple = MAX6675(cs_pin, clock_pin, data_pin, units)
    
#===================================================================================================


inpt = 11  # for current/voltage
GPIO.setup(inpt, GPIO.IN, pull_up_down = GPIO.PUD_UP)

inpt1 = 13 #for actPower
GPIO.setup(inpt1, GPIO.IN, pull_up_down = GPIO.PUD_UP)

inpt2 = 22 #for freq  # 22nd pin is GPIO 25
GPIO.setup(inpt2, GPIO.IN, pull_up_down = GPIO.PUD_UP)

inpt3 = 29 #for temperature # 29th pin is GPIO 5
GPIO.setup(inpt3, GPIO.IN, pull_up_down = GPIO.PUD_UP)

inpt4 = 31 #for vibration # 31st pin is GPIO 6
GPIO.setup(inpt4, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

inpt5 = 18 #for head  # 18th pin is GPIO 24

inpt7 = 33 #for rpm # 33rd pin is GPIO 13
GPIO.setup(inpt7, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

inpt8 = 35 #for water flow # 35th pin is GPIO 19
GPIO.setup(inpt8, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)


inpt9 = 38 #for freq  test # 35th pin is GPIO 20
GPIO.setup(inpt9, GPIO.OUT)


inpt10 = 40 #for freq test # 35th pin is GPIO 21
GPIO.setup(inpt10, GPIO.OUT)

global cv_enable
cv_enable = 15 #for current # 15th pin is GPIO 22
GPIO.setup(cv_enable, GPIO.OUT )
cv_enable = True




trig = 16
echo = 18

GPIO.setup(trig,GPIO.OUT)
GPIO.setup(echo, GPIO.IN)


class UpdateLabel():
    global count
    count = 0

    global count1
    count1 = 0

    global count2
    count2 = 0
    
    global count3
    count3 = 0
    
    global head
    head = 0
    
    global count4
    count4 = 0
    
    global count5
    count5 = 0
    
    global time1
    time1 = 0



    def countPulse(channel):
        global count
        count = count+1

    def countPulse1(channel1):
        global count1
        count1 = count1+1
    def countPulse2(channel2):
        global count2
        count2 = count2+1
    def countPulse3(channel3):
        global count3
        count3 = "YES "
    def countPulse4(channel4):
        global count4
        count4 = count4+1
        
    def countPulse5(channel5):
        global count5
        count5 = count5+1
    

    GPIO.add_event_detect(inpt,GPIO.RISING,callback=countPulse)
    GPIO.add_event_detect(inpt1,GPIO.RISING,callback=countPulse1)
    GPIO.add_event_detect(inpt2, GPIO.RISING, callback=countPulse2)
    #GPIO.add_event_detect(inpt3, GPIO.RISING, callback=countPulse3)
    GPIO.add_event_detect(inpt4, GPIO.RISING, callback=countPulse3)
    GPIO.add_event_detect(inpt7, GPIO.RISING, callback=countPulse4)
    GPIO.add_event_detect(inpt8, GPIO.RISING, callback=countPulse5)
    
    



    def __init__(self):
        self.win = tk.Tk()
        self.win.title("CONTROL & OVERVIEW OF HYDRO POWER PLANT")
        #self.win.minsize(800, 600)
        self.win.configure(bg="black")
        self.win.geometry('1075x680+0+0')
        self.win.resizable(height=False, width=False)


        self.ctr0 = 0    #ctr for current
        self.tk_voltage = tk.StringVar()
        self.tk_voltage.set("0")
        l2 = tk.Label(self.win, text="Terminal Voltage in Volts", bg='#004466', fg="#ccccb3", relief=RAISED,
                      font='Times 15 bold')
        l2.place(x=146, y=5)
        volLabel=tk.Label(self.win, textvariable=self.tk_voltage,
                          relief=RAISED,font='Times 20',bg='#004466',fg="#66ff33")
        volLabel.place(x=146,y=36)

        self.ctr1 = 0
        self.tk_actPow = tk.StringVar()
        self.tk_actPow.set("0")

        l5 = tk.Label(self.win, text="Active Power in Watts", bg='#004466', fg="#ccccb3", relief=RAISED,
                      font='Times 15 bold')
        l5.place(x=740, y=5)
        activePowerLabel=tk.Label(self.win, textvariable=self.tk_actPow, relief=RAISED,font='Times 20',bg='#004466',
                        fg="#66ff33")
        activePowerLabel.place(x=740,y=36)


        self.ctr2 = 0    #ctr2 for freq
        self.tk_freq = tk.StringVar()
        self.tk_freq.set("0")
        l1 = tk.Label(self.win, text="Frequency in Hz", bg='#004466', fg="#ccccb3", relief=RAISED, font='Times 15 bold')
        l1.place(x=0, y=5)
        freqLabel = tk.Label(self.win, textvariable=self.tk_freq,
                             relief=RAISED, font='Times 20 ', bg='#004466', fg="#66ff33")
        freqLabel.place(x=0, y=36)
        
        
        self.ctr3 = 0    #ctr3 for temperature
        self.tk_temperature = tk.StringVar()
        self.tk_temperature.set("0")
        l3=tk.Label(self.win,text="Temperature in *C",bg='#004466',fg="#ccccb3",
                    relief=RAISED,font='Times 15 bold')
        l3.place(x=400,y=90)
        temperatureLabel=tk.Label(self.win, textvariable=self.tk_temperature, relief=RAISED,
                                  font='Times 20',bg='#004466',fg="#66ff33")
        temperatureLabel.place(x=400,y=120)


        self.ctr4 = 0    #ctr4 for vibration
        self.tk_vibration = tk.StringVar()
        self.tk_vibration.set("0")
        l4 = tk.Label(self.win, text="Vibration Status", bg='#004466', fg="#ccccb3", relief=RAISED,
                      font='Times 15 bold')
        l4.place(x=580, y=90)
        vibrationLabel = tk.Label(self.win, textvariable=self.tk_vibration, relief=RAISED,
                                  font='Times 20', bg='#004466',fg="#66ff33")
        vibrationLabel.place(x=580, y=120)
        
        
        
        
        self.ctr5 = 0    #ctr5 for head
        self.tk_head = tk.StringVar()
        self.tk_head.set("0")
        l0=tk.Label(self.win,text="Head",bg='#004466',fg="#ccccb3",relief=RAISED,font='Times 15 bold')
        l0.place(x=740,y=90)
        headLabel=tk.Label(self.win, textvariable=self.tk_head, relief=RAISED,font='Times 20',
                           bg='#004466',fg="#66ff33")
        headLabel.place(x=740,y=120)
        
        
        self.ctr7 = 0    #ctr7 for waterflow
        self.tk_waterflow = tk.StringVar()
        self.tk_waterflow.set("0")
        lwf=tk.Label(self.win,text="Water Flow in liter/sec",bg='#004466',fg="#ccccb3",relief=RAISED,
                    font='Times 15 bold',padx=4)
        lwf.place(x=146,y=90)
        waterFlowLabel=tk.Label(self.win, textvariable=self.tk_waterflow, relief=RAISED,
                                font='Times 20',bg='#004466',fg="#66ff33")
        waterFlowLabel.place(x=146,y=120)


        self.ctr6 = 0    #ctr6 for rpm
        self.tk_rpm = tk.StringVar()
        self.tk_rpm.set("0")
        lrpm=tk.Label(self.win,text="RPMs",bg='#004466',fg="#ccccb3",relief=RAISED,font='Times 15 bold')
        lrpm.place(x=0,y=90)
        rpmLabel=tk.Label(self.win, textvariable=self.tk_rpm, relief=RAISED,font='Times 20',
                          bg='#004466',fg="#66ff33")
        rpmLabel.place(x=0,y=120)
        
        
        
        lpf=tk.Label(self.win,text="Power Factor",bg='#004466',fg="#ccccb3",relief=RAISED,
                     font='Times 15 bold')
        lpf.place(x=580,y=5)
        pfLabel=tk.Label(self.win, textvariable=self.tk_head, relief=RAISED,font='Times 20',bg='#004466',fg="#66ff33")
        pfLabel.place(x=580,y=36)
        
        
        
        
        self.ctr = 0    #ctr for current
        self.tk_current = tk.StringVar()
        self.tk_current.set("0")
        llc=tk.Label(self.win,text="Load Current in A",bg='#004466',fg="#ccccb3",
                    relief=RAISED,font='Times 15 bold')
        llc.place(x=400,y=5)
        temperatureLabel=tk.Label(self.win, textvariable=self.tk_current, relief=RAISED,
                                  font='Times 20',bg='#004466',fg="#66ff33")
        temperatureLabel.place(x=400,y=36)
        
#============================================== TIME AND DATE ========================================   
        clock = Label(self.win, font=('times', 20,'bold'), bg='#004466', fg="#66ff33")
        clock.place(x=740, y=590)
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
        dateLable =tk.Label(self.win, font=('times', 20,'bold'), bg='#004466',fg="#66ff33",text=dateVariable)
        dateLable.place(x=740,y=625)
#===========================================================================================================
        
        mainSwitch=tk.Button(self.win,bd=4,fg="#004466",bg='red',font="Times 20",text="SHUT DOWN",
                             activebackground="#66ff33"
                     ,padx=10,pady=10,relief = RAISED,command=mainSwitch_function)
        mainSwitch.place(x=1,y=617)
        
        

        spillwayControlButton=tk.Button(self.win,bd=2,fg="#004466",bg='#66ff33',font="Times 16 bold",
                                        text="Spillway Control",activebackground="#ff0000",
                                        relief=SUNKEN,command=spillwayControlButton_function)
        spillwayControlButton.place(x=540,y=625)
        
        

        gateControlButton=tk.Button(self.win,bd=2,fg="#004466",bg='#66ff33',font="Times 16 bold",
                                    text="Gate Control",activebackground="#ff0000",
                                    relief=SUNKEN,command=gateControlButton_function)
        gateControlButton.place(x=200,y=625)
        
        
        

        loadControlButton=tk.Button(self.win,bd=2,fg="#004466",bg='#66ff33',font="Times 16 bold",
                                   text="Load Control",activebackground="#ff0000",
                                    relief=SUNKEN,command=loadControlButton_function)
        loadControlButton.place(x=370,y=625)


        self.updater()
        self.win.mainloop()

        
    def updater(self):
            old_time = time.time()
            #print(old_time)
            global count
            global count1
            global count2
            global count3
            global head
            global cv_enable
            global count4
            global count5
            
            if (count2 > 10):
                GPIO.output(inpt9,True)
                GPIO.output(inpt10,False)
                        
            elif (count2 < 10):
                GPIO.output(inpt9,False)
                GPIO.output(inpt10,True)
                        
            elif (count2 == 10):
                GPIO.output(inpt9,False)
                GPIO.output(inpt10,False)
#=====================================================Ultra Sonic Sensor=========================
            time.sleep(0.000001)
            GPIO.output(trig,True)
            time.sleep(0.000001)
            GPIO.output(trig,False)

            while GPIO.input(echo)==0:
                pulse_start = time.time()

            while GPIO.input(echo)==1:
                pulse_end = time.time()

            pulse_duration=pulse_end - pulse_start
            print("pulse = ", pulse_duration)

            head = pulse_duration*17150

            head = round(head, 2)
            print("distance: ",head, "cm")
#========================================================================================================
            
            if(cv_enable == True):
                cv_enable = False
                print("low")
                self.ctr0 = round(count*0.5,3)
            else:
                cv_enable = True
                print("high")
                self.ctr = round(count*0.015,3)
                
            #self.ctr = round(count*0.015,3)
            self.ctr0 = round(count*0.5 , 3)    
            self.ctr1 = round(count1*12,3)
            self.ctr2 = count2
            self.ctr3 = thermocouple.get()
            self.ctr4 = count3
            self.ctr5 = head
            self.ctr6 = count4*60
            self.ctr7 = round(count5/7.5,3)
            count = 0
            count1 = 0
            count2 = 0
            count3 = "NO"
            count4 = 0
            count5 = 0
            self.tk_voltage.set(str(self.ctr0))
            self.tk_current.set(str(self.ctr))
            self.tk_actPow.set(str(self.ctr1))
            self.tk_freq.set(str(self.ctr2))
            self.tk_temperature.set(str(self.ctr3))
            self.tk_vibration.set(str(self.ctr4))
            self.tk_head.set(str(self.ctr5))
            self.tk_rpm.set(str(self.ctr6))
            self.tk_waterflow.set(str(self.ctr7))
            print(time.time()-old_time)
            self.win.after(960, self.updater)
            
UL=UpdateLabel()

