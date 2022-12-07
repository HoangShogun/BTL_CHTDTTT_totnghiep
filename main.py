from tkinter import *
import thuat_toan

from PIL import ImageTk

# UI:
top = Tk()
top.geometry("400x340")

result=0
def getVal():
    global result
    danso = int(danso_entry.get())
    gdp = int(gdp_entry.get())
    ur = float(ur_entry.get())
    result = thuat_toan.thuattoan(danso, gdp, ur)
    ketqua.config(text="Ket qua: " + str(round(result,4)))


# def inra():

Label(top, text="Dân số: ").place(x=40, y=60)
Label(top, text="GDP: ").place(x=40, y=100)

Label(top, text="UR: ").place(x=40, y=140)
Button(top, text="Submit", command=getVal).place(x=40, y=170)
# Button(top, text="Submit", command=getVal).place(x=80, y=170)
danso_entry = Entry(top, width=30)
danso_entry.place(x=110, y=60)
gdp_entry = Entry(top, width=30)
gdp_entry.place(x=110, y=100)
ur_entry = Entry(top, width=30)
ur_entry.place(x=110, y=140)
ketqua=Label(top, text="Ket qua:")
ketqua.place(x=40, y=240)
# canvas= Canvas(top, width= 1100, height= 1100)
# canvas.pack()
# img= PhotoImage(file="Untitled.png")
# canvas.create_image(1,1,anchor=NW,image=img)

#

top.mainloop()
