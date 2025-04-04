from tkinter import *

root = Tk()
root.geometry("1100x600")
root.resizable(False, False)

def Reset():
    entry_Burger.delete(0, END)
    entry_Sandwitch.delete(0, END)
    entry_Pizza.delete(0, END)
    entry_Peddis.delete(0, END)
    entry_CAKE.delete(0, END)
    entry_COOLA.delete(0, END)
    entry_TEA.delete(0, END)
    entry_discount.delete(0, END)
    entry_discount.insert(0, "0")  # Set discount back to 0 on reset

def Total():
    try:
        a1 = int(Burger.get())
    except:
        a1 = 0
    try:
        a2 = int(Sandwitch.get())
    except:
        a2 = 0
    try:
        a3 = int(Pizza.get())
    except:
        a3 = 0
    try:
        a4 = int(Peddis.get())
    except:
        a4 = 0
    try:
        a5 = int(CAKE.get())
    except:
        a5 = 0
    try:
        a6 = int(COOLA.get())
    except:
        a6 = 0
    try:
        a7 = int(TEA.get())
    except:
        a7 = 0

    # Define cost of each item per quantity
    c1 = 50 * a1
    c2 = 20 * a2
    c3 = 45 * a3
    c4 = 30 * a4
    c5 = 40 * a5
    c6 = 15 * a6
    c7 = 10 * a7

    totalcost = c1 + c2 + c3 + c4 + c5 + c6 + c7

    # Display total amount
    string_bill = "US. " + str('%.2f' % totalcost)
    Total_Bill.set(string_bill)

    # Get discount
    try:
        discount_percent = float(entry_discount.get())
        total_after_discount = totalcost - discount_amount
        string_after_discount = "US. " + str('%.2f' % total_after_discount)
        Total_After_Discount.set(string_after_discount)
    except:
        Total_After_Discount.set("US. 0.00")

# Label for Bill Management
Label(text="BILL MANAGEMENT", bg="black", fg="white", font=("calibri", 33), width="300", height="2").pack()

# Bill Manager Name Entry
label_manager_name = Label(root, text="Enter Bill Management Name:", font=("arial", 12), fg="black")
label_manager_name.place(x=750, y=10)
entry_manager_name = Entry(root, font=("arial", 12), fg="black", width=15)
entry_manager_name.place(x=750, y=40)

# Menu Card
f = Frame(root, bg="lightgreen", highlightbackground="black", highlightthickness=1, width=300, height=370)
f.place(x=10, y=118)

Label(f, text="Menu", font=("Gabriola", 40, "bold"), fg="black", bg="lightgreen").place(x=80, y=0)
Label(f, font=("Lucida Calligraphy", 15, 'bold'), text="Burger.......USD.50/Per", fg="black", bg="lightgreen").place(x=10, y=80)
Label(f, font=("Lucida Calligraphy", 15, 'bold'), text="Sandwitch.......USD.20/Per", fg="black", bg="lightgreen").place(x=10, y=110)
Label(f, font=("Lucida Calligraphy", 15, 'bold'), text="Pizza.......USD.45/Per", fg="black", bg="lightgreen").place(x=10, y=140)
Label(f, font=("Lucida Calligraphy", 15, 'bold'), text="Peddis.......USD.30/Per", fg="black", bg="lightgreen").place(x=10, y=170)
Label(f, font=("Lucida Calligraphy", 15, 'bold'), text="CAKE.......USD.40/Per", fg="black", bg="lightgreen").place(x=10, y=200)
Label(f, font=("Lucida Calligraphy", 15, 'bold'), text="COOLA.......USD.150/Per", fg="black", bg="lightgreen").place(x=10, y=230)
Label(f, font=("Lucida Calligraphy", 15, 'bold'), text="TEA.......USD.10/Per", fg="black", bg="lightgreen").place(x=10, y=260)

# BILL
f2 = Frame(root, bg="lightyellow", highlightbackground="black", highlightthickness=1, width=300, height=370)
f2.place(x=690, y=118)

Bill = Label(f2, text="Bill", font=('calibri', 20), bg="white")

