from tkinter import *
import thuat_toan

from PIL import ImageTk

# UI:
top = Tk()
top.geometry("360x340")
top.title("BTL")

result=0
def getVal():
    global result
    danso = int(danso_entry.get())
    gdp = int(gdp_entry.get())
    ur = float(ur_entry.get())
    result = thuat_toan.thuattoan(danso, gdp, ur)
    ketqua.config(text="Kết quả: " + str(round(result,4)))
    pd=""
    if result<3:
        pd="Kém Phát Triển"
    elif result<7:
        pd="Phát Triển"
    else:
        pd="Phát Triển Nhanh"
    phandoan.config(text="Đây là một quốc gia " +pd)


# def inra():

Label(top, text="Dân số: ").place(x=40, y=60)
Label(top, text="GDP: ").place(x=40, y=100)
Label(top, text="(triệu Đô)").place(x=240, y=100)
Label(top, text="(triệu dân)").place(x=240, y=60)
Label(top, text="UR: ").place(x=40, y=140)
Label(top, text="(%)").place(x=240, y=140)
Button(top, text="Submit", command=getVal).place(x=40, y=170)
# Button(top, text="Submit", command=getVal).place(x=80, y=170)
danso_entry = Entry(top, width=20)
danso_entry.focus()
danso_entry.place(x=110, y=60)
gdp_entry = Entry(top, width=20)
gdp_entry.place(x=110, y=100)
ur_entry = Entry(top, width=20)
ur_entry.place(x=110, y=140)
ketqua=Label(top, text="Kết quả:")
ketqua.place(x=40, y=240)
phandoan=Label(top, text="")
phandoan.place(x=40, y=260)
# canvas= Canvas(top, width= 300, height= 300)
# img= PhotoImage(file="R.png")
# canvas.create_image(270,10,image=img)

#

top.mainloop()
