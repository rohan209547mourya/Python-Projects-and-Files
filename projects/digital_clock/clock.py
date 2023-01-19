from tkinter import Label, Tk
import time


def clock():
    time_live = time.strftime("%H:%M:%S")
    label.config(text=time_live)
    label.after(200, clock)


_application_window_ = Tk()
_application_window_.title("Digital Clock")
_application_window_.geometry("420x150")
_application_window_.configure(background="white")
_application_window_.resizable(True, True)
_application_window_.minsize = 10

_application_font_ = ("Boulder", 68, 'bold')
_application_background_ = "white"
foreground = "#363529"
_application_border_width_ = 25

label = Label(_application_window_, font=_application_font_, bg=_application_background_, fg=foreground,
              bd=_application_border_width_)
label.grid(row=0, column=1)

clock()
_application_window_.mainloop()
