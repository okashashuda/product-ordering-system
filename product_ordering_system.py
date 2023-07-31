from tkinter import * #imports tkinter lib
import tkinter.messagebox #imports tkinter messagebox from tkinter lib

addtocart = [] #empty list for total quantity in shopping cart
quadstellar = [] #empty list for quantity of specified item
moonrock = []
snowflake = []
boomer = []
interstellar = []
nasasuper = []
heatwave = []
zoomer = []
quantity = [1] #list used to append 1 item to each respective cart
price = [2800, 4000, 1000, 900] #list for prices

def clearcart(): #function to clear cart after pressing clear cart button on home page (OKASHA)
    quadstellar.clear() #clears each respective list
    moonrock.clear()
    snowflake.clear()
    boomer.clear()
    interstellar.clear()
    nasasuper.clear()
    heatwave.clear()
    zoomer.clear()
    addtocart.set(0) #resets cart to 0 because this is set as an IntVar, so we cannot use clear command
    
def menu(): #function for the sidebar menu
    def sidebarhide(): #function to hide the sidebar(HARNOOR)
        sidebarlol = Label(app, width=33, height=41, bg="AntiqueWhite3").place(relx=0.0096, rely=0.40) #label that had a bg of white that covers the sidebar
        sidebar = Button(app, text="=", width=25, height=1, bg="#383838", command=menu, fg="white", font=("Calibri", 13, "bold")) #sidebar button which makes the side bar appear and disappear
        sidebar.place(relx=0.01, rely=0.350) #coordinates for sidebar
        product = Label(app, width=500, height=310, bg="AntiqueWhite3").place(relx=0.165, rely=0.335) #label that hides products
        
    def pcs(): #function for PC products(HARNOOR)
        pc = PhotoImage(file = "pc1.png", height=300) #imports image for first pc
        w = Label(app, image = pc) #creates a label for the image so we can use it to edit dimensions and properties
        w.place(relx=0.165, rely=0.350) #coords for image
        w.photo = pc 
        pc = Label(app, text="Quadstellar", width=10, height=1, bg="#383838", fg="#ffa500", font=("Calibri", 13, "bold")) #adds label of our product name
        pc.place(relx=0.165, rely=0.350) #coords for product name
        pctext = Label(app, text="Price: $2800", width=33, font=("Calibri", 13, "bold")) #prices(appearance only)
        pctext.place(relx=0.165, rely=0.650) #coords for prices
        pctext2 = Label(app, text="Intel Core i7 8700K\n RTX 2060 Super\n DDR4 16GB 3200Mhz\n 1TB HDD", width=33, font=("Calibri", 13, "bold")) #PC specs
        pctext2.place(relx=0.165, rely=0.690) #pc specs coords
        cartbutton = Button(app, text="Add To Cart", width=33, borderwidth=3, relief="solid", bg="#383838", fg="#ffa500", command=cartqty1, font=("Calibri", 13, "bold")) #add to cart button which appends to the main cart, and the secondary product cart which is used for the checkout screen to see how much of what you ordered
        cartbutton.place(relx=0.165, rely=0.790)
        
        pc = PhotoImage(file = "pc2.png", height=300)
        w = Label(app, image = pc)
        w.place(relx=0.365, rely=0.350)
        w.photo = pc
        pc = Label(app, text="Moonrock", width=10, height=1, bg="#383838", fg="#ffa500", font=("Calibri", 13, "bold"))
        pc.place(relx=0.365, rely=0.350)
        pc.pack
        pctext = Label(app, text="Price: $4000", width=33, font=("Calibri", 13, "bold"))
        pctext.place(relx=0.365, rely=0.650)
        pctext2 = Label(app, text="AMD Threadripper 2950X\n RTX 2080Ti\n DDR4 64GB 3200Mhz\n 2TB SSD", width=33, font=("Calibri", 13, "bold"))
        pctext2.place(relx=0.365, rely=0.690)
        cartbutton = Button(app, text="Add To Cart", width=33, borderwidth=3, relief="solid", bg="#383838", fg="#ffa500", command=cartqty2, font=("Calibri", 13, "bold"))
        cartbutton.place(relx=0.365, rely=0.790)
        
        pc = PhotoImage(file = "pc3.png", height=300)
        w = Label(app, image = pc)
        w.place(relx=0.565, rely=0.350)
        w.photo = pc
        pc = Label(app, text="Snowflake", width=10, height=1, bg="#383838", fg="#ffa500", font=("Calibri", 13, "bold"))
        pc.place(relx=0.565, rely=0.350)
        pc.pack
        pctext = Label(app, text="Price: $1000", width=33, font=("Calibri", 13, "bold"))
        pctext.place(relx=0.565, rely=0.650)
        pctext2 = Label(app, text="AMD Ryzen 7 2700x\n RTX 2060 OC\n DDR4 16GB 3200Mhz\n 1TB HDD", width=33, font=("Calibri", 13, "bold"))
        pctext2.place(relx=0.565, rely=0.690)
        cartbutton = Button(app, text="Add To Cart", width=33, borderwidth=3, relief="solid", bg="#383838", fg="#ffa500", command=cartqty3, font=("Calibri", 13, "bold"))
        cartbutton.place(relx=0.565, rely=0.790)
        
        pc = PhotoImage(file = "pc4.png", height=300)
        w = Label(app, image = pc)
        w.place(relx=0.765, rely=0.350)
        w.photo = pc
        pc = Label(app, text="Boomer", width=10, height=1, bg="#383838", fg="#ffa500", font=("Calibri", 13, "bold"))
        pc.place(relx=0.765, rely=0.350)
        pc.pack
        pctext = Label(app, text="Price: $900", width=33, font=("Calibri", 13, "bold"))
        pctext.place(relx=0.765, rely=0.650)
        pctext2 = Label(app, text="AMD Ryzen 5 1600\n GTX 1660Ti\n DDR4 8GB 3200Mhz\n 1TB HDD", width=33, font=("Calibri", 13, "bold"))
        pctext2.place(relx=0.765, rely=0.690)
        cartbutton = Button(app, text="Add To Cart", width=33, borderwidth=3, relief="solid", bg="#383838", fg="#ffa500", command=cartqty4, font=("Calibri", 13, "bold"))
        cartbutton.place(relx=0.765, rely=0.790)
        
        Button(app, text="Checkout", width=11, height=2, borderwidth=3, relief="solid", bg="#ffa500", fg="black", command=checkoutscreen, font=("Calibri", 10, "bold")).place(relx=0.947, rely=0.240) #checkout button which opens checkout screen
        Button(app, text="Clear Cart", width=11, height=2, borderwidth=3, relief="solid", bg="#ffa500", fg="black", command=clearcart, font=("Calibri", 10, "bold")).place(relx=0.947, rely=0.205) #clear cart button which clears the main and secondary carts
        
        Label(app, text="Items In Cart:", width=11, height=2, borderwidth=3, relief="solid", font=("Calibri", 10, "bold")).place(relx=0.917, rely=0.285) 
        Label(app, textvariable = addtocart, width=8, height=2, borderwidth=3, relief="solid", font=("Calibri", 10, "bold")).place(relx=0.960, rely=0.285) #label which shows the total number of items in the cart
        
    def laptops(): #same things as PCs(OKASHA)
        pc = PhotoImage(file = "laptop1.png", height=300)
        w = Label(app, image = pc)
        w.place(relx=0.165, rely=0.350)
        w.photo = pc
        pc = Label(app, text="Interstellar", width=10, height=1, bg="#383838", fg="#ffa500", font=("Calibri", 13, "bold"))
        pc.place(relx=0.165, rely=0.350)
        pc.pack
        pctext = Label(app, text="Price: $2800", width=33, font=("Calibri", 13, "bold"))
        pctext.place(relx=0.165, rely=0.650)
        pctext2 = Label(app, text="Intel Core i5 6700K\n GTX 1060Ti\n DDR4 16GB 3000Mhz\n 1TB HDD", width=33, font=("Calibri", 13, "bold"))
        pctext2.place(relx=0.165, rely=0.690)
        cartbutton = Button(app, text="Add To Cart", width=33, borderwidth=3, relief="solid", bg="#383838", fg="#ffa500", command=cartqty5, font=("Calibri", 13, "bold"))
        cartbutton.place(relx=0.165, rely=0.790)
        
        pc = PhotoImage(file = "laptop2.png", height=300)
        w = Label(app, image = pc)
        w.place(relx=0.365, rely=0.350)
        w.photo = pc
        pc = Label(app, text="NASA Super", width=10, height=1, bg="#383838", fg="#ffa500", font=("Calibri", 13, "bold"))
        pc.place(relx=0.365, rely=0.350)
        pc.pack
        pctext = Label(app, text="Price: $4000", width=33, font=("Calibri", 13, "bold"))
        pctext.place(relx=0.365, rely=0.650)
        pctext2 = Label(app, text="AMD Threadripper 2950X\n RTX 2080Ti\n DDR4 64GB 3200Mhz\n 2TB SSD", width=33, font=("Calibri", 13, "bold"))
        pctext2.place(relx=0.365, rely=0.690)
        cartbutton = Button(app, text="Add To Cart", width=33, borderwidth=3, relief="solid", bg="#383838", fg="#ffa500", command=cartqty6, font=("Calibri", 13, "bold"))
        cartbutton.place(relx=0.365, rely=0.790)
        
        pc = PhotoImage(file = "laptop3.png", height=300)
        w = Label(app, image = pc)
        w.place(relx=0.565, rely=0.350)
        w.photo = pc
        pc = Label(app, text="Heatwave", width=10, height=1, bg="#383838", fg="#ffa500", font=("Calibri", 13, "bold"))
        pc.place(relx=0.565, rely=0.350)
        pc.pack
        pctext = Label(app, text="Price: $1000", width=33, font=("Calibri", 13, "bold"))
        pctext.place(relx=0.565, rely=0.650)
        pctext2 = Label(app, text="AMD Ryzen 5 1600g\n GTX 1050Ti OC\n DDR4 8GB 3000Mhz\n 1TB HDD", width=33, font=("Calibri", 13, "bold"))
        pctext2.place(relx=0.565, rely=0.690)
        cartbutton = Button(app, text="Add To Cart", width=33, borderwidth=3, relief="solid", bg="#383838", fg="#ffa500", command=cartqty7, font=("Calibri", 13, "bold"))
        cartbutton.place(relx=0.565, rely=0.790)
        
        pc = PhotoImage(file = "laptop4.png", height=300)
        w = Label(app, image = pc)
        w.place(relx=0.765, rely=0.350)
        w.photo = pc
        pc = Label(app, text="Zoomer", width=10, height=1, bg="#383838", fg="#ffa500", font=("Calibri", 13, "bold"))
        pc.place(relx=0.765, rely=0.350)
        pc.pack
        pctext = Label(app, text="Price: $900", width=33, font=("Calibri", 13, "bold"))
        pctext.place(relx=0.765, rely=0.650)
        pctext2 = Label(app, text="AMD Ryzen 5 1600\n GTX 950Ti\n DDR4 8GB 3000Mhz\n 1TB HDD", width=33, font=("Calibri", 13, "bold"))
        pctext2.place(relx=0.765, rely=0.690)
        cartbutton = Button(app, text="Add To Cart", width=33, borderwidth=3, relief="solid", bg="#383838", fg="#ffa500", command=cartqty8, font=("Calibri", 13, "bold"))
        cartbutton.place(relx=0.765, rely=0.790)
                
        Button(app, text="Checkout", width=11, height=2, borderwidth=3, relief="solid", bg="#ffa500", fg="black", command=checkoutscreen, font=("Calibri", 10, "bold")).place(relx=0.947, rely=0.240)
        Button(app, text="Clear Cart", width=11, height=2, borderwidth=3, relief="solid", bg="#ffa500", fg="black", command=clearcart, font=("Calibri", 10, "bold")).place(relx=0.947, rely=0.205)
        
        Label(app, text="Items In Cart:", width=11, height=2, borderwidth=3, relief="solid", font=("Calibri", 10, "bold")).place(relx=0.917, rely=0.285)
        Label(app, textvariable = addtocart, width=8, height=2, borderwidth=3, relief="solid", font=("Calibri", 10, "bold")).place(relx=0.960, rely=0.285)

    sidebarlol = Label(app, width=33, height=41, bg="#383838").place(relx=0.0096, rely=0.40)
    button2 = Button(app, text="=", width=25, height=1, bg="#383838", command=sidebarhide, fg="white", font=("Calibri", 13, "bold")) #button which hides the sidebar
    button2.place(relx=0.01, rely=0.350)
    
    gaming = Button(app, text="Gaming PCs", width=23, height=1, bg="#ffa500", fg="#383838", borderwidth=3, relief="solid", command=pcs, font=("Calibri", 13, "bold")) #button that shows pc products
    gaming.place(relx=0.0145, rely=0.410)
    
    laptop = Button(app, text="Laptops", width=23, height=1, bg="#ffa500", fg="#383838", borderwidth=3, relief="solid", command=laptops, font=("Calibri", 13, "bold")) #button that shows laptop products
    laptop.place(relx=0.0145, rely=0.470)

