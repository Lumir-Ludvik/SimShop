# SimShop copyright Radek Simkanič
from tkinter import *
from tkinter import font as tkFont
from PIL import ImageTk, Image
from math import *


class Util:

    def __init__(self, root):
        self._root = root

    def forget(self):
        for frame in self._root.grid_slaves():
            frame.grid_forget()
        for frame in self._root.pack_slaves():
            frame.pack_forget()
    
    def addWeight(self, frame, rowRange, columnRange, weight):
        for r in range(rowRange):
            Grid.rowconfigure(frame, r, weight=weight)
        for c in range(columnRange):
            Grid.columnconfigure(frame, c, weight=weight)
    
    def createButton(self, frame, text, command, side, anchor):
        button = Button(frame, text=text, command=command)
        button.pack(side=side, anchor=anchor)

    def findDuplicity(self, collection, item):
        length = len(collection)
        found = False
        for index in range(length):
            if collection[index][0] == item[0]:
                collection[index][1] += 1
                found = True
        if not found:
            collection.append([item[0], 1, item[2]])
    
    def createGridLabel(self, frame, text, row, column, sticky, padx):
        label = Label(frame, text=text)
        label.grid(row=row, column=column, sticky=sticky, padx=padx)
    
    def createPackLabel(self, frame, text, side, anchor):
        label = Label(frame, text=text)
        label.pack(side=side, anchor=anchor)
    
    def createImage(self, frame, path, sizeX, sizeY, side, anchor):
        image = Image.open(path)
        image = image.resize((sizeX, sizeY), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(image)
        panel = Label(frame, image=img)
        panel.image = img
        panel.pack(side=side, anchor=anchor)
    
    def createGridButton(self, frame, text, command, row, column, padx):
        button = Button(self._root, text=text, command=command)
        button.grid(row=row, column=column, padx=padx)



class MainPage:

    selectedCat = 0
    shoppingCart = []

    listDict = {
        0: "Ovoce & zelenina",
        1: "Maso!",
        2: "Trvanlivé potraviny",
        3: "Napoje",
        4: "Lekarna & drogerie",
        5: "Specialni nabidky"
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
        0: ("Simeros", "images/06/simeros.png", 69.69),
        1: ("Simeros", "images/06/simeros.png", 69.69),
        2: ("Simeros", "images/06/simeros.png", 69.69),
        3: ("Simeros", "images/06/simeros.png", 69.69),
        4: ("Simeros", "images/06/simeros.png", 69.69),
        5: ("Simeros", "images/06/simeros.png", 69.69)
    }

    def __init__(self, root):
        self._root = root
        self.util = Util(root)
        self._root.title("SimShop")
        self.initHomePage()

    def initHomePage(self):
        self._createMenuBar()
        self.util.createGridLabel(self._root, "Kategorie:", 0, 0, N+W, 30)
        self._createSelectedCatLabel()
        self._createSelectedCatLabel()
        self._createListBox()
        self._createItemsGrid()

    def _onAboutClick(self):
        self.util.forget()
        About(self._root)

    def _onShoppingCartClick(self):
        self.util.forget()
        ShoppingCart(self._root, self.shoppingCart)

    def _currentItemSelected(self, event):
        widget = event.widget
        index = int(widget.curselection()[0])

        self.selectedCat = index
        self._forgetGrid()
        self._createItemsGrid()

    def _createMenuBar(self):
        self._menuBar = Menu(self._root)
        self._menuBar.add_command(
            label="O SimShop", command=self._onAboutClick)
        self._menuBar.add_command(
            label="Nakupni kosik", command=self._onShoppingCartClick)
        self._root.config(menu=self._menuBar)

    def _createListBox(self):
        self._listBox = Listbox(self._root, height=6)
        for key, value in self.listDict.items():
            self._listBox.insert(key, value)
        self._listBox.grid(row=1, column=0, sticky=N+W)
        self._listBox.bind('<<ListboxSelect>>', self._currentItemSelected)

    def _createItemsGrid(self):
        cat = [self.listVegetables, self.listMeat, self.listDurable,
               self.listDrinks, self.listDrugstore, self.listSpecial]
        index = 0

        for r in range(2):
            for c in range(3):
                dictionary = cat[self.selectedCat][index]
                text = dictionary[0]
                path = dictionary[1]
                price = dictionary[2]

                frame = Frame(self._root)
                frame.grid(row=r + 1, column=c + 1, padx=30, pady=30, sticky=W+E+N+S)

                Grid.rowconfigure(self._root, r + 1, weight=1)
                Grid.columnconfigure(self._root, c + 1, weight=1)

                self._createAddButton(frame, dictionary)
                self._createLabels(frame, text, price)
                self.util.createImage(frame, path, 180, 180, TOP, N)
                index += 1

    def _forgetGrid(self):
        for frame in self._root.grid_slaves():
            if int(frame.grid_info()["column"]) > 1:
                frame.grid_forget()

    def _createLabels(self, frame, name, price):
        self.util.createPackLabel(frame, name, LEFT, NW)
        self.util.createPackLabel(frame, "Cena: " + str(price), BOTTOM, SW)

    def _createAddButton(self, frame, item):
        self.util.createButton(frame, "+", lambda: self._addItemToShoppingCart(item), RIGHT, NE)

    def _createSelectedCatLabel(self):
        self._categoryLabel = Label(
            self._root, text=self.listDict[self.selectedCat])
        self._categoryLabel.grid(row=0, column=1, sticky=N+W, padx=30)

    def _overriteCatLabel(self):
        self._categoryLabel.config(text=self.listDict[self.selectedCat])

    def _addItemToShoppingCart(self, item):
        self.util.findDuplicity(self.shoppingCart, item)



class About():

    def __init__(self, root):
        self._root = root
        self.util = Util(root)
        self._createAboutPage()

    def _createAboutPage(self):
        aboutText = "Vitejte v SimShop!\n\nNakupujte pouze cerstvo a prirodni potraviny.\nNase sluzby jsou tu vzdy pro vas.\nRychlost je nase druhe jmeno"

        self.util.createImage(self._root, "images/about.png", 200, 200, TOP, NW)
        self.util.createPackLabel(self._root, aboutText, TOP, N)
        self.util.createButton(self._root, "Hlavni stranka", self._returnToIndex, BOTTOM, SW)

    def _returnToIndex(self):
        self.util.forget()
        MainPage(self._root)


class ShoppingCart():

    def __init__(self, root, shoppingCart):
        self._root = root
        self.util = Util(root)
        self.shoppingCart = shoppingCart
        self._createShoppingCart()

    def _createShoppingCart(self):
        #self._createProgressLabel()
        self._createItemList()
        self._createButtons()
        self.util.addWeight(self._root, 2, 2, 1)

    def _createProgressLabel(self):
        self.util.createGridLabel(self._root, "Nakupni kosik", 0, 0, W+E, 30)
        self.util.createGridLabel(self._root, "Doprava & platba", 0, 1, W+E, 30)
        self.util.createGridLabel(self._root, "Dodaci adresa", 0, 2, W+E, 0)


    def _createItemList(self):
        listbox = Listbox(self._root)
        for index in range(len(self.shoppingCart)):
            name = str(self.shoppingCart[index][0])
            count = "\t\t Kusu: " + str(self.shoppingCart[index][1])
            price = " Cena: " + str(self.shoppingCart[index][1] * self.shoppingCart[index][2])
            value = name + count + price
            listbox.insert(index, value)
        listbox.grid(row=1, column=0, columnspan=3, sticky=W+E+N+S)

    def _createButtons(self):
        self.util.createGridButton(self._root, "Hlavni stranka", self._returnToIndex, 2, 0, 30)
        self.util.createGridButton(self._root, "Doprava & platba", self._goToShipment, 2, 2, 30)

    def _returnToIndex(self):
        self.util.forget()
        MainPage(self._root)

    def _goToShipment(self):
        self.util.forget()
        Shipping(self._root, self.shoppingCart)


class Shipping():

    shippmentDict = {
        0: ("Posta", "150"),
        1: ("Riksa", "100"),
        2: ("Osel", "90"),
        3: ("Ja si to odnesu sam", "80"),
        4: ("Pirtskou lodi az domu", "70"),
        5: ("Ponorkou vnitrostatne", "60"),
        6: ("Dronem z lega", "50"),
        7: ("Poslu v lahvi ze sve piratske lodi", "40")
    }

    paymentDict = {
        0: "Daruji penize",
        1: "Daruji kartu",
        2: "Exekuce majetku",
        3: "Odsedim si to v lochu!",
        4: "Uver na SimBance",
        5: "SimCoin (sance na slevu)",
        6: "Daruji dceru pro dobrou vec"
    }

    def __init__(self, root, shoppingCart):
        self._root = root
        self.util = Util(root)
        self.shoppingCart = shoppingCart
        self._createShipping()

    def _createShipping(self):
        shippingFrame = Frame(self._root)
        paymentFrame = Frame(self._root)
        # shippingFrame.grid(row=0, column=0, padx=30, sticky=S+N)
        # paymentFrame.grid(row=0, column=1, sticky=S+N)
        self.util.createPackLabel(self._root, "Doprava", TOP, NW)
        shippingFrame.pack(side=TOP, anchor=NW, fill=X)
        self.util.createPackLabel(self._root, "Platba", TOP, NE)
        paymentFrame.pack(side=TOP, anchor=NE, fill=X)
        self.util.addWeight(self._root, 0, 1, 1)
        self._addShipping(shippingFrame)
        self._addPayment(paymentFrame)
        self.util.createButton(self._root, "Zpet", self._returnToShoppingCart, LEFT, SW)
        self.util.createButton(self._root, "Dodaci informace", self._goToAddress, RIGHT, SE)


    def _addShipping(self, frame):
        for item in self.shippmentDict.values():
            shippment = IntVar()
            text = item[0] + " Cena: " + item[1]
            checkBox = Checkbutton(frame, text=text, variable=shippment)
            checkBox.pack(side=TOP, anchor=W)

    def _addPayment(self, frame):
        for item in self.paymentDict.values():
            shippment = IntVar()
            checkBox = Checkbutton(frame, text=item, variable=shippment)
            checkBox.pack(side=TOP, anchor=W)        

    def _returnToShoppingCart(self):
        self.util.forget()
        ShoppingCart(self._root, self.shoppingCart)

    def _goToAddress(self):
        self.util.forget()
        Address(self._root, self.shoppingCart)


class Address():

    addressDict = {
        0: "Ulice:",
        1: "Mesto:",
        2: "PSC:",
        3: "Jmeno:",
        4: "Prijmeni:"
    }

    def __init__(self, root, shoppingCart):
        self._root = root
        self.util = Util(root)
        self.shoppingCart = shoppingCart
        self._createAddress()

    def _createAddress(self):
        for item in self.addressDict.values():
            self.util.createPackLabel(self._root, item, TOP, W)
            self._createEntry()
        self.util.createButton(self._root, "Zpet", self._returnToShippment, LEFT, SW)
        self.util.createButton(self._root, "Objednat", self._submit, RIGHT, SE)


    def _createLabel(self, text):
        label = Label(self._root, text=text)
        label.pack(side=TOP, anchor=W)
    
    def _createEntry(self):
        entry = Entry(self._root)
        entry.pack(side=TOP, anchor=W)
    
    def _returnToShippment(self):
        self.util.forget()
        Shipping(self._root, self.shoppingCart)

    def _submit(self):
        self.util.forget()
        self.util.createPackLabel(self._root, "Objednano!", TOP, W)
        self.util.createButton(self._root, "Hlavni stranka", self._returnToHome, LEFT, SW)
    
    def _returnToHome(self):
        self.util.forget()
        MainPage(self._root)


def main():
    root = Tk()
    app = MainPage(root)
    root.mainloop()
    root.destroy()


main()
