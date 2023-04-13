from tkinter import *
from tkinter.messagebox import askyesno
from threading import Timer


def func(event):
    global current, blocked, pairs
    btn = event.widget
    if blocked:
        return
    if btn["text"] != " ":
        return
    if current:
        btn.configure(text=btn.v)
        if current["text"] == btn["text"]:
            pairs -= 1
            current = None
            if pairs == 0:
               end_game()
        else:
            blocked = True
            t = Timer(2, lambda: hide_buttons(current, btn))
            t.start()
    else:
        btn.configure(text=btn.v)
        current = btn


def end_game():
    gamer_over = askyesno(title="Конец игры",
                 message="Поздровляем, вы победили. Хотите сыграть ещё?")
    if gamer_over:
        clear_field()
    else:
        window.destroy()


def clear_field():
    global current, blocked, pairs
    current, blocked, pairs = None, False, n * m // 2
    for mas in bs:
        for button in mas:
            button.configure(text=" ")


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
n, m = 2, 3  # чтобы игра работала, хотя бы одно число должно быть чётным
pairs = n * m // 2
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
