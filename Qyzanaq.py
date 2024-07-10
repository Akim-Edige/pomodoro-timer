import pygame
from tkinter import *
import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
ptichka="✓"
round=1
reset_sw=False
stop_sw=False

# import os
# import sys
#
#
# def resource_path(relative_path):
#     """ Get absolute path to resource, works for dev and for PyInstaller """
#     try:
#         # PyInstaller creates a temp folder and stores path in _MEIPASS
#         base_path = sys._MEIPASS
#     except Exception:
#         base_path = os.path.abspath(".")
#
#     return os.path.join(base_path, relative_path)


# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start():
    global stop_sw
    canvas.itemconfig(image, image=tomato)
    canvas.config(bg=YELLOW)
    label2.config(text="")
    label.config(text="Timer")
    stop_sw = False
    canvas.itemconfig(timer_text, text=f"00:00")
    window.after_cancel(timer)
    window.after
    fbutton3.config(text="Stop")
    timer(0, 0, round, WORK_MIN)

#     break_time(round)
#
# def break_time(round):
#     timer(0,0,round,SHORT_BREAK_MIN)

def restart():
    global reset_sw
    reset_sw=True

def stop():
    global stop_sw

    if not stop_sw:
        fbutton3.config(text="Continue")
        stop_sw = True
    else:
        fbutton3.config(text="Stop")
        stop_sw = False




def timer(count, min, round, work):
    # canvas.itemconfig(timer)
    global reset_sw

    if reset_sw:
        canvas.itemconfig(image, image=tomato)
        canvas.config(bg=YELLOW)
        label2.config(text="")
        canvas.itemconfig(timer_text, text=f"00:00")
        window.after_cancel(timer)
        fbutton3.config(text="Stop")
        reset_sw=False
        return
    elif stop_sw:
        window.after(1000, timer, count, min, round, work)
    else:
        if count == 60:
            min += 1
            count = 0

        if (min < 10 and count < 10):
            canvas.itemconfig(timer_text, text=f"0{min}:0{count}")
        elif (min < 10 and count >= 10):
            canvas.itemconfig(timer_text, text=f"0{min}:{count}")
        elif (min >= 10 and count >= 10):
            canvas.itemconfig(timer_text, text=f"{min}:{count}")
        elif (min >= 10 and count < 10):
            canvas.itemconfig(timer_text, text=f"{min}:0{count}")

        if min == 25 and work == 25:

            canvas.itemconfig(image, image=time_up_tomato)
            canvas.config(bg=YELLOW)
            label.config(text="Break")

            window.attributes('-topmost', True)
            window.update()

            # Sound
            pygame.mixer.music.load("assets/break.mp3")
            pygame.mixer.music.play(loops=0)

            if round == 4:
                window.after(1000, timer, 0, 0, round, LONG_BREAK_MIN)
            else:
                window.after(1000, timer, 0, 0, round, SHORT_BREAK_MIN)


        elif min == 5 and work == 5:

            t = ""
            for x in range(round):
                t += ptichka
            label2.config(text=t)

            round += 1

            label.config(text="Timer")
            canvas.itemconfig(image, image=tomato)
            canvas.config(bg=YELLOW)

            window.attributes('-topmost', False)
            window.update()

            window.after(1000, timer, 0, 0, round, WORK_MIN)
        elif min == 20 and work == 20:
            canvas.itemconfig(image, image=tomato)
            canvas.config(bg=YELLOW)
            t = ""
            for x in range(round):
                t += ptichka
            label2.config(text=t)

            label.config(text="Timer")

            canvas.itemconfig(timer_text, text=f"00:00")
            window.after_cancel(timer)

        else:
            window.after(1000, timer, count + 1, min, round, work)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window= Tk()
window.title("Qyzanaq")
window.config(padx=70,pady=34, bg=YELLOW)

#Sound
pygame.mixer.init()




canvas=Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato=PhotoImage(file="assets/tomato.png")
time_up_tomato=PhotoImage(file="assets/Time_is_up.png")
image = canvas.create_image(100, 112, image=tomato)
canvas.grid(column=1,row=2)
timer_text=canvas.create_text(100,130, text="00:00",fill="white", font=(FONT_NAME,33,"bold"))

fbutton = Button(text="Start", command=start, height=2, width=8, relief=GROOVE)
fbutton.grid(column=0,row=3)

fbutton2 = Button(text="Reset", command=restart, height=2, width=8)
fbutton2.grid(column=3,row=3)

fbutton3 = Button(text="Stop", command=stop,height=2, width=8)
fbutton3.grid(column=1,row=5)

label=Label(text="Timer", fg=GREEN, font=(FONT_NAME, 45, ), bg=YELLOW)
label.grid(column=1,row=0)

label2=Label(text="", fg=GREEN, font=(FONT_NAME, 35, ), bg=YELLOW)
label2.grid(column=1,row=3)




window.mainloop()