app = Tk() #main form for main menu(HARNOOR AND OKASHA)
app.title("APC - A PC BUILT LIKE A TANK") #title for main form
app.state("zoomed") #basically makes the form fullscreen automatically
app.resizable(0,0) #makes it so you cannot resize the form
app.config(bg="AntiqueWhite3") #bg of form
logo = PhotoImage(file = "logo.png", height=350) #photo that displays our logo at the top header
w = Label(app, image = logo)
w.photo = logo
w.pack()

sidebar = Button(app, text="=", width=23, height=1, bg="#383838", command=menu, fg="white", font=("Calibri", 13, "bold")) #sidebar button which opens and closes sidebar
sidebar.place(relx=0.01, rely=0.350)

addtocart = IntVar() #makes addtocart an intvar
addtocart.set(0) #sets add to cart to 0 because it is an intvar

def checkoutscreen(): #function for our checkout screen (HARNOOR)
    global e1 #globals our entry boxes which basically makes them visible to the entire code
    global e2
    global e3
    global e4
    global e5
    global e6
    global e7
    global e8
    global e9
    global e10
    global e11
    global e12
    global chk
    chk = Tk() #form for our checkout screen
    chk.title("Checkout")
    chk.geometry("800x800+540+120") #the size  of our checkout screen which makes it centered as well
    chk.config(bg="#383838")
    chk.resizable(0,0) 
    
    Label(chk, width=3, height=100, bg="white").place(relx=0.37, rely=0.298)
    Label(chk, text= "View Order", bg="orange", width="500", height="8", font=("Calibri", 18, "bold")).pack()
    Label(chk, text= "Quantity:", bg="orange", width=8, height=2, font=("Calibri", 10, "bold")).place(relx=0.01, rely=0.320)
    Label(chk, text = sum(quadstellar), width=8, height=2, borderwidth=3, relief="solid", font=("Calibri", 10, "bold")).place(relx=0.01, rely=0.375) #label which includes the sum of items in the quadstellar cart, we basically made multiple lists or carts for each product so we can show the user how much of what they ordered and then eventually give them a total.
    Label(chk, text = sum(moonrock), width=8, height=2, borderwidth=3, relief="solid", font=("Calibri", 10, "bold")).place(relx=0.01, rely=0.425)
    Label(chk, text = sum(snowflake), width=8, height=2, borderwidth=3, relief="solid", font=("Calibri", 10, "bold")).place(relx=0.01, rely=0.475)
    Label(chk, text = sum(boomer), width=8, height=2, borderwidth=3, relief="solid", font=("Calibri", 10, "bold")).place(relx=0.01, rely=0.525)
    Label(chk, text = sum(interstellar), width=8, height=2, borderwidth=3, relief="solid", font=("Calibri", 10, "bold")).place(relx=0.01, rely=0.575)
    Label(chk, text = sum(nasasuper), width=8, height=2, borderwidth=3, relief="solid", font=("Calibri", 10, "bold")).place(relx=0.01, rely=0.625)
    Label(chk, text = sum(heatwave), width=8, height=2, borderwidth=3, relief="solid", font=("Calibri", 10, "bold")).place(relx=0.01, rely=0.675)
    Label(chk, text = sum(zoomer), width=8, height=2, borderwidth=3, relief="solid", font=("Calibri", 10, "bold")).place(relx=0.01, rely=0.725)
    Label(chk, text= "Item:", bg="orange", width=15, height=2, font=("Calibri", 10, "bold")).place(relx=0.10, rely=0.320)
    Label(chk, text = "Quadstellar", width=15, height=2, borderwidth=3, relief="solid", font=("Calibri", 10, "bold")).place(relx=0.10, rely=0.375)
    Label(chk, text = "Moonrock", width=15, height=2, borderwidth=3, relief="solid", font=("Calibri", 10, "bold")).place(relx=0.10, rely=0.425)
    Label(chk, text = "Snowflake", width=15, height=2, borderwidth=3, relief="solid", font=("Calibri", 10, "bold")).place(relx=0.10, rely=0.475)
    Label(chk, text = "Boomer", width=15, height=2, borderwidth=3, relief="solid", font=("Calibri", 10, "bold")).place(relx=0.10, rely=0.525)
    Label(chk, text = "Interstellar", width=15, height=2, borderwidth=3, relief="solid", font=("Calibri", 10, "bold")).place(relx=0.10, rely=0.575)
    Label(chk, text = "NasaSuper", width=15, height=2, borderwidth=3, relief="solid", font=("Calibri", 10, "bold")).place(relx=0.10, rely=0.625)
    Label(chk, text = "Heatwave", width=15, height=2, borderwidth=3, relief="solid", font=("Calibri", 10, "bold")).place(relx=0.10, rely=0.675)
    Label(chk, text = "Zoomer", width=15, height=2, borderwidth=3, relief="solid", font=("Calibri", 10, "bold")).place(relx=0.10, rely=0.725)
    Label(chk, text= "Price:", bg="orange", width=10, height=2, font=("Calibri", 10, "bold")).place(relx=0.25, rely=0.320)
    Label(chk, text = sum(quadstellar)*(price[0]), width=10, height=2, borderwidth=3, relief="solid", font=("Calibri", 10, "bold")).place(relx=0.25, rely=0.375) #label which multiplies the quantity of the item and its respective price
    Label(chk, text = sum(moonrock)*(price[1]), width=10, height=2, borderwidth=3, relief="solid", font=("Calibri", 10, "bold")).place(relx=0.25, rely=0.425)
    Label(chk, text = sum(snowflake)*(price[2]), width=10, height=2, borderwidth=3, relief="solid", font=("Calibri", 10, "bold")).place(relx=0.25, rely=0.475)
    Label(chk, text = sum(boomer)*(price[3]), width=10, height=2, borderwidth=3, relief="solid", font=("Calibri", 10, "bold")).place(relx=0.25, rely=0.525)
    Label(chk, text = sum(interstellar)*(price[0]), width=10, height=2, borderwidth=3, relief="solid", font=("Calibri", 10, "bold")).place(relx=0.25, rely=0.575)
    Label(chk, text = sum(nasasuper)*(price[1]), width=10, height=2, borderwidth=3, relief="solid", font=("Calibri", 10, "bold")).place(relx=0.25, rely=0.625)
    Label(chk, text = sum(heatwave)*(price[2]), width=10, height=2, borderwidth=3, relief="solid", font=("Calibri", 10, "bold")).place(relx=0.25, rely=0.675)
    Label(chk, text = sum(zoomer)*(price[3]), width=10, height=2, borderwidth=3, relief="solid", font=("Calibri", 10, "bold")).place(relx=0.25, rely=0.725)
    total = Label(chk, text = sum(quadstellar)*(price[0]) + sum(moonrock)*(price[1]) + sum(snowflake)*(price[2]) + sum(boomer)*(price[3]) + sum(interstellar)*(price[0]) + sum(nasasuper)*(price[1]) + sum(heatwave)*(price[2]) + sum(zoomer)*(price[3]), width=10, height=2, borderwidth=3, relief="solid", font=("Calibri", 10, "bold")).place(relx=0.25, rely=0.775) #label which gets the total price of all items
        
    #(OKASHA)    
    Label(chk, text = "First Name: *", width=18, height=2, bg="orange", font=("Calibri", 10, "bold")).place(relx=0.43, rely=0.320) #label for first name entry
    e1 = Entry(chk, borderwidth=3, relief="solid") #entry for first name label
    e1.place(relx=0.60, rely=0.320, height=37) #coords for entry box
    e1.get() #gets info written in entry box 
    Label(chk, text = "Last Name: *", width=18, height=2, bg="orange", font=("Calibri", 10, "bold")).place(relx=0.43, rely=0.370)
    e2 = Entry(chk, borderwidth=3, relief="solid")
    e2.place(relx=0.60, rely=0.370, height=37)
    e2.get()
    Label(chk, text = "Phone Number: *", width=18, height=2, bg="orange", font=("Calibri", 10, "bold")).place(relx=0.43, rely=0.420)
    e3 = Entry(chk, borderwidth=3, relief="solid")
    e3.place(relx=0.60, rely=0.420, height=37)
    e3.get()
    Label(chk, text = "Email Address: *", width=18, height=2, bg="orange", font=("Calibri", 10, "bold")).place(relx=0.43, rely=0.470)
    e4 = Entry(chk, borderwidth=3, relief="solid")
    e4.place(relx=0.60, rely=0.470, height=37)
    e4.get()
    Label(chk, text = "Address: *", width=18, height=2, bg="orange", font=("Calibri", 10, "bold")).place(relx=0.43, rely=0.520)
    e5 = Entry(chk, borderwidth=3, relief="solid")
    e5.place(relx=0.60, rely=0.520, height=37)
    e5.get()
    Label(chk, text = "Address: (optional)", width=18, height=2, bg="orange", font=("Calibri", 10, "bold")).place(relx=0.43, rely=0.570)
    Entry(chk, borderwidth=3, relief="solid").place(relx=0.60, rely=0.570, height=37)
    Label(chk, text = "City: *", width=18, height=2, bg="orange", font=("Calibri", 10, "bold")).place(relx=0.43, rely=0.620)
    e6 = Entry(chk, borderwidth=3, relief="solid")
    e6.place(relx=0.60, rely=0.620, height=37)
    e6.get()
    Label(chk, text = "Province/State: *", width=18, height=2, bg="orange", font=("Calibri", 10, "bold")).place(relx=0.43, rely=0.670)
    e7 = Entry(chk, borderwidth=3, relief="solid")
    e7.place(relx=0.60, rely=0.670, height=37)
    e7.get()
    Label(chk, text = "Country: *", width=18, height=2, bg="orange", font=("Calibri", 10, "bold")).place(relx=0.43, rely=0.720)
    e8 = Entry(chk, borderwidth=3, relief="solid")
    e8.place(relx=0.60, rely=0.720, height=37)
    e8.get()
    Label(chk, text = "Postal Code/Zip Code: *", width=18, height=2, bg="orange", font=("Calibri", 10, "bold")).place(relx=0.43, rely=0.770)
    e9 = Entry(chk, borderwidth=3, relief="solid")
    e9.place(relx=0.60, rely=0.770, height=37)
    e9.get()
    Label(chk, text="Credit Card Number: *", width=18, height=2, bg="orange", font=("Calibri", 10, "bold")).place(relx=0.43, rely=0.820)
    e10 = Entry(chk, borderwidth=3, relief="solid")
    e10.place(relx=0.60, rely=0.820, height=37)
    e10.get()
    Label(chk, text="CVV Code: *", width=18, height=2, bg="orange", font=("Calibri", 10, "bold")).place(relx=0.43, rely=0.870)
    e11 = Entry(chk, borderwidth=3, relief="solid")
    e11.place(relx=0.60, rely=0.870, height=37)
    e11.get()
    Label(chk, text="Expiration Date: *", width=18, height=2, bg="orange", font=("Calibri", 10, "bold")).place(relx=0.43, rely=0.920)
    e12 = Entry(chk, borderwidth=3, relief="solid")
    e12.place(relx=0.60, rely=0.920, height=37)
    e12.get()
    Button(chk, text="Checkout", width=14, height=1, bg="#383838", fg="white", command=save_data, font=("Calibri", 13, "bold")).place(relx=0.79, rely=0.920) #button which initiates save data function
    chk.mainloop() 
    
