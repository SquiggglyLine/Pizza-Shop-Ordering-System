

import tkinter as tk
from tkinter import font
Total = 0
root = tk.Tk()
root.title("Pizza Order")
root.attributes('-fullscreen', True)
root.configure(bg='black')
custom_font = font.Font(family="Cooper", size=15, weight="bold")
Smallerfont = font.Font(family="Cooper", size=15, weight="bold")
Labelfont = font.Font(family="Times New Roman", size=25, weight="bold")
Labelfont1 = font.Font(family="Times New Roman", size=20, weight="bold")
pizzasize = ""
toppingsW = ""
toppings1 = ""
toppings2 = ""
cook = ""
No = ""
Order = []
buttons_per_row = 6
number_of_columns = 3
items = 0
Continue = True
label123 = tk.Label(root,height = 2, width = 45, relief=tk.RAISED, bg="Dark Red", fg="White", font=Labelfont, text= pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
def change_button_color0(index):
    Whole_[index].config(bg = '#393D47', fg="white")
    WholeStromboli_[index].config(bg = '#393D47',  fg="white")
def change_button_color0P(index):
    Whole_[index].config(bg = 'Light gray', fg="Black")
    WholeStromboli_[index].config(bg = 'Light gray', fg="Black")
def change_button_color1(index):
    Half1_[index].config(bg = '#393D47',  fg="white")
def change_button_color2(index):
    Half2_[index].config(bg = '#393D47',  fg="white")
def change_button_colorS(index):
    SupremeChange_[index].config(bg = '#393D47',  fg="white")
def change_button_colorT(index):
     TacoChange_[index].config(bg = '#393D47',  fg="white")
def change_button_colorC(index):
     ChicagoChange_[index].config(bg = '#393D47',  fg="white")
def change_button_colorLS(index):
    SupremeChange1_[index].config(bg = '#393D47',  fg="white")
def change_button_colorV(index):
    VegChange_[index].config(bg = '#393D47',  fg="white")
    VegSChange_[index].config(bg = '#393D47',  fg="white")
def change_button_colorM(index):
    MeatChange_[index].config(bg = '#393D47',  fg="white")
    MeatSChange_[index].config(bg = '#393D47',  fg="white")
def change_button_colorBuff(index):
    BuffPizza_[index].config(bg = '#393D47',  fg="white")
def New():
    for button in initial_screen:
        button.pack_forget()
    for button in Where_:
        button.pack(pady = 5)

def Finish():
    for button in LgPizza_ + MdPizza_ + SmPizza_ + SicPizza_ + GluPizza_:
        button.pack_forget()
    for button in Front_:
        button.pack(pady = 5)
def Front():
    for button in LgPizza_:
        button.pack_forget()
    for button in Where_:
        button.pack_forget()
    for button in Front_:
        button.pack(pady = 5)
def Pizza():
    for button in Where_:
        button.pack_forget()
    for button in Pizza_:
        button.pack(pady = 5)
def LgPizza():
    global Total, pizzasize
    for button in Pizza_:
        button.pack_forget()
    for button in LgPizza_:
        button.pack(pady = 5)
    Total += 15.99
    pizzasize += "L"
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
def MdPizza():
    global Total, pizzasize
    for button in Pizza_:
        button.pack_forget()
    for button in MdPizza_:
        button.pack(pady = 5)
    Total += 13.99
    pizzasize +="M"
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
def SmPizza():
    global Total, pizzasize
    for button in Pizza_:
        button.pack_forget()
    for button in SmPizza_:
        button.pack(pady = 5)
    Total += 11.99
    pizzasize +="S"
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
def SicPizza():
    global Total, pizzasize
    for button in Pizza_:
        button.pack_forget()
    for button in SicPizza_:
        button.pack(pady = 5)
    Total += 19.99
    pizzasize +="Sic"
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
def GluPizza():
    global Total, pizzasize
    for button in Pizza_:
        button.pack_forget()
    for button in GluPizza_:
        button.pack(pady = 5)
    Total += 15.49
    pizzasize +="Gluten"
def GmaPizza():
    global Total, pizzasize
    for button in Pizza_:
        button.pack_forget()
    for button in FinishPizza_:
        button.pack(pady = 5)
    Total += 19.99
    pizzasize +="GMA"
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
def BallPizza():
    global Total
    for button in Pizza_:
        button.pack_forget()
    for button in Done_:
        button.pack(pady = 3)
    Total += 4.29


def SicSup():
    for button in Gourmet_:
        button.grid_forget()
    for button in SicSup_:
        button.pack(pady = 3)
    for label in SicSup_:
        label.pack()

def SicTB():
    for button in Gourmet_:
        button.grid_forget()
    for button in SicTB_:
        button.pack(pady = 3)
    for label in SicTB_:
        label.pack()

def Taco():
    for button in Gourmet_:
        button.grid_forget()
    for button in Taco_:
        button.pack(pady = 3)
    for label in Taco_:
        label.pack()

def Chicago():
    for button in Gourmet_:
        button.grid_forget()
    for button in Chicago_:
        button.pack(pady = 3)
    for label in Chicago_:
        label.pack()

def Sup():
    for button in Gourmet_:
        button.grid_forget()
    for button in Sup_:
        button.pack(pady = 3)
    for label in Sup_:
        label.pack()

def White():
    for button in Gourmet_:
        button.grid_forget()
    for button in White_:
        button.pack(pady = 3)
    for label in White_:
        label.pack()

def Hawaii():
    for button in Gourmet_:
        button.grid_forget()
    for button in Hawaii_:
        button.pack(pady = 3)
    for label in Hawaii_:
        label.pack()

def Margherita():
    for button in Gourmet_:
        button.grid_forget()
    for button in Margherita_:
        button.pack(pady = 3)
    for label in Margherita_:
        label.pack()

def RoundTB():
    for button in Gourmet_:
        button.grid_forget()
    for button in RoundTB_:
        button.pack(pady = 3)
    for label in RoundTB_:
        label.pack()

def VegPizza():
    for button in Gourmet_:
        button.grid_forget()
    for button in VegPizza_:
        button.pack(pady = 3)
    for label in VegPizza_:
        label.pack()

def MeatPizza():
    for button in Gourmet_:
        button.grid_forget()
    for button in MeatPizza_:
        button.pack(pady = 3)
    for label in MeatPizza_:
        label.pack()

def ParmPizza():
    for button in Gourmet_:
        button.grid_forget()
    for button in ParmPizza_:
        button.pack(pady = 3)
    for label in ParmPizza_:
        label.pack()

def BBQPizza():
    for button in Gourmet_:
        button.grid_forget()
    for button in BBQPizza_:
        button.pack(pady = 3)
    for label in BBQPizza_:
        label.pack()

def BuffPizza():
    for button in Gourmet_:
        button.grid_forget()
    for button in BuffPizza_:
        button.pack(pady = 3)
    for label in BuffPizza_:
        label.pack()

def CBRPizza():
    for button in Gourmet_:
        button.grid_forget()
    for button in CBRPizza_:
        button.pack(pady = 3)
    for label in CBRPizza_:
        label.pack()

def SandSPizza():
    for button in Gourmet_:
        button.grid_forget()
    for button in SandSPizza_:
        button.pack(pady = 3)
    for label in SandSPizza_:
        label.pack()

def Gourmet():
    for button in Pizza_:
        button.pack_forget()
    for button in SicSup_:
        button.pack_forget()
    for button in SicTB_:
        button.pack_forget()
    for button in Taco_:
        button.pack_forget()
    for button in Chicago_:
        button.pack_forget()
    for button in White_:
        button.pack_forget()
    for button in Hawaii_:
        button.pack_forget()
    for button in Margherita_:
        button.pack_forget()
    for button in RoundTB_:
        button.pack_forget()
    for button in VegPizza_:
        button.pack_forget()
    for button in MeatPizza_:
        button.pack_forget()
    for button in BuffPizza_:
        button.pack_forget()
    for button in BBQPizza_:
        button.pack_forget()
    for button in CBRPizza_:
        button.pack_forget()
    for button in SandSPizza_:
        button.pack_forget()
    for button in ParmPizza_:
        button.pack_forget()
    for button in Sup_:
        button.pack_forget()
    global No
    No = ""
    
    
    for button in Gourmet_:
        button.grid_forget()  # Ensure all buttons are reset before placing them

    row, col = 1, 0
    for button in Gourmet_:
        button.grid(row=row, column=col, padx=5, pady=5, sticky = 'nsew')
        col += 1
        if col >= number_of_columns:
            col = 0
            row += 1

#, SicSup_, SicTB_, Taco_, Chicago_, White_, Hawaii_, Margherita_, RoundTB_, VegPizza_, MeatPizza_,
# BuffPizza_, BBQPizza_, CBRPizza_, SandSPizza_, ParmPizza_]:

def Stromboli():
    for button in Where_:
        button.pack_forget()
    for button in Roll_:
        button.pack_forget()
    for button in TradStrom_:
        button.pack_forget()
    for button in VegStrom_:
        button.pack_forget()
    for button in MeatStrom_:
        button.pack_forget()
    for button in StkStrom_:
        button.pack_forget()
    for button in Calzone_:
        button.pack_forget()
    for button in Stromboli_:
        button.pack_forget()
    row, col = 1, 0
    for button in Stromboli_:
        button.grid(row=row, column=col, padx=5, pady=5, sticky = 'nsew')
        col += 1
        if col >= number_of_columns:
            col = 0
            row += 1



def Sandwiches():
    for button in Where_:
        button.pack_forget()
    for button in Sandwiches_:
        button.pack(pady = 3)

def Burgers():
    for button in Where_:
        button.pack_forget()
    for button in Burgers_:
        button.pack(pady = 3)


initial_screen = [
    tk.Button(root,height = 10, width = 45, relief=tk.RAISED, font=custom_font, text="Create New Order", command=New),
]


Where_ = [
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Pizza",command=Pizza),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Stromboli", command = Stromboli),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Sandwiches", command = Sandwiches),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Burgers", command = Burgers),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Dinners"),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Salad"),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Appetizers")
]

Front_ = [
    tk.Button(root, relief=tk.RAISED, font=custom_font,text="Pizza",command=Pizza),
    tk.Button(root, relief=tk.RAISED, font=custom_font,text="Stromboli", command = Stromboli)
]

Pizza_ = [
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Large Cheese..... $15.99",command=LgPizza),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Medium Cheese.... $13.99",command=MdPizza),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Small Cheese..... $11.99",command=SmPizza),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Sicilian Cheese.. $19.99",command=SicPizza),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Gluten Free...... $15.99",command=GluPizza),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Grandma Pizza...... $19.99",command=GmaPizza),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Dough Ball....... $4.29",command=BallPizza),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Gourmet",command=Gourmet)
]

def Cheesesteaks():
    for button in Sandwiches_:
        button.pack_forget()
    for button in Cheesesteaks_:
        button.pack()
    

def HotSand():
    for button in Sandwiches_:
        button.pack_forget()
    for button in HotSand_:
        button.pack()

def Burger():
    for button in Sandwiches_:
        button.pack_forget()
    for button in Burgers_:
        button.pack()

def Hoagie():
    for button in Sandwiches_:
        button.pack_forget()
    for button in Hoagies_:
        button.pack()

def Wrap():
    for button in Sandwiches_:
        button.pack_forget()
    for button in Wraps_:
        button.pack()






Sandwiches_ = [
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Cheesesteaks",command=Cheesesteaks),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Hot Sandwiches",command=HotSand),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Burgers and Chicken Sandwich",command=Burger),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Hoagies",command=Hoagie),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Wraps",command=Wrap),
]




def WholeTop():
    for button in LgPizza_:
        button.pack_forget()
    for button in MdPizza_:
        button.pack_forget()
    for button in SmPizza_:
        button.pack_forget()
    for button in SicPizza_:
        button.pack_forget()
    for button in GluPizza_:
        button.pack_forget()
    for button in FinishPizza_:
        button.pack_forget()
    
    for button in Whole_:
        button.grid_forget()  # Ensure all buttons are reset before placing them

    row, col = 1, 0
    for button in Whole_:
        button.grid(row=row, column=col, padx=5, pady=5, sticky = 'nsew')
        col += 1
        if col >= number_of_columns:
            col = 0
            row += 1


def WholeTopS():
    for button in FinishStromboli_:
        button.pack_forget()
    
    
    for button in WholeStromboli_:
        button.grid_forget()  # Ensure all buttons are reset before placing them

    row, col = 1, 0
    for button in WholeStromboli_:
        button.grid(row=row, column=col, padx=5, pady=5, sticky = 'nsew')
        col += 1
        if col >= number_of_columns:
            col = 0
            row += 1    

def HalfTop1():
    global toppings1
    for button in LgPizza_:
        button.pack_forget()
    for button in MdPizza_:
        button.pack_forget()
    for button in SmPizza_:
        button.pack_forget()
    for button in SicPizza_:
        button.pack_forget()
    for button in GluPizza_:
        button.pack_forget()
    for button in FinishPizza_:
        button.pack_forget()
    for button in Half1_:
        button.grid_forget()  # Ensure all buttons are reset before placing them
    toppings1 += "½"
    row, col = 1, 0
    for button in Half1_:
        button.grid(row=row, column=col, padx=5, pady=5, sticky = 'nsew')
        col += 1
        if col >= number_of_columns:
            col = 0
            row += 1

def HalfTop2():
    global toppings2
    for button in LgPizza_:
        button.pack_forget()
    for button in MdPizza_:
        button.pack_forget()
    for button in SmPizza_:
        button.pack_forget()
    for button in SicPizza_:
        button.pack_forget()
    for button in GluPizza_:
        button.pack_forget()
    for button in FinishPizza_:
        button.pack_forget()
    for button in Half2_:
        button.pack_forget()
    
    row, col = 1, 0
    for button in Half2_:
        button.grid(row=row, column=col, padx=5, pady=5, sticky = 'nsew')
        col += 1
        if col >= number_of_columns:
            col = 0
            row += 1
    toppings2 += "½"
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)








def Finish1():
    for button in FinishPizza_:
        button.pack_forget()
    for button in LgPizza_:
        button.pack_forget()
    for button in MdPizza_:
        button.pack_forget()
    for button in SmPizza_:
        button.pack_forget()
    for button in SicPizza_:
        button.pack_forget()
    for button in GluPizza_:
        button.pack_forget()
    for button in FinishStromboli_:
        button.pack_forget()
    label123.pack()
    for button in Done_:
        button.pack(pady = 10)


def Finish2():
    for button in FinishStromboli_:
        button.pack_forget()
    label123.pack()
    for button in Done_:
        button.pack(pady = 3)




def DifferentCook():
    for button in FinishPizza_:
        button.pack_forget()
    for button in Cooked:
        button.pack(pady = 5)

