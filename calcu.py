import tkinter as tk
from tkinter import Button,font
root=tk.Tk()
root.title("Project Calc")
b=font.Font(family="Aerial",size=14)
# Makes all 4 columns grow equally
for i in range(4):
    root.columnconfigure(i, weight=1)

# Makes all 6 rows (0,sticky="nswe" to 5) grow equally
for i in range(6):
    root.rowconfigure(i, weight=1)

#clear button
def del_all():
    entry1.delete(0,"end")
def clear():
    ind=entry1.index(tk.INSERT)
    if ind>0:
        entry1.delete(ind-1)
#enter button
def equal():
    expression=entry1.get()
    result=eval(expression)
    entry1.delete(0,"end")
    entry1.insert(0,str(result))
#screen showing numbers
entry1=tk.Entry(root,font=b)
entry1.grid(row=0,sticky="nswe",column=0,columnspan=4,)
#buttons
B1=tk.Button(root,text="   1     ",font=b,command=lambda:entry1.insert("end",1))
B1.grid(row=1,column=0,sticky="nswe")
B2=tk.Button(root,text="   2     ",font=b,command=lambda:entry1.insert("end",2))
B2.grid(row=1,column=1,sticky="nswe")
B3=tk.Button(root,text="   3     ",font=b,command=lambda:entry1.insert("end",3))
B3.grid(row=1,column=2,sticky="nswe")
B4=tk.Button(root,text="   4     ",font=b,command=lambda:entry1.insert("end",4))
B4.grid(row=2,column=0,sticky="nswe")
B5=tk.Button(root,text="   5     ",font=b,command=lambda:entry1.insert("end",5))
B5.grid(row=2,column=1,sticky="nswe")
B6=tk.Button(root,text="   6     ",font=b,command=lambda:entry1.insert("end",6))
B6.grid(row=2,column=2,sticky="nswe")
B7=tk.Button(root,text="   7     ",font=b,command=lambda:entry1.insert("end",7))
B7.grid(row=3,column=0,sticky="nswe")
B8=tk.Button(root,text="   8     ",font=b,command=lambda:entry1.insert("end",8))
B8.grid(row=3,column=1,sticky="nswe")
B9=tk.Button(root,text="   9     ",font=b,command=lambda:entry1.insert("end",9))
B9.grid(row=3,column=2,sticky="nswe")
B0=tk.Button(root,text="   0     ",font=b,command=lambda:entry1.insert("end",0,sticky="nswe"))
B0.grid(row=4,column=1,sticky="nswe")
#clear
B_clear=tk.Button(root,text=" AC",font=b,command=del_all)
B_clear.grid(row=4,column=0,sticky="nswe")
B_sclear=tk.Button(root,text="clear",font=b,command=clear)
B_sclear.grid(row=4,column=2,sticky="nswe")
#operations
B_add=tk.Button(root,text="+",font=b,command=lambda:entry1.insert("end","+"))
B_add.grid(row=1,column=3,sticky="nswe")
B_sub=tk.Button(root,text="-",font=b,command=lambda:entry1.insert("end","-"))
B_sub.grid(row=2,column=3,sticky="nswe")
B_div=tk.Button(root,text="/",font=b,command=lambda:entry1.insert("end","/"))
B_div.grid(row=3,column=3,sticky="nswe")
B_mul=tk.Button(root,text="x",font=b,command=lambda:entry1.insert("end","*"))
B_mul.grid(row=4,column=3,sticky="nswe")
B_equal=tk.Button(root,text="=",font=b,command=equal)
B_equal.grid(row=5,column=3,sticky="nswe")
B_point=tk.Button(root,text=".",font=b,command=lambda:entry1.insert("end","."))
B_point.grid(row=5,column=0,sticky="nswe")
B_Fdiv=tk.Button(root,text="//",font=b,command=lambda:entry1.insert("end","//"))
B_Fdiv.grid(row=5,column=1,sticky="nswe")
B_mod=tk.Button(root,text="%",font=b,command=lambda:entry1.insert("end","%"))
B_mod.grid(row=5,column=2,sticky="nswe")
root.mainloop()