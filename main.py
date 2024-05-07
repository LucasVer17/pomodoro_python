from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="TIMER")
    check_label.config(text="")
    global reps
    reps = 0

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break_sec)
        timer_label.config(
            text="BREAK",
            font=(FONT_NAME, 50, "bold"),
            foreground=RED,
            background=YELLOW,
        )
    elif reps % 2 == 0:
        countdown(short_break_sec)
        timer_label.config(
            text="BREAK",
            font=(FONT_NAME, 50, "bold"),
            foreground=PINK,
            background=YELLOW,
        )
    else:
        countdown(work_sec)
        timer_label.config(
            text="WORK",
            font=(FONT_NAME, 50, "bold"),
            foreground=GREEN,
            background=YELLOW,
        )

def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(reps / 2)):
            marks += "✓"
        check_label.config(text=marks)

window = Tk()
window.title("Pomodoro!")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(
    text="TIMER", font=(FONT_NAME, 50, "bold"), foreground=GREEN, background=YELLOW
)
timer_label.grid(column=1, row=0)

check_label = Label(font=(FONT_NAME, 20, "bold"), foreground=GREEN, background=YELLOW)
check_label.grid(column=1, row=3)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)
timer_text = canvas.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
)
canvas.grid(column=1, row=1)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()