def DifferentCook1():
    for button in FinishStromboli_:
        button.pack_forget()
    for button in Cooked1:
        button.pack(pady = 5)


FinishPizza_ = [tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Finish Pizza",command=Finish1),
                tk.Button(root,height = 3, width = 40,pady = 5, relief=tk.RAISED, font=custom_font,text="      Add Whole Topping      ",command=WholeTop),
                tk.Button(root,height = 3, width = 40,pady = 5, relief=tk.RAISED, font=custom_font,text="Add Half Topping on Side 1",command=HalfTop1),
                tk.Button(root,height = 3, width = 40,pady = 5, relief=tk.RAISED, font=custom_font,text="Add Half Topping on Side 2",command=HalfTop2),
                tk.Button(root,height = 3, width = 40,pady = 5, relief=tk.RAISED, font=custom_font,text="Different Cook",command=DifferentCook),
]

FinishStromboli_ = [tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="             Finish Pizza             ",command=Finish2),
                tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="      Add Topping      ",command=WholeTopS),
                tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Different Cook",command=DifferentCook1),
]




LgPizza_ = [tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="          Plain          ",command=Finish1),
            tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Add Whole Topping........... $3.29",command=WholeTop),
            tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Add Half Topping.............. $2.29",command=HalfTop1),
]
MdPizza_ = [tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Plain",command=Finish1),
            tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Add Whole Topping............. $3.29",command=WholeTop),
            tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Add Half Topping.............. $2.29",command=HalfTop1),
            ]
SmPizza_ = [tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Plain",command=Finish1),
            tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Add Whole Topping............. $3.29",command=WholeTop),
            tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Add Half Topping.............. $2.29",command=HalfTop1),
            ]
SicPizza_ = [tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Plain",command=Finish1),
            tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Add Whole Topping............. $3.29",command=WholeTop),
            tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Add Half Topping.............. $2.29",command=HalfTop1),
            ]
GluPizza_ = [tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Plain",command=Finish1),
            tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Add Whole Topping............. $3.29",command=WholeTop),
            tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Add Half Topping.............. $2.29",command=HalfTop1),
            ]
Gourmet_ = [tk.Label(root, relief=tk.RAISED, bg="Dark Red", fg="White",font=Labelfont, text= "Gourmet Pizzas"),
            tk.Button(root, relief=tk.RAISED, font=custom_font,text="Sicilian Supreme... $28.99",command=SicSup),
            tk.Button(root, relief=tk.RAISED, font=custom_font,text="Sicilian Tomato Basil..... $24.99",command=SicTB),
            tk.Button(root, relief=tk.RAISED, font=custom_font,text="Taco.............. $24.99",command=Taco),
            tk.Button(root, relief=tk.RAISED, font=custom_font,text="Chicago Style Stuffed.... $28.99",command=Chicago),
            tk.Button(root, relief=tk.RAISED, font=custom_font,text="Supreme Pizza...... Sm/Md/Lg",command=Sup),
            tk.Button(root, relief=tk.RAISED, font=custom_font,text="White Pizza........ Sm/Md/Lg",command=White),
            tk.Button(root, relief=tk.RAISED, font=custom_font,text="Hawaiian Pizza..... Sm/Md/Lg",command=Hawaii),
            tk.Button(root, relief=tk.RAISED, font=custom_font,text="Margherita Pizza..... Sm/Md/Lg",command=Margherita),
            tk.Button(root, relief=tk.RAISED, font=custom_font,text="Tomato Basil Pizza..... Sm/Md/Lg",command=RoundTB),
            tk.Button(root, relief=tk.RAISED, font=custom_font,text="Vegetable Pizza...... Sm/Md/Lg",command=VegPizza),
            tk.Button(root, relief=tk.RAISED, font=custom_font,text="Meat Lover's Pizza.... Sm/Md/Lg",command=MeatPizza),
            tk.Button(root, relief=tk.RAISED, font=custom_font,text="Chicken Parm Pizza..... Sm/Lg", command=ParmPizza),
            tk.Button(root, relief=tk.RAISED, font=custom_font,text="BBQ Chicken Pizza...... Sm/Lg", command=BBQPizza),
            tk.Button(root, relief=tk.RAISED, font=custom_font,text="Buffalo Chicken Pizza.... Sm/Lg", command=BuffPizza),
            tk.Button(root, relief=tk.RAISED, font=custom_font,text="Chicken Bacon Ranch Pizza........ Sm/Lg", command=CBRPizza),           
            tk.Button(root, relief=tk.RAISED, font=custom_font,text="Sweet 'N' Spicy Pizza..... Sm/Lg", command=SandSPizza),
]




def Pepperoni():
    global toppingsW, Total
    toppingsW +=" P"
    Total += 3.29
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_color0(1)
def Sausage():
    global toppingsW, Total
    toppingsW +=" S"
    Total += 3.29
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_color0(2)
def  Bacon():
    global toppingsW, Total
    toppingsW +=" B"
    Total += 3.29
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_color0(3)
def  Onions():
    global toppingsW, Total
    toppingsW +=" O"
    Total += 3.29
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_color0(4)
def  Mushroom():
    global toppingsW, Total
    toppingsW +=" M"
    Total += 3.29
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_color0(5)
def  GreenPeppers():
    global toppingsW, Total
    toppingsW +=" GP"
    Total += 3.29
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_color0(6)
def  HamburgerMeat():
    global toppingsW, Total
    toppingsW +=" HB"
    Total += 3.29
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_color0(7)
def  Ham():
    global toppingsW, Total
    toppingsW +=" Ham"
    Total += 3.29
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_color0(8)
def  Meatball():
    global toppingsW, Total
    toppingsW +=" MB"
    Total += 3.29
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_color0(9)
def  XCheese():
    global toppingsW, Total
    toppingsW +=" XCh"
    Total += 3.29
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_color0(10)
def  BlackOlives():
    global toppingsW, Total
    toppingsW +=" BlO"
    Total += 3.29
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_color0(11)
def  Anchovies():
    global toppingsW, Total
    toppingsW +=" Anchovies"
    Total += 3.29
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_color0(12)
def  Broccoli():
    global toppingsW, Total
    toppingsW +=" Broc"
    Total += 3.29
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_color0(13)
def  Spinach():
    global toppingsW, Total
    toppingsW +=" Spin"
    Total += 3.29
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_color0(14)
def  Pineapple():
    global toppingsW, Total
    toppingsW +=" Pine"
    Total += 3.29
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_color0(15)
def  HotPeppers():
    global toppingsW, Total
    toppingsW +=" Hot"
    Total += 3.29
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_color0(16)
def  SweetPeppers():
    global toppingsW, Total
    toppingsW +=" Sweet"
    Total += 3.29
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_color0(17)
def  SlicedTomato():
    global toppingsW, Total
    toppingsW +=" Sliced Tomato"
    Total += 3.29
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_color0(18)
def  Garlic():
    global toppingsW, Total
    toppingsW +=" Garlic"
    Total += 3.29
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_color0(19)
def  ChickenSteak():
    global toppingsW, Total
    toppingsW +=" Chicken Steak"
    Total += 6.99
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_color0(20)
def  Steak():
    global toppingsW, Total
    toppingsW +=" Steak"
    Total += 6.99
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_color0(21)
def  GrilledChicken():
    global toppingsW, Total
    toppingsW +=" Grilled Chicken"
    Total += 6.99

    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_color0(22)

def  DoneWhole():
    for button in Whole_:
        button.grid_forget()
    for button in FinishPizza_:
        button.pack(pady = 3)
    for i, button in enumerate(Whole_):
        if i == 0 or i == len(Whole_) - 1:
            continue
        button.config(fg="black", bg="light gray")

def  DoneWhole1():
    for button in WholeStromboli_:
        button.grid_forget()
    for button in FinishStromboli_:
        button.pack(pady = 3)
    for i, button in enumerate(WholeStromboli_):
        if i == 0 or i == len(WholeStromboli_) - 1:
            continue
        button.config(fg="black", bg="light gray")


def DoneHalf1():
    for button in Half1_:
        button.grid_forget()
    for button in FinishPizza_:
        button.pack(pady = 3)
    for i, button in enumerate(Half1_):
        if i == 0 or i == len(Half1_) - 1:
            continue
        button.config(fg="black", bg="light gray")
def DoneHalf2():
    for button in Half2_:
        button.grid_forget()
    for button in FinishPizza_:
        button.pack(pady = 3)
    for i, button in enumerate(Half2_):
        if i == 0 or i == len(Half2_) - 1:
            continue
        button.config(fg="black", bg="light gray")




def Pepperoni1():
    global toppings1, Total
    toppings1 +=" P"
    Total += 2.29

    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_color1(1)
def  Sausage1():
    global toppings1, Total
    toppings1 +=" S"
    Total += 2.29
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_color1(2)
def  Bacon1():
    global toppings1, Total
    toppings1 +=" B"
    Total += 2.29
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_color1(3)
def  Onions1():
    global toppings1, Total
    toppings1 +=" O"
    Total += 2.29
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_color1(4)
def  Mushroom1():
    global toppings1, Total
    toppings1 +=" M"
    Total += 2.29
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_color1(5)
def  GreenPeppers1():
    global toppings1, Total
    toppings1 +=" GP"
    Total += 2.29
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_color1(6)
def  HamburgerMeat1():
    global toppings1, Total
    toppings1 +=" HB"
    Total += 2.29
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_color1(7)
def  Ham1():
    global toppings1, Total
    toppings1 +=" Ham"
    Total += 2.29
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_color1(8)
def  Meatball1():
    global toppings1, Total
    toppings1 +=" MB"
    Total += 2.29
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_color1(9)
def  XCheese1():
    global toppings1, Total
    toppings1 +=" XCh"
    Total += 2.29
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_color1(10)
def  BlackOlives1():
    global toppings1, Total
    toppings1 +=" BlO"
    Total += 2.29
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_color1(11)
def  Anchovies1():
    global toppings1, Total
    toppings1 +=" Anchovies"
    Total += 2.29
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_color1(12)
def  Broccoli1():
    global toppings1, Total
    toppings1 +=" Broc"
    Total += 2.29
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_color1(13)
def  Spinach1():
    global toppings1, Total
    toppings1 +=" Spin"
    Total += 2.29
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_color1(14)
def  Pineapple1():
    global toppings1, Total
    toppings1 +=" Pine"
    Total += 2.29
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_color1(15)
def  HotPeppers1():
    global toppings1, Total
    toppings1 +=" Hot"
    Total += 2.29
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_color1(16)
def  SweetPeppers1():
    global toppings1, Total
    toppings1 +=" Sweet"
    Total += 2.29
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_color1(17)
def  SlicedTomato1():
    global toppings1, Total
    toppings1 +=" Sliced Tomato"
    Total += 2.29
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_color1(18)
def  Garlic1():
    global toppings1, Total
    toppings1 +=" Garlic"
    Total += 2.29
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_color1(19)
def  ChickenSteak1():
    global toppings1, Total
    toppings1 +=" Chicken Steak"
    Total += 5.49
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_color1(20)
def  Steak1():
    global toppings1, Total
    toppings1 +=" Steak"
    Total += 5.49
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_color1(21)
def  GrilledChicken1():
    global toppings1, Total
    toppings1 +=" Grilled Chicken"
    Total += 5.49
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_color1(22)




def Pepperoni2():
    global toppings2, Total
    toppings2 +=" P"
    Total += 2.29
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_color2(1)
def  Sausage2():
    global toppings2, Total
    toppings2 +=" S"
    Total += 2.29
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_color2(2)
def  Bacon2():
    global toppings2, Total
    toppings2 +=" B"
    Total += 2.29
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_color2(3)
def  Onions2():
    global toppings2, Total
    toppings2 +=" O"
    Total += 2.29
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_color2(4)
def  Mushroom2():
    global toppings2, Total
    toppings2 +=" M"
    Total += 2.29
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_color2(5)
def  GreenPeppers2():
    global toppings2, Total
    toppings2 +=" GP"
    Total += 2.29
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_color2(6)
def  HamburgerMeat2():
    global toppings2, Total
    toppings2 +=" HB"
    Total += 2.29
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_color2(7)
def  Ham2():
    global toppings2, Total
    toppings2 +=" Ham"
    Total += 2.29
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_color2(8)
def  Meatball2():
    global toppings2, Total
    toppings2 +=" MB"
    Total += 2.29
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_color2(9)
def  XCheese2():
    global toppings2, Total
    toppings2 +=" XCh"
    Total += 2.29
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_color2(10)
def  BlackOlives2():
    global toppings2, Total
    toppings2 +=" BlO"
    Total += 2.29
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_color2(11)
def  Anchovies2():
    global toppings2, Total
    toppings2 +=" Anchovies"
    Total += 2.29
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_color2(12)
def  Broccoli2():
    global toppings2, Total
    toppings2 +=" Broc"
    Total += 2.29
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_color2(13)
def  Spinach2():
    global toppings2, Total
    toppings2 +=" Spin"
    Total += 2.29
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_color2(14)
def  Pineapple2():
    global toppings2, Total
    toppings2 +=" Pine"
    Total += 2.29
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_color2(15)
def  HotPeppers2():
    global toppings2, Total
    toppings2 +=" Hot"
    Total += 2.29
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_color2(16)
def  SweetPeppers2():
    global toppings2, Total
    toppings2 +=" Sweet"
    Total += 2.29
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_color2(17)
def  SlicedTomato2():
    global toppings2, Total
    toppings2 +=" Sliced Tomato"
    Total += 2.29
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_color2(18)
def  Garlic2():
    global toppings2, Total
    toppings2 +=" Garlic"
    Total += 2.29
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_color2(19)
def  ChickenSteak2():
    global toppings2, Total
    toppings2 +=" Chicken Steak"
    Total += 5.49
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_color2(20)
def  Steak2():
    global toppings2, Total
    toppings2 +=" Steak"
    Total += 5.49
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_color2(21)
def  GrilledChicken2():
    global toppings2, Total
    toppings2 +=" Grilled Chicken"
    Total += 5.49
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_color2(22)

def  ChickenSteak1():
    global toppings1, Total
    toppings1 +=" Chicken Steak"
    Total += 5.49
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_color1(20)
def  Steak1():
    global toppings1, Total
    toppings1 +=" Steak"
    Total += 5.49
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_color1(21)
def  GrilledChicken1():
    global toppings1, Total
    toppings1 +=" Grilled Chicken"
    Total += 5.49
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_color1(22)


def  XLight():
    global cook, Total
    cook ="X-Light Cook"
    Total += 5.49
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    for button in Cooked:
        button.pack_forget()
    for button in FinishPizza_:
        button.pack(pady = 3)
def  Light():
    global cook, Total
    cook ="Light Cook"
    Total += 5.49
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    for button in Cooked:
        button.pack_forget()
    for button in FinishPizza_:
        button.pack(pady = 3)
