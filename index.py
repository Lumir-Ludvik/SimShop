# SimShop copyright Radek Simkanič
from tkinter import *
from tkinter import font as tkFont
from PIL import ImageTk, Image
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
        self.initHomePage()

    def initHomePage(self):
        self._createMenuBar()
        self._createCatLabel()
        self._createSelectedCatLabel()
        self._createListBox()
        self._createItemsGrid()

    def _onContactClick(self):
        pass 

    def _onAboutClick(self):
        pass

    def _onShoppingCartClick(self):
        pass

    def _currentItemSelected(self, event):
        widget = event.widget
        index = int(widget.curselection()[0])
        value = widget.get(index)
        self._owerriteCatLabel(value)

    def _createMenuBar(self):
        self._menuBar = Menu(self._root)
        self._menuBar.add_command(label="Contact", COMMAND=self._onContactClick())
        self._menuBar.add_command(label="About", COMMAND=self._onAboutClick())
        self._menuBar.add_command(label="ShoppingCart", COMMAND=self._onShoppingCartClick())
        self._root.config(menu=self._menuBar)
    
    def _createListBox(self):
        self._listBox = Listbox(self._root, height=6)
        for key, value in self.listDict.items():
            self._listBox.insert(key, value)
        self._listBox.bind('<<ListboxSelect>>', self._currentItemSelected)
        self._listBox.select_set(0)
        self._listBox.activate
        self._listBox.event_generate('<<ListboxSelect>>')
        self._listBox.grid(row=1, column=0, sticky=N+W)

    def _createCatLabel(self):
        self._listBoxLabel = Label(self._root, text="Categories:")
        self._listBoxLabel.grid(row=0, column=0, sticky=N+W, padx=30)

    def _createItemsGrid(self):
        frame1 = Frame(self._root, width=150, height= 150, background="Blue")
        frame1.grid(row=1, column=1, padx=30, sticky=W+E+N+S)
        nameLabel = Label(frame1, text='Name')
        nameLabel.pack(side=LEFT, anchor=NW)
        button = Button(frame1, text="+", command=self._addItemToShoppingCart)
        button.pack(side=RIGHT, anchor=NE)
        priceLabel = Label(frame1, text="price")
        priceLabel.pack(side=BOTTOM, anchor=SW)
        img = ImageTk.PhotoImage(Image.open("images/cry.png"))
        panel = Label(frame1, image=img)
        panel.image = img
        panel.pack()
    
    def _createSelectedCatLabel(self):
        self._categoryLabel = Label(self._root)
        self._categoryLabel.grid(row=0, column=1, sticky=N+W, padx=30)

    def _owerriteCatLabel(self, text):
        self._categoryLabel.config(text=text)

    def _addItemToShoppingCart(self):
        pass
        




def main():
    root = Tk()
    app = mainPage(root)
    root.mainloop()
    root.destroy()

main()
