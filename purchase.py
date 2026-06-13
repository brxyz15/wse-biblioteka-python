from tkinter import *
from datetime import time, datetime
import tkinter.messagebox
import random as rd
import pandas as pd
import book as bk

def sellBook(purchaseWindow, bookList, bookId, customerId, sellCount=1):
    for argument in (bookId, customerId):
        if argument.isspace() or len(argument) == 0:
            tkinter.messagebox.showwarning("Ostrzeżenie!", "Podano nieprawidłowe numery id.", parent=purchaseWindow)
            return
    if sellCount.isspace() or len(sellCount) == 0:
        sellCount = 1
    if int(sellCount) <= 0 or not str(sellCount).isnumeric():
        tkinter.messagebox.showwarning("Ostrzeżenie!", "Podano nieprawidłową ilość książek.", parent=purchaseWindow)
        return
    
    bookInfo = bk.parseBooks()
    bookIds = bookInfo.get("ID").tolist()
    customerInfo = pd.read_csv("customer.csv")[['ID', 'NAME']]
    customerIds = customerInfo.get("ID").tolist()
    
    for bookIndex, bookIdIterator in enumerate(bookIds):
        if bookId == bookIdIterator:
            for customerIndex, customerIdIterator in enumerate(customerIds):
                if int(customerId) == int(customerIdIterator):
                    bookCount = bookInfo.at[bookIndex,'NO_EBOOK_AVAILABLE']
                    if int(bookCount) < int(sellCount):
                        tkinter.messagebox.showwarning("Ostrzeżenie!", "Liczba kupowanych książek przekracza dostępny zapas.", parent=purchaseWindow)    
                        return
                    textFile = open(str("DATABASE/" + customerId + ".txt"), "a")
                    textFile.write(bookInfo.at[bookIndex,'ID'] + " " + bookInfo.at[bookIndex,'AUTHOR'] + " " + bookInfo.at[bookIndex,'TITLE'] + " " + sellCount + "\n")
                    try:
                        currentDate = str(datetime.now()).split()[0]
                        dataSet = (bookInfo.at[bookIndex,'ID'], bookInfo.at[bookIndex,'AUTHOR'], bookInfo.at[bookIndex,'TITLE'], 
                                   str(int(bookCount) - int(sellCount)), bookInfo.at[bookIndex,'CREATED'], currentDate)
                        newLine = ",".join(dataSet)
                        print(newLine)
                        modifiedFile = pd.read_excel("book.xlsx")
                        modifiedFile.at[bookIndex, 'ID,AUTHOR,TITLE,NO_EBOOK_AVAILABLE,CREATED,UPDATED'] = newLine
                        modifiedFile.to_excel("book.xlsx", index=False)
                        
                        bookInfo = bk.parseBooks()
                        
                        bookList.delete(bookIndex)
                        bookList.insert(bookIndex, (bookInfo.at[bookIndex,'ID'], bookInfo.at[bookIndex,'AUTHOR'], bookInfo.at[bookIndex,'TITLE'], bookInfo.at[bookIndex,'NO_EBOOK_AVAILABLE']))
                                
                        tkinter.messagebox.showinfo("Działanie wykonane", "Sprzedano książki klientowi", parent=purchaseWindow)
        
                    except FileNotFoundError as e:
                        tkinter.messagebox.showerror("FileNotFoundError", e, parent=purchaseWindow)
                        return
                    
def increaseBookCount(purchaseWindow, bookList, bookId, bookCount=1):
    if bookId.isspace() or len(bookId) == 0:
        tkinter.messagebox.showwarning("Ostrzeżenie!", "Podano nieprawidłowe id książki.", parent=purchaseWindow)
        return
    if bookCount.isspace() or len(bookCount) == 0:
        bookCount = 1
    if int(bookCount) <= 0 or not str(bookCount).isnumeric():
        tkinter.messagebox.showwarning("Ostrzeżenie!", "Podano nieprawidłową ilość książek.", parent=purchaseWindow)
        return
    
    bookInfo = bk.parseBooks()
    bookIds = bookInfo.get("ID").tolist()
    
    for bookIndex, bookIdIterator in enumerate(bookIds):
        if bookId == bookIdIterator:
            currentDate = str(datetime.now()).split()[0]    
            dataSet = (bookInfo.at[bookIndex,'ID'], bookInfo.at[bookIndex,'AUTHOR'], bookInfo.at[bookIndex,'TITLE'], 
                                   str(int(bookInfo.at[bookIndex,'NO_EBOOK_AVAILABLE']) + int(bookCount)), bookInfo.at[bookIndex,'CREATED'], currentDate)
            newLine = ",".join(dataSet)
            print(newLine)
            modifiedFile = pd.read_excel("book.xlsx")
            modifiedFile.at[bookIndex, 'ID,AUTHOR,TITLE,NO_EBOOK_AVAILABLE,CREATED,UPDATED'] = newLine
            modifiedFile.to_excel("book.xlsx", index=False)
                        
            bookInfo = bk.parseBooks()
                        
            bookList.delete(bookIndex)
            bookList.insert(bookIndex, (bookInfo.at[bookIndex,'ID'], bookInfo.at[bookIndex,'AUTHOR'], bookInfo.at[bookIndex,'TITLE'], bookInfo.at[bookIndex,'NO_EBOOK_AVAILABLE']))
                                
            tkinter.messagebox.showinfo("Działanie wykonane", "Uzupełniono asortyment książek", parent=purchaseWindow)