def  Normal():
    global cook, Total
    cook =""
    Total += 5.49
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    for button in Cooked:
        button.pack_forget()
    for button in FinishPizza_:
        button.pack(pady = 3)
def  LightWD():
    global cook, Total
    cook ="Light-W/D"
    Total += 5.49
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    for button in Cooked:
        button.pack_forget()
    for button in FinishPizza_:
        button.pack(pady = 3)
def  WD():
    global cook, Total
    cook ="W/D"
    Total += 5.49
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    for button in Cooked:
        button.pack_forget()
    for button in FinishPizza_:
        button.pack(pady = 3)
def  XWD():
    global cook, Total
    cook ="X-W/D"
    Total += 5.49
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No + No)
    for button in Cooked:
        button.pack_forget()
    for button in FinishPizza_:
        button.pack(pady = 3)








def  XLight1():
    global cook, Total
    cook +="X-Light Cook"
    Total = 5.49
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    for button in Cooked1:
        button.pack_forget()
    for button in FinishStromboli_:
        button.pack(pady = 3)
def  Light1():
    global cook, Total
    cook ="Light Cook"
    Total += 5.49
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    for button in Cooked1:
        button.pack_forget()
    for button in FinishStromboli_:
        button.pack(pady = 3)
def  Normal1():
    global cook, Total
    cook +=""
    Total += 5.49
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    for button in Cooked1:
        button.pack_forget()
    for button in FinishStromboli_:
        button.pack(pady = 3)
def  LightWD1():
    global cook, Total
    cook ="Light-W/D"
    Total += 5.49
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    for button in Cooked1:
        button.pack_forget()
    for button in FinishStromboli_:
        button.pack(pady = 3)
def  WD1():
    global cook, Total
    cook ="W/D"
    Total += 5.49
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    for button in Cooked1:
        button.pack_forget()
    for button in FinishStromboli_:
        button.pack(pady = 3)
def  XWD1():
    global cook, Total
    cook ="X-W/D"
    Total += 5.49
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No + No)
    for button in Cooked1:
        button.pack_forget()
    for button in FinishStromboli_:
        button.pack(pady = 3)










def LightCheese():
    global toppingsW
    toppingsW +=" Light Cheese"
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_color0(24)
def LightSauce():
    global toppingsW
    toppingsW +=" Light Sauce"
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_color0(23)
Whole_ = [tk.Label(root, relief=tk.RAISED, bg="Dark Red", fg="White",font=Labelfont, text= "Whole Toppings"),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Pepperoni", command=Pepperoni),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Sausage", command=Sausage),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Bacon", command=Bacon),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Onions", command=Onions),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Mushroom", command=Mushroom),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Green Peppers", command=GreenPeppers),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Hamburger Meat", command=HamburgerMeat),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Ham", command=Ham),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Meatball", command=Meatball),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Extra Cheese", command=XCheese),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Black Olives", command=BlackOlives),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Anchovies", command=Anchovies),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Broccoli", command=Broccoli),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Spinach", command=Spinach),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Pineapple", command=Pineapple),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Hot Peppers", command=HotPeppers),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Sweet Peppers", command=SweetPeppers),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Sliced Tomatos", command=SlicedTomato),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Fresh Garlic", command=Garlic),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Chicken Steak", command=ChickenSteak),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Steak", command=Steak),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Grilled Chicken", command=GrilledChicken),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Light Sauce", command=LightSauce),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Light Cheese", command=LightCheese),
   
        tk.Button(root, relief=tk.RAISED, font=custom_font,text="Done", command=DoneWhole, bg = "#2E2E2E", fg = 'White')
]

WholeStromboli_ = [tk.Label(root, relief=tk.RAISED, bg="Dark Red", fg="White",font=Labelfont, text= "Whole Toppings"),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Pepperoni", command=Pepperoni),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Sausage", command=Sausage),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Bacon", command=Bacon),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Onions", command=Onions),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Mushroom", command=Mushroom),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Green Peppers", command=GreenPeppers),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Hamburger Meat", command=HamburgerMeat),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Ham", command=Ham),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Meatball", command=Meatball),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Extra Cheese", command=XCheese),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Black Olives", command=BlackOlives),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Anchovies", command=Anchovies),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Broccoli", command=Broccoli),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Spinach", command=Spinach),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Pineapple", command=Pineapple),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Hot Peppers", command=HotPeppers),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Sweet Peppers", command=SweetPeppers),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Sliced Tomatos", command=SlicedTomato),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Fresh Garlic", command=Garlic),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Chicken Steak", command=ChickenSteak),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Steak", command=Steak),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Grilled Chicken", command=GrilledChicken),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Light Sauce", command=LightSauce),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Light Cheese", command=LightCheese),
   
        tk.Button(root, relief=tk.RAISED, font=custom_font,text="Done", command=DoneWhole1, bg = "#2E2E2E", fg = 'White')
]







def LightCheese1():
    global toppings1
    toppings1 +="  Light Cheese"
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_color1(24)
def LightSauce1():
    global toppings1
    toppings1 +="  Light Sauce"
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_color1(25)
Half1_ = [tk.Label(root, relief=tk.RAISED,  bg="Dark Red", fg="White",font=Labelfont,text="Side One"),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Pepperoni", command=Pepperoni1),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Sausage", command=Sausage1),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Bacon", command=Bacon1),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Onions", command=Onions1),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Mushroom", command=Mushroom1),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Green Peppers", command=GreenPeppers1),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Hamburger Meat", command=HamburgerMeat1),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Ham", command=Ham1),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Meatball", command=Meatball1),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Extra Cheese", command=XCheese1),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Black Olives", command=BlackOlives1),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Anchovies", command=Anchovies1),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Broccoli", command=Broccoli1),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Spinach", command=Spinach1),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Pineapple", command=Pineapple1),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Hot Peppers", command=HotPeppers1),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Sweet Peppers", command=SweetPeppers1),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Sliced Tomatos", command=SlicedTomato1),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Fresh Garlic", command=Garlic1),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Chicken Steak", command=ChickenSteak2),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Steak", command=Steak2),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Grilled Chicken", command=GrilledChicken2),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Light Sauce", command=LightSauce1),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Light Cheese", command=LightCheese1),
        tk.Button(root, relief=tk.RAISED, font=custom_font,text="Done", command=DoneHalf1, bg = "#2E2E2E", fg = 'White')
]
def LightCheese2():
    global toppings2
    toppings2 +="  Light Cheese"
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_color2(25)
def LightSauce2():
    global toppings2
    toppings2 +="  Light Cheese"
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_color2(26)
Half2_ = [tk.Label(root, relief=tk.RAISED, bg="Dark Red", fg="White", font=Labelfont,text="Side Two"),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Pepperoni", command=Pepperoni2),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Sausage", command=Sausage2),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Bacon", command=Bacon2),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Onions", command=Onions2),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Mushroom", command=Mushroom2),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Green Peppers", command=GreenPeppers2),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Hamburger Meat", command=HamburgerMeat2),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Ham", command=Ham2),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Meatball", command=Meatball2),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Extra Cheese", command=XCheese2),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Black Olives", command=BlackOlives2),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Anchovies", command=Anchovies2),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Broccoli", command=Broccoli2),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Spinach", command=Spinach2),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Pineapple", command=Pineapple2),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Hot Peppers", command=HotPeppers2),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Sweet Peppers", command=SweetPeppers2),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Sliced Tomatos", command=SlicedTomato2),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Fresh Garlic", command=Garlic2),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Chicken Steak", command=ChickenSteak2),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Steak", command=Steak2),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Grilled Chicken", command=GrilledChicken2),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Light Sauce", command=LightSauce2),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Light Cheese", command=LightCheese2),
        tk.Button(root, relief=tk.RAISED, font=Smallerfont,text="Done", command=DoneHalf2, bg = "#2E2E2E", fg = 'White')
]

Cooked = [tk.Label(root,height = 2, width = 45, relief=tk.RAISED, bg="Dark Red", fg="White", font=Labelfont,text="How would you like it cooked?"),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=Smallerfont,text="X-Light", command=XLight),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=Smallerfont,text="Light", command=Light),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=Smallerfont,text="Normal", command=Normal),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=Smallerfont,text="W/D", command=WD),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=Smallerfont,text="X-W/D", command=XWD),
        ]

Cooked1 = [tk.Label(root,height = 2, width = 45, relief=tk.RAISED, bg="Dark Red", fg="White", font=Labelfont,text="How would you like it cooked?"),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=Smallerfont,text="X-Light", command=XLight1),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=Smallerfont,text="Light", command=Light1),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=Smallerfont,text="Normal", command=Normal1),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=Smallerfont,text="W/D", command=WD1),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=Smallerfont,text="X-W/D", command=XWD1),
        ]





def OrderSicTB():
    global Total, pizzasize
    for button in SicTB_:
        button.pack_forget()
    for button in FinishPizza_:
        button.pack(pady = 3)
    Total += 24.99
    pizzasize += "Sic TB"
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
def OrderTaco():
    global Total, pizzasize
    for button in Taco_:
        button.pack_forget()
    for button in FinishPizza_:
        button.pack(pady = 3)
    Total += 24.99
    pizzasize += "Taco"
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
def OrderChicago():
    global Total, pizzasize
    for button in Chicago_:
        button.pack_forget()
    for button in FinishPizza_:
        button.pack(pady = 3)
    Total += 28.99
    pizzasize += "Chicago"
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
def OrderSicSup():
    global Total, pizzasize
    for button in SicSup_:
        button.pack_forget()
    for button in FinishPizza_:
        button.pack(pady = 3)
    Total += 28.99
    pizzasize += "Sic Sup"
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
def ChangeSicSup():
    global pizzasize, No
    for button in SicSup_:
        button.pack_forget()
    row, col = 1, 0
    for button in SupremeChange_:
        button.grid(row=row, column=col, padx=5, pady=5, sticky = 'nsew')
        col += 1
        if col >= number_of_columns:
            col = 0
            row += 1
    pizzasize += "Sic Sup"
    No += "  No"
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
def ChangeChicago():
    for button in Chicago_:
         button.pack_forget()
    row, col = 1, 0
    for button in ChicagoChange_:
        button.grid(row=row, column=col, padx=5, pady=5, sticky = 'nsew')
        col += 1
    if col >= number_of_columns:
        col = 0
        row += 1
    global No, pizzasize
    pizzasize += "Chicago"
    No += " No"

def NoSaus():
    global No
    No += " S"
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_colorS(0)
def NoMB():
    global No
    No += " MB"
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_colorS(1)
def NoPep():
    global No
    No += " P"
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_colorS(2)
def NoO():
    global No
    No += " O"
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_colorS(3)
def NoM():
    global No
    No += " M"
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_colorS(4)
def NoGP():
    global No
    No += " GP"
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_colorS(5)
def NoB():
    global No
    No += " B"
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_colorS(6)

def NoSaus1():
    global No
    No += " S"
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_colorLS(0)
def NoMB1():
    global No
    No += " MB"
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_colorLS(1)
def NoPep1():
    global No
    No += " P"
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_colorLS(2)
def NoO1():
    global No
    No += " O"
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_colorLS(3)
def NoM1():
    global No
    No += " M"
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_colorLS(4)
def NoGP1():
    global No
    No += " GP"
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_colorLS(5)
def NoB1():
    global No
    No += " B"
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_colorLS(6)
def Done():
    for button in SupremeChange_:
        button.grid_forget()
    for button in TacoChange_:
        button.grid_forget()
    for button in ChicagoChange_:
        button.grid_forget()
    for button in VegChange_:
        button.grid_forget()
    for button in MeatChange_:
        button.grid_forget()
    for button in SupremeChange1_:
        button.grid_forget()
    for button in FinishPizza_:
        button.pack(pady = 3)
    for i, button in enumerate(SupremeChange_):
        if i == len(SupremeChange_) - 1:
            continue
        button.config(fg="black", bg="light gray")
    for i, button in enumerate(TacoChange_):
        if i == len(TacoChange_) - 1:
            continue
        button.config(fg="black", bg="light gray")
    for i, button in enumerate(ChicagoChange_):
        if i == len(ChicagoChange_) - 1:
            continue
        button.config(fg="black", bg="light gray")
    for i, button in enumerate(VegChange_):
        if i == len(VegChange_) - 1:
            continue
        button.config(fg="black", bg="light gray")
    for i, button in enumerate(MeatChange_):
        if i == len(MeatChange_) - 1:
            continue
        button.config(fg="black", bg="light gray")
    for i, button in enumerate(SupremeChange1_):
        if i == len(SupremeChange1_) - 1:
            continue
        button.config(fg="black", bg="light gray")



def Done1():
    for button in SupremeChange1_:
        button.grid_forget()
    for button in Sup_:
        button.pack(pady = 3)
    for i, button in enumerate(SupremeChange1_):
        if i == len(SupremeChange1_) - 1:
            continue
        button.config(fg="white", bg="#2E2E2E")
def Done2V():
    for button in VegSChange_:
        button.grid_forget()
    for button in VegStromS_:
        button.pack(pady = 3)
    for i, button in enumerate(VegSChange_):
        if i == len(VegSChange_) - 1:
            continue
        button.config(fg="white", bg="#2E2E2E")
def Done2M():
    for button in MeatSChange_:
        button.grid_forget()
    for button in MeatStromS_:
        button.pack(pady = 3)
    for i, button in enumerate(MeatSChange_):
        if i == len(MeatSChange_) - 1:
            continue
        button.config(fg="white", bg="#2E2E2E")



def TNoBeef():
    global No
    No += " P"
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_colorT(0)
def TNoLett():
    global No
    No += " Lettuce"
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_colorT(1)
def TNoTom():
    global No
    No += " Tomato"
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_colorT(2)
def TNoO():
    global No
    No += " O"
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_colorT(3)
def TNoChed():
    global No
    No += " Cheddar Cheese"
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_colorT(4)
def TNoTaco():
    global No
    No += " Taco Sauce"
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_colorT(5)
def ChangeTaco():
    global No
    for button in Taco_:
        button.pack_forget()
    row, col = 1, 0
    for button in TacoChange_:
        button.grid(row=row, column=col, padx=5, pady=5, sticky = 'nsew')
        col += 1
        if col >= number_of_columns:
            col = 0
            row += 1
    No += " No"
def CNoHam():
    global No
    No += " Ham"
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_colorC(0)
def CNoMB():
    global No
    No += " MB"
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_colorC(1)
def CNoPep():
    global No
    No += " P"
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_colorC(2)

def VNoBroc():
    global No
    No += " Broc"
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_colorV(0)
def VNoSpin():
    global No
    No += " Spin"
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_colorV(1)
def VNoM():
    global No
    No += " M"
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_colorV(2)
def VNoO():
    global No
    No += " O"
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_colorV(3)
def VNoGP():
    global No
    No += " GP"
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_colorT(4)

