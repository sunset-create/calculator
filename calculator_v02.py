import tkinter

def btn_click():
    num = int(txt.get())
    num2 = int(txt2.get())
    global n1, n2
    n1 = num
    n2 = num2
    root.destroy()

def btn_click2():
    root.destroy()

root = tkinter.Tk()

root.geometry('1000x400')

root.title('計算機')

lbl = tkinter.Label(text='計算する値を入力してください')
lbl.place(x=10, y=30)

lbl = tkinter.Label(text='A')
lbl.place(x=30, y=70)

txt = tkinter.Entry(width=50)
txt.place(x=90, y=70)

lbl2 = tkinter.Label(text='B')
lbl2.place(x=30, y=110)

txt2 = tkinter.Entry(width=50)
txt2.place(x=90, y=110)

btn = tkinter.Button(root, text='計算', command=btn_click)
btn.place(x=140, y=170)

root.mainloop()

root = tkinter.Tk()
root.geometry('200x400')

lbl = tkinter.Label(text='入力された値は A= ' + str(n1) + ', B =' + str(n2) + ' です')
lbl.place(x=10, y=10)

lbl = tkinter.Label(text='A + B = ' + str(n1 + n2) + ' です')
lbl.place(x=10, y=40)

lbl = tkinter.Label(text='A - B = ' + str(n1 - n2) + ' です')
lbl.place(x=10, y=60)

lbl = tkinter.Label(text='A * B = ' + str(n1 * n2) + ' です')
lbl.place(x=10, y=80)

lbl = tkinter.Label(text='A / B = ' + str(n1 / n2) + ' です')
lbl.place(x=10, y=100)

lbl = tkinter.Label(text='A % B = ' + str(n1 % n2) + ' です')
lbl.place(x=10, y=120)

btn = tkinter.Button(root, text='終了', command=btn_click2)
btn.place(x=40, y=150)

root.mainloop()