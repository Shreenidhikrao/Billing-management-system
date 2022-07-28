from tkinter import *
from tkinter import messagebox
import tempfile
import os
import random

root = Tk()
root.title("BILLING MANAGEMENT SYSTEM ")
root.geometry('1960x1820')

#====================== VARIABLES ==============================

# we will define if we want string or interger



Bread = IntVar()
Chips = IntVar()
Cake  = IntVar()
Juice = IntVar()
Total = IntVar()

cb = StringVar()
cch = StringVar()
cca = StringVar()
cj = StringVar()

total_cost = StringVar()


#===================== FUNCTIONS =============================

#total function

def tot():
    if Bread.get()==0 and Chips.get()==0 and Cake.get()==0 and Juice.get()==0:
        messagebox.showerror('Error','please select number of quantity')
    else:
        b = Bread.get()
        ch = Chips.get()
        ca = Cake.get()
        j = Juice.get()

        t = int(b*20 + ch*10 + ca*50 + j*20)
        Total.set(b+ch+ca+j)
        total_cost.set(str(round(t,2))) # it round's up to 2 digit

        cb.set(b*20)
        cch.set(ch*10)
        cca.set(ca*50)
        cj.set(j*20)

#lets define the reciept function

def reciept():
    textarea.delete(1.0,END)
    textarea.insert(END,'\t         DESI BITES')
    textarea.insert(END, f'\n\nName  - \t{ntext.get()}')
    textarea.insert(END,f'\n\nPhone no  - \t{phtext.get()}')
    textarea.insert(END, f'\n\nBill no  - \t{bitext.get()}')
    textarea.insert(END,'\n\n---------------------------------------------')
    textarea.insert(END,'\n\nItems\t     Total Items\t  Item Cost')
    textarea.insert(END,f'\n\nBread\t\t{Bread.get()}\t{cb.get()}')
    textarea.insert(END, f'\n\nChips\t\t{Chips.get()}\t{cch.get()}')
    textarea.insert(END, f'\n\nCake\t\t{Cake.get()}\t{cca.get()}')
    textarea.insert(END, f'\n\nJuice\t\t{Juice.get()}\t{cj.get()}')
    textarea.insert(END,'\n----------------------------------------------')
    textarea.insert(END, f'\n\nTotal\t\t{Total.get()}\t{total_cost.get()}')
    textarea.insert(END, '\n----------------------------------------------')

def Print():
    q = textarea.get('1.0','end-1c')
    filename = tempfile.mktemp('.txt')  # creating a temporary file .txt by module tempfile using maketemp
    open(filename,'w').write(q) #opening the filename in write format
    os.startfile(filename,'Print') #0S module provides function to interact with the operating system
    #startfile start's the file of given name and opens it in a user specific format. In this case its print


def reset():
    textarea.delete(1.0,END)#deletes everything thats there in the reciept area from begining to end

    #setting all the items to zero
    Bread.set(0)
    Chips.set(0)
    Cake.set(0)
    Juice.set(0)
    Total.set(0)

    #setting all the cost with string as empty strings
    cb.set('')
    cch.set('')
    cca.set('')
    cj.set('')
    total_cost.set('')

def exit():
    if messagebox.askyesno('Exit','Do you really want to exit'): #askyesno creats a messagebox for exit
        root.destroy() # if yes is given in the messagebox then the whole window is destroyed



title = Label(root,text='BILLING MANAGEMENT SYSTEM ',bg='grey',fg='white',font=('font families ',35,'bold'),relief=GROOVE ,bd=12) #relief gives design with border 12
title.pack(fill=X) # fill = X fills the heading in whole line in x or y direction by specifing it

#====================== PRODUCT DETAILS ==========================

f1 = LabelFrame(root,text='Product Details ',font=('times new roman ',18,'bold'),fg='black',bg = 'grey',relief=RIDGE,bd=10) # frame creates a fram in the window for specific size with label
f1.place(x=5,y=200,width=800,height=500)

#===================== HEADINGS ==================================

itms = Label(f1,text = 'Items',font=('helvetic',25,'bold','underline'),fg='black',bg='grey')
itms.grid(row=0,column=0,padx=20,pady=15) # padx and pady will put some space between the widgets