def MNoS():
    global No
    No += " S"
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_colorM(0)
def MNoP():
    global No
    No += " P"
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_colorM(1)
def MNoB():
    global No
    No += " B"
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_colorM(2)
def MNoHam():
    global No
    No += " Ham"
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_colorM(3)
def MNoMB():
    global No
    No += " MB"
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    change_button_colorM(4)




# Gourmet Pizzas that can change--> Supreme, Taco, Chicago, Veg, Meat Lov, Buff

SupremeChange_ = [tk.Button(root, relief=tk.RAISED, font=custom_font, text="No Sausage",command=NoSaus),
        tk.Button(root, relief=tk.RAISED, font=custom_font, text="No Meatballs",command=NoMB),
        tk.Button(root, relief=tk.RAISED, font=custom_font, text="No Pepperoni",command=NoPep),
        tk.Button(root, relief=tk.RAISED, font=custom_font, text="No Onions",command=NoO),
        tk.Button(root, relief=tk.RAISED, font=custom_font, text="No Musrooms",command=NoM),
        tk.Button(root, relief=tk.RAISED, font=custom_font, text="No Green Peppers",command=NoGP),
        tk.Button(root, relief=tk.RAISED, font=custom_font, text="No Bacon",command=NoB),
        tk.Button(root, relief=tk.RAISED, font=custom_font,text ="Done", command=Done, bg = "#2E2E2E")
]
SupremeChange1_ = [tk.Button(root, relief=tk.RAISED, font=custom_font, text="No Sausage",command=NoSaus1),
        tk.Button(root, relief=tk.RAISED, font=custom_font, text="No Meatballs",command=NoMB1),
        tk.Button(root, relief=tk.RAISED, font=custom_font, text="No Pepperoni",command=NoPep1),
        tk.Button(root, relief=tk.RAISED, font=custom_font, text="No Onions",command=NoO1),
        tk.Button(root, relief=tk.RAISED, font=custom_font, text="No Musrooms",command=NoM1),
        tk.Button(root, relief=tk.RAISED, font=custom_font, text="No Green Peppers",command=NoGP1),
        tk.Button(root, relief=tk.RAISED, font=custom_font, text="No Bacon",command=NoB1),
        tk.Button(root, relief=tk.RAISED, font=custom_font,text ="Done", command=Done1, bg = "#2E2E2E")
]
TacoChange_ = [tk.Button(root, relief=tk.RAISED, font=custom_font, text="No Beef",command=TNoBeef),
        tk.Button(root, relief=tk.RAISED, font=custom_font, text="No Lettuce",command=TNoLett),
        tk.Button(root, relief=tk.RAISED, font=custom_font, text="No Tomato",command=TNoTom),
        tk.Button(root, relief=tk.RAISED, font=custom_font, text="No Onions",command=TNoO),
        tk.Button(root, relief=tk.RAISED, font=custom_font, text="No Cheddar Cheese",command=TNoChed),
        tk.Button(root, relief=tk.RAISED, font=custom_font, text="No Taco Sauce",command=TNoTaco),
        tk.Button(root, relief=tk.RAISED, font=custom_font,text ="Done", command=Done, bg = "#2E2E2E")
]

VegChange_ = [tk.Button(root, relief=tk.RAISED, font=custom_font, text="No Broccoli",command=VNoBroc),
        tk.Button(root, relief=tk.RAISED, font=custom_font, text="No Spinach",command=VNoSpin),
        tk.Button(root, relief=tk.RAISED, font=custom_font, text="No Mushrooms",command=VNoM),
        tk.Button(root, relief=tk.RAISED, font=custom_font, text="No Onions",command=VNoO),
        tk.Button(root, relief=tk.RAISED, font=custom_font, text="No Green Peppers",command=VNoGP),
        tk.Button(root, relief=tk.RAISED, font=custom_font,text ="Done", command=Done, bg = "#2E2E2E")
]

ChicagoChange_ = [tk.Button(root, relief=tk.RAISED, font=custom_font, text="No Ham",command=CNoHam),
        tk.Button(root, relief=tk.RAISED, font=custom_font, text="No Meatballs",command=CNoMB),
        tk.Button(root, relief=tk.RAISED, font=custom_font, text="No Pepperoni",command=CNoPep),
        tk.Button(root, relief=tk.RAISED, font=custom_font,text ="Done", command=Done, bg = "#2E2E2E")
]

MeatChange_ = [tk.Button(root, relief=tk.RAISED, font=custom_font, text="No Sausage",command=MNoS),
        tk.Button(root, relief=tk.RAISED, font=custom_font, text="No Pepperoni",command=MNoP),
        tk.Button(root, relief=tk.RAISED, font=custom_font, text="No Bacon",command=MNoB),
        tk.Button(root, relief=tk.RAISED, font=custom_font, text="No Ham",command=MNoHam),
        tk.Button(root, relief=tk.RAISED, font=custom_font, text="No Meatballs",command=MNoMB),
        tk.Button(root, relief=tk.RAISED, font=custom_font,text ="Done", command=Done, bg = "#2E2E2E")
]

SicSup_ = [tk.Label(root,height = 2, width = 45, relief=tk.RAISED,  bg="Dark Red", fg="White",font=Labelfont1, text="Mozzarella, Sauce, Sausage, Meatballs, Pepperoni, Onions, Mushrooms, Green Peppers, & Bacon"),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Order As Is or Add topping",command=OrderSicSup),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Remove topping",command=ChangeSicSup)
]

SicTB_ = [tk.Label(root,height = 2, width = 45, relief=tk.RAISED,  bg="Dark Red", fg="White", font=Labelfont, text="Fresh seasoned tomato, basil, & mozzarella"),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Order",command=OrderSicTB)
]

Taco_ = [tk.Label(root,height = 2, width = 45, relief=tk.RAISED, font=Labelfont,  bg="Dark Red", fg="White", text="Ground beef, lettuce, tomato, onions, cheddar cheese, & taco sauce"),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Order As Is or Add Topping",command=OrderTaco),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Remove topping",command=ChangeTaco)
]

Chicago_ = [tk.Label(root,height = 2, width = 45, relief=tk.RAISED, font=Labelfont,  bg="Dark Red", fg="White", text="Ham, Pepperoni, Sauseage, Mozzarella, & Sauce"),
         tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Order As Is",command=OrderChicago),
            tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Add or Remove topping",command=ChangeChicago)
]
def SmSup():
    global pizzasize, Total
    pizzasize +="S Supreme"
    Total += 18.99
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No + No)
    for button in Sup_:
        button.pack_forget()
    for button in FinishPizza_:
        button.pack(pady = 3)
def MdSup():
    global pizzasize, Total
    pizzasize +="M Supreme"
    Total += 23.99
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No + No)
    for button in Sup_:
        button.pack_forget()
    for button in FinishPizza_:
        button.pack(pady = 3)
def LgSup():
    global pizzasize, Total
    pizzasize +="L Supreme"
    Total += 25.99
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No + No)
    for button in Sup_:
        button.pack_forget()
    for button in FinishPizza_:
        button.pack(pady = 3)

def ModSup():
    global No  
    for button in Sup_:
        button.pack_forget()
    row, col = 1, 0
    for button in SupremeChange1_:
        button.grid(row=row, column=col, padx=5, pady=5, sticky = 'nsew')
        col += 1
        if col >= number_of_columns:
            col = 0
            row += 1
    No += " No"
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
def ModVeg():
    global No  
    for button in VegPizza_:
        button.pack_forget()
    row, col = 1, 0
    for button in VegChange_:
        button.grid(row=row, column=col, padx=5, pady=5, sticky = 'nsew')
        col += 1
        if col >= number_of_columns:
            col = 0
            row += 1
    No += " No"
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
def ModMeat():
    global No
    for button in MeatPizza_:
        button.pack_forget()
    row, col = 1, 0
    for button in MeatChange_:
        button.grid(row=row, column=col, padx=5, pady=5, sticky = 'nsew')
        col += 1
        if col >= number_of_columns:
            col = 0
            row += 1
    No += " No"
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
def SmWhite():
    global pizzasize, Total
    for button in White_:
        button.pack_forget()
    for button in FinishPizza_:
        button.pack(pady = 3)
    pizzasize += "S White"
    Total += 15.99
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
def MdWhite():
    global pizzasize, Total
    for button in White_:
        button.pack_forget()
    for button in FinishPizza_:
        button.pack(pady = 3)
    pizzasize += "M White"
    Total += 17.99
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
def LgWhite():
    global pizzasize, Total
    for button in White_:
        button.pack_forget()
    for button in FinishPizza_:
        button.pack(pady = 3)
    pizzasize += "L White"
    Total += 18.99
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
def SmHawaii():
    global pizzasize, Total
    for button in Hawaii_:
        button.pack_forget()
    for button in FinishPizza_:
        button.pack(pady = 3)
    pizzasize += "S Hawaii"
    Total += 15.99
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
def MdHawaii():
    global pizzasize, Total
    for button in Hawaii_:
        button.pack_forget()
    for button in FinishPizza_:
        button.pack(pady = 3)
    pizzasize += "M Hawaii"
    Total += 17.99
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
def LgHawaii():
    global pizzasize, Total
    for button in Hawaii_:
        button.pack_forget()
    for button in FinishPizza_:
        button.pack(pady = 3)
    pizzasize += "L Hawaii"
    Total += 19.99
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
def SmMargherita():
    global pizzasize, Total
    for button in Margherita_:
        button.pack_forget()
    for button in FinishPizza_:
        button.pack(pady = 3)
    pizzasize += "S Margherita"
    Total += 15.99
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
def MdMargherita():
    global pizzasize, Total
    for button in Margherita_:
        button.pack_forget()
    for button in FinishPizza_:
        button.pack(pady = 3)
    pizzasize += "M Margherita"
    Total += 17.99
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
def LgMargherita():
    global pizzasize, Total
    for button in Margherita_:
        button.pack_forget()
    for button in FinishPizza_:
        button.pack(pady = 3)
    pizzasize += "L Margherita"
    Total += 19.99
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
def SmRoundTB():
    global pizzasize, Total
    for button in RoundTB_:
        button.pack_forget()
    for button in FinishPizza_:
        button.pack(pady = 3)
    pizzasize += "S RoundTB"
    Total += 15.99
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
def MdRoundTB():
    global pizzasize, Total
    for button in RoundTB_:
        button.pack_forget()
    for button in FinishPizza_:
        button.pack(pady = 3)
    pizzasize += "M RoundTB"
    Total += 17.99
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
def LgRoundTB():
    global pizzasize, Total
    for button in RoundTB_:
        button.pack_forget()
    for button in FinishPizza_:
        button.pack(pady = 3)
    pizzasize += "L RoundTB"
    Total += 19.99
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
def SmVegPizza():
    global pizzasize, Total
    for button in VegPizza_:
        button.pack_forget()
    for button in FinishPizza_:
        button.pack(pady = 3)
    pizzasize += "S Veg"
    Total += 18.99
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
def MdVegPizza():
    global pizzasize, Total
    for button in VegPizza_:
        button.pack_forget()
    for button in FinishPizza_:
        button.pack(pady = 3)
    pizzasize += "M Veg"
    Total += 23.99
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
def LgVegPizza():
    global pizzasize, Total
    for button in VegPizza_:
        button.pack_forget()
    for button in FinishPizza_:
        button.pack(pady = 3)
    pizzasize += "L Veg"
    Total += 25.99
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
def SmMeatPizza():
    global pizzasize, Total
    for button in MeatPizza_:
        button.pack_forget()
    for button in FinishPizza_:
        button.pack(pady = 3)
    pizzasize += "S Meat"
    Total += 18.99
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
def MdMeatPizza():
    global pizzasize, Total
    for button in MeatPizza_:
        button.pack_forget()
    for button in FinishPizza_:
        button.pack(pady = 3)
    pizzasize += "M Meat"
    Total += 23.99
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
def LgMeatPizza():
    global pizzasize, Total
    for button in MeatPizza_:
        button.pack_forget()
    for button in FinishPizza_:
        button.pack(pady = 3)
    pizzasize += "L Meat"
    Total += 25.99
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)



Sup_ = [tk.Label(root,height = 2, width = 45, relief=tk.RAISED, font=Labelfont1,  bg="Dark Red", fg="White", text= "Sauce, Mozzarella, Sausage, Meatballs, Pepperoni, Onions, Mushrooms, Green Peppers, & Bacon"),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Small....$18.99",command=SmSup),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Medium...$23.99",command=MdSup),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Large....$25.99",command=LgSup),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Remove Toppings", command=ModSup),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Go back",command=Gourmet)
]

White_ = [tk.Label(root,height = 2, width = 45, relief=tk.RAISED, font=Labelfont,   bg="Dark Red", fg="White",text= "Ricotta & Mozzarella Cheese (no sauce)"),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Small....$15.99",command=SmWhite),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Medium...$17.99",command=MdWhite),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Large....$18.99",command=LgWhite),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Go back",command=Gourmet)
]

Hawaii_ = [tk.Label(root,height = 2, width = 45, relief=tk.RAISED, font=Labelfont,  bg="Dark Red", fg="White", text= "Mozzarella, Sauce, Ham, Pinapple"),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Small....$15.99",command=SmHawaii),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Medium...$18.99",command=MdHawaii),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Large....$19.99",command=LgHawaii),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Go back",command=Gourmet)
]

Margherita_ = [tk.Label(root,height = 2, width = 45, relief=tk.RAISED, font=Labelfont,   bg="Dark Red", fg="White",text= "Mozzarella, plum tomato sauce, parmesan, garlic, olive oil, & oregano"),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Small....$15.99",command=SmMargherita),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Medium...$18.99",command=MdMargherita),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Large....$19.99",command=LgMargherita),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Go back",command=Gourmet)
]

RoundTB_ = [tk.Label(root,height = 2, width = 45, relief=tk.RAISED, font=Labelfont,   bg="Dark Red", fg="White",text= "Fresh seasoned tomato, basil, & Mozzarella"),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Small....$15.99",command=SmRoundTB),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Medium...$18.99",command=MdRoundTB),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Large....$19.99",command=LgRoundTB),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Go back",command=Gourmet)
]

VegPizza_ = [tk.Label(root,height = 2, width = 45, relief=tk.RAISED, font=Labelfont,   bg="Dark Red", fg="White",text= "Broccoli, Spinach, Mushrooms, Onions, Green Peppers, Sauce, Mozzarella"),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Small....$18.99",command=SmVegPizza),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Medium...$23.99",command=MdVegPizza),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Large....$25.99",command=LgVegPizza),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Remove Toppings", command=ModVeg),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Go back",command=Gourmet)
]

