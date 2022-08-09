from tkinter import *
from tkinter import messagebox

loc_final=['0','1','2','3','4']

top=Tk()
top.geometry("500x500")
top.title("House Price Predictor")

heading = Label(top,text="Housing Price Predictor", bg="blue",fg="white",font = ("Ariel",26)).grid(row=0, column=1)

vloc = StringVar(top)
vloc.set(loc_final[0])

vsqft = IntVar(top)
vbath = IntVar(top)
vbhk = IntVar(top)

loc = Label(top, text="Location", bg="light green").grid(row=1, column=0)
loc_ = OptionMenu(top, vloc, *loc_final).grid(row=1, column=1, ipadx="100")
  
sqft = Label(top, text="Area in square feet", bg="light green").grid(row=2, column=0)
sqft_ = Entry(top,textvariable = vsqft).grid(row=2, column=1, ipadx="100")
  
bath = Label(top, text="Number of bathrooms", bg="light green").grid(row=3, column=0)
bath_ = Entry(top,textvariable = vbath).grid(row=3, column=1, ipadx="100") 
  
bhk = Label(top, text="Number of bedrooms(BHK)", bg="light green").grid(row=4, column=0) 
bhk_ = Entry(top,textvariable = vbhk).grid(row=4, column=1, ipadx="100") 

    
def ok():
    s = vloc.get()
    ans = (float(vsqft.get())+int(vbath.get())+int(vbhk.get()))
    label = Label(top, text = "Predicted Price(in Lakhs): " + str(ans))
    label.grid(row=12,column=1)

submit = Button(top, text="Submit", fg="Black", bg="Red",command = ok) 
submit.grid(row=10, column=1)

top.mainloop()