num = Label(f1,text = 'Number Of Items ',font=('helvetic',25,'bold','underline'),fg='black',bg='grey')
num.grid(row=0,column=1,padx=20,pady=15) # padx and pady will put some space between the widgets

cost = Label(f1,text = 'Cost Of Items ',font=('helvetic',25,'bold','underline'),fg='black',bg='grey')
cost.grid(row=0,column=2,padx=20,pady=15) # padx and pady will put some space between the widgets

#======================= PRODUCTS ================================

bread = Label(f1,text = 'Bread',font=('times new roman ',20,'bold'),fg='black',bg='grey') #items
bread.grid(row=1,column=0,padx=20,pady=15)
btext = Entry(f1,font=('arial' , 15 , 'bold'),relief = SUNKEN,bd=7,justify=CENTER,textvariable=Bread) # number of items entry  , justify makes the entery to be in the specified position , in this case its center
btext.grid(row=1,column=1,padx=20,pady=15)
cbtext = Entry(f1,font=('arial' , 15 , 'bold'),relief = SUNKEN,bd=7,justify=CENTER,textvariable=cb) # cost of items entry
cbtext.grid(row=1,column=2,padx=20,pady=15)

chips = Label(f1,text = 'Chips',font=('times new roman ',20,'bold'),fg='black',bg='grey') #items
chips.grid(row=2,column=0,padx=20,pady=15)
ctext = Entry(f1,font=('arial' , 15 , 'bold'),relief = SUNKEN,bd=7,justify=CENTER,textvariable=Chips) # number of items entry
ctext.grid(row=2,column=1,padx=20,pady=15)
cctext = Entry(f1,font=('arial' , 15 , 'bold'),relief = SUNKEN,bd=7,justify=CENTER,textvariable=cch) # cost of items entry
cctext.grid(row=2,column=2,padx=20,pady=15)

cake = Label(f1,text = 'Cake',font=('times new roman ',20,'bold'),fg='black',bg='grey') #items
cake.grid(row=3,column=0,padx=20,pady=15)
catext = Entry(f1,font=('arial' , 15 , 'bold'),relief = SUNKEN,bd=7,justify=CENTER,textvariable=Cake) # number of items entry
catext.grid(row=3,column=1,padx=20,pady=15)
ccatext = Entry(f1,font=('arial' , 15 , 'bold'),relief = SUNKEN,bd=7,justify=CENTER,textvariable=cca) # cost of items entry
ccatext.grid(row=3,column=2,padx=20,pady=15)

juice = Label(f1,text = 'Juice',font=('times new roman ',20,'bold'),fg='black',bg='grey') #items
juice.grid(row=4,column=0,padx=20,pady=15)
jtext = Entry(f1,font=('arial' , 15 , 'bold'),relief = SUNKEN,bd=7,justify=CENTER,textvariable=Juice) # number of items entry
jtext.grid(row=4,column=1,padx=20,pady=15)
cjtext = Entry(f1,font=('arial' , 15 , 'bold'),relief = SUNKEN,bd=7,justify=CENTER,textvariable=cj) # cost of items entry
cjtext.grid(row=4,column=2,padx=20,pady=15)


total = Label(f1,text = 'Total Price ',font=('times new roman ',20,'bold'),fg='black',bg='grey') #items
total.grid(row=5,column=0,padx=20,pady=15)
ttext = Entry(f1,font=('arial' , 15 , 'bold'),relief = SUNKEN,bd=7,justify=CENTER,textvariable=Total) # number of items entry
ttext.grid(row=5,column=1,padx=20,pady=15)
cttext = Entry(f1,font=('arial' , 15 , 'bold'),relief = SUNKEN,bd=7,justify=CENTER,textvariable=total_cost) # cost of items entry
cttext.grid(row=5,column=2,padx=20,pady=15)

#================== BILLING AREA ======================

f2 = Frame(root,relief=GROOVE,bd=10)
f2.place(x=820,y=200,width=430,height=500)

billtitle = Label(f2,text='Recipt',font=('arial',15,'bold'),relief = GROOVE , bd=7)
billtitle.pack(fill=X)

#================== SCROLLBAR =========================

#lets create scrollbar for recipt section using Scrollbar()

scroll = Scrollbar(f2,orient=VERTICAL) # orient helps to create the scrollbar vertical or horizontal
scroll.pack(side=RIGHT,fill=Y) # we should give the location in pack and fill it in y direction