MeatPizza_ = [tk.Label(root,height = 2, width = 45, relief=tk.RAISED, font=Labelfont,   bg="Dark Red", fg="White",text= "Sausage, Pepperoni, Bacon, Ham, Meatballs, Sauce, Mozzarella"),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Small....$18.99",command=SmMeatPizza),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Medium...$23.99",command=MdMeatPizza),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Large....$25.99",command=LgMeatPizza),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Remove Toppings", command=ModMeat),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Go back",command=Gourmet)
]

def SmParmPizza():
    global pizzasize, Total
    for button in ParmPizza_:
        button.pack_forget()
    for button in FinishPizza_:
        button.pack(pady = 3)
    pizzasize += "S Chick Parm"
    Total += 16.99
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
def LgParmPizza():
    global pizzasize, Total
    for button in ParmPizza_:
        button.pack_forget()
    for button in FinishPizza_:
        button.pack(pady = 3)
    pizzasize += "L Chick Parm"
    Total += 25.99
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
def SmBBQPizza():
    global pizzasize, Total
    for button in BBQPizza_:
        button.pack_forget()
    for button in FinishPizza_:
        button.pack(pady = 3)
    pizzasize += "S BBQ"
    Total += 16.99
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
def LgBBQPizza():
    global pizzasize, Total
    for button in BBQPizza_:
        button.pack_forget()
    for button in FinishPizza_:
        button.pack(pady = 3)
    pizzasize += "L BBQ"
    Total += 25.99
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
def SmBuffPizza():
    global pizzasize, Total
    for button in BuffPizza_:
        button.pack_forget()
    for button in FinishPizza_:
        button.pack(pady = 3)
    pizzasize += "S Buff"
    Total += 16.99
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
def LgBuffPizza():
    global pizzasize, Total
    for button in BuffPizza_:
        button.pack_forget()
    for button in FinishPizza_:
        button.pack(pady = 3)
    pizzasize += "L Buff"
    Total += 25.99
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)

def NoBlu():
    global No
    No += "No BluCh "
    change_button_colorBuff(3)
def Ranch():
    global toppingsW
    toppingsW += ",Ranch"
    change_button_colorBuff(4)

def SmCBRPizza():
    global pizzasize, Total
    for button in CBRPizza_:
        button.pack_forget()
    for button in FinishPizza_:
        button.pack(pady = 3)
    pizzasize += "S CBR"
    Total += 16.99
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
def LgCBRPizza():
    global pizzasize, Total
    for button in BuffPizza_:
        button.pack_forget()
    for button in FinishPizza_:
        button.pack(pady = 3)
    pizzasize += "L CBR"
    Total += 25.99
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)

def SmSandSPizza():
    global pizzasize, Total
    for button in SandSPizza_:
        button.pack_forget()
    for button in FinishPizza_:
        button.pack(pady = 3)
    pizzasize += "S S/S"
    Total += 16.99
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
def LgSandSPizza():
    global pizzasize, Total
    for button in SandSPizza_:
        button.pack_forget()
    for button in FinishPizza_:
        button.pack(pady = 3)
    pizzasize += "L S/S"
    Total += 25.99
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)


ParmPizza_ = [tk.Label(root,height = 2, width = 45, relief=tk.RAISED,  bg="Dark Red", fg="White", font=Labelfont, text= "Chicken Parm, Sauce, Mozzarella"),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Small....$16.99",command=SmParmPizza),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Large....$25.99",command=LgParmPizza),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Go back",command=Gourmet)
]

BBQPizza_ = [tk.Label(root,height = 2, width = 45, relief=tk.RAISED, font=Labelfont,  bg="Dark Red", fg="White", text= "Breaded chicken, BBQ sauce, bacon, cheddar cheese, Mozzarella"),
             tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Small....$16.99",command=SmBBQPizza),
            tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Large....$25.99",command=LgBBQPizza),
            tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Go back",command=Gourmet)
]
def Goback():
    global No, toppingsW
    No = ""
    toppingsW = ""
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
    for button in BuffPizza_:
        button.pack_forget()
    for button in Gourmet_:
        button.grid_forget()
    row, col = 1, 0
    for button in Gourmet_:
        button.grid(row=row, column=col, padx=5, pady=5, sticky = 'nsew')
        col += 1
        if col >= number_of_columns:
            col = 0
            row += 1
BuffPizza_ = [tk.Label(root,height = 2, width = 45, relief=tk.RAISED, font=Labelfont,  bg="Dark Red", fg="White", text= "Breaded chicken, Hot sauce, Blue Cheese, cheddar cheese, Mozzarella"),
             tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Small....$16.99",command=SmBuffPizza),
            tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Large....$25.99",command=LgBuffPizza),
            tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="No Blu Cheese",command= NoBlu),
            tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="With Ranch",command=Ranch),
            tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Go back",command=Goback)
]

CBRPizza_ = [tk.Label(root,height = 2, width = 45, relief=tk.RAISED, font=Labelfont,  bg="Dark Red", fg="White", text= "Breaded chicken, BBQ sauce, bacon, cheddar cheese, Mozzarella"),
             tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Small....$16.99",command=SmCBRPizza),
            tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Large....$25.99",command=LgCBRPizza),
            tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Go back",command=Gourmet)
]

SandSPizza_ = [tk.Label(root,height = 2, width = 45, relief=tk.RAISED, font=Labelfont,  bg="Dark Red", fg="White", text= "Breaded chicken, BBQ sauce, bacon, cheddar cheese, Mozzarella"),
             tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Small....$16.99",command=SmSandSPizza),
             tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Large....$25.99",command=LgSandSPizza),
             tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Go back",command=Gourmet)
]















for col in range(number_of_columns):
        root.grid_columnconfigure(col, weight=1)
for row in range(len(Whole_) // number_of_columns + 2):  # +2 for the label row and potential extra row
    root.grid_rowconfigure(row, weight=1)
label123 = tk.Label(root,height = 2, width = 45, relief=tk.RAISED, bg="Dark Red", fg="White", font=Labelfont, text= pizzasize + toppingsW + toppings1 + toppings2 + cook + No)


def Roll():
    for button in Stromboli_:
        button.grid_forget()
    for button in Roll_:
        button.pack(pady = 3)
    for label in Roll_:
        label.pack()

def TradStrom():
    for button in Stromboli_:
        button.grid_forget()
    for button in TradStrom_:
        button.pack(pady = 3)
    for label in TradStrom_:
        label.pack()

def VegStrom():
    for button in Stromboli_:
        button.grid_forget()
    for button in VegStrom_:
        button.pack(pady = 3)
    for label in VegStrom_:
        label.pack()

def Calzone():
    for button in Stromboli_:
        button.grid_forget()
    for button in Calzone_:
        button.pack(pady = 3)
    for label in Calzone_:
        label.pack()

def StkStrom():
    for button in Stromboli_:
        button.grid_forget()
    for button in StkStrom_:
        button.pack(pady = 3)
    for label in StkStrom_:
        label.pack()

def MeatStrom():
    for button in Stromboli_:
        button.grid_forget()
    for button in MeatStrom_:
        button.pack(pady = 3)
    for label in MeatStrom_:
        label.pack()


def MdRoll():
    global pizzasize, Total
    for button in Roll_:
        button.pack_forget()
    for button in FinishStromboli_:
        button.pack(pady = 3)
    pizzasize += "M Stromboli Roll"
    Total += 18.99
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
def LgRoll():
    global pizzasize, Total
    for button in Roll_:
        button.pack_forget()
    for button in FinishStromboli_:
        button.pack(pady = 3)
    pizzasize += "L Stromboli Roll"
    Total += 19.99
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)

def SmTradStrom():
    global pizzasize, Total
    for button in TradStrom_:
        button.pack_forget()
    for button in FinishStromboli_:
        button.pack(pady = 3)
    pizzasize += "S Stromboli"
    Total += 18.99
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
def MdTradStrom():
    global pizzasize, Total
    for button in TradStrom_:
        button.pack_forget()
    for button in FinishStromboli_:
        button.pack(pady = 3)
    pizzasize += "M Stromboli"
    Total += 23.99
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
def LgTradStrom():
    global pizzasize, Total
    for button in TradStrom_:
        button.pack_forget()
    for button in FinishStromboli_:
        button.pack(pady = 3)
    pizzasize += "L Stromboli"
    Total += 25.99
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)

def SmVegStrom():
    global pizzasize, Total
    for button in VegStrom_:
        button.pack_forget()
    for button in VegStromS_:
        button.pack_forget()
    for button in FinishStromboli_:
        button.pack(pady = 3)
    pizzasize += "S Veg Strom"
    Total += 12.99
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
def MdVegStrom():
    global pizzasize, Total
    for button in VegStrom_:
        button.pack_forget()
    for button in VegStromS_:
        button.pack_forget()
    for button in FinishStromboli_:
        button.pack(pady = 3)
    pizzasize += "M Veg Strom"
    Total += 21.99
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
def LgVegStrom():
    global pizzasize, Total
    for button in VegStrom_:
        button.pack_forget()
    for button in VegStromS_:
        button.pack_forget()
    for button in FinishStromboli_:
        button.pack(pady = 3)
    pizzasize += "L Veg Strom"
    Total += 23.99
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)

def SmMeatStrom():
    global pizzasize, Total
    for button in MeatStrom_:
        button.pack_forget()
    for button in MeatStromS_:
        button.pack_forget()
    for button in FinishStromboli_:
        button.pack(pady = 3)
    pizzasize += "S Meat Strom"
    Total += 12.99
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
def MdMeatStrom():
    global pizzasize, Total
    for button in VegStrom_:
        button.pack_forget()
    for button in MeatStromS_:
        button.pack_forget()
    for button in FinishStromboli_:
        button.pack(pady = 3)
    pizzasize += "M Meat Strom"
    Total += 21.99
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
def LgMeatStrom():
    global pizzasize, Total
    for button in MeatStrom_:
        button.pack_forget()
    for button in MeatStromS_:
        button.pack_forget()
    for button in FinishStromboli_:
        button.pack(pady = 3)
    pizzasize += "L Meat Strom"
    Total += 23.99
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)

def SmStkStrom():
    global pizzasize, Total
    for button in StkStrom_:
        button.pack_forget()
    for button in FinishStromboli_:
        button.pack(pady = 3)
    pizzasize += "S Steak Strom"
    Total += 12.99
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
def MdStkStrom():
    global pizzasize, Total
    for button in StkStrom_:
        button.pack_forget()
    for button in FinishStromboli_:
        button.pack(pady = 3)
    pizzasize += "M Steak Strom"
    Total += 21.99
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
def LgStkStrom():
    global pizzasize, Total
    for button in StkStrom_:
        button.pack_forget()
    for button in FinishStromboli_:
        button.pack(pady = 3)
    pizzasize += "L Steak Strom"
    Total += 23.99
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)

def SmCalzone():
    global pizzasize, Total
    for button in StkStrom_:
        button.pack_forget()
    for button in FinishStromboli_:
        button.pack(pady = 3)
    pizzasize += "S Steak Strom"
    Total += 12.99
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
def MdCalzone():
    global pizzasize, Total
    for button in Calzone_:
        button.pack_forget()
    for button in FinishStromboli_:
        button.pack(pady = 3)
    pizzasize += "M Steak Strom"
    Total += 21.99
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)
def LgCalzone():
    global pizzasize, Total
    for button in Calzone_:
        button.pack_forget()
    for button in FinishStromboli_:
        button.pack(pady = 3)
    pizzasize += "L Steak Strom"
    Total += 23.99
    label123.config(text =  pizzasize + toppingsW + toppings1 + toppings2 + cook + No)


def ModMeat1():
    for button in MeatStrom_:
        button.pack_forget()
    row, col = 1, 0
    for button in MeatSChange_:
        button.grid(row=row, column=col, padx=5, pady=5, sticky = 'nsew')
        col += 1
        if col >= number_of_columns:
            col = 0
            row += 1
    global No
    No += " No"

MeatSChange_ = [tk.Button(root, relief=tk.RAISED, font=custom_font, text="No Sausage",command=MNoS),
        tk.Button(root, relief=tk.RAISED, font=custom_font, text="No Pepperoni",command=MNoP),
        tk.Button(root, relief=tk.RAISED, font=custom_font, text="No Bacon",command=MNoB),
        tk.Button(root, relief=tk.RAISED, font=custom_font, text="No Ham",command=MNoHam),
        tk.Button(root, relief=tk.RAISED, font=custom_font, text="No Meatballs",command=MNoMB),
        tk.Button(root, relief=tk.RAISED, font=custom_font,text ="Done", command=Done2M, bg = "#2E2E2E")
]
def ModVeg1():
    for button in VegStrom_:
        button.pack_forget()
    row, col = 1, 0
    for button in VegSChange_:
        button.grid(row=row, column=col, padx=5, pady=5, sticky = 'nsew')
        col += 1
        if col >= number_of_columns:
            col = 0
            row += 1
    global No
    No += " No"
VegSChange_ = [tk.Button(root, relief=tk.RAISED, font=custom_font, text="No Broccoli",command=VNoBroc),
        tk.Button(root, relief=tk.RAISED, font=custom_font, text="No Spinach",command=VNoSpin),
        tk.Button(root, relief=tk.RAISED, font=custom_font, text="No Mushrooms",command=VNoM),
        tk.Button(root, relief=tk.RAISED, font=custom_font, text="No Onions",command=VNoO),
        tk.Button(root, relief=tk.RAISED, font=custom_font, text="No Green Peppers",command=VNoGP),
        tk.Button(root, relief=tk.RAISED, font=custom_font,text ="Done", command=Done2V, bg = "#2E2E2E")
]






Roll_ = [tk.Label(root,height = 2, width = 45, relief=tk.RAISED, font=Labelfont,   bg="Dark Red", fg="White",text= "Ham, Salami, Cheese, Green Peppers, & Sauce"),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Medium...$18.99",command=MdRoll),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Large....$19.99",command=LgRoll),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Go back",command=Stromboli)
]
TradStrom_ = [tk.Label(root,height = 2, width = 45, relief=tk.RAISED, font=Labelfont,   bg="Dark Red", fg="White",text= "Ham, Salami, Cheese, Green Peppers, & Sauce"),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Small....$12.99",command=SmTradStrom),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Medium...$21.99",command=MdTradStrom),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Large....$23.99",command=LgTradStrom),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Go back",command=Stromboli)
]

VegStrom_ = [tk.Label(root,height = 2, width = 45, relief=tk.RAISED, font=Labelfont,   bg="Dark Red", fg="White",text= "Broccoli, spinach, mushrooms, onions, green peppers, sauce, & cheese"),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Small....$12.99",command=SmVegStrom),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Medium...$21.99",command=MdVegStrom),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Large....$23.99",command=LgVegStrom),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Remove Toppings",command=ModVeg1),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Go back",command=Stromboli)
]

