# SimShop copyright Radek Simkanič
from tkinter import * 
from tkinter import font as tkFont
from math import *

class mainPage:
    def __init__(self, root):
        self._root = root
        self._root.title("SimShop")
        _createMenuBar()

    def _createMenuBar(self):
        self._menuBarFrame = Frame(self._root,)
        self._menuBarFrame.pack(fill=X, expand=1, padx=4, pady=4)

def main():
    root = Tk()
    app = mainPage(root)
    root.mainloop()
    root.destroy()

main()