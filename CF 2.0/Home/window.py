from tkinter import *


def btn_clicked():
    print("Button Clicked")
    
def change_to_result():
    homeframe.forget()
    resultframe.pack(fill='both', expand=1)

def change_to_info():
    resultframe.forget()
    infoframe.pack(fill='both', expand=1)
    
def sel():
    var.get()
    global category
    if var.get()== 1:
        category = 1
    elif var.get() == 2:
        category = 2
    elif var.get() == 3 :
        category = 3
    return category

def search():
    global budget
    global category
    if category == 1:
        if budget == 10:
            print("Under 10 SUV")
        if budget == 20:
            print("Under 20 SUV")
        if budget == 35:
            print("Under 35 SUV")
    if category== 2:
        if budget ==10:
            print("Under 10 Sedan")
        if budget == 20:
            print("Under 20 Sedan")
        if budget == 35:
            print("Under 35 Sedan")
    if category== 3:
        if budget ==10:
            print("Under 10 Hatchback")
        if budget == 20:
            print("Under 20 Hatchback")
        if budget == 35:
            print("Under 35 Hatchback")
    else:
        pass
    
def clicked10():
    global budget
    budget = 10
    return budget
def clicked20():
    global budget
    budget = 20
    return budget
def clicked35():
    global budget
    budget = 35
    return budget
def clickedluxury():
    global budget
    budget = 100
    return budget


window = Tk()

window.title("Car Finder")
window.iconphoto(True, PhotoImage(file='Logo1.png'))
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

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    531.5, 384.0,
    image=background_img)

#######################RADIO BUTTONS############################

category = 0
budget = 0

var = IntVar()
R1 = Radiobutton(window, text="SUV", variable=var, value=1,
                  command=sel)
R1.place( x=400,y=360,anchor=W )

R2 = Radiobutton(window, text="Sedan", variable=var, value=2,
                  command=sel)
R2.place( x=460,y=360,anchor = W )

R3 = Radiobutton(window, text="Hatchback", variable=var, value=3,
                  command=sel)
R3.place( x=530,y=360,anchor=W)


label = Label(window)
label.pack()

######################BUTTONS#######################################

img6 = PhotoImage(file = f"img6.png")
b6 = Button(
    image = img6,
    borderwidth = 0,
    highlightthickness = 0,
    command = search,
    relief = "flat")

b6.place(
    x = 450, y = 547,
    width = 89,
    height = 37)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = clicked35,
    relief = "flat")

b1.place(
    x = 527, y = 488,
    width = 195,
    height = 37)

img2 = PhotoImage(file = f"img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b2.place(
    x = 438, y = 599,
    width = 113,
    height = 37)

img3 = PhotoImage(file = f"img3.png")
img3clicked = PhotoImage(file = f"active.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = clicked10,
    relief = "flat")

b3.place(
    x = 277, y = 415,
    width = 195,
    height = 36)

img4 = PhotoImage(file = f"img4.png")
b4 = Button(
    image = img4,
    borderwidth = 0,
    highlightthickness = 0,
    command = clicked20,
    relief = "flat")

b4.place(
    x = 527, y = 415,
    width = 195,
    height = 36)

img5 = PhotoImage(file = f"img5.png")
b5 = Button(
    image = img5,
    borderwidth = 0,
    highlightthickness = 0,
    command = clickedluxury,
    relief = "flat")

b5.place(
    x = 277, y = 489,
    width = 195,
    height = 36)

window.resizable(False, False)
window.mainloop()
