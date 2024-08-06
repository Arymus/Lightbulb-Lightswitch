from PIL import Image, ImageTk
import tkinter

win = tkinter.Tk()
win.geometry("600x600")
win.configure(bg = "purple")

heading = tkinter.Label(win, text = "Lightbulb Project", bg = "purple", fg = "white", font = ("Sans", 25))
heading.pack()

on = Image.open("Python/bulb_on.png")
off = Image.open("Python/bulb_off.png")
turn_on = ImageTk.PhotoImage(image = on)
turn_off = ImageTk.PhotoImage(image = off)

replace_label = tkinter.Label(text = "The lightbulb will be displayed here.", fg = "white")

def light_on():
  replace_label.config(image = turn_on)
  replace_label.pack()
  return replace_label

def light_off():
  replace_label.config(image = turn_off)
  replace_label.pack()
  return replace_label

on_btn = tkinter.Button(win, text = "On", command = light_on)
on_btn.pack()
off_btn = tkinter.Button(win, text = "Off", command = light_off)
off_btn.pack()

win.mainloop()