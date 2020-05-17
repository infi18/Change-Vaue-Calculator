'''
The program below implements a coin value calculator that calculates values of Quarter, Nickel, Penny and Dime, dollar and half dollar
The program is implemented  using Tkinter module

Author : Siddhi Naik

'''

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#Initializing Tkinter
window=Tk()
window.title("Coins Value Calculator")
window.geometry('600x300')
window.configure(background="khaki")

#Lables and Text Boxes

h = Label(window, text="Enter the Coin values and hit compute:")
h.grid(row=0, column=3, pady=5)

dr = Label(window, text="Dollar", width=10)
dr.grid(row=1, column=0, pady=5)
dr1 = Entry(window, width=10, borderwidth=1, relief="solid")
dr1.insert(0, 0)
dr1.grid(row=1, column=1, padx=5, pady=5)
dr2 = Label(window, text="Dollar Value $:", width=15,)
dr2.grid(row=1, column=5, padx=5, pady=5)
dr3 = Label(window, text="0.00", width=10, borderwidth=1, relief="solid")
dr3.grid(row=1, column=6, padx=5, pady=5)

hd = Label(window, text="Half Dollar", width=10)
hd.grid(row=2, column=0, pady=5)
hd1 = Entry(window, width=10, borderwidth=1, relief="solid")
hd1.insert(0, 0)
hd1.grid(row=2, column=1, padx=5, pady=5)
hd2 = Label(window, text="Half Dollar Value $:", width=15,)
hd2.grid(row=2, column=5, padx=5, pady=5)
hd3 = Label(window, text="0.00", width=10, borderwidth=1, relief="solid")
hd3.grid(row=2, column=6, padx=5, pady=5)

q = Label(window, text="Quarter", width=10)
q.grid(row=3, column=0, pady=5)
q1 = Entry(window, width=10, borderwidth=1, relief="solid")
q1.insert(0, 0)
q1.grid(row=3, column=1, padx=5, pady=5)
q2 = Label(window, text="Quarter Value $:", width=15,)
q2.grid(row=3, column=5, padx=5, pady=5)
q3 = Label(window, text="0.00", width=10, borderwidth=1, relief="solid")
q3.grid(row=3, column=6, padx=5, pady=5)

d = Label(window, text="Dimes", width=10)
d.grid(row=4, column=0, padx=5, pady=5)
d1 = Entry(window, width=10, borderwidth=1, relief="solid")
d1.insert(0, 0)
d1.grid(row=4, column=1, padx=5, pady=5)
d2 = Label(window, text="Dime Value $:", width=15)
d2.grid(row=4, column=5, padx=5, pady=5)
d3 = Label(window, text="0.00", width=10, borderwidth=1, relief="solid")
d3.grid(row=4, column=6, padx=5, pady=5)

n = Label(window, text="Nickels", width=10)
n.grid(row=5, column=0, padx=5, pady=5)
n1 = Entry(window, width=10, borderwidth=1, relief="solid")
n1.insert(0, 0)
n1.grid(row=5, column=1, padx=5, pady=5)
n2 = Label(window, text="Nickel Value $:", width=15)
n2.grid(row=5, column=5, padx=5, pady=5)
n3 = Label(window, text="0.00", width=10, borderwidth=1, relief="solid")
n3.grid(row=5, column=6, padx=5, pady=5)

p = Label(window, text="Pennies", width=10)
p.grid(row=6, column=0, padx=5, pady=5)
p1 = Entry(window, width=10, borderwidth=1, relief="solid")
p1.insert(0, 0)
p1.grid(row=6, column=1, padx=5, pady=5)
p2 = Label(window, text="Penny Value $:", width=15)
p2.grid(row=6, column=5, padx=5, pady=5)
p3 = Label(window, text="0.00", width=10, borderwidth=1, relief="solid")
p3.grid(row=6, column=6, padx=5, pady=5)

total = Label(window, text="Total Money $:", width=15)
total.grid(row=7, column=5, padx=5, pady=5)
total_1 = Label(window, text="0.00", width=10, borderwidth=1, relief="solid")
total_1.grid(row=7, column=6, padx=5, pady=5)

# Resets all values back to zero
def clearAll():
    dr1.delete(0, END)
    dr1.insert(0, 0)
    hd1.delete(0, END)
    hd1.insert(0, 0)
    q1.delete(0, END)
    q1.insert(0, 0)
    d1.delete(0, END)
    d1.insert(0, 0)
    n1.delete(0, END)
    n1.insert(0, 0)
    p1.delete(0, END)
    p1.insert(0, 0)
    dr3.configure(text="0.00")
    hd3.configure(text="0.00")
    q3.config(text="0.00")
    d3.config(text="0.00")
    n3.config(text="0.00")
    p3.config(text="0.00")
    total_1.config(text="0.00")

# Calculates value of each coins entered and the total value of all of those
def coinCalculator():

    if (((dr1.get()).isdigit() == False) or ((hd1.get()).isdigit() == False) or
            ((q1.get()).isdigit() == False) or ((d1.get()).isdigit() == False) or
            ((n1.get()).isdigit() == False) or ((p1.get()).isdigit() == False)):
        messagebox.showwarning("Warning", "Please Enter Appropriate Value !")
    else:
        dollarValue = float(dr1.get()) * (100 / 100)
        halfDollarValue = float(hd1.get()) * (50 / 100)
        quarterValue = float(q1.get()) * (25/100)
        dimeValue = float(d1.get()) * (10/100)
        nickelValue = float(n1.get()) * (5/100)
        pennyValue = float(p1.get()) * (1/100)
        totalValue = "%.2f" %(dollarValue + halfDollarValue + quarterValue + dimeValue + nickelValue + pennyValue)

        dr3.configure(text="%.2f" % dollarValue)
        hd3.configure(text="%.2f" % halfDollarValue)
        q3.configure(text="%.2f" %quarterValue)
        d3.configure(text="%.2f" %dimeValue)
        n3.configure(text="%.2f" %nickelValue)
        p3.configure(text="%.2f" %pennyValue)
        total_1.configure(text=totalValue)


# Reset Button
btn = ttk.Button(window, text="Reset Values", command=clearAll)
btn.grid(row=10, column=6, padx=5)

# Compute Button
btn = ttk.Button(window, text="Compute", command=coinCalculator)
btn.grid(row=10, column=0, padx=5)

#Start
window.mainloop()