# Entry work
f1 = Frame(root, bd=5, height=370, width=300, relief=RAISED)
f1.pack()
Burger = StringVar()
Sandwitch = StringVar()
Pizza = StringVar()
Peddis = StringVar()
CAKE = StringVar()
COOLA = StringVar()
TEA = StringVar()
Total_Bill = StringVar()
Total_After_Discount = StringVar()

# Labels
lbl_Burger = Label(f1, font=("aria", 20, 'bold'), text="Burger", width=12, fg="blue4")
lbl_Sandwitch = Label(f1, font=("aria", 20, 'bold'), text="Sandwitch", width=12, fg="blue4")
lbl_Pizza = Label(f1, font=("aria", 20, 'bold'), text="Pizza", width=12, fg="blue4")
lbl_Peddis = Label(f1, font=("aria", 20, 'bold'), text="Peddis", width=12, fg="blue4")
lbl_CAKE = Label(f1, font=("aria", 20, 'bold'), text="CAKE", width=12, fg="blue4")
lbl_COOLA = Label(f1, font=("aria", 20, 'bold'), text="COOLA", width=12, fg="blue4")
lbl_TEA = Label(f1, font=("aria", 20, 'bold'), text="TEA", width=12, fg="blue4")

lbl_Burger.grid(row=1, column=0)
lbl_Sandwitch.grid(row=2, column=0)
lbl_Pizza.grid(row=3, column=0)
lbl_Peddis.grid(row=4, column=0)
lbl_CAKE.grid(row=5, column=0)
lbl_COOLA.grid(row=6, column=0)
lbl_TEA.grid(row=7, column=0)

# Entries
entry_Burger = Entry(f1, font=("arial", 20, 'bold'), textvariable=Burger, bd=6, width=8, bg="lightpink")
entry_Sandwitch = Entry(f1, font=("arial", 20, 'bold'), textvariable=Sandwitch, bd=6, width=8, bg="lightpink")
entry_Pizza = Entry(f1, font=("arial", 20, 'bold'), textvariable=Pizza, bd=6, width=8, bg="lightpink")
entry_Peddis = Entry(f1, font=("arial", 20, 'bold'), textvariable=Peddis, bd=6, width=8, bg="lightpink")
entry_CAKE = Entry(f1, font=("arial", 20, 'bold'), textvariable=CAKE, bd=6, width=8, bg="lightpink")
entry_COOLA = Entry(f1, font=("arial", 20, 'bold'), textvariable=COOLA, bd=6, width=8, bg="lightpink")
entry_TEA = Entry(f1, font=("arial", 20, 'bold'), textvariable=TEA, bd=6, width=8, bg="lightpink")

entry_Burger.grid(row=1, column=1)
entry_Sandwitch.grid(row=2, column=1)
entry_Pizza.grid(row=3, column=1)
entry_Peddis.grid(row=4, column=1)
entry_CAKE.grid(row=5, column=1)
entry_COOLA.grid(row=6, column=1)
entry_TEA.grid(row=7, column=1)

# Discount Label and Entry
lbl_discount = Label(f2, font=("arial", 13, 'bold'), text="Discount(%)", width=18, fg="blue4", bg="lightyellow")
lbl_discount.place(x=0, y=150)
entry_discount = Entry(f2, font=("arial", 15, 'bold'), bd=6, width=10, bg="lightpink")
entry_discount.place(x=160, y=150)
entry_discount.insert(0, "0")  # Initialize the discount field with 0

# Total After Discount Label
lbl_after_discount = Label(f2, font=("arial", 15, 'bold'), text="Total:", width=18, fg="blue4", bg="lightyellow")
lbl_after_discount.place(x=0, y=200)

# Display Total After Discount
entry_after_discount = Entry(f2, font=("arial", 15, 'bold'), textvariable=Total_After_Discount, bd=6, width=15, bg="lightgreen")
entry_after_discount.place(x=160, y=200)

# Buttons
btn_reset = Button(f1, bd=5, fg="black", bg="lightblue", font=("arial", 16, 'bold'), width=10, text="Reset", command=Reset)
btn_reset.grid(row=8, column=0)

btn_total = Button(f1, bd=5, fg="black", bg="lightblue", font=("arial", 16, 'bold'), width=10, text='Total', command=Total)
btn_total.grid(row=9, column=1)

root.mainloop()
