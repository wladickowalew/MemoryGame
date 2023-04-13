import random
from tkinter import *
from tkinter.messagebox import askyesno
from threading import Timer
from consts import *


def button_click(event):
    global current, blocked, pairs
    btn = event.widget
    if blocked:
        return
    if btn["text"] != DEFAULT_CELL_VALUE:
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
            t = Timer(TIMER_DELAY, lambda: hide_buttons(current, btn))
            t.start()
    else:
        btn.configure(text=btn.v)
        current = btn


def end_game():
    gamer_over = askyesno(title=END_WINDOW_TITLE, message=END_WINDOW_MESSAGE)
    if gamer_over:
        clear_field()
    else:
        window.destroy()


def clear_field():
    global current, blocked, pairs, v
    current, blocked, pairs = None, False, FIELD_ROW * FIELD_COLUMN // 2
    v = create_field(FIELD_ROW, FIELD_COLUMN)
    for i in range(FIELD_ROW):
        for j in range(FIELD_COLUMN):
            bs[i][j].v = v[i][j]
            bs[i][j].configure(text=DEFAULT_CELL_VALUE)


def hide_buttons(btn1, btn2):
    global current, blocked
    btn1.configure(text=DEFAULT_CELL_VALUE)
    btn2.configure(text=DEFAULT_CELL_VALUE)
    current = None
    blocked = False


def create_field():
    pairs = random.sample(ALPHA, FIELD_ROW * FIELD_COLUMN // 2)
    pairs += pairs
    random.shuffle(pairs)
    v = []
    for i in range(FIELD_ROW):
        mas = [pairs[i * FIELD_COLUMN + j] for j in range(FIELD_COLUMN)]
        v.append(mas)
    return v


window = Tk()
window.title(WINDOW_TITLE)
fw = CELL_WIDTH * FIELD_COLUMN + (FIELD_COLUMN + 1) * PADDING  # ширина окна
fh = CELL_HEIGHT * FIELD_ROW + (FIELD_ROW + 1) * PADDING  # высота окна
window.geometry(f"{fw}x{fh}")

pairs = FIELD_ROW * FIELD_COLUMN // 2
current, blocked = None, False
bs, v = [], create_field()
for i in range(FIELD_ROW):
    row = []
    for j in range(FIELD_COLUMN):
        btn = Button(window, text=DEFAULT_CELL_VALUE, font=CELL_FONT)
        btn.place(x=PADDING * (j + 1) + CELL_WIDTH * j,
                  y=PADDING * (i + 1) + CELL_HEIGHT * i,
                  width=CELL_WIDTH, height=CELL_HEIGHT)
        btn.bind("<Button-1>", button_click)
        btn.v = v[i][j]
        row.append(btn)
    bs.append(row)

window.mainloop()
