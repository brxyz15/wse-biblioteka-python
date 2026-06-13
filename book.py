from tkinter import *
from datetime import time, datetime
import tkinter.messagebox
import random as rd
import pandas as pd

def parseBooks():
    try:
        bookDataFrame = pd.read_excel("book.xlsx")["ID,AUTHOR,TITLE,NO_EBOOK_AVAILABLE,CREATED,UPDATED"].apply(lambda x: pd.Series(x.split(",")))
        bookDataFrame.rename(columns={0:'ID', 1:'AUTHOR', 2:'TITLE', 3:'NO_EBOOK_AVAILABLE', 4:'CREATED', 5:'UPDATED'}, inplace=True)
        return bookDataFrame[['ID', 'AUTHOR', 'TITLE', 'NO_EBOOK_AVAILABLE', 'CREATED', 'UPDATED']]
    
    except FileNotFoundError as e:
        tkinter.messagebox.showerror("FileNotFoundError", e)

def addBook(bookWindow, title, author, bookCount):
    if (len(title) == 0 or title.isspace() or len(author) == 0 or author.isspace()):
        tkinter.messagebox.showwarning("Ostrzeżenie!", "Nie wszystkie wymagane wartości zostały wpisane.", parent=bookWindow)
        return
    try:
        if (int(bookCount) <= 0):
            tkinter.messagebox.showwarning("Ostrzeżenie!", "Nieprawidłowa ilość egzemplarzy książek", parent=bookWindow)
    except ValueError as e:
            tkinter.messagebox.showerror("ValueError", e, parent=bookWindow)
            return
    
    bookInfo = parseBooks()[['ID', 'AUTHOR', 'TITLE']]
    lastId = bookInfo.get("ID").tail(1)
    authors = bookInfo.get("AUTHOR").tolist()
    titles = bookInfo.get("TITLE").tolist()
    currentDate = str(datetime.now()).split()[0]
    
    addedPair = (author, title)
    for pair in zip(authors, titles):
        if pair == addedPair:
            tkinter.messagebox.showwarning("Ostrzeżenie!", "Książka jest już w bazie danych.", parent=bookWindow)
            return
    
    try:
        dataSet = (str(int(lastId)+1), author, title, bookCount, currentDate, currentDate)
        newLine = ",".join(dataSet)
        modifiedFile = pd.concat([pd.read_excel("book.xlsx"), 
                                  pd.DataFrame({'ID,AUTHOR,TITLE,NO_EBOOK_AVAILABLE,CREATED,UPDATED': [newLine]})], ignore_index=True)
        modifiedFile.to_excel("book.xlsx", index=False)
        
        tkinter.messagebox.showinfo("Działanie wykonane", "Dodano książkę do biblioteki", parent=bookWindow)
        
    except FileNotFoundError as e:
        tkinter.messagebox.showerror("FileNotFoundError", e, parent=bookWindow)
        return
        
                    
                    
def removeBook(bookWindow, bookList, title = "", bookId = 0):
    try:
        if((len(title) == 0 or title.isspace()) and (bookId == 0 or len(bookId) == 0 or bookId.isspace())):
            tkinter.messagebox.showwarning("Ostrzeżenie!", "Nie wpisano poprawnych wartości.", parent=bookWindow)
            return
    except ValueError as e:
        tkinter.messagebox.showerror("ValueError", e, parent=bookWindow)
        return
    
    bookInfo = parseBooks()
    bookIds = bookInfo.get("ID").tolist()
    titles = bookInfo.get("TITLE").tolist()
    
    for index, (idIterator, titleIterator) in enumerate(zip(bookIds, titles)):
        if bookId == idIterator or title == titleIterator:
            try:
                modifiedFile = pd.read_excel("book.xlsx")
                modifiedFile.drop([index]).to_excel("book.xlsx", index=False)
                bookList.delete(index)
                return
            except FileNotFoundError as e:
                tkinter.messagebox.showerror("FileNotFoundError", e, parent=bookWindow)
                return      