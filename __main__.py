from tkinter import *
from datetime import time, datetime
import tkinter.messagebox
import random as rd
import pandas as pd
import book as bk
import customer as cst
import purchase as pur
  
def closeOtherWindows(mainWindow):
    for childWindow in mainWindow.winfo_children():
        if isinstance(childWindow, Toplevel):
            childWindow.destroy()

def initBookWindow(mode):                    
    closeOtherWindows(mainWindow)
        
    bookWindow = Toplevel()
    bookWindow.geometry("640x480")
    
    if mode=="add":
        bookWindow.title("Dodawanie książki")
         
        titleFrame = Frame(bookWindow)
        titleFrame.pack(anchor=CENTER, padx=16, pady=16, side=TOP)
         
        authorFrame = Frame(bookWindow)
        authorFrame.pack(anchor=CENTER, padx=16, pady=16, side=TOP)
        
        countFrame = Frame(bookWindow)
        countFrame.pack(anchor=CENTER, padx=16, pady=16, side=TOP)
         
        Label(titleFrame, text="Tytuł:").grid(column=0, row=0)
        Label(authorFrame, text="Autor:").grid(column=0, row=0)
        Label(countFrame, text="Ilość książek:").grid(column=0, row=0)
         
        title = StringVar(titleFrame)
        author = StringVar(authorFrame)
        bookCount = StringVar(countFrame)
         
        Entry(titleFrame, textvariable=title).grid(column=1, row=0)
        Entry(authorFrame, textvariable=author).grid(column=1, row=0)
        Entry(countFrame, textvariable=bookCount).grid(column=1, row=0)
         
        Button(bookWindow, text="Dodaj", command= lambda: bk.addBook(bookWindow, title.get(), author.get(), bookCount.get())).pack(anchor=S, padx=16, pady=16)
         
    else:
        bookWindow.title("Usuwanie książki")
        
        bookList = Listbox(bookWindow, width=480)
        bookList.pack(anchor=CENTER, padx=16, pady=16, side=TOP)
        
        bookInfo = bk.parseBooks()[['ID', 'AUTHOR', 'TITLE']]
        i = 1
        for book in zip(bookInfo.get("ID").tolist(), bookInfo.get("AUTHOR").tolist(), bookInfo.get("TITLE").tolist()):
            bookList.insert(i, book)    
            i = i+1

        titleFrame = Frame(bookWindow)
        titleFrame.pack(anchor=CENTER, padx=16, pady=16, side=TOP)
        
        idFrame = Frame(bookWindow)
        idFrame.pack(anchor=CENTER, padx=16, pady=16, side=TOP)
         
        Label(titleFrame, text="Tytuł:").grid(column=0, row=0)
        Label(idFrame, text="ID:").grid(column=0, row=0)
         
        title = StringVar(titleFrame)
        bookId = StringVar(idFrame)
         
        Entry(titleFrame, textvariable=title).grid(column=1, row=0)
        Entry(idFrame, textvariable=bookId).grid(column=1, row=0)
         
        Button(bookWindow, text="Usuń", command= lambda: bk.removeBook(bookWindow, bookList, title.get(), bookId.get())).pack(anchor=S, padx=16, pady=16)
        
    bookWindow.mainloop()

##### CUSTOMER MODULE

