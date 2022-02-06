import time
import threading
from tkinter import *


class GameOfLife(Tk):

    def __init__(self):
        super().__init__()
        self.title("jeu de la vie")
        self.geometry("1200x1000")
        self.configure(bg="grey")
        self.resizable(False, False)
        self.grid = []
        self.blacks = []
        self.add_buttons = []
        self.del_buttons = []
        self.play = False

        options = Frame(self)
        options.pack(side=LEFT)

        self.counter = Label(options, text="loop: 0")
        self.counter.pack()

        launch = Button(options, text="launch")
        launch.configure(command=lambda: self.launch())
        launch.pack()

        reset = Button(options, text="reset")
        reset.configure(command=lambda: self.reset())
        reset.pack()

        frame = Frame(self)
        frame.place(rely=0.5, relx=0.5, anchor=CENTER)

        for i in range(70):
            row = []
            for x in range(70):
                image = PhotoImage(file="./img/case.png")
                lbl = Label(image=image)
                lbl.image = image
                button = Button(frame, background="white", image=image, command=lambda r=i, c=x: self.select(r, c))
                button.grid(row=i, column=x)
                row.append(button)
            self.grid.append(row)

        self.mainloop()

    def get_black_near_count(self, row, column):
        count = 0
        r = row - 1
        while r <= (row + 1):
            c = column - 1
            while c <= (column + 1):
                if not (row == r and c == column):
                    if r <= 69 and c <= 69:
                        button = self.grid[r][c]
                        if button.cget("bg") == "black":
                            count += 1
                c += 1
            r += 1
        return count

    def reset(self):
        for button in self.blacks:
            button.configure(bg="white")
        self.blacks.clear()
        self.counter.configure(text=f"loop: 0")

    def launch(self):
        count = self.counter.cget("text").split(" ")[1]
        self.counter.configure(text=f"loop: {int(count) + 1}")
        for row in range(70):
            for column in range(70):
                button = self.grid[row][column]
                if button.cget("bg") == "black":
                    count = self.get_black_near_count(row, column)
                    if count != 2 and count != 3:
                        self.del_buttons.append(button)
                else:
                    count = self.get_black_near_count(row, column)
                    if count == 3:
                        self.add_buttons.append(button)
        for button in self.add_buttons:
            button.configure(bg="black")
            if not self.blacks.__contains__(button):
                self.blacks.append(button)
        self.add_buttons.clear()
        for button in self.del_buttons:
            button.configure(bg="white")
            if self.blacks.__contains__(button):
                self.blacks.remove(button)
        self.del_buttons.clear()

    def select(self, row, column):
        button = self.grid[row][column]
        if button.cget("bg") == "white":
            button.configure(bg="black")
            if not self.blacks.__contains__(button):
                self.blacks.append(button)
        else:
            button.configure(bg="white")
            if self.blacks.__contains__(button):
                self.blacks.remove(button)


GameOfLife()
