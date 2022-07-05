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

Resultswin = Canvas(
    window,
    bg = "#ffffff",
    height = 589,
    width = 608,
    bd = 0,
    highlightthickness = 1,
    relief = "ridge")
Resultswin.config(highlightbackground="black",highlightcolor="black")
Resultswin.place(x = 375, y = 53)


background_img = PhotoImage(file = f"background1.png")
background = canvas.create_image(
    179.0, 112.5,
    image=background_img)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 375, y = 28,
    width = 24,
    height = 24)

Resultswin.create_text(
    320, 40,
    text = "Top results for your search\n",
    fill = "#000000",
    font = ("None", int(16.0)))

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    769.5, 306.0,
    image = entry0_img)

entry0 = Text(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 1)
entry0.config(highlightbackground = "Black", highlightcolor= "Black")

entry0.place(
    x = 615, y = 248,
    width = 309,
    height = 114)

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    769.5, 175.0,
    image = entry1_img)

entry1 = Text(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 1)
entry1.config(highlightbackground = "Black", highlightcolor= "Black")

entry1.place(
    x = 615, y = 117,
    width = 309,
    height = 114)

entry2_img = PhotoImage(file = f"img_textBox2.png")
entry2_bg = canvas.create_image(
    769.5, 437.0,
    image = entry2_img)

entry2 = Text(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 1)
entry2.insert(1.0,"HI")
entry2.config(highlightbackground = "Black", highlightcolor= "Black")

entry2.place(
    x = 615, y = 379,
    width = 309,
    height = 114)

entry3_img = PhotoImage(file = f"img_textBox3.png")
entry3_bg = canvas.create_image(
    769.5, 568.0,
    image = entry3_img)

entry3 = Text(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 1)
entry3.config(highlightbackground = "Black", highlightcolor= "Black")

entry3.place(
    x = 615, y = 510,
    width = 309,
    height = 114)

img1 = PhotoImage(file = f"img1.png") #35LAKH
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 73, y = 458,
    width = 195,
    height = 37)

img2 = PhotoImage(file = f"img3.png") #10LAKH
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

img8 = PhotoImage(file = f"img5.png")  #LUXURY
b8 = Button(
    image = img8,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b8.place(
    x = 73, y = 533,
    width = 195,
    height = 36)

img9 = PhotoImage(file = f"img4.png")    #20LAKH
b9 = Button(
    image = img9,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b9.place(
    x = 73, y = 387,
    width = 195,
    height = 36)

b2.place(
    x = 73, y = 323,
    width = 195,
    height = 36)

img7 = PhotoImage(file = f"img7.png") #READMORE
b4 = Button(
    image = img7,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")
b4.place(
    x = 830, y = 197,
    width = 85,
    height = 24)
 #READMORE
b5 = Button(
    image = img7,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")
b5.place(
    x = 830, y = 327,
    width = 85,
    height = 24)
#READMORE
b6 = Button(
    image = img7,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")
b6.place(
    x = 830, y = 457,
    width = 85,
    height = 24)
#READMORE
b7 = Button(
    image = img7,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")
b7.place(
    x = 830, y = 587,
    width = 85,
    height = 24)





img10 = PhotoImage(file = f"img2.png")   #CONTACT US
b10 = Button(
    image = img10,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b10.place(
    x = 114, y = 597,
    width = 113,
    height = 37)

window.resizable(False, False)
window.mainloop()
