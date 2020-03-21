# SimShop copyright Radek Simkanič
from tkinter import *
from tkinter import font as tkFont
from PIL import ImageTk, Image
from math import *


class mainPage:

    selectedCat = 0
    shoppingCart = []

    listDict = {
        0: "Fruits & vegetables",
        1: "Meat",
        2: "Durable food",
        3: "Drinks",
        4: "Drugstore",
        5: "Special offers"
    }

    listVegetables = {
        0: ("Jablko", "images/01/apple.png", 28.99),
        1: ("Banan", "images/01/banana.png", 24.99),
        2: ("Okurka", "images/01/cucumber.png", 15.99),
        3: ("Meloun", "images/01/melon.png", 9.50),
        4: ("Broskev", "images/01/peach.png", 53.89),
        5: ("Rajce", "images/01/tomato.png", 33.50)
    }

    listMeat = {
        0: ("Hovězí jazyk", "images/02/jazyk.png", 114.99),
        1: ("Veprova kotleta", "images/02/kotleta.png", 130),
        2: ("Kralik cely", "images/02/kralik.png", 150.50),
        3: ("Veprova krkovice", "images/02/krkovice.png", 104),
        4: ("Veprove droby", "images/02/srdce.png", 80.99),
        5: ("Veprovy bok", "images/02/bok.png", 98.50)
    }

    listDrinks = {
        0: ("Kofola", "images/03/kofola.png", 20.50),
        1: ("Pepsi", "images/03/pepsi.png", 20.99),
        2: ("Rajec", "images/03/rajec.png", 18.25),
        3: ("Jablecny juice", "images/03/relax.png", 25.99),
        4: ("Svijany", "images/03/svijany.png", 13),
        5: ("Russian standard", "images/03/vodka.png", 250)
    }

    listDurable = {
        0: ("Fazole", "images/04/fazole.png", 26.50),
        1: ("Krupice", "images/04/krupice.png", 20.99),
        2: ("Ryze", "images/04/ryze.png", 40.25),
        3: ("Spagety", "images/04/spaghet.png", 23.50),
        4: ("Mouka", "images/04/mouka.png", 9.89),
        5: ("Hrach", "images/04/hrach.png", 21.50)
    }

    listDrugstore = {
        0: ("Brufen 400", "images/05/brufen.png", 120.50),
        1: ("Gutalax", "images/05/gutalax.png", 150.50),
        2: ("Paracetamol", "images/05/paracentanol.png", 130),
        3: ("Simpers", "images/05/plenky.png", 350.89),
        4: ("Proenzi", "images/05/proenzi.png", 700.99),
        5: ("Nasivin", "images/05/nasivin.png", 200.25)
    }

    listSpecial = {
        0: ("Simeros", "images/06/simeros.png", 69.69)
    }

    def __init__(self, root):
        self._root = root
        self._root.title("SimShop")
        self.initHomePage()

    def initHomePage(self):
        self._createMenuBar()
        self._createCatLabel()
        self._createSelectedCatLabel()
        self._createSelectedCatLabel()
        self._createListBox()
        self._createItemsGrid()

    def _onContactClick(self):
        print("Contact")
        pass

    def _onAboutClick(self):
        print("About")
        pass

    def _onShoppingCartClick(self):
        print("SC")
        pass

    def _currentItemSelected(self, event):
        widget = event.widget
        index = int(widget.curselection()[0])
        self.selectedCat = index
        self._forgetGrid()
        self._createItemsGrid()

    def _createMenuBar(self):
        self._menuBar = Menu(self._root)
        self._menuBar.add_command(
            label="Contact", command=self._onContactClick)
        self._menuBar.add_command(label="About", command=self._onAboutClick)
        self._menuBar.add_command(
            label="ShoppingCart", command=self._onShoppingCartClick)
        self._root.config(menu=self._menuBar)

    def _createListBox(self):
        self._listBox = Listbox(self._root, height=6)
        for key, value in self.listDict.items():
            self._listBox.insert(key, value)
        self._listBox.grid(row=1, column=0, sticky=N+W)
        self._listBox.bind('<<ListboxSelect>>', self._currentItemSelected)

    def _createCatLabel(self):
        self._listBoxLabel = Label(self._root, text="Categories:")
        self._listBoxLabel.grid(row=0, column=0, sticky=N+W, padx=30)

    def _createItemsGrid(self):
        cat = [self.listVegetables, self.listMeat, self.listDurable,
               self.listDrinks, self.listDrugstore, self.listSpecial]
        index = 0

        for r in range(2):
            for c in range(3):
                frame = Frame(self._root)
                frame.grid(row = r + 1, column = c + 1, padx=30, pady=30, sticky=W+E+N+S)
                Grid.rowconfigure(self._root, r + 1 , weight=1)
                Grid.columnconfigure(self._root, c + 1, weight=1)
                self._createAddButton(frame, cat[self.selectedCat][index][0])
                self._createLabels(frame, cat[self.selectedCat][index][0], cat[self.selectedCat][index][2])
                self._createImage(frame, cat[self.selectedCat][index][1])
                index += 1

    def _forgetGrid(self):
        for frame in self._root.grid_slaves():
            if int(frame.grid_info()["column"]) > 1:
                frame.grid_forget()

    def _createLabels(self, frame, name, price):
        nameLabel = Label(frame, text=name)
        nameLabel.pack(side=LEFT, anchor=NW)
        priceLabel = Label(frame, text="Cena: " + str(price))
        priceLabel.pack(side=BOTTOM, anchor=SW)

    def _createAddButton(self, frame, item):
        button = Button(frame, text="+", command= lambda: self._addItemToShoppingCart(item))
        button.pack(side=RIGHT, anchor=NE)

    def _createImage(self, frame, path):
        image = Image.open(path)
        image = image.resize((180, 180), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(image)
        panel = Label(frame, image=img)
        panel.image = img
        panel.pack()

    def _createSelectedCatLabel(self):
        self._categoryLabel = Label(self._root, text=self.listDict[self.selectedCat])
        self._categoryLabel.grid(row=0, column=1, sticky=N+W, padx=30)

    def _overriteCatLabel(self):
        self._categoryLabel.config(text=self.listDict[self.selectedCat])

    def _addItemToShoppingCart(self, item):
        self.shoppingCart.append((item, 1))


def main():
    root = Tk()
    app = mainPage(root)
    root.mainloop()
    root.destroy()


main()