def save_data(): #save data function initiated by the button #(HARNOOR AND OKASHA)
    if e1.get()=="" or e2.get()=="" or e3.get()=="" or e4.get()=="" or e5.get()=="" or e6.get()=="" or e7.get()=="" or e8.get()=="" or e9.get()=="" or e10.get()=="" or e11.get()=="" or e12.get()=="": #writes errors if entry boxes are empty
        tkinter.messagebox.showerror("Error", "Please fill out all required fields.") #shows tkinter.messagebox error
        chk.destroy()
    else:
        fileD = open("database.txt", "a") #opens text file which gets ready to append data and eventually close
        fileD.write("First Name:\n")
        fileD.write("%s\n" % e1.get()) #writes data recieved from entry field by using get and imports it in to text file
        fileD.write("Last Name:\n")
        fileD.write("%s\n" %e2.get())
        fileD.write("Phone Number:\n")
        fileD.write("%s\n" %e3.get())
        fileD.write("Email Address:\n")
        fileD.write("%s\n" %e4.get())
        fileD.write("Address:\n")
        fileD.write("%s\n" %e5.get())
        fileD.write("City:\n")
        fileD.write("%s\n" %e6.get())
        fileD.write("Province/State:\n")
        fileD.write("%s\n" %e7.get())
        fileD.write("Country:\n")
        fileD.write("%s\n" %e8.get())
        fileD.write("Postal Code/Zip Code:\n")
        fileD.write("%s\n" %e9.get())
        fileD.write("Credit Card Number:\n")
        fileD.write("%s\n" %e10.get())
        fileD.write("CVV Code:\n")
        fileD.write("%s\n" %e11.get())
        fileD.write("Expiration Date:\n")
        fileD.write("%s\n" %e12.get())
        tkinter.messagebox.showinfo("Success", "Your order has been placed!") #if the entry boxes are not empty and everything is filled, shows success
        quadstellar.clear() #clears all items from carts
        moonrock.clear()
        snowflake.clear()
        boomer.clear()
        interstellar.clear()
        nasasuper.clear()
        heatwave.clear()
        zoomer.clear()
        addtocart.set(0) #sets main cart to 0
        chk.destroy()
    
#(HARNOOR)
    
def cartqty1():
    addtocart.set(addtocart.get() +1) #adds 1 to main cart/list (for quantity)
    quadstellar.append(quantity[0]) #appends the price of a quadstellar pc to the prices list.
    
def cartqty2():
    addtocart.set(addtocart.get() +1)
    moonrock.append(quantity[0])
    
def cartqty3():
    addtocart.set(addtocart.get() +1)
    snowflake.append(quantity[0])    
    
def cartqty4():
    addtocart.set(addtocart.get() +1)
    boomer.append(quantity[0])
    
#(OKASHA)    
    
def cartqty5():
    addtocart.set(addtocart.get() +1)
    interstellar.append(quantity[0])
    
def cartqty6():
    addtocart.set(addtocart.get() +1)
    nasasuper.append(quantity[0])
    
def cartqty7():
    addtocart.set(addtocart.get() +1)
    heatwave.append(quantity[0])
    
def cartqty8():
    addtocart.set(addtocart.get() +1)
    zoomer.append(quantity[0])
    
app.mainloop() #re loops form