VegStromS_ = [tk.Label(root,height = 2, width = 45, relief=tk.RAISED, font=Labelfont,   bg="Dark Red", fg="White",text= "Broccoli, spinach, mushrooms, onions, green peppers, sauce, & cheese"),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Small....$12.99",command=SmVegStrom),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Medium...$21.99",command=MdVegStrom),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Large....$23.99",command=LgVegStrom),
]

MeatStrom_ = [tk.Label(root,height = 2, width = 45, relief=tk.RAISED, font=Labelfont,   bg="Dark Red", fg="White",text= "Meatballs, sausage, pepperoni, bacon, ham, sauce, & cheese"),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Small....$12.99",command= SmMeatStrom),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Medium...$21.99",command=MdMeatStrom),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Large....$23.99",command=LgMeatStrom),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Remove Toppings",command=ModMeat1),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Go back",command=Stromboli)
]

MeatStromS_ = [tk.Label(root,height = 2, width = 45, relief=tk.RAISED, font=Labelfont,   bg="Dark Red", fg="White",text= "Meatballs, sausage, pepperoni, bacon, ham, sauce, & cheese"),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Small....$12.99",command= SmMeatStrom),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Medium...$21.99",command=MdMeatStrom),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Large....$23.99",command=LgMeatStrom),
]



StkStrom_ = [tk.Label(root,height = 2, width = 45, relief=tk.RAISED, font=Labelfont,   bg="Dark Red", fg="White",text= "Steak & cheese (includes sauce on the side unless otherwise requested)"),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Small....$12.99",command=SmStkStrom),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Medium...$21.99",command=MdStkStrom),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Large....$23.99",command=LgStkStrom),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Go back",command=Stromboli)
]

Calzone_ = [tk.Label(root,height = 2, width = 45, relief=tk.RAISED, font=Labelfont,   bg="Dark Red", fg="White",text= "Ham, ricotta, & mozzarella"),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Small....$12.99",command=SmCalzone),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Medium...$21.99",command=MdCalzone),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Large....$23.99",command=LgCalzone),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Go back",command=Stromboli)
]



Stromboli_ = [tk.Label(root, relief=tk.RAISED, bg="Dark Red", fg="White",font=Labelfont, text= "Strombolis"),
            tk.Button(root,relief=tk.RAISED, font=custom_font,text="Stromboli Roll....Md/Lg",command=Roll),
            tk.Button(root,relief=tk.RAISED, font=custom_font,text="Traditional Stromboli.... Sm/Md/Lg",command=TradStrom),
            tk.Button(root,relief=tk.RAISED, font=custom_font,text="Vegetable Stromboli...Sm/Md/Lg",command=VegStrom),
            tk.Button(root,relief=tk.RAISED, font=custom_font,text="Meat Lovers Stromboli... Sm/Md/Lg",command=MeatStrom),
            tk.Button(root,relief=tk.RAISED, font=custom_font,text="Steak Stromboli...... Sm/Md/Lg",command=StkStrom),
            tk.Button(root,relief=tk.RAISED, font=custom_font,text="Calzone........ Sm/Md/Lg",command=Calzone),
]

def Chst():
    global pizzasize
    for button in Cheesesteaks_:
        button.pack_forget()
    for button in Chst_:
        button.pack()
    pizzasize = "Chst"

def ChickChst():
    global pizzasize
    for button in Cheesesteaks_:
        button.pack_forget()
    for button in Chst_:
        button.pack()
    pizzasize = "Chick Chst"

def ChstH():
    global pizzasize
    for button in Cheesesteaks_:
        button.pack_forget()
    for button in ChstH_:
        button.pack()
    pizzasize = "Chst H"

def ChickChstH():
    global pizzasize
    for button in Cheesesteaks_:
        button.pack_forget()
    for button in ChstH_:
        button.pack()
    pizzasize = "Chick Chst H"

def BuffChickChst():
    for button in Cheesesteaks_:
        button.pack_forget()
    for button in BuffChickChst_:
        button.pack()
    global pizzasize
    pizzasize = "Buff Chick Chst"

def PhillyChst():
    for button in Cheesesteaks_:
        button.pack_forget()
    for button in PhillyChst_:
        button.pack()
    global pizzasize
    pizzasize = "Philly Chst"

def GoBack1():
    for button in PhillyChst_:
        button.pack_forget()
    global pizzasize, No, toppingsW
    pizzasize=""
    No = ""
    toppingsW = ""
    for button in Cheesesteaks_:
        button.pack()

Cheesesteaks_ = [
    tk.Label(root,height = 2, width = 45, relief=tk.RAISED, bg="Dark Red", fg="White",font=Labelfont,text="Cheesesteaks"),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Cheesesteak",command=Chst),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Cheesesteak Hoagie",command=ChstH),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Chicken Cheesesteak",command=ChickChst),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Chicken Cheeseteak Hoagie",command=ChickChstH),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Philly Cheesesteak",command=PhillyChst),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Buffalo Chicken Cheesesteak",command=BuffChickChst),

]
def change_button_colorChst(index):
    Chst_[index].config(bg = '#393D47',  fg="white")
def change_button_colorChstH(index):
    ChstHAdd_[index].config(bg = '#393D47',  fg="white")
def change_button_colorChstHR(index):
    ChstHRemove_[index].config(bg = '#393D47',  fg="white")
def change_button_colorChstBuff(index):
    BuffChickChst_[index].config(bg = '#393D47',  fg="white")
def change_button_colorChstP(index):
    PhillyChstRemove_[index].config(bg = '#393D47',  fg="white")

def SauceS():
    global toppingsW
    toppingsW += " S"
    change_button_colorChst(0)

def OnionsS():
    global toppingsW
    toppingsW += " O"
    change_button_colorChst(1)
    
def MushroomS():
    global toppingsW
    toppingsW += " Mush"
    change_button_colorChst(2)

def HotPeppersS():
    global toppingsW
    toppingsW += " Hot"
    change_button_colorChst(3)
    change_button_colorChstH(0)

def PicklesS():
    global toppingsW
    toppingsW += " Pick"
    change_button_colorChst(4)
    change_button_colorChstH(2)
    
def SweetPeppersS():
    global toppingsW
    toppingsW += " Sweet"
    change_button_colorChst(5)
    change_button_colorChstH(1)
    
def XCheeseS():
    global toppingsW
    toppingsW += " XCh"
    change_button_colorChst(6)

def MayoS():
    global toppingsW
    toppingsW += " Mayo"
    change_button_colorChstH(6)


def NoCheeseS():
    global No
    No += "No Ch"
    change_button_colorChst(7)

def DoneSand():
    global pizzasize, toppingsW, No
    pizzasize = ""
    toppingsW = ""
    No = ""
    for button in Chst_:
        button.pack_forget()
    for button in ChstH_:
        button.pack_forget()
    label123.pack()
    for button in Done_:
        button.pack()

def GobackS():
    global pizzasize, toppingsW, No
    pizzasize = ""
    toppingsW = ""
    No = ""
    for button in Chst_:
        button.pack_forget()
    for button in ChstH_():
        button.pack_forget()
    
    
    for button in Cheesesteaks_:
        button.pack()


def ChstGoBackR():
    global No 
    No = ""
    for button in ChstHRemove_:
        button.pack_forget()
    for button in ChstH_:
        button.pack()

def ChstGoBackN():
    for button in ChstHAdd_:
        button.pack_forget()
    for button in ChstH_:
        button.pack()




def ChstHRemove():
    for button in ChstH_:
        button.pack_forget()
    for button in ChstHRemove_:
        button.pack()
    global No
    No = "No"

def ChstHadd():
    for button in ChstH_:
        button.pack_forget()
    for button in ChstHAdd_:
        button.pack()

def DoneChstR():
    for button in ChstHAdd_:
        button.pack_forget()
    for button in ChstHRemove_:
        button.pack_forget()
    for button in ChstH_:
        button.pack()

def DoneChstP():
    for button in PhillyChstRemove_:
        button.pack_forget()
    for button in ChstHRemove_:
        button.pack_forget()
    for button in PhillyChst_:
        button.pack()



Chst_ = [
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Sauce",command=SauceS),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Onions",command=OnionsS),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Mushrooms",command=MushroomS),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Hot Peppers",command= HotPeppersS),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Pickles",command=PicklesS),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Sweet Peppers",command=SweetPeppersS),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Extra Cheese",command=XCheeseS),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="No Cheese",command=NoCheeseS),
    tk.Button(root,height = 2, width = 45, bg = "#2E2E2E",fg = "White",relief=tk.RAISED, font=custom_font,text="Next",command=DoneSand),
    tk.Button(root,height = 2, width = 45,fg = "White",relief=tk.RAISED, font=custom_font,text="Go Back",command=GobackS),
]


ChstH_ = [
    tk.Label(root,height = 2, width = 45, relief=tk.RAISED, font=Labelfont,   bg="Dark Red", fg="White",text= "Lettuce, Tomato, Onions, Oil and Vinegar"),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Order as is",command=DoneSand),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Remove",command=ChstHRemove),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Add",command=ChstHadd),
    tk.Button(root,height = 2, width = 45, bg = "#2E2E2E",fg = "White",relief=tk.RAISED, font=custom_font,text="Go Back",command=GobackS),
]

ChstHAdd_ = [
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Hot Peppers",command=HotPeppersS),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Sweet Peppers",command=OnionsS),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Pickles",command=PicklesS),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Mayo",command= MayoS),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Go Back",command=ChstGoBackR),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Done",command=DoneChstR),

]
def NoLettS():
    global No
    No += " Lettuce"
    change_button_colorChstHR(0)

def NoOS():
    global No
    No += " Onions"
    change_button_colorChstHR(1)

def NoTomS():
    global No
    No += " Tomato"
    change_button_colorChstHR(2)

def NoOVS():
    global No
    No += "  O/V"
    change_button_colorChstHR(3)

def NoCheeseS():
    global No
    No += "  Cheese"
    change_button_colorChstHR(4)

ChstHRemove_ = [tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="No Lettuce",command=NoLettS),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="No Onions",command=NoOS),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="No Tomato",command=NoTomS),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="No O/V",command= NoOVS),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="No Cheese",command= NoCheeseS),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Go Back",command=ChstGoBackR),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Done",command=DoneChstR),
]
def NoCh():
    global No
    No = " NoCh"
    change_button_colorChstBuff(1)
def WOn():
    global toppingsW
    toppingsW = " With O"
    change_button_colorChstBuff(2)
def RemPhilly():
    global No
    for button in PhillyChst_:
        button.pack_forget()
    for button in PhillyChstRemove_:
        button.pack()
    No = "No"
def BuffBack():
    for button in BuffChickChst_:
        button.pack_forget()
    for button in Chst_:
        button.pack()
    global pizzasize, No, toppingsW
    pizzasize, No, toppingsW = "", "", ""
BuffChickChst_ = [tk.Label(root,height = 2, width = 45, relief=tk.RAISED, bg="Dark Red", fg="White",font=Labelfont,text="Buffalo Chicken Cheesesteak"),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="No Cheese",command=NoCh),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="With Onions",command=WOn),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Go Back",command=BuffBack),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Done",command=DoneSand),
]
def ChstGoBackP():
    for button in PhillyChstRemove_:
        button.pack_forget()
    for button in PhillyChst_:
        button.pack()
    global No
    No = ""
PhillyChst_ = [tk.Label(root,height = 2, width = 45, relief=tk.RAISED, bg="Dark Red", fg="White",font=Labelfont,text="Steak, sauce, onions, green peppers, sausage, mushrooms, & cheese"),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Order as is",command=DoneSand),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Remove Toppings",command=RemPhilly),
        tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Go Back",command=GoBack1),
]

def NoSauceP():
    global No
    No += " Sauce"
    change_button_colorChstP(0)
def NoOP():
    global No
    No += " O"
    change_button_colorChstP(1)
def NoGPP():
    global No
    No += " GP"
    change_button_colorChstP(2)
def NoSausP():
    global No
    No += " Saus"
    change_button_colorChstP(3)
def NoMushP():
    global No
    No += " Mush"
    change_button_colorChstP(4)
def NoCheeseP():
    global No
    No += " Ch"
    change_button_colorChstP(5)





PhillyChstRemove_ = [
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="No Sauce",command=NoSauceP),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="No Onions",command=NoOP),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="No Green Peppers",command=NoGPP),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="No Sausage",command= NoSausP),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="No Mushroom",command= NoMushP),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="No Cheese",command= NoCheeseP),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Go Back",command=ChstGoBackP),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Done",command=DoneChstP),
]

def change_button_colorCB(index):
   CheeseBurger_[index].config(bg = '#393D47',  fg="white")
def change_button_colorHB(index):
   Hamburger_[index].config(bg = '#393D47',  fg="white")
def change_button_colorCaliHB(index):
    CaliHB_[index].config(bg = '#393D47',  fg="white")
def change_button_colorCaliCB(index):
    CaliCB_[index].config(bg = '#393D47',  fg="white")
def change_button_colorBacon(index):
    BaconCB_[index].config(bg = '#393D47',  fg="white")
def change_button_colorChick(index):
    ChickSand_[index].config(bg = '#393D47',  fg="white")

def DoneBurger():
    for button in CheeseBurger_:
        button.pack_forget()
    for button in Hamburger_:
        button.pack_forget()
    for button in CaliHB_:
        button.pack_forget()
    for button in CaliCB_:
        button.pack_forget()
    for button in BaconCB_:
        button.pack_forget()
    for button in ChickSand_:
        button.pack_forget()
    for button in CBSub_:
        button.pack_forget()
    label123.pack()
    for button in Done_:
        button.pack()


        
def CB():
    for button in Burgers_:
        button.pack_forget()
    for button in CheeseBurger_:
        button.pack()
    global pizzasize
    pizzasize = "CB"
def HB():
    for button in Burgers_:
        button.pack_forget()
    for button in Hamburger_:
        button.pack()
    global pizzasize
    pizzasize = "HB"
def CaliHB():
    for button in Burgers_:
        button.pack_forget()
    for button in CaliHB_:
        button.pack()
    global pizzasize
    pizzasize = "Cali HB"
def CaliCB():
    for button in Burgers_:
        button.pack_forget()
    for button in CaliCB_:
        button.pack()
    global pizzasize
    pizzasize = "Cali CB"
def BaconCB():
    for button in Burgers_:
        button.pack_forget()
    for button in BaconCB_:
        button.pack()
    global pizzasize
    pizzasize = "Bacon CB"
def ChickSand():
    for button in Burgers_:
        button.pack_forget()
    for button in ChickSand_:
        button.pack()
    global pizzasize
    pizzasize = "Chick Sand"