def initCustomerWindow(mode):
    closeOtherWindows(mainWindow)
    
    customerWindow = Toplevel()
    customerWindow.geometry("640x480")
    
    if mode=="add":
        customerWindow.title("Rejestracja klienta")
        allFrame = Frame(customerWindow)
        allFrame.pack(side=TOP)
        
        ### CUSTOMER PERSONAL DATA
        customerFrame = Frame(allFrame)
        customerFrame.pack(anchor=W, padx=16, pady=16, side=LEFT)
         
        firstNameFrame = Frame(customerFrame)
        firstNameFrame.pack(anchor=CENTER, padx=16, pady=16, side=TOP)
        
        lastNameFrame = Frame(customerFrame)
        lastNameFrame.pack(anchor=CENTER, padx=16, pady=16, side=TOP)
         
        emailFrame = Frame(customerFrame)
        emailFrame.pack(anchor=CENTER, padx=16, pady=16, side=TOP)
        
        phoneFrame = Frame(customerFrame)
        phoneFrame.pack(anchor=CENTER, padx=16, pady=16, side=TOP)
         
        Label(firstNameFrame, text="Imię/Imiona:").grid(column=0, row=0)
        Label(lastNameFrame, text="Nazwisko:").grid(column=0, row=0)
        Label(emailFrame, text="Adres e-mail:").grid(column=0, row=0)
        Label(phoneFrame, text="Nr telefonu:").grid(column=0, row=0)
         
        firstName = StringVar(firstNameFrame)
        lastName = StringVar(lastNameFrame)
        email = StringVar(emailFrame)
        phoneNumber = StringVar(phoneFrame)
         
        Entry(firstNameFrame, textvariable=firstName).grid(column=1, row=0)
        Entry(lastNameFrame, textvariable=lastName).grid(column=1, row=0)
        Entry(emailFrame, textvariable=email).grid(column=1, row=0)
        Entry(phoneFrame, textvariable=phoneNumber).grid(column=1, row=0)
        
        ### ADDRESS DATA
        addressFrame = Frame(allFrame)
        addressFrame.pack(anchor=E, padx=16, pady=16, side=LEFT)
         
        streetFrame = Frame(addressFrame)
        streetFrame.pack(anchor=CENTER, padx=16, pady=16, side=TOP)
        
        cityFrame = Frame(addressFrame)
        cityFrame.pack(anchor=CENTER, padx=16, pady=16, side=TOP)
         
        countryFrame = Frame(addressFrame)
        countryFrame.pack(anchor=CENTER, padx=16, pady=16, side=TOP)
        
         
        Label(streetFrame, text="Ulica:").grid(column=0, row=0)
        Label(cityFrame, text="Miasto:").grid(column=0, row=0)
        Label(countryFrame, text="Kraj:").grid(column=0, row=0)
         
        street = StringVar(addressFrame)
        city = StringVar(streetFrame)
        country = StringVar(countryFrame)
         
        Entry(streetFrame, textvariable=street).grid(column=1, row=0)
        Entry(cityFrame, textvariable=city).grid(column=1, row=0)
        Entry(countryFrame, textvariable=country).grid(column=1, row=0)
         
        Button(customerWindow, text="Dodaj", command= lambda: cst.addCustomer(customerWindow, firstName.get(), lastName.get(), email.get(), phoneNumber.get(),
                                                                        street.get(), city.get(), country.get(), cst.generateId)).pack(anchor=S, padx=16, pady=16, side=TOP)
    
    else:
        customerWindow.title("Usuwanie klienta")
        
        customerList = Listbox(customerWindow, width=480)
        customerList.pack(anchor=CENTER, padx=16, pady=16, side=TOP)
        
        try:
            customerInfo = pd.read_csv("customer.csv")[['ID', 'NAME']]
            cityAddress = pd.read_csv("address.csv")[['CITY']]
            i = 1
            for customer in zip(customerInfo.get("ID").tolist(), customerInfo.get("NAME").tolist(), cityAddress.get("CITY").tolist()):
                customerList.insert(i, customer)    
                i = i+1
        except FileNotFoundError as e:
            tkinter.messagebox.showerror("FileNotFoundError", e) 

        nameFrame = Frame(customerWindow)
        nameFrame.pack(anchor=CENTER, padx=16, pady=16, side=TOP)
        
        idFrame = Frame(customerWindow)
        idFrame.pack(anchor=CENTER, padx=16, pady=16, side=TOP)
         
        Label(nameFrame, text="Imię i nazwisko:").grid(column=0, row=0)
        Label(idFrame, text="ID:").grid(column=0, row=0)
         
        name = StringVar(nameFrame)
        customerId = StringVar(idFrame)
         
        Entry(nameFrame, textvariable=name).grid(column=1, row=0)
        Entry(idFrame, textvariable=customerId).grid(column=1, row=0)
         
        Button(customerWindow, text="Usuń", command= lambda: cst.removeCustomer(customerWindow, customerList, name.get(), customerId.get())).pack(anchor=S, padx=16, pady=16)
        
    customerWindow.mainloop()

