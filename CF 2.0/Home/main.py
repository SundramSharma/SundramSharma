import tkinter as tk             # This has all the code for GUIs.
import tkinter.font as font      # This lets us use different fonts.
from tkinter import ttk
import webbrowser



def changetore():
    global category
    global budget
    category1 = category + 1
    budget1 = budget + 10
    homeframe.forget()
    print(category1)
    print(budget1)
    work_frame.pack(fill='both', expand=1)


def changetohome():
    homeframe.pack(fill='both', expand=1)
    work_frame.forget()

def btn_clicked():
    print("Button Clicked")

def contactus():
    webbrowser.open('https://hihello.me/p/f5d99e99-3c30-4376-9b9e-040dbd2e34fb')
    
def sel():
    var.get()
    global category
    if var.get()== 1:
        category = 1
    elif var.get() == 2:
        category = 2
    elif var.get() == 3 :
        category = 3
    print(category)
    return category

def sel1():
    varre.get()
    global category
    if varre.get()== 1:
        category = 1
    elif varre.get() == 2:
        category = 2
    elif varre.get() == 3 :
        category = 3
    print(category)
    return category

def search():
    global budget
    global category
    global entry0
    global entry2
    print(category)
    category1 = category + 1
    budget1 = budget + 10
    changetore()
    print(category1)
    print(budget1)
    _10suv1 = '''TATA Punch
          Price:Rs.5.64 - 8.98 Lakh
          ARAI Mileage: 18.82kmpl 
          Engine Displacement:1199cc'''
    _10suv2 = '''TATA Nexon
        Price:Rs.7.39 - 13.34 Lakh
        ARAI Mileage: 21.5kmpl
        Engine Displacement:1499cc'''
    _10suv3 = '''Maruti Vitara Brezza
        Price:Rs.7.69 - 11.34 Lakh
        ARAI Mileage: 18.76 kmpl
        Engine Displacement: 1462'''
    _10suv4 = '''Hyundai Venue
        Price:Rs.6.99 - 11.87 Lakh
        ARAI Mileage: 18.15 kmpl
        Engine Displacement: 998cc'''
    _10suv5 = '''Mahindra XUV 300
        Price: Rs.8.16 - 13.67 Lakh
        ARAI Mileage: 20.0 kmpl  
        Engine Displacement: 1497cc'''
    _10suv6 = '''Kia Sonet 
        Price: Rs.6.95 - 13.69 Lakh
        ARAI Mileage: 19.0 kmpl
        Engine Displacement: 1493cc'''
    _10suv7 = '''Nissan Magnite
        Price: Rs.5.76 - 10.15 Lakh
        ARAI Mileage: 17.7kmpl
        Engine Displacement: 999cc'''
    _10suv8 = '''Renault Kiger
        Price:Rs.5.79 - 10.22 Lakh
        ARAI Mileage: 20.53 kmpl
        Engine Displacement:999 cc'''
    _10suv9 = '''Maruti S-Cross
         Price: Rs.8.80 - 12.77 Lakh
         ARAI Mileage: 18.55 kmpl
         Engine Displacement: 1462cc'''
    _10suv10 = '''Honda WR-V
         Price: Rs.8.82 - 11.86 Lakh
         ARAI Mileage: 23.7 kmpl
         Engine Displacement: 1498 cc'''

    _20suv1 = '''Mahindra Thar 
        Price: Rs.13.17 - 15.53 Lakh
        ARAI Mileage: 15.2 kmpl
        Engine Displacement: 2184 cc'''
    _20suv2 = '''Tata Harrier
        Price: Rs.14.49 - 21.34 Lakh
        ARAI Mileage: 17.0 kmpl
        Engine Displacement: 1956 cc'''
    _20suv3 = '''Mahindra XUV700
        Price: Rs.12.95 - 23.79 Lakh
        ARAI Mileage: 17.0kmpl
        Engine Displacement: 2198 cc'''
    _20suv4 = '''Mahindra Scorpio
        Price: Rs.13.18 - 18.14 Lakh
        ARAI Mileage: 15.0kmpl
        Engine Displacement: 2179 cc'''

    _35suv1 = '''Toyota Fortuner
        Price:Rs.31.39 - 43.43 Lakh
        ARAI Mileage: 10.0 kmpl
        Engine Displacement:2755 cc'''
    _35suv2 = '''Jeep Compass
        Price:Rs.17.79 - 29.34 Lakh
        ARAI Mileage: 17.1 kmpl
        Engine Displacement: 1956 cc'''
    _35suv3 = '''Hyundai Tucson
        Price: Rs.22.69 - 27.47 Lakh
        ARAI Mileage: 15.38 kmpl
        Engine Displacement: 1999 cc'''
    _35suv4 = '''MG Gloster
        Price: Rs.30.99 - 38.99 Lakh
        ARAI Mileage: 14.5 kmpl
        Engine Displacement: 1996 cc'''

    _10sed1 = ''' '''
    _10sed2 = ''' '''
    _10sed3 = ''' '''
    _10sed4 = ''' '''
    
    _20sed1 = ''' '''
    _20sed2 = ''' '''
    _20sed3 = ''' '''
    _20sed4 = ''' '''

    _35sed1 = ''' '''
    _35sed2 = ''' '''
    _35sed3 = ''' '''
    _35sed4 = ''' '''
    
    _10hat1 = ''' '''
    _10hat2 = ''' '''
    _10hat3 = ''' '''
    _10hat4 = ''' '''
    
    _20hat1 = ''' '''
    _20hat2 = ''' '''
    _20hat3 = ''' '''
    _20hat4 = ''' '''

    _35hat1 = ''' '''
    _35hat2 = ''' '''
    _35hat3 = ''' '''
    _35hat4 = ''' '''
    
    if category1 == 2:
        print('Category chosen = SUV')
        if budget1 == 20:
            print('Budget Chosen = 10 Lakh')
            print("Under 10 SUV")
            entry0.config(state='normal')
            entry1.config(state='normal')
            entry2.config(state='normal')
            entry3.config(state='normal')
            
            entry0.replace(1.0 ,10.0, _10suv1)
            entry1.replace(1.0 ,10.0, _10suv2)
            entry2.replace(1.0 ,10.0, _10suv3)  
            entry3.replace(1.0 ,10.0, _10suv3)
        
            entry0.config(state='disabled')
            entry1.config(state='disabled')
            entry2.config(state='disabled')
            entry3.config(state='disabled')
            
        if budget1 == 30:
            print('Budget Chosen = 20 Lakh')
            print("Under 20 SUV")
            entry0.config(state='normal')
            entry1.config(state='normal')
            entry2.config(state='normal')
            entry3.config(state='normal')

            entry0.replace(1.0 , 10.0, _20suv1)
            entry1.replace(1.0 , 10.0, _20suv2)
            entry2.replace(1.0 , 10.0, _20suv3)
            entry3.replace(1.0 , 10.0, _20suv4)
            
            entry0.config(state='disabled')
            entry1.config(state='disabled')
            entry2.config(state='disabled')
            entry3.config(state='disabled')
            
        if budget1 == 45:
            print('Budget Chosen = 35 Lakh')
            print("Under 35 SUV")
            entry0.config(state='normal')
            entry1.config(state='normal')
            entry2.config(state='normal')
            entry3.config(state='normal')

            entry0.replace(1.0 , 10.0, _35suv1)
            entry1.replace(1.0 , 10.0, _35suv2)
            entry2.replace(1.0 , 10.0, _35suv3)
            entry3.replace(1.0 , 10.0, _35suv4)
        
            entry0.config(state='disabled')
            entry1.config(state='disabled')
            entry2.config(state='disabled')
            entry3.config(state='disabled')
            
    if category1 == 3:
        print('Category chosen = Sedan')
        if budget1 ==20:
            print('Budget Chosen = 10 Lakh')
            print("Under 10 Sedan")
            entry0.config(state='normal')
            entry1.config(state='normal')
            entry2.config(state='normal')
            entry3.config(state='normal')
            
            entry0.replace(1.0 ,10.0, _10sed1)
            entry1.replace(1.0 ,10.0, _10sed2)
            entry2.replace(1.0 ,10.0, _10sed3)  
            entry3.replace(1.0 ,10.0, _10sed3)
        
            entry0.config(state='disabled')
            entry1.config(state='disabled')
            entry2.config(state='disabled')
            entry3.config(state='disabled')

        if budget1 == 30:
            print('Budget Chosen = 20 Lakh')
            print("Under 20 Sedan")
            entry0.config(state='normal')
            entry1.config(state='normal')
            entry2.config(state='normal')
            entry3.config(state='normal')
            
            entry0.replace(1.0 ,10.0, _20sed1)
            entry1.replace(1.0 ,10.0, _20sed2)
            entry2.replace(1.0 ,10.0, _20sed3)  
            entry3.replace(1.0 ,10.0, _20sed3)
        
            entry0.config(state='disabled')
            entry1.config(state='disabled')
            entry2.config(state='disabled')
            entry3.config(state='disabled') 
        if budget1 == 45:
            print('Budget Chosen = 35 Lakh')
            print("Under 35 Sedan")
            entry0.config(state='normal')
            entry1.config(state='normal')
            entry2.config(state='normal')
            entry3.config(state='normal')
            
            entry0.replace(1.0 ,10.0, _35sed1)
            entry1.replace(1.0 ,10.0, _35sed2)
            entry2.replace(1.0 ,10.0, _35sed3)  
            entry3.replace(1.0 ,10.0, _35sed3)
        
            entry0.config(state='disabled')
            entry1.config(state='disabled')
            entry2.config(state='disabled')
            entry3.config(state='disabled')
            
    if category1 == 4:
        print('Category chosen = Hatchback')
        if budget1 ==20:
            print('Budget Chosen = 10 Lakh')
            print("Under 10 Hatchback")
            entry0.config(state='normal')
            entry1.config(state='normal')
            entry2.config(state='normal')
            entry3.config(state='normal')
            
            entry0.replace(1.0 ,10.0, _10hat1)
            entry1.replace(1.0 ,10.0, _10hat2)
            entry2.replace(1.0 ,10.0, _10hat3)  
            entry3.replace(1.0 ,10.0, _10hat3)
        
            entry0.config(state='disabled')
            entry1.config(state='disabled')
            entry2.config(state='disabled')
            entry3.config(state='disabled')
            
        if budget1 == 30:
            print('Budget Chosen = 20 Lakh')
            print("Under 20 Hatchback")
            entry0.config(state='normal')
            entry1.config(state='normal')
            entry2.config(state='normal')
            entry3.config(state='normal')
            
            entry0.replace(1.0 ,10.0, _20hat1)
            entry1.replace(1.0 ,10.0, _20hat2)
            entry2.replace(1.0 ,10.0, _20hat3)  
            entry3.replace(1.0 ,10.0, _20hat3)
        
            entry0.config(state='disabled')
            entry1.config(state='disabled')
            entry2.config(state='disabled')
            entry3.config(state='disabled')
            
        if budget1 == 45:
            print('Budget Chosen = 35 Lakh')
            print("Under 35 Hatchback")
            entry0.config(state='normal')
            entry1.config(state='normal')
            entry2.config(state='normal')
            entry3.config(state='normal')
            
            entry0.replace(1.0 ,10.0, _35hat1)
            entry1.replace(1.0 ,10.0, _35hat2)
            entry2.replace(1.0 ,10.0, _35hat3)  
            entry3.replace(1.0 ,10.0, _35hat3)
        
            entry0.config(state='disabled')
            entry1.config(state='disabled')
            entry2.config(state='disabled')
            entry3.config(state='disabled')
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

