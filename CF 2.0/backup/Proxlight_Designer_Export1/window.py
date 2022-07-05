from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("1007x650")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 650,
    width = 1007,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

canvas1 = Canvas(
    window,
    bg="white",
    height = 608,
    width = 602,
    bd = 1,
    highlightthickness = 1,
    relief = 'ridge')
canvas1.place(x = 375, y = 22)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    179.0, 112.5,
    image=background_img)

canvas1.create_text(
    325, 54,
    text = "Top results for your search\n",
    fill = "#000000",
    font = ("None", int(16.0)))

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas1.create_image(
    769.5, 290.0,
    image = entry0_img)

entry0 = Text(
    bd = 1,
    bg = "#ffffff",
    highlightthickness = 1)

entry0.place(
    x = 615, y = 232,
    width = 309,
    height = 114)

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    769.5, 159.0,
    image = entry1_img)

entry1 = Text(
    bd = 1,
    bg = "#ffffff",
    highlightthickness = 1)

entry1.place(
    x = 615, y = 101,
    width = 309,
    height = 114)

entry2_img = PhotoImage(file = f"img_textBox2.png")
entry2_bg = canvas.create_image(
    769.5, 421.0,
    image = entry2_img)

entry2 = Text(
    bd = 1,
    bg = "#ffffff",
    highlightthickness = 1)

entry2.place(
    x = 615, y = 363,
    width = 309,
    height = 114)

entry3_img = PhotoImage(file = f"img_textBox3.png")
entry3_bg = canvas.create_image(
    769.5, 552.0,
    image = entry3_img)
l = '''9.TATA Tiago NRG
      Price: Rs.6.62 - 7.17 Lakh
      ARAI Mileage: 15.0 kmpl
      Engine Displacement: 1199cc
      Max Power(bhp@rpm): 84.48bhp@6000rpm
      Seating Capacity:5
      Boot Space (Litres): 242 
      Fuel Type: Petrol
      Fuel Tank Capacity: 35 L 
      Transmission Type: Automatic
      Service Cost (Avg. of 5 years): Unknown'''
entry3 = Text(
    bd = 1,
    bg = "#ffffff",
    highlightthickness = 1)

entry3.insert(1.0, l)
entry3.config(state=DISABLED)

entry3.place(
    x = 615, y = 494,
    width = 309,
    height = 114)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 81, y = 415,
    width = 195,
    height = 37)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 81, y = 270,
    width = 195,
    height = 36)

img2 = PhotoImage(file = f"img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b2.place(
    x = 81, y = 490,
    width = 195,
    height = 36)

img3 = PhotoImage(file = f"img3.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b3.place(
    x = 81, y = 344,
    width = 195,
    height = 36)

img4 = PhotoImage(file = f"img4.png")
b4 = Button(
    image = img4,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b4.place(
    x = 122, y = 554,
    width = 113,
    height = 37)

window.resizable(False, False)
window.mainloop()
