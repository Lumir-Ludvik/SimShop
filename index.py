# SimShop copyright Radek Simkanič
from tkinter import *
from tkinter import font as tkFont
from PIL import ImageTk, Image
from math import *


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
        self._root.title("SimShop")
        self.initHomePage()

    def initHomePage(self):
        self._createMenuBar()
        self._createCatLabel()
        self._createSelectedCatLabel()
        self._createSelectedCatLabel()
        self._createListBox()
        self._createItemsGrid()

    def _onAboutClick(self):
        self._deletePage()
        About(self._root)

    def _onShoppingCartClick(self):
        self._deletePage()
        ShoppingCart(self._root, self.shoppingCart)

    def _deletePage(self):
        for frame in self._root.grid_slaves():
            frame.grid_forget()
        for frame in self._root.pack_slaves():
            frame.pack_forget()

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

    def _createCatLabel(self):
        self._listBoxLabel = Label(self._root, text="Kategorie:")
        self._listBoxLabel.grid(row=0, column=0, sticky=N+W, padx=30)

    def _createItemsGrid(self):
        cat = [self.listVegetables, self.listMeat, self.listDurable,
               self.listDrinks, self.listDrugstore, self.listSpecial]
        index = 0

        for r in range(2):
            for c in range(3):
                frame = Frame(self._root)
                frame.grid(row=r + 1, column=c + 1,
                           padx=30, pady=30, sticky=W+E+N+S)
                Grid.rowconfigure(self._root, r + 1, weight=1)
                Grid.columnconfigure(self._root, c + 1, weight=1)
                self._createAddButton(frame, cat[self.selectedCat][index])
                self._createLabels(
                    frame, cat[self.selectedCat][index][0], cat[self.selectedCat][index][2])
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
        button = Button(frame, text="+",
                        command=lambda: self._addItemToShoppingCart(item))
        button.pack(side=RIGHT, anchor=NE)

    def _createImage(self, frame, path):
        image = Image.open(path)
        image = image.resize((180, 180), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(image)
        panel = Label(frame, image=img)
        panel.image = img
        panel.pack()

    def _createSelectedCatLabel(self):
        self._categoryLabel = Label(
            self._root, text=self.listDict[self.selectedCat])
        self._categoryLabel.grid(row=0, column=1, sticky=N+W, padx=30)

    def _overriteCatLabel(self):
        self._categoryLabel.config(text=self.listDict[self.selectedCat])

    def _addItemToShoppingCart(self, item):
        length = len(self.shoppingCart)
        if length == 0:
            self.shoppingCart.append([item[0], 1, item[2]])
        else:
            for index in range(len(self.shoppingCart)):
                if self.shoppingCart[index][0] == item[0]:
                    self.shoppingCart[index][1] += 1
                else:
                    self.shoppingCart.append([item[0], 1, item[2]])


class About():

    def __init__(self, root):
        self._root = root
        self._createAboutPage()

    def _createAboutPage(self):
        self._createSimPhoto()
        self._createInfoString()
        self._createBackButton()

    def _createBackButton(self):
        button = Button(self._root, text="Hlavni stranka",
                        command=self._returnToIndex)
        button.pack(side=BOTTOM, anchor=SW)

    def _createInfoString(self):
        label = Label(
            self._root, text="Vitejte v SimShop!\n\nNakupujte pouze cerstvo a prirodni potraviny.\nNase sluzby jsou tu vzdy pro vas.\nRychlost je nase druhe jmeno")
        label.pack(side=TOP)

    def _createSimPhoto(self):
        image = Image.open("images/about.png")
        image = image.resize((200, 200), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(image)
        panel = Label(self._root, image=img)
        panel.image = img
        panel.pack(side=TOP, anchor=NW)

    def _returnToIndex(self):
        for frame in self._root.grid_slaves():
            frame.grid_forget()
        for frame in self._root.pack_slaves():
            frame.pack_forget()
        MainPage(self._root)


class ShoppingCart():

    def __init__(self, root, shoppingCart):
        self._root = root
        self.shoppingCart = shoppingCart
        self._createShoppingCart()

    def _createShoppingCart(self):
        self._createProgressLabel()
        self._createItemList()
        self._createButtons()
        self._addWeight()

    def _createProgressLabel(self):
        shopCartLabel = Label(self._root, text="Nakupni kosik")
        shippingLabel = Label(self._root, text="doprava & platba")
        addressLabel = Label(self._root, text="dodaci adresa")
        shopCartLabel.grid(row=0, column=0, padx=30, sticky=W+E)
        shippingLabel.grid(row=0, column=1, padx=30, sticky=W+E)
        addressLabel.grid(row=0, column=2, sticky=W+E)

    def _createItemList(self):
        listbox = Listbox(self._root)
        for index in range(len(self.shoppingCart)):
            value = str(self.shoppingCart[index][0]) + "\t\t Kusu: " + str(self.shoppingCart[index][1]) + " Cena: " + str(self.shoppingCart[index][1] * self.shoppingCart[index][2])
            listbox.insert(index, value)
        listbox.grid(row=1, column=0, columnspan=3, sticky=W+E+N+S)

    def _createButtons(self):
        backButton = Button(self._root, text="Hlavni stranka",
                            command=self._returnToIndex)
        nextButton = Button(
            self._root, text="doprava & platba", command=self._goToShipment)
        backButton.grid(row=2, column=0, padx=30)
        nextButton.grid(row=2, column=2)

    def _returnToIndex(self):
        for frame in self._root.grid_slaves():
            frame.grid_forget()
        for frame in self._root.pack_slaves():
            frame.pack_forget()
        MainPage(self._root)

    def _goToShipment(self):
        for frame in self._root.grid_slaves():
                frame.grid_forget()
        for frame in self._root.pack_slaves():
            frame.pack_forget()
        Shipping(self._root, self.shoppingCart)

    def _addWeight(self):
        for r in range(2):
            Grid.rowconfigure(self._root, r, weight=1)
        for c in range(2):
            Grid.columnconfigure(self._root, c, weight=1)


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
        self.shoppingCart = shoppingCart
        self._createShipping()

    def _createShipping(self):
        shippingFrame = Frame(self._root)
        paymentFrame = Frame(self._root)
        shippingFrame.grid(row=0, column=0, padx=30, sticky=S+N)
        paymentFrame.grid(row=0, column=1, sticky=S+N)
        self._addWeight()
        self._addShipping(shippingFrame)
        self._addPayment(paymentFrame)
        self._createButton(shippingFrame, "Zpet", self._returnToShoppingCart)
        self._createButton(paymentFrame, "Dodaci informace", self._goToAddress)

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

    def _createButton(self, frame, text, command):
        button = Button(frame, text=text, command=command)
        button.pack(side=BOTTOM, anchor=SW)

    def _returnToShoppingCart(self):
        for frame in self._root.grid_slaves():
                frame.grid_forget()
        for frame in self._root.pack_slaves():
            frame.pack_forget()
        ShoppingCart(self._root, self.shoppingCart)

    def _goToAddress(self):
        for frame in self._root.grid_slaves():
                frame.grid_forget()
        for frame in self._root.pack_slaves():
            frame.pack_forget()
        Address(self._root, self.shoppingCart)

    def _addWeight(self):
        for c in range(1):
            Grid.columnconfigure(self._root, c, weight=2)


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
        self.shoppingCart = shoppingCart
        self._createAddress()

    def _createAddress(self):
        for item in self.addressDict.values():
            self._createLabel(item)
            self._createEntry()
        
        self._createButton(self._root, "Zpet", self._returnToShippment, BOTTOM, LEFT, SW)
        self._createButton(self._root, "Objednat", self._submit, BOTTOM, RIGHT, SE)

    def _createLabel(self, text):
        label = Label(self._root, text=text)
        label.pack(side=TOP, anchor=W)
    
    def _createEntry(self):
        entry = Entry(self._root)
        entry.pack(side=TOP, anchor=W)

    def _createButton(self, frame, text, command, frameSide, side, anchor):
        bottomFrame = Frame(self._root)
        bottomFrame.pack(side=frameSide, anchor=anchor)
        button = Button(frame, text=text, command=command)
        button.pack(side=side)
    
    def _returnToShippment(self):
        for frame in self._root.grid_slaves():
                frame.grid_forget()
        for frame in self._root.pack_slaves():
            frame.pack_forget()
        Shipping(self._root, self.shoppingCart)

    def _submit(self):
        for frame in self._root.grid_slaves():
                frame.grid_forget()
        for frame in self._root.pack_slaves():
            frame.pack_forget()
        self._createLabel("Objednáno!")
        self._createButton(self._root,"Hlavni stranka",self._returnToHome,BOTTOM,LEFT, SW)
    
    def _returnToHome(self):
        for frame in self._root.grid_slaves():
                frame.grid_forget()
        for frame in self._root.pack_slaves():
            frame.pack_forget()
        MainPage(self._root)


def main():
    root = Tk()
    app = MainPage(root)
    root.mainloop()
    root.destroy()


main()
