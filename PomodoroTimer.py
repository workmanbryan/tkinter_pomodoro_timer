import time
from tkinter import *
from tkinter import Tk, Label, Frame, colorchooser
import tkinter.font as font
import pygame


root = Tk(className="Pomodoro Timer")

############################################_ALERT_SOUNDS_########################################
pygame.mixer.init()
sound_1 = pygame.mixer.Sound("sounds/game.wav")
sound_2 = pygame.mixer.Sound("sounds/complete.mp3")
sound_3 = pygame.mixer.Sound("sounds/gong.mp3")

#############################################_FUNCTIONS_##########################################
counter = 0
rounds = 0
sbreaks = 0
lbreaks = 0
user_color = "#ffffff"
mood = "#1DA6C4"
status_color = "#005599"

def pomRound():
    status_label.config(text="Study!", font=("Big Caslon", 32), fg=status_color)
    global counter
    global rounds
    root.config(bg=mood)
    frame0.config(bg=mood)
    frame1.config(bg=mood)
    frame2.config(bg=mood)
    status_label.config(bg=mood)
    totbreak_label.config(bg=mood)
    totwork_label.config(bg=mood)
    worktime_label.config(bg=mood)
    breaktime_label.config(bg=mood)
    t = 25 * 60
    while t > -1:
        mins = (t//60)
        secs = (t%60)
        min_label.config(text="{00:2d}".format(mins),bg=mood, fg=user_color)
        sec_label.config(text="{00:2d}".format(secs),bg=mood, fg=user_color)
        colon_label.config(bg=mood, fg=user_color)
        root.update()
        time.sleep(1)
        t -= 1

    updateStatus1() #status update
    sound_1.play()
    rounds += 1
    updateWorktime()
    counter += 1
    if counter < 4:
        shortBreak()
    else:
        longBreak()
    
        
def shortBreak():
    global sbreaks
    b = 5 * 60
    while b > -1:
        mins = (b//60)
        secs = (b%60)

        min_label.config(text="{00:2d}".format(mins))
        sec_label.config(text="{00:2d}".format(secs))
        root.update()
        time.sleep(1)
        b -= 1

    sbreaks += 1
    updateBreaktime()
    updateStatus2() #status update
    sound_2.play()
    pomRound()


def longBreak():
    global counter
    global lbreaks
    t = 30 * 60
    while t > -1:
        mins = t // 60
        secs = t % 60

        min_label.config(text="{00:2d}".format(mins))
        sec_label.config(text="{00:2d}".format(secs))
        root.update()
        time.sleep(1)
        t -= 1       

    lbreaks += 1
    updateBreaktime()
    updateStatus3() #status update
    sound_3.play()
    counter = 0
    
def updateStatus1():
    status_label.config(text="Take A Break!")

def updateStatus2():
    status_label.config(text="Study!")

def updateStatus3():
    status_label.config(text="You Got This!")

def updateWorktime():
    global rounds
    r = (rounds * 25)
    H = r // 60
    M = r % 60
    worktime_label.config(text = str(H) + " HRS : " + str(M) + " MINS")

def updateBreaktime():
    global sbreaks
    global lbreaks
    s = (sbreaks * 5)
    l = (lbreaks * 30)
    t = s + l
    H = t // 60
    M = t % 60
    breaktime_label.config(text = str(H) + " HRS : " + str(M) + " MINS")

def timerColor():
    global user_color
    user_color = colorchooser.askcolor()[1]

def bgColor():
    global mood
    mood = colorchooser.askcolor()[1]

def statusColor():
    global status_color
    status_color = colorchooser.askcolor()[1]


################################################_LAYOUT_#########################################
root.configure(bg=mood)
root.geometry("600x600")
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=1)

frame0 = Frame(root)
frame1 = Frame(root)
frame2 = Frame(root)

frame0.grid(row=0, column=0)
frame1.grid(row=1, column=0)
frame2.grid(row=2, column=0)

frame0.configure(bg=mood)
frame1.configure(bg=mood)
frame2.configure(bg=mood)

#Frame1
status_label = Label(frame1, text="", font= ("Big Caslon", 32), bg=mood)
status_label.grid(column = 2, row = 3, pady=50)


#Frame0
min_label=Label(frame0, text="00", font=("Baskerville", 48), bg=mood, fg="#ffffff")
min_label.grid(column=1, row=1)

sec_label=Label(frame0, text="00", font=("Baskerville", 48), bg=mood, fg="#ffffff")
sec_label.grid(column=3, row=1)

colon_label=Label(frame0, text=":", font=("Baskerville", 48), bg=mood, fg="#ffffff")
colon_label.grid(column=2, row=1)


#Frame 2
totwork_label = Label(frame2, text="Total Study:", font= ("Big Caslon", 24), bg=mood, fg="#ffffff")
totwork_label.grid(column = 1, row = 4, padx= 25)

worktime_label = Label(frame2, text="0 HRS : 0 MINS", font= ("Baskerville", 24), bg=mood, fg="#ffffff")
worktime_label.grid(column = 1, row = 5, padx= 25)

totbreak_label = Label(frame2, text="Total Break:", font= ("Big Caslon", 24), bg=mood, fg="#ffffff")
totbreak_label.grid(column = 3, row = 4, padx= 25)

breaktime_label = Label(frame2, text="0 HRS : 0 MINS", font= ("Baskerville", 24), bg=mood, fg="#ffffff")
breaktime_label.grid(column = 3, row = 5, padx= 25)

################################################_BUTTONS_###################################################
#start button
start_text = StringVar()
start_btn = Button(frame1, textvariable = start_text, command = lambda:pomRound(), font = ("Big Caslon", 24), fg = "#226644", height = 2, width = 8)
start_text.set("Start")
start_btn.grid(column = 2, row = 2)

#timer color button
custom_btn = Button(frame1, text="Change Timer Color", font=("Big Caslon", 18), command=timerColor)
custom_btn.grid(column=2, row = 4)

#bg color button
custom_btn = Button(frame1, text="Change Background Color", font=("Big Caslon", 18), command=bgColor)
custom_btn.grid(column=2, row = 5, pady=5)

#status color button
custom_btn = Button(frame1, text="Change Text Color", font=("Big Caslon", 18), command=statusColor)
custom_btn.grid(column=2, row = 6)

root.mainloop()