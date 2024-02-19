from tkinter import Tk,Label,Button,Entry,Frame,StringVar
r=Tk()
r.title("SIMPLE CALCULATOR")
r.geometry("400x390+30+30")
r.configure(bg="#17161b")
scvalue=StringVar(r,"")
screen=Entry(r,font="lucida 50 bold",textvariable=scvalue)
screen.pack()

f=Frame(r)
def button_click(number):
    if number=="C":
       screen.delete(0,"end")
    elif number=="=":
        try:
            expression = screen.get()
            result = eval(expression)
            screen.delete(0, "end")
            screen.insert("end", result)
        except Exception:
            screen.delete(0,"end")
            screen.insert("end","Error")
    else:
        current=screen.get()
        screen.delete(0,"end")
        screen.insert("end",current+str(number))

b1=Button(f,text="9",width=5,height=1,fg="#fff",bg="#2a2d36",font="lucida 20 bold",border=5,command=lambda: button_click(9))
b1.grid(row=1,column=2)

b2=Button(f,text="8",width=5,height=1,fg="#fff",bg="#2a2d36",font="lucida 20 bold",border=5,command=lambda: button_click(8))
b2.grid(row=1,column=1)

b3=Button(f,text="7",width=5,height=1,fg="#fff",bg="#2a2d36",font="lucida 20 bold",border=5,command=lambda: button_click(7))
b3.grid(row=1,column=0)

b4=Button(f,text="6",width=5,height=1,fg="#fff",bg="#2a2d36",font="lucida 20 bold",border=5,command=lambda: button_click(6))
b4.grid(row=2,column=2)

b5=Button(f,text="5",width=5,height=1,fg="#fff",bg="#2a2d36",font="lucida 20 bold",border=5,command=lambda: button_click(5))
b5.grid(row=2,column=1)

b6=Button(f,text="4",width=5,height=1,fg="#fff",bg="#2a2d36",font="lucida 20 bold",border=5,command=lambda: button_click(4))
b6.grid(row=2,column=0)

b7=Button(f,text="3",width=5,height=1,fg="#fff",bg="#2a2d36",font="lucida 20 bold",border=5,command=lambda: button_click(3))
b7.grid(row=3,column=2)

b8=Button(f,text="2",width=5,height=1,fg="#fff",bg="#2a2d36",font="lucida 20 bold",border=5,command=lambda: button_click(2))
b8.grid(row=3,column=1)

b9=Button(f,text="1",width=5,height=1,fg="#fff",bg="#2a2d36",font="lucida 20 bold",border=5,command=lambda: button_click(1))
b9.grid(row=3,column=0)

b10=Button(f,text="0",width=5,height=1,fg="#fff",bg="#2a2d36",font="lucida 20 bold",border=5,command=lambda: button_click(0))
b10.grid(row=4,column=0)


b11=Button(f,text=". ",width=5,height=1,fg="#fff",bg="#2a2d36",font="lucida 20 bold",border=5,command=lambda: button_click("."))
b11.grid(row=0,column=1)

b12=Button(f,text="+",width=5,height=1,fg="#fff",bg="#2a2d36",font="lucida 20 bold",border=5,command=lambda: button_click("+"))
b12.grid(row=2,column=3)

b13=Button(f,text="-",width=5,height=1,fg="#fff",bg="#2a2d36",font="lucida 20 bold",border=5,command=lambda: button_click("-"))
b13.grid(row=1,column=3)

b14=Button(f,text="*",width=5,height=1,fg="#fff",bg="#2a2d36",font="lucida 20 bold",border=5,command=lambda: button_click("*"))
b14.grid(row=0,column=3)

b15=Button(f,text="C",width=5,height=1,fg="#ED9121",bg="#007FFF",font="lucida 20 bold",border=5,command=lambda: button_click("C"))
b15.grid(row=0,column=0)

b16=Button(f,text="(",width=5,height=1,fg="#fff",bg="#2a2d36",font="lucida 20 bold",border=5,command=lambda: button_click("("))
b16.grid(row=4,column=1)

b17=Button(f,text=")",width=5,height=1,fg="#fff",bg="#2a2d36",font="lucida 20 bold",border=5,command=lambda: button_click(")"))
b17.grid(row=4,column=2)

b18=Button(f,text="/ ",width=5,height=1,fg="#fff",bg="#2a2d36",font="lucida 20 bold",border=5,command=lambda: button_click("/"))
b18.grid(row=0,column=2)

b19=Button(f,text="=",width=5,height=3,fg="#fff",bg="#FF7F24",font="lucida 20 bold",border=5,command=lambda: button_click("="))
b19.place(x=303,y=185)

f.pack()

r.mainloop()
