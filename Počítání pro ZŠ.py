"""Navrhněte a vytvořte aplikaci pro testování žáků prvního stupně ZŠ. Aplikace bude generovat příklady na sčítání,
odčítání násobení a dělení (bezezbytku) do sta. Uživatel si volí, které matematické operace chce cvičit.
Např. jen sčítání a dělení. Uživateli je také vypsána statistika úspěšnosti.
http://hroch.spseol.cz/~nozka/python/priklad_pocitaniZS/
"""

from tkinter import *
import random


class App:
    def __init__(self, master):
        frame = Frame(master)
        frame1 = Frame(frame)
        frame2 = Frame(frame)
        frame3 = Frame(frame)

        frame1.pack()
        frame2.pack()
        frame3.pack()
        frame.pack()

        self.dobre = 0
        self.celkem = -1

        title_label = Label(frame1, text="Operace")
        self.operace_entry = Entry(frame1, width=8)
        self.operace_entry.insert(0, '+-*/')
        self.a_entry = Entry(frame2, width=4)
        self.operace_label = Label(frame2, text="-")
        self.b_entry = Entry(frame2, width=4)
        vysledek_label = Label(frame2, text="=")
        self.c_entry = Entry(frame2, width=4)
        kontorla_button = Button(frame3, text="Zkontrolovat", command=self.kontrola)
        self.kontrola_label = Label(frame3, text="0/0")

        title_label.pack(side=LEFT)
        self.operace_entry.pack(side=LEFT)
        self.a_entry.pack(side=LEFT)
        self.operace_label.pack(side=LEFT)
        self.b_entry.pack(side=LEFT)
        vysledek_label.pack(side=LEFT)
        self.c_entry.pack(side=LEFT)
        kontorla_button.pack(side=LEFT)
        self.kontrola_label.pack(side=LEFT)
        self.novy_priklad()

    def novy_priklad(self):
        self.akce = self.operace_entry.get()
        operace = ""
        self.celkem += 1

        for i in self.akce:
            if i in "+-*/":
                operace += i

        self.akce = operace[random.randint(0, len(operace)-1)]
        self.operace_entry.delete(0, END)
        self.operace_entry.insert(0, operace)
        self.a_entry.config(state=NORMAL)
        self.b_entry.config(state=NORMAL)
        self.a_entry.delete(0, END)
        self.b_entry.delete(0, END)
        self.c_entry.delete(0, END)

        if self.akce == "+":
            self.akce = 0
            self.operace_label.config(text="+")
            self.a_entry.insert(0, random.randint(1, 100))
            self.b_entry.insert(0, random.randint(1, 101 - int(self.a_entry.get())))
        elif self.akce == "-":
            self.akce = 1
            self.operace_label.config(text="-")
            self.a_entry.insert(0, random.randint(1, 100))
            self.b_entry.insert(0, random.randint(1, int(self.a_entry.get())-1))
        elif self.akce == "*":
            self.akce = 2
            self.operace_label.config(text="*")
            self.a_entry.insert(0, random.randint(1, 10))
            self.b_entry.insert(0, random.randint(1, 10))
            pass
        elif self.akce == "/":
            self.akce = 3
            self.operace_label.config(text="/")
            b = random.randint(1, 20)
            self.b_entry.insert(0, b)
            while True:
                a = random.randint(1, 100)
                if a % b == 0:
                    self.a_entry.insert(0, a)
                    break
        self.a_entry.config(state=DISABLED)
        self.b_entry.config(state=DISABLED)

    def kontrola(self):
        if len(self.c_entry.get()) != 0:
            try:
                if self.akce == 0:
                    if int(self.a_entry.get()) + int(self.b_entry.get()) == int(self.c_entry.get()):
                        self.dobre += 1
                elif self.akce == 1:
                    if int(self.a_entry.get()) - int(self.b_entry.get()) == int(self.c_entry.get()):
                        self.dobre += 1
                elif self.akce == 2:
                    if int(self.a_entry.get()) * int(self.b_entry.get()) == int(self.c_entry.get()):
                        self.dobre += 1
                elif self.akce == 3:
                    if int(self.a_entry.get()) / int(self.b_entry.get()) == int(self.c_entry.get()):
                        self.dobre += 1
                self.novy_priklad()
                self.kontrola_label.config(text=(self.dobre, "/", self.celkem))
            except ValueError:
                pass

if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()
