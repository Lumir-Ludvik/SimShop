# SimShop copyright Radek Simkanič
from tkinter import * 
from tkinter import font as tkFont
from math import *

class mainPage:

    listDict = {
        0: "Fruits & vegetables",
        1: "Meat",
        2: "Durable food",
        3: "Drinks",
        4: "Drugstore",
        5: "Special offers"
    }

    def __init__(self, root):
        self._root = root
        self._root.title("SimShop")
        self._createMenuBar()
        self._createListBox()

    def _onContactClick(self):
        pass 

    def _onAboutClick(self):
        pass

    def _onShoppingCartClick(self):
        pass
    
    def _createMenuBar(self):
        self._menuBar = Menu(self._root)
        self._menuBar.add_command(label="Contact", COMMAND=self._onContactClick())
        self._menuBar.add_command(label="About", COMMAND=self._onAboutClick())
        self._menuBar.add_command(label="ShoppingCart", COMMAND=self._onShoppingCartClick())
        self._root.config(menu=self._menuBar)
    
    def _createListBox(self):
        self._listBoxFrame = Frame(self._root)
        self._listBox = Listbox(self._root)
        for key, value in self.listDict.items():
            self._listBox.insert(key, value)
        self._listBox.pack(fill=Y, side=LEFT)




def main():
    root = Tk()
    app = mainPage(root)
    root.mainloop()
    root.destroy()

main()