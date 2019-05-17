from tkinter import *

def click(event):
    text=event.widget.cget("text")
    if text=="=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            try:
             value=eval(screen.get())
            except Exception as e:
                print(e)
                value="Error"

        scvalue.set(value)
        screen.update()
    elif text=="C":
        scvalue.set("")
        screen.update()
    else :
        scvalue.set(scvalue.get()+text)
        screen.update()


root=Tk()
root.geometry("360x710")
root.maxsize(360 , 710)
root.minsize(360, 710)
root.title("CALCULATOR")
root.wm_iconbitmap("1.ico")


scvalue=StringVar()
scvalue.set("")
screen=Entry(root,text=scvalue, font="courier 40 italic", relief=RIDGE)
screen.pack(fill=X, pady=10, padx=10, )

f = Frame(root, bg="lightslategray")
b = Button(f, text="9", padx=28, pady=18, font="courier 21 " )
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>",click)

b = Button(f, text="8", padx=28, pady=18, font="courier 21 ")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>",click)

b = Button(f, text="7", padx=28, pady=18, font="courier 21 ")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>",click)

f.pack(fill=BOTH)

f = Frame(root, bg="lightslategray")
b = Button(f, text="6", padx=28, pady=18, font="courier 21 ")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>",click)

b = Button(f, text="5", padx=28, pady=18, font="courier 21 ")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>",click)

b = Button(f, text="4", padx=28, pady=18, font="courier 21 ")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>",click)

f.pack(fill=BOTH)

f = Frame(root, bg="lightslategray")
b = Button(f, text="3", padx=28, pady=18, font="courier 21 ")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>",click)

b = Button(f, text="2", padx=28, pady=18, font="courier 21 ")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>",click)

b = Button(f, text="1", padx=28, pady=18, font="courier 21 ")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>",click)

f.pack(fill=BOTH)

f = Frame(root, bg="lightslategray")
b = Button(f, text="0", padx=28, pady=18, font="courier 21 ")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>",click)

b = Button(f, text="-", padx=28, pady=18, font="courier 21 ")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>",click)

b = Button(f, text="+", padx=28, pady=18, font="courier 21 ")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>",click)

f.pack(fill=BOTH)

f = Frame(root, bg="lightslategray")
b = Button(f, text="*", padx=28, pady=18, font="courier 21 ")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>",click)

b = Button(f, text="C", padx=28, pady=18, font="courier 21 ")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>",click)

b = Button(f, text="/", padx=28, pady=18, font="courier 21 ")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>",click)

f.pack(fill=BOTH)

f = Frame(root, bg="lightslategray")
b = Button(f, text=".", padx=28, pady=18, font="courier 21 ")
b.pack(side=LEFT, padx=11, pady=5)
b.bind("<Button-1>",click)

b = Button(f, text="=", padx=88, pady=18, font="courier 21 ")
b.pack(side=LEFT, padx=11, pady=5 )
b.bind("<Button-1>",click)



f.pack(fill=BOTH)



root.mainloop()
