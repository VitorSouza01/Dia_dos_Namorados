# Import da Pergunta
import tkinter as tk
from tkinter import *
import random
from tkinter import messagebox

# Import do Coração
import turtle


# Código da Pergunta
while True:
    root = tk.Tk()
    root.title("Presente")
    root.geometry("600x600")
    root.configure(background="#ffc8dd")


    def move_button_1(e):
        if abs(e.x - button_1.winfo_x()) < 50 and abs(e.y - button_1.winfo_y()) < 40:
            x = random.randint(0, root.winfo_width() - button_1.winfo_width())
            y = random.randint(0, root.winfo_width() - button_1.winfo_width())
        button_1.place(x=x, y=y)


    def accepted():
        messagebox.showinfo(
            "Te amo", "Meu Amor, eu também te amo muito muito muito!❤")


    def denied():
        button_1.destroy()


    margin = Canvas(root, width=500, bg="#ffc8dd", height=100,
                    bd=0, highlightthickness=0, relief="ridge")
    margin.pack()
    text_id = Label(root, bg="#ffc8dd", text="Você me ama?",
                    fg="#590d22", font=("Montserrat", 24, "bold"))
    text_id.pack()
    button_1 = tk.Button(root, text="Não", bg="#ffb3c1", command=denied,
                         relief=RIDGE, bd=3, font=("Montserrat", 12, "bold"))
    button_1.pack()
    root.bind("<Motion>", move_button_1)
    button_2 = tk.Button(root, text="Sim", bg="#ffb3c1", relief=RIDGE,
                         bd=3, command=accepted, font=("Montserrat", 12, "bold"))
    button_2.pack()

    root.mainloop()
    break

# Código do Coração
while True:
    window = turtle.Screen()
    window.bgcolor("#ffc8dd")
    window.title("Presente")

    pen = turtle.Turtle()
    pen.color("red")
    pen.fillcolor("red")
    pen.pensize(3)
    pen.speed(7)

    pen.begin_fill()
    pen.left(140)
    pen.forward(224)
    for _ in range(200):
        pen.right(1)
        pen.forward(2)
    pen.left(120)
    for _ in range(200):
        pen.right(1)
        pen.forward(2)
    pen.forward(224)
    pen.end_fill()

    pen.up()
    pen.goto(0, -70)
    pen.down()
    pen.color("black")
    pen.write("Feliz Dia Dos Namorados Meu Amor!",
              align="center", font=("Arial", 16, "bold"))

    pen.hideturtle()

    turtle.done()
    break