def CBSub():
    for button in Burgers_:
        button.pack_forget()
    for button in CBSub_:
        button.pack()
    global pizzasize
    pizzasize = "CB Sub"
def NoCheese():
    global No
    No = " No Ch"
    change_button_colorChick(1)
def CBCheese():
    global toppingsW
    toppingsW += " Ch"
    change_button_colorChick(1)
def CBLett():
    global toppingsW
    toppingsW += " Lett"
    change_button_colorCB(1)
    change_button_colorBacon(1)
    change_button_colorHB(1)
    change_button_colorChick(2)
def CBTom():
    global toppingsW
    toppingsW += " Tom"
    change_button_colorCB(2)
    change_button_colorBacon(2)
    change_button_colorHB(2)
    change_button_colorChick(3)
def CBO():
    global toppingsW
    toppingsW += " O"
    change_button_colorCB(3)
    change_button_colorBacon(3)
    change_button_colorHB(3)
    change_button_colorChick(4)
def CBPick():
    global toppingsW
    toppingsW += " Pick"
    change_button_colorCB(4)
    change_button_colorBacon(4)
    change_button_colorHB(4)
    change_button_colorChick(5)
def CBKetch():
    global toppingsW
    toppingsW += " Ketch"
    change_button_colorCB(5)
    change_button_colorCaliHB(1)
    change_button_colorCaliCB(1)
    change_button_colorBacon(5)
    change_button_colorHB(5)
    change_button_colorChick(6)
def CBMust():
    global toppingsW
    toppingsW += " Must"
    change_button_colorCB(6)
    change_button_colorCaliHB(2)
    change_button_colorCaliCB(2)
    change_button_colorBacon(6)
    change_button_colorHB(6)
    change_button_colorChick(7)
def CBHMust():
    global toppingsW
    toppingsW += " Honey Must"
    change_button_colorCB(7)
    change_button_colorCaliHB(3)
    change_button_colorCaliCB(3)
    change_button_colorBacon(7)
    change_button_colorHB(7)
    change_button_colorChick(8)
def CBMayo():
    global toppingsW
    toppingsW += " Mayo"
    change_button_colorCB(8)
    change_button_colorCaliHB(4)
    change_button_colorCaliCB(4)
    change_button_colorBacon(8)
    change_button_colorHB(8)
    change_button_colorChick(9)




Burgers_ = [
    tk.Label(root,height = 2, width = 45, relief=tk.RAISED, bg="Dark Red", fg="White",font=Labelfont,text="Burgers"),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Cheeseburger......$6.49",command=CB),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Hamburger........$5.99",command=HB),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="California Hamburger....$6.49",command=CaliHB),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="California Cheeseburger...$7.49",command=CaliCB),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Bacon Cheeseburger...$7.99",command=BaconCB),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Chicken sandwich....$6.49",command=ChickSand),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Cheeseburger Sub...$10.99",command=CBSub),
]


CBSub_ = [
    tk.Label(root,height = 2, width = 45, relief=tk.RAISED, bg="Dark Red", fg="White",font=Labelfont,text = "Cheesebuerger Sub"),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="No Cheese",command=NoCheese),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Add Lettuce",command=CBLett),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Add Tomato",command=CBTom),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Add Onions",command=CBO),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Add Pickles",command=CBPick),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Ketchup",command=CBKetch),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Mustard",command=CBMust),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Honey Mustard",command=CBHMust),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Mayo",command=CBMayo),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,bg = "#2E2E2E",fg = "White", text="Done",command=DoneBurger),
]
ChickSand_ = [
    tk.Label(root,height = 2, width = 45, relief=tk.RAISED, bg="Dark Red", fg="White",font=Labelfont,text = "Chicken Sandwich"),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Add Cheese",command=CBCheese),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Add Lettuce",command=CBLett),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Add Tomato",command=CBTom),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Add Onions",command=CBO),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Add Pickles",command=CBPick),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Ketchup",command=CBKetch),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Mustard",command=CBMust),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Honey Mustard",command=CBHMust),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Mayo",command=CBMayo),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,bg = "#2E2E2E",fg = "White",text="Done",command=DoneBurger),
]
BaconCB_ = [
    tk.Label(root,height = 2, width = 45, relief=tk.RAISED, bg="Dark Red", fg="White",font=Labelfont,text="Bacon Cheeseburger"),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Add Lettuce",command=CBLett),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Add Tomato",command=CBTom),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Add Onions",command=CBO),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Add Pickles",command=CBPick),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Ketchup",command=CBKetch),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Mustard",command=CBMust),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Honey Mustard",command=CBHMust),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Mayo",command=CBMayo),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,bg = "#2E2E2E",fg = "White",text="Done",command=DoneBurger),
]
CaliCB_ = [
    tk.Label(root,height = 2, width = 45, relief=tk.RAISED, bg="Dark Red", fg="White",font=Labelfont,text="Cheeseburger with Lettuce, tomato, pickles, & onions"),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Ketchup",command=CBKetch),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Mustard",command=CBMust),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Honey Mustard",command=CBHMust),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Mayo",command=CBMayo),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,bg = "#2E2E2E",fg = "White",text="Done",command=DoneBurger),
]
CaliHB_ = [
    tk.Label(root,height = 2, width = 45, relief=tk.RAISED, bg="Dark Red", fg="White",font=Labelfont,text="Hamburger with Lettuce, tomato, pickles, & onions"),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Ketchup",command=CBKetch),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Mustard",command=CBMust),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Honey Mustard",command=CBHMust),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Mayo",command=CBMayo),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,bg = "#2E2E2E",fg = "White",text="Done",command=DoneBurger),
]


CheeseBurger_= [
    tk.Label(root,height = 2, width = 45, relief=tk.RAISED, bg="Dark Red", fg="White",font=Labelfont,text="Cheeseburger"),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Add Lettuce",command=CBLett),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Add Tomato",command=CBTom),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Add Onions",command=CBO),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Add Pickles",command=CBPick),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Ketchup",command=CBKetch),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Mustard",command=CBMust),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Honey Mustard",command=CBHMust),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Mayo",command=CBMayo),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,bg = "#2E2E2E",fg = "White",text="Done",command=DoneBurger),
]

Hamburger_= [
    tk.Label(root,height = 2, width = 45, relief=tk.RAISED, bg="Dark Red", fg="White",font=Labelfont,text="Hamburger"),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Add Lettuce",command=CBLett),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Add Tomato",command=CBTom),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Add Onions",command=CBO),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Add Pickles",command=CBPick),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Ketchup",command=CBKetch),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Mustard",command=CBMust),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Honey Mustard",command=CBHMust),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Mayo",command=CBMayo),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,bg = "#2E2E2E",fg = "White",text="Done",command=DoneBurger),
]

def DoneH():
    for button in ItalH_:
        button.pack_forget()
    for button in AmerH_:
        button.pack_forget()
    for button in HamProvH_:
        button.pack_forget()
    for button in HamAmerH_:
        button.pack_forget()
    for button in SpecH_:
        button.pack_forget()
    for button in TunaH_:
        button.pack_forget()
    for button in TurkH_:
        button.pack_forget()
    label123.pack()
    for button in Done_:
        button.pack()
def GoBackH():
    for button in ItalH_:
        button.pack_forget()
    for button in AmerH_:
        button.pack_forget()
    for button in HamProvH_:
        button.pack_forget()
    for button in HamAmerH_:
        button.pack_forget()
    for button in SpecH_:
        button.pack_forget()
    for button in TunaH_:
        button.pack_forget()
    for button in TurkH_:
        button.pack_forget()
    for button in Hoagies_:
        button.pack()
    global pizzasize, toppingsW, No
    pizzasize, No, toppingsW = "","",""
def ItalH():
    for button in Hoagies_:
        button.pack_forget()
    for button in ItalH_:
        button.pack()
    global pizzasize
    pizzasize = "H"
def AmerH():
    for button in Hoagies_:
        button.pack_forget()
    for button in AmerH_:
        button.pack()
    global pizzasize
    pizzasize = "Amer H"
def SpecH():
    for button in Hoagies_:
        button.pack_forget()
    for button in SpecH_:
        button.pack()
    global pizzasize
    pizzasize = "Spec H"
def HamProvH():
    for button in Hoagies_:
        button.pack_forget()
    for button in HamProvH_:
        button.pack()
    global pizzasize
    pizzasize = "Ham and Prov H"
def HamAmerH():
    for button in Hoagies_:
        button.pack_forget()
    for button in HamAmerH_:
        button.pack()
    global pizzasize
    pizzasize = "Ham and American H"
def TunaH():
    for button in Hoagies_:
        button.pack_forget()
    for button in TunaH_:
        button.pack()
    global pizzasize
    pizzasize = "Tuna H"
def TurkH():
    for button in Hoagies_:
        button.pack_forget()
    for button in TurkH_:
        button.pack()
    global pizzasize
    pizzasize = "Turkey H"
Hoagies_ = [
    tk.Label(root,height = 2, width = 45, relief=tk.RAISED, bg="Dark Red", fg="White",font=Labelfont,text="Hoagies"),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Italian Hoagie....$10.49",command=ItalH),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="American Hoagie......$10.49",command=AmerH),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Ham and American Cheese Hoagie........$10.49",command=HamAmerH),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Ham and Provolone Cheese Hoagie........$10.49",command=HamProvH),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Tuna Hoagie.......$10.49",command=TunaH),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Mario's Special Hoagie...$11.49",command=SpecH),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Turkey Hoagie.......$11.49",command=TurkH),
]
def change_button_colorItalHR(index):
   ItalRemove_[index].config(bg = '#393D47',  fg="white")
   AmerHRemove_[index].config(bg = '#393D47',  fg="white")
   HamAmerHRemove_[index].config(bg = '#393D47',  fg="white")   
def change_button_colorItalHA(index):
   ItalAdd_[index].config(bg = '#393D47',  fg="white")
   AmerHAdd_[index].config(bg = '#393D47',  fg="white")
   HamAmerHAdd_[index].config(bg = '#393D47',  fg="white")
   TunaHAdd_[index].config(bg = '#393D47',  fg="white")
   TurkHAdd_[index].config(bg = '#393D47',  fg="white")
def change_button_colorSpec(index):
   SpecHRemove_[index].config(bg = '#393D47',  fg="white")
def change_button_colorHamCh(index):
   HamProvHRemove_[index].config(bg = '#393D47',  fg="white")
   HamAmerHRemove_[index].config(bg = '#393D47',  fg="white")

def ItalHAdd():
    for button in ItalH_:
        button.pack_forget()
    for button in ItalAdd_:
        button.pack()

def ItalHRemove():
    for button in ItalH_:
        button.pack_forget()
    for button in ItalRemove_:
        button.pack()
    global No
    No = "No"
def DoneItalH():
    for button in ItalRemove_:
        button.pack_forget()
    for button in ItalAdd_:
        button.pack_forget()
    for button in ItalH_:
        button.pack()
def AmerHAdd():
    for button in AmerH_:
        button.pack_forget()
    for button in AmerHAdd_:
        button.pack()

def AmerHRemove():
    for button in ItalH_:
        button.pack_forget()
    for button in ItalRemove_:
        button.pack()
    global No
    No = "No"
def AmerHDone():
    for button in AmerHRemove_:
        button.pack_forget()
    for button in AmerHAdd_:
        button.pack_forget()
    for button in AmerH_:
        button.pack()





def HamAmerHAdd():
    for button in HamAmerH_:
        button.pack_forget()
    for button in HamAmerHAdd_:
        button.pack()

def HamAmerHRemove():
    for button in HamAmerH_:
        button.pack_forget()
    for button in HamAmerHRemove_:
        button.pack()
    global No
    No = "No"
def HamAmerHDone():
    for button in HamAmerHRemove_:
        button.pack_forget()
    for button in HamAmerHAdd_:
        button.pack_forget()
    for button in HamAmerH_:
        button.pack()



def HamProvHAdd():
    for button in HamProvH_:
        button.pack_forget()
    for button in HamProvHAdd_:
        button.pack()

def HamProvHRemove():
    for button in HamProvH_:
        button.pack_forget()
    for button in HamProvHRemove_:
        button.pack()
    global No
    No = "No"
def HamProvHDone():
    for button in HamProvHRemove_:
        button.pack_forget()
    for button in HamProvHAdd_:
        button.pack_forget()
    for button in HamProvH_:
        button.pack()


def SpecHAdd():
    for button in SpecH_:
        button.pack_forget()
    for button in SpecHAdd_:
        button.pack()

def SpecHRemove():
    for button in SpecH_:
        button.pack_forget()
    for button in SpecHRemove_:
        button.pack()
    global No
    No = "No"
def SpecHDone():
    for button in SpecHRemove_:
        button.pack_forget()
    for button in SpecHAdd_:
        button.pack_forget()
    for button in SpecH_:
        button.pack()


def RLett():
    global No
    No += " Lett"
    change_button_colorItalHR(0)
def RTom():
    global No
    No += " Tom"
    change_button_colorItalHR(1)
def RO():
    global No
    No += " O"
    change_button_colorItalHR(2)
def ROil():
    global No
    No += " Oil"
    change_button_colorItalHR(3)
def RVin():
    global No
    No += " Vin"
    change_button_colorItalHR(4)
def RHam():
    global No
    No += " Ham"
    change_button_colorItalHR(5)
def Rsal():
    global No
    No += " Salami"
    change_button_colorItalHR(6)
def RProv():
    global No
    No += " Provolone"
    change_button_colorItalHR(7)
def RAmer():
    global No
    No += " American"
    change_button_colorItalHR(7)
def RProvHCh():
    global No
    No += " Provolone"
    change_button_colorHamCh(7)
def RHamAmer():
    global No
    No += " American"
    change_button_colorHamCh(7)

def RCapSpec():
    global No
    No += " Capicola"
    change_button_colorSpec(8)
def HHot():
    global toppingsW
    toppingsW += " Hot"
    change_button_colorItalHA(0)
def HSweet():
    global toppingsW
    toppingsW += " Sweet"
    change_button_colorItalHA(1)
def ItalHDone():
    for button in ItalRemove_:
        button.pack_forget()
    for button in ItalAdd_:
        button.pack_forget()
    for button in ItalH_:
        button.pack()

def HPick():
    global toppingsW
    toppingsW += " Pick"
    change_button_colorItalHA(2)
def HMayo():
    global toppingsW
    toppingsW += " Mayo"
    change_button_colorItalHA(3)
def Grinder():
    global toppingsW
    toppingsW += " Grinder"
    change_button_colorItalHA(4)
