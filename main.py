from tkinter import *
from tkinter.messagebox import askyesno
from threading import Timer


def func(event):
    global current, blocked
    if blocked:
        return
    btn = event.widget
    if current:
        btn.configure(text=btn.v)
        if current["text"] == btn["text"]:
            current = None
        else:
            blocked = True
            t = Timer(2, lambda: hide_buttons(current, btn))
            t.start()
    else:
        btn.configure(text=btn.v)
        current = btn


def hide_buttons(btn1, btn2):
    global current, blocked
    btn1.configure(text=" ")
    btn2.configure(text=" ")
    current = None
    blocked = False


# v = [["A", "B", "D", "G", "U", "F"],
#      ["Y", "H", "Q", "A", "E", "Y"],
#      ["C", "Q", "U", "R", "R", "C"],
#      ["F", "B", "E", "G", "H", "D"]]

v = [["A", "B", "C"], ["B", "C", "A"]]

window = Tk()
window.title("Память")
w, h, d = 50, 50, 15
n, m = 2, 3
fw = w * m + (m + 1) * d
fh = h * n + (n + 1) * d
window.geometry(f"{fw}x{fh}")
current = None
blocked = False
bs = []
step = 0
for i in range(n):
    row = []
    for j in range(m):
        btn = Button(window, text=" ",
                     font=("Arial Bold", 35))
        btn.place(x=d * (j + 1) + w * j,
                  y=d * (i + 1) + h * i,
                  width=w, height=h)
        btn.bind("<Button-1>", func)
        btn.v = v[i][j]
        row.append(btn)
    bs.append(row)

window.mainloop()