def initPurchaseWindow(mode):
    closeOtherWindows(mainWindow)
    
    purchaseWindow = Toplevel()
    purchaseWindow.geometry("960x480")
    
    if mode=="sell":
        purchaseWindow.title("Sprzedaż książek")
        
        listsFrame = Frame(purchaseWindow)
        listsFrame.pack(anchor=CENTER, padx=16, pady=16, side=TOP)
        
        bookListFrame = Frame(listsFrame)
        bookListFrame.pack(anchor=W, padx=16, pady=16, side=LEFT)
        
        customerListFrame = Frame(listsFrame)
        customerListFrame.pack(anchor=E, padx=16, pady=16, side=LEFT)

        bookList = Listbox(bookListFrame, width=64)
        bookList.pack(anchor=N, side=TOP, expand=False)
        bookInfo = bk.parseBooks()[['ID', 'AUTHOR', 'TITLE', 'NO_EBOOK_AVAILABLE']]
        i = 1
        for book in zip(bookInfo.get("ID").tolist(), bookInfo.get("AUTHOR").tolist(), bookInfo.get("TITLE").tolist(), bookInfo.get("NO_EBOOK_AVAILABLE").tolist()):
            bookList.insert(i, book)    
            i = i+1

        customerList = Listbox(customerListFrame, width=48)
        customerList.pack(anchor=N, side=TOP, expand=False)
        try:
            customerInfo = pd.read_csv("customer.csv")[['ID', 'NAME']]
            cityAddress = pd.read_csv("address.csv")[['CITY']]
            i = 1
            for customer in zip(customerInfo.get("ID").tolist(), customerInfo.get("NAME").tolist(), cityAddress.get("CITY").tolist()):
                customerList.insert(i, customer)    
                i = i+1
        except FileNotFoundError as e:
            tkinter.messagebox.showerror("FileNotFoundError", e) 
            
        bookIdFrame = Frame(bookListFrame)
        bookIdFrame.pack(anchor=CENTER, side=TOP)
            
        bookId = StringVar(bookIdFrame)
        Label(bookIdFrame, text="ID książki:").grid(column=0, row=0)
        Entry(bookIdFrame, textvariable=bookId).grid(column=1, row=0)
        
        customerIdFrame = Frame(customerListFrame)
        customerIdFrame.pack(anchor=CENTER, side=TOP)
        
        customerId = StringVar(customerIdFrame)
        Label(customerIdFrame, text="ID klienta:").grid(column=0, row=0)
        Entry(customerIdFrame, textvariable=customerId).grid(column=1, row=0)
            
        otherFrame = Frame(purchaseWindow)
        otherFrame.pack(anchor=CENTER, padx=16, pady=16, side=TOP)
        sellCount = StringVar(otherFrame)
        Label(otherFrame, text="Ilość książek do sprzedaży (puste pole = 1):").grid(column=0, row=0)
        Entry(otherFrame, textvariable=sellCount).grid(column=1, row=0)
        Button(purchaseWindow, text="Sprzedaj", command= lambda: pur.sellBook(purchaseWindow, bookList, bookId.get(), customerId.get(), sellCount.get())).pack(anchor=S, padx=16, pady=16)
        
    else:
        purchaseWindow.title("Uzupełnienie asortymentu")
        
        bookList = Listbox(purchaseWindow, width=86)
        bookList.pack(anchor=N, side=TOP, expand=False, padx=16, pady=16)
        bookInfo = bk.parseBooks()[['ID', 'AUTHOR', 'TITLE', 'NO_EBOOK_AVAILABLE']]
        i = 1
        for book in zip(bookInfo.get("ID").tolist(), bookInfo.get("AUTHOR").tolist(), bookInfo.get("TITLE").tolist(), bookInfo.get("NO_EBOOK_AVAILABLE").tolist()):
            bookList.insert(i, book)    
            i = i+1
            
        bookIdFrame = Frame(purchaseWindow)
        bookIdFrame.pack(anchor=CENTER, side=TOP)
        
        bookId = StringVar(bookIdFrame)
        Label(bookIdFrame, text="ID książki:").grid(column=0, row=0)
        Entry(bookIdFrame, textvariable=bookId).grid(column=1, row=0)
        
        countFrame = Frame(purchaseWindow)
        countFrame.pack(anchor=CENTER, side=TOP)
        
        bookCount = StringVar(countFrame)
        Label(countFrame, text="Liczba książek (puste pole = 1):").grid(column=0, row=0)
        Entry(countFrame, textvariable=bookCount).grid(column=1, row=0)
        
        Button(purchaseWindow, text="Dodaj", command= lambda: pur.increaseBookCount(purchaseWindow, bookList, bookId.get(), bookCount.get())).pack(anchor=S, padx=16, pady=16)
        

def __main__():
    global mainWindow
    mainWindow = Tk()
    mainWindow.title("Narzędzie administracji biblioteki")
    mainWindow.geometry('640x480')
    
    containerFrame = Frame(mainWindow)
    containerFrame.pack(anchor=CENTER, expand=TRUE, padx=16, pady=16)
    
    bookFrame = Frame(containerFrame)
    bookFrame.pack(anchor=W, side=LEFT)
    
    Label(bookFrame, text="Zarządzanie książkami").pack(anchor=N, padx=16, pady=16)
    Button(bookFrame, text="Dodaj książkę", command= lambda: initBookWindow("add")).pack(anchor=CENTER, padx=16, pady=16)
    Button(bookFrame, text="Usuń książkę", command= lambda: initBookWindow("delete")).pack(anchor=S, padx=16, pady=16)
    
    customerFrame = Frame(containerFrame)
    customerFrame.pack(anchor=CENTER, side=LEFT)
    
    Label(customerFrame, text="Zarządzanie klientami").pack(anchor=N, padx=16, pady=16)
    Button(customerFrame, text="Rejestruj klienta", command= lambda: initCustomerWindow("add")).pack(anchor=CENTER, padx=16, pady=16)
    Button(customerFrame, text="Usuń klienta", command= lambda: initCustomerWindow("delete")).pack(anchor=S, padx=16, pady=16)
    
    purchaseFrame = Frame(containerFrame)
    purchaseFrame.pack(anchor=E, side=LEFT)
    
    Label(purchaseFrame, text="Magazyn").pack(anchor=N, padx=16, pady=16)
    Button(purchaseFrame, text="Sprzedaj książki", command= lambda: initPurchaseWindow("sell")).pack(anchor=CENTER, padx=16, pady=16)
    Button(purchaseFrame, text="Uzupełnij asortyment", command= lambda: initPurchaseWindow("buy")).pack(anchor=S, padx=16, pady=16)
    
    mainWindow.mainloop()

if __name__ == "__main__":
    __main__()
    