# to move the scrollbar lets create a text area

textarea = Text(f2,font='arial 15 ',yscrollcommand=scroll.set) #yscrollcommand provides a side controller that is used to impliment vertical scrolled widgets
textarea.pack(fill=BOTH) #both gives the movement of scrollbar in both the directions
scroll.config(command=textarea.yview) # command is a procedure to be called whenever the scrollbar is moved


#============== F4 ===================================
#another frame for customer name

f4 = Frame(root,relief=GROOVE,bd=10,bg='grey')
f4.place(x=5,y=90,width=1245,height=120)

name = Label(f4,text = 'Name',font=('times new roman ',20,'bold','underline'),fg='black',bg='grey')
name.grid(row=0,column=0,padx=20,pady=15)
ntext = Entry(f4,font=('arial' , 15 , 'bold'),relief = SUNKEN,bd=7,justify=CENTER) #
ntext.grid(row=0,column=1,pady = 15)

phno = Label(f4,text = 'Phone no',font=('times new roman ',20,'bold','underline'),fg='black',bg='grey')
phno.grid(row=0,column=2,padx=20,pady=15)
phtext = Entry(f4,font=('arial' , 15 , 'bold'),relief = SUNKEN,bd=7,justify=CENTER) #
phtext.grid(row=0,column=3,padx=20,pady=15)

billno = Label(f4,text = 'Bill no',font=('times new roman ',20,'bold','underline'),fg='black',bg='grey')
billno.grid(row=0,column=4,padx=20,pady=15)
bitext = Entry(f4,font=('arial' , 15 , 'bold'),relief = SUNKEN,bd=7,justify=CENTER) #
bitext.grid(row=0,column=5,padx=20,pady=15)
random_entry = random.randint(1000,9999)# to give a random bill nummber to the entry
bitext.insert(END,random_entry)


#====================== F5 ===========================

f5 = Frame(root,relief=GROOVE,bd=10)
f5.place(x=1270,y=210,width=250,height=490)

menu = Label(f5,text = 'Menu',font=('normal ',20,'bold','underline'),fg='black')
menu.grid(row=0,padx=75,pady=10)

menu_a = Label(f5,text = 'Bread   -   rs 20',font=('normal ',20),fg='black')
menu_a.grid(row=1,column=0,padx=5,pady=10)

menu_b = Label(f5,text = 'Chips   -   rs 10',font=('times new roman ',20),fg='black')
menu_b.grid(row=2,column=0,padx=5,pady=10)

menu_c = Label(f5,text = 'Cake   -    rs 50',font=('times new roman ',20),fg='black')
menu_c.grid(row=3,column=0,padx=5,pady=10)

menu_4 = Label(f5,text = 'juice    -    rs 20',font=('times new roman ',20),fg='black')
menu_4.grid(row=4,column=0,padx=5,pady=10)

#======================= BUTTON ======================

# lets create a frame for buttons

f3 = Frame(root,relief=GROOVE,bd=10,bg='grey')
f3.place(x=5,y=710,width=1245,height=120)

btn1 = Button(f3,text='Total',font=('arial',25,'bold'),bg='#d9d7d0',fg='black',padx=5,pady=5,width=10,command=tot) #command function is used to call the functions that we have defined
btn1.grid(row=0,column=0,padx=10,pady=10)

btn2 = Button(f3,text='Recipt',font=('arial',25,'bold'),bg='#d9d7d0',fg='black',padx=5,pady=5,width=10,command=reciept)
btn2.grid(row=0,column=1,padx=10,pady=10)

btn3 = Button(f3,text='Print',font=('arial',25,'bold'),bg='#d9d7d0',fg='black',padx=5,pady=5,width=10,command=Print)
btn3.grid(row=0,column=2,padx=10,pady=10)

btn4 = Button(f3,text='Reset',font=('arial',25,'bold'),bg='#d9d7d0',fg='black',padx=5,pady=5,width=10,command=reset)
btn4.grid(row=0,column=3,padx=10,pady=10)

btn5 = Button(f3,text='Exit',font=('arial',25,'bold'),bg='#d9d7d0',fg='black',padx=5,pady=5,width=10,command=exit)
btn5.grid(row=0,column=4,padx=10,pady=10)

root.mainloop()