# Now we get to the program itself:-
# Let's set up the window ...
root = tk.Tk()
root.title("My Work - Swapping frames")
root.geometry("1007x650")
root.configure(bg='#ffffff')
# Set the icon used for your program
root.iconphoto(True, tk.PhotoImage(file='logo.png'))

#screen_width = root.winfo_screenwidth()
#screen_height = root.winfo_screenheight()

# Here, we create two frames of which only one will be visible at a time.
homeframe = tk.Frame(root)
work_frame = tk.Frame(root)

# Let's create the fonts that we need.
font_large = font.Font(family='Georgia',
                       size='24',
                       weight='bold')
font_small = font.Font(family='Georgia',
                       size='12')

# The widgets needed for the quiz frame.
# First, let's display te logo.
canvas = tk.Canvas(
    homeframe,
    bg = "#ffffff",
    height = 650,
    width = 1007,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = tk.PhotoImage(file = f"background.png")
background = canvas.create_image(
    531.5, 384.0,
    image=background_img)


category = 0
budget = 0
##################################RADIO#####################################
var = tk.IntVar()
R1 = tk.Radiobutton(homeframe, text="SUV", variable=var, value=1,
                  command=sel)
R1.place( x=400,y=360,anchor= 'w' )

R2 = tk.Radiobutton(homeframe, text="Sedan", variable=var, value=2,
                  command=sel)
R2.place( x=460,y=360,anchor = 'w' )

R3 = tk.Radiobutton(homeframe, text="Hatchback", variable=var, value=3,
                  command=sel)
R3.place( x=530,y=360,anchor='w')



##########################################BUTTONS##############################
img6 = tk.PhotoImage(file = f"img6.png")
b6 = tk.Button(
    homeframe,
    image = img6,
    borderwidth = 0,
    highlightthickness = 0,
    command = search,
    relief = "flat")

b6.place(
    x = 450, y = 547,
    width = 89,
    height = 37)

img1 = tk.PhotoImage(file = f"img1.png")
b1 = tk.Button(
    homeframe,
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = clicked35,
    relief = "flat")

b1.place(
    x = 527, y = 488,
    width = 195,
    height = 37)

img2 = tk.PhotoImage(file = f"img2.png")
b2 = tk.Button(
    homeframe,
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = contactus,
    relief = "flat")

b2.place(
    x = 438, y = 599,
    width = 113,
    height = 37)

img3 = tk.PhotoImage(file = f"img3.png")
b3 = tk.Button(
    homeframe,
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = clicked10,
    relief = "flat")

b3.place(
    x = 277, y = 415,
    width = 195,
    height = 36)

img4 = tk.PhotoImage(file = f"img4.png")
b4 = tk.Button(
    homeframe,
    image = img4,
    borderwidth = 0,
    highlightthickness = 0,
    command = clicked20,
    relief = "flat")

b4.place(
    x = 527, y = 415,
    width = 195,
    height = 36)

img5 = tk.PhotoImage(file = f"img5.png")
b5 = tk.Button(
    homeframe,
    image = img5,
    borderwidth = 0,
    highlightthickness = 0,
    command = clickedluxury,
    relief = "flat")

b5.place(
    x = 277, y = 489,
    width = 195,
    height = 36)


img_logo = tk.PhotoImage(file='logo.png')
lbl_logo_quiz = tk.Label(homeframe,
                         image=img_logo)

# And finally, the button to swap between the frames.
#btn_changetore = tk.Button(homeframe,
   #                            text='Change to work',
      #                         font=font_small,
    #                           command=changetore)
#btn_changetore.pack(pady=20)

# The widgets needed for the work frame.
# These are only being used in this example
# to show that both frames are working as expected.
canvasresults = tk.Canvas(
    work_frame,
    bg = "#ffffff",
    height = 650,
    width = 1007,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvasresults.place(x=0,y=0)

Resultswin = tk.Canvas(
    work_frame,
    bg = "#ffffff",
    height = 589,
    width = 608,
    bd = 0,
    highlightthickness = 1,
    relief = "ridge")
Resultswin.config(highlightbackground="black",highlightcolor="black")
Resultswin.place(x = 375, y = 53)


background_img1 = tk.PhotoImage(file = f"background1.png")
background1 = canvasresults.create_image(
    186.5, 125.0,
    image=background_img1)

Resultswin.create_text(
    320, 40,
    text = "Top results for your search\n",
    fill = "#000000",
    font = ("None", int(16.0)))

#############################TEXTBOXES#######################################
entry0_img = tk.PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvasresults.create_image(
    769.5, 306.0,
    image = entry0_img)

entry0 = tk.Text(
    work_frame,
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 1)
entry0.config(highlightbackground = "Black", highlightcolor= "Black")

entry0.place(
    x = 615, y = 248,
    width = 309,
    height = 114)

entry1_img = tk.PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvasresults.create_image(
    769.5, 175.0,
    image = entry1_img)

entry1 = tk.Text(
    work_frame,
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 1)
entry1.config(highlightbackground = "Black", highlightcolor= "Black")

entry1.place(
    x = 615, y = 117,
    width = 309,
    height = 114)

entry2_img = tk.PhotoImage(file = f"img_textBox2.png")
entry2_bg = canvasresults.create_image(
    769.5, 437.0,
    image = entry2_img)

entry2 = tk.Text(
    work_frame,
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 1)
entry2.insert(1.0,"HI")
entry2.config(highlightbackground = "Black", highlightcolor= "Black")

entry2.place(
    x = 615, y = 379,
    width = 309,
    height = 114)

entry3_img = tk.PhotoImage(file = f"img_textBox3.png")
entry3_bg = canvasresults.create_image(
    769.5, 568.0,
    image = entry3_img)

entry3 = tk.Text(
    work_frame,
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 1)
entry3.config(highlightbackground = "Black", highlightcolor= "Black")

entry3.place(
    x = 615, y = 510,
    width = 309,
    height = 114)

#################################RADIO BUTTONS###############################
varre = tk.IntVar()
R1re = tk.Radiobutton(work_frame, text="SUV", variable=varre, value=1,
                  command=sel1)
R1re.place( x=75,y=257,anchor= 'w' )

R2re = tk.Radiobutton(work_frame, text="Sedan", variable=varre, value=2,
                  command=sel1)
R2re.place( x=135,y=257,anchor = 'w' )

R3re = tk.Radiobutton(work_frame, text="Hatchback", variable=varre, value=3,
                  command=sel1)
R3re.place( x=205,y=257,anchor='w')


#################################BUTTONS RESULTS PAGE#########################
img0 = tk.PhotoImage(file = f"img0.png")        #BACK BUTTON
b0 = tk.Button(
    work_frame,
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = changetohome,
    relief = "flat")

b0.place(
    x = 375, y = 28,
    width = 24,
    height = 24)

 #35LAKH
b1 = tk.Button(
    work_frame,
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = clicked35,
    relief = "flat")

b1.place(
    x = 73, y = 433,
    width = 195,
    height = 37)

 #10LAKH
b2 = tk.Button(
    work_frame,
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = clicked10,
    relief = "flat")

b2.place(
    x = 75, y = 311,
    width = 195,
    height = 36)

 #LUXURY
b8 = tk.Button(
    work_frame,
    image = img5,
    borderwidth = 0,
    highlightthickness = 0,
    command = clickedluxury,
    relief = "flat")

b8.place(
    x = 75, y = 495,
    width = 195,
    height = 36)

    #20LAKH
b9 = tk.Button(
    work_frame,
    image = img4,
    borderwidth = 0,
    highlightthickness = 0,
    command = clicked20,
    relief = "flat")

b9.place(
    x = 73, y = 372,
    width = 195,
    height = 36)

img7 = tk.PhotoImage(file = f"img7.png") #READMORE
b4 = tk.Button(
    work_frame,
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
b5 = tk.Button(
    work_frame,
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
b6 = tk.Button(
    work_frame,
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
b7 = tk.Button(
    work_frame,
    image = img7,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")
b7.place(
    x = 830, y = 587,
    width = 85,
    height = 24)

#SEARCH BUTTON
b11 = tk.Button(
    work_frame,
    image = img6,
    borderwidth = 0,
    highlightthickness = 0,
    command = search,
    relief = "flat")

b11.place(
    x = 128, y = 549,
    width = 89,
    height = 37)



img10 = tk.PhotoImage(file = f"img2.png")   #CONTACT US
b10 = tk.Button(
    work_frame,
    image = img10,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b10.place(
    x = 114, y = 597,
    width = 113,
    height = 37)



# Only the quiz frame needs to be shown
# when the program starts.  The work frame
# will only appear when the Change button
# is clicked.
homeframe.pack(fill='both', expand=1)

root.resizable(False, False)
root.mainloop()