ItalH_ = [
    tk.Label(root,height = 2, width = 70, relief=tk.RAISED, bg="Dark Red", fg="White",font=Labelfont,text="Ham, Salami, Provolone, Lettuce, Tomato, Onion, and Oil & Vinager"),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Add to it",command=ItalHAdd),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Remove from it",command=ItalHRemove),
    tk.Button(root,height = 2, width = 45,bg = "#2E2E2E",fg = "White", relief=tk.RAISED, font=custom_font,text="Done",command=DoneH),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Go Back",command=GoBackH)
]
AmerH_ = [
    tk.Label(root,height = 2, width = 70, relief=tk.RAISED, bg="Dark Red", fg="White",font=Labelfont,text="Ham, Salami, American Cheese, Lettuce, Tomato, Onion, and Oil & Vinager"),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Add to it",command=AmerHAdd),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Remove from it",command=AmerHRemove),
    tk.Button(root,height = 2, width = 45,bg = "#2E2E2E",fg = "White", relief=tk.RAISED, font=custom_font,text="Done",command=DoneH),
    tk.Button(root,height = 2, width = 80, relief=tk.RAISED, font=custom_font,text="Go Back",command=GoBackH)
]
HamAmerH_ = [
    tk.Label(root,height = 2, width = 70, relief=tk.RAISED, bg="Dark Red", fg="White",font=Labelfont,text="Ham, American Cheese, Lettuce, Tomato, Onion, and Oil & Vinager"),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Add to it",command=HamAmerHAdd),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Remove from it",command=HamAmerHRemove),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Done",bg = "#2E2E2E",fg = "White",command=DoneH),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Go Back",command=GoBackH)
]
HamProvH_ = [
    tk.Label(root,height = 2, width = 70, relief=tk.RAISED, bg="Dark Red", fg="White",font=Labelfont,text="Ham, Provolone, Lettuce, Tomato, Onion, and Oil & Vinager"),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Add to it",command=HamProvHAdd),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Remove from it",command=HamProvHRemove),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Done",bg = "#2E2E2E",fg = "White",command=DoneH),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Go Back",command=GoBackH)
]
SpecH_ = [
    tk.Label(root,height = 2, width = 70, relief=tk.RAISED, bg="Dark Red", fg="White",font=Labelfont,text="Ham, Salami, Capicola, American Cheese, Lettuce, Tomato, Onion, and Oil & Vinager"),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Add to it",command=SpecHAdd),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Remove from it",command=SpecHRemove),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Done",bg = "#2E2E2E",fg = "White",command=DoneH),
    tk.Button(root,height = 2, width = 80, relief=tk.RAISED, font=custom_font,text="Go Back",command=GoBackH)
]

ItalRemove_ = [
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text=" Lettuce",command=RLett),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text=" Tomato",command=RTom),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text=" Onions",command=RO),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Oil",command=ROil),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Vinegar",command=RVin),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Ham",command=RHam),  
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Salami",command=Rsal),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Provolone",command=RProv),  
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Done",bg = "#2E2E2E",fg = "White",command=ItalHDone),  
]
ItalAdd_ = [
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text=" Hot Peppers",command=HHot),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text=" Sweet Peppers",command=HSweet),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text=" Add Pickles",command=HPick),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Mayo",command=HMayo),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Grinder",command=Grinder),  
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Done",bg = "#2E2E2E",fg = "White",command=ItalHDone),  
]

AmerHRemove_ = [
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text=" Lettuce",command=RLett),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Tomato",command=RTom),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text=" Onions",command=RO),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Oil",command=ROil),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Vinegar",command=RVin),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Ham",command=RHam),  
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Salami",command=Rsal),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="American Cheese",command=RAmer),  
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Done",bg = "#2E2E2E",fg = "White",command=AmerHDone),  
]
AmerHAdd_ = [
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Hot Peppers",command=HHot),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Sweet Peppers",command=HSweet),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Add Pickles",command=HPick),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Mayo",command=HMayo),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Grinder",command=Grinder),  
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Done",bg = "#2E2E2E",fg = "White",command=AmerHDone),  
]

SpecHRemove_ = [
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text=" Lettuce",command=RLett),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Tomato",command=RTom),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text=" Onions",command=RO),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Oil",command=ROil),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Vinegar",command=RVin),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Ham",command=RHam),  
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Salami",command=Rsal),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Provalone",command=RProv),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Capicola",command=RCapSpec),  
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Done",bg = "#2E2E2E",fg = "White",command=SpecHDone),  
]
SpecHAdd_ = [
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Hot Peppers",command=HHot),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Sweet Peppers",command=HSweet),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Add Pickles",command=HPick),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Mayo",command=HMayo),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Grinder",command=Grinder),  
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Done",bg = "#2E2E2E",fg = "White",command=SpecHDone),  
]

HamAmerHRemove_ = [
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text=" Lettuce",command=RLett),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Tomato",command=RTom),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text=" Onions",command=RO),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Oil",command=ROil),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Vinegar",command=RVin),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Ham",command=RHam),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="American Cheese",command=RProv),  
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Done",bg = "#2E2E2E",fg = "White",command=AmerHDone),  
]
HamAmerHAdd_ = [
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Hot Peppers",command=HHot),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Sweet Peppers",command=HSweet),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Add Pickles",command=HPick),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Mayo",command=HMayo),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Grinder",command=Grinder),  
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Done",bg = "#2E2E2E",fg = "White",command=AmerHDone),  
]

HamProvHRemove_ = [
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text=" Lettuce",command=RLett),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Tomato",command=RTom),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text=" Onions",command=RO),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Oil",command=ROil),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Vinegar",command=RVin),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Ham",command=RHam),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Provolone",command=RProvHCh),  
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Done",bg = "#2E2E2E",fg = "White",command=AmerHDone),  
]
HamProvHAdd_ = [
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Hot Peppers",command=HHot),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Sweet Peppers",command=HSweet),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Add Pickles",command=HPick),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Mayo",command=HMayo),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Grinder",command=Grinder),  
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Done",bg = "#2E2E2E",fg = "White",command=AmerHDone),  
]
def change_button_colorTunaR(index):
  TunaHRemove_[index].config(bg = '#393D47',  fg="white")
  TurkHRemove_[index].config(bg = '#393D47',  fg="white")
def change_button_colorTunaA(index):
  TunaHAdd_[index].config(bg = '#393D47',  fg="white")
  TurkHAdd_[index].config(bg = '#393D47',  fg="white")
def TunaAddDone():
    for button in TunaHAdd_:
        button.pack_forget()
    for button in TunaH_:
        button.pack()
def TunaRemoveDone():
    for button in TunaHRemove_:
        button.pack_forget()
    for button in TunaH_:
        button.pack()
def TunaHRemove():
    for button in TunaH_:
        button.pack_forget()
    for button in TunaHRemove_:
        button.pack()
    global No
    No = "No"
def TunaHAdd():
    for button in TunaH_:
        button.pack_forget()
    for button in TunaHAdd_:
        button.pack()


def TurkAddDone():
    for button in TurkHAdd_:
        button.pack_forget()
    for button in TurkH_:
        button.pack()
def TurkRemoveDone():
    for button in TurkHRemove_:
        button.pack_forget()
    for button in TurkH_:
        button.pack()
def TurkHRemove():
    for button in TurkH_:
        button.pack_forget()
    for button in TurkHRemove_:
        button.pack()
    global No
    No = "No"
def TurkHAdd():
    for button in TurkH_:
        button.pack_forget()
    for button in TurkHAdd_:
        button.pack()



def TunaHRLett():
    global No
    No += " Lett"
    change_button_colorTunaR(0)
def TunaHRTom():
    global No
    No += " Tom"
    change_button_colorTunaR(1)
def TunaHRO():
    global No
    No += " O"
    change_button_colorTunaR(2)
def TunaHRMayo():
    global No
    No += " Mayo"
    change_button_colorTunaR(3)


TunaH_ = [
    tk.Label(root,height = 2, width = 45, relief=tk.RAISED, bg="Dark Red", fg="White",font=Labelfont,text="Tuna (with mayo), Lettuce, Tomato, Onion"),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Add to it",command=TunaHAdd),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Remove from it",command=TunaHRemove),
    tk.Button(root,height = 2, width = 45,relief=tk.RAISED, font=custom_font,text="Done",bg = "#2E2E2E",fg = "White",command=DoneH),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Go Back",command=GoBackH)
]

TunaHRemove_ = [
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Lettuce",command=TunaHRLett),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Tomato",command=TunaHRTom),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Onions",command=TunaHRO),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Done",bg = "#2E2E2E",fg = "White",command=TunaAddDone),
]

TunaHAdd_ = [
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text=" Hot Peppers",command=HHot),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text=" Sweet Peppers",command=HSweet),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text=" Add Pickles",command=HPick),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Mayo",command=HMayo),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Grinder",command=Grinder),  
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Done",bg = "#2E2E2E",fg = "White",command=TunaRemoveDone),  
]

TurkH_ = [
    tk.Label(root,height = 2, width = 45, relief=tk.RAISED, bg="Dark Red", fg="White",font=Labelfont,text="Turkey, Lettuce, Tomato, Onion and Mayo"),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Add to it",command=TunaHAdd),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Remove from it",command=TunaHRemove),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Done",bg = "#2E2E2E",fg = "White",command=DoneH),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Go Back",command=GoBackH)
]

TurkHRemove_ = [
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Lettuce",command=TunaHRLett),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Tomato",command=TunaHRTom),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Onions",command=TunaHRO),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Done",bg = "#2E2E2E",fg = "White",command=TurkAddDone),
]

TurkHAdd_ = [
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text=" Hot Peppers",command=HHot),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text=" Sweet Peppers",command=HSweet),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text=" Add Pickles",command=HPick),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Mayo",command=HMayo),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Grinder",command=Grinder),  
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Done",bg = "#2E2E2E",fg = "White",command=TurkRemoveDone),  
]

def MeatParm():
    for button in HotSand_:
        button.pack_forget()
    global pizzasize
    pizzasize = "Meatball Parm"
    label123.pack()
    for button in Done_:
        button.pack()
    
def ChickParm():
    for button in HotSand_:
        button.pack_forget()
    global pizzasize
    pizzasize = "Chicken Parm"
    label123.pack()
    for button in Done_:
        button.pack()
def SausParm():
    for button in HotSand_:
        button.pack_forget()
    global pizzasize
    pizzasize = "Sausage Parm"
    label123.pack()
    for button in Done_:
        button.pack()
def EggParm():
    for button in HotSand_:
        button.pack_forget()
    global pizzasize
    pizzasize = "Eggplant Parm"
    label123.pack()
    for button in Done_:
        button.pack()
def SausGPO():
    for button in HotSand_:
        button.pack_forget()
    global pizzasize
    pizzasize = "Saus GP O Sand"
    label123.pack()
    for button in Done_:
        button.pack()
def Fish():
    for button in HotSand_:
        button.pack_forget()
    global pizzasize
    pizzasize = "Fish Fillet"
    label123.pack()
    for button in Done_:
        button.pack()



HotSand_ = [
    tk.Label(root,height = 2, width = 45, relief=tk.RAISED,bg="Dark Red", fg="White", font=Labelfont,text="Hot Sandwiches"),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Meatball Parmesan....$10.99",command=MeatParm),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Chicken Parmesan....$10.99",command=ChickParm),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Sausage Parmesan....$10.99",command=SausParm),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Eggplant Parmesan....$10.99",command=EggParm),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Sausage, Green Pepper, and Onion...$10.99",command=SausGPO),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Fish Fillet......$10.99",command=Fish),
]
def ChstWrap():
    for button in Wraps_:
        button.pack_forget()
    global pizzasize
    pizzasize = "Chst Wrap"
    label123.pack()
    for button in Done_:
        button.pack()
def CaesarWrap():
    for button in Wraps_:
        button.pack_forget()
    global pizzasize
    pizzasize = "Caesar Wrap"
    label123.pack()
    for button in Done_:
        button.pack()
def TurkWrap():
    for button in Wraps_:
        button.pack_forget()
    global pizzasize
    pizzasize = "Turk Wrap"
    label123.pack()
    for button in Done_:
        button.pack()
def TunaWrap():
    for button in Wraps_:
        button.pack_forget()
    global pizzasize
    pizzasize = "Tuna Wrap"
    label123.pack()
    for button in Done_:
        button.pack()
def BuffWrap():
    global pizzasize
    pizzasize = "Buff Wrap"
    for button in Wraps_:
        button.pack_forget()
    label123.pack()
    for button in Done_:
        button.pack()
Wraps_ = [
    tk.Label(root,height = 2, width = 45, relief=tk.RAISED, bg="Dark Red", fg="White",font=Labelfont,text="Wraps (HOAGIES CANNOT BE MODIFIED)"),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Cheesesteak Hoagie Wrap...$9.99",command=ChstWrap),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Grilled Chicken Caesar Wrap....$9.99",command=CaesarWrap),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Turkey and Cheese Wrap....$9.99",command=TurkWrap),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Tuna and Cheese Wrap....$9.99",command=TunaWrap),
    tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font,text="Buffalo Chicken Cheesesteak Wrap...$9.99",command=BuffWrap),
]







def NewItem():
    global items, pizzasize, toppingsW, toppings1, toppings2, cook, No
    Order.append(label123)
    pizzasize, toppingsW, toppings1, toppings2, cook, No = "", "", "", "", "", ""
    for button in Done_:
        button.pack_forget()
    for button in Where_:
        button.pack(pady = 3)
    label123.pack_forget()
def DisplayOrder():
    button_text = "\n".join(Order)
    Text.config(text=button_text, font = Labelfont,  bg="Dark Red", fg="White")
    for button in Done_:
        button.pack_forget()
    label123.pack_forget()
    for label in Text:    
        label.pack()
    

def OrderDone():  
    
    global pizzasize, toppingsW, toppings1, toppings2, cook, No
    Order.append(label123)
    
    pizzasize, toppingsW, toppings1, toppings2, cook, No = "", "", "", "", "", ""
    label123.pack_forget()
    Text.pack()

button_text = "\n ".join(Order) 

def on_button_click(item, button):
    items.remove(item)  
    button.destroy()   
    for items in items[:]:
        button.pack_forget()
    for label in Text:
        label.pack()
def Deleteitem():
    for button in Text:
        button.pack_forget()
    for item in items:
        button = tk.Button(root, text=Order, command=lambda i=item: on_button_click(i))
    button.pack(pady=5)



Done_ = [tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Add Item", command = NewItem),
         tk.Button(root,height = 2, width = 45, relief=tk.RAISED, font=custom_font, text="Complete Order", command = OrderDone),
]







Text = [tk.Label(root, relief=tk.RAISED, font=Labelfont, text=button_text,  bg="Dark Red", fg="White")
]

Done123 = tk.Button(root, relief=tk.RAISED, font=custom_font, text="Done", command = OrderDone),
Deleteitem_ = tk.Button(root, relief=tk.RAISED, font=custom_font, text="Delete item", command = Deleteitem),
for button in initial_screen:
    button.pack(pady = 3)
root.mainloop()
