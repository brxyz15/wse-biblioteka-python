from tkinter import *
from datetime import time, datetime
import tkinter.messagebox
import random as rd
import pandas as pd

def generateId():
    repeat = True
    while(repeat):
        randomId = str(rd.randrange(10)) + str(rd.randrange(10)) + str(rd.randrange(10)) + str(rd.randrange(10))
    
        try:
            for customerId in pd.read_csv("customer.csv").get("ID").tolist():
                if customerId == randomId:
                    break
            return randomId             
            
        except FileNotFoundError as e:
            repeat = False
            tkinter.messagebox.showerror("FileNotFoundError", e)
            

def addCustomer(customerWindow, firstName, lastName, email, phoneNumber, street, city, country, generateId):
    for argument in (firstName, lastName, email, street, city, country):
        if len(argument) == 0 and argument.isspace:
            tkinter.messagebox.showwarning("Ostrzeżenie!", "Nie podano wszystkich danych.", parent=customerWindow)    
            return
    
    if not phoneNumber.isnumeric() and not (len(phoneNumber) == 0 or phoneNumber.isspace()):
        tkinter.messagebox.showwarning("Ostrzeżenie!", "Nieprawidłowy nr telefonu.", parent=customerWindow)    
        return
    
    if len(phoneNumber) == 0 or phoneNumber == 0:
        phoneNumber = "NULL"

    try:
        modifiedCustomerFile = pd.read_csv("customer.csv", na_filter=False)
        modifiedAddressFile = pd.read_csv("address.csv")
        
        idNumber = generateId()
        fullName = firstName.strip() + " " + lastName.strip()
        currentDate = str(datetime.now()).split()[0]
        
        newCustomerDataFrame = pd.DataFrame({"ID": [idNumber], "NAME": [fullName], "E-MAIL": [email], "PHONE": [phoneNumber], "CREATED": [currentDate], "UPDATED": [currentDate]})
        modifiedCustomerFile = pd.concat([modifiedCustomerFile, newCustomerDataFrame], ignore_index=True)
        modifiedCustomerFile.to_csv("customer.csv", index=False)
        
        newAddressDataFrame = pd.DataFrame({"ID": [idNumber], "STREET": [street], "CITY": [city], "COUNTRY": [country]})
        modifiedAddressFile = pd.concat([modifiedAddressFile, newAddressDataFrame], ignore_index=True)
        modifiedAddressFile.to_csv("address.csv", index=False)
        
        open(str("DATABASE/" + idNumber + ".txt"), "a")
        
        tkinter.messagebox.showinfo("Działanie wykonane", "Dodano klienta do biblioteki", parent=customerWindow)
    
    except FileNotFoundError as e:
        tkinter.messagebox.showerror("FileNotFoundError", e, parent=customerWindow)
        return


def removeCustomer(customerWindow, customerList, name = "", customerId = 0):    
    name = name.strip()
    try:
        if((len(name) == 0 or name.isspace()) and (customerId == 0 or len(customerId) == 0 or customerId.isspace())):
            tkinter.messagebox.showwarning("Ostrzeżenie!", "Nie wpisano poprawnych wartości.", parent=customerWindow)
            return
    except ValueError as e:
        tkinter.messagebox.showerror("ValueError", e, parent=customerWindow)
        return
    
    customerInfo = pd.read_csv("customer.csv")[['ID', 'NAME']]
    customerIds = customerInfo.get("ID").tolist()
    names = customerInfo.get("NAME").tolist()
    
    for index, (idIterator, nameIterator) in enumerate(zip(customerIds, names)):
        if int(customerId) == int(idIterator) or name == nameIterator:
            try:
                modifiedCustomerFile = pd.read_csv("customer.csv")
                modifiedAddressFile = pd.read_csv("address.csv")
                
                modifiedCustomerFile.drop([index]).to_csv("customer.csv", index=False)
                modifiedAddressFile.drop([index]).to_csv("address.csv", index=False)
                
                customerList.delete(index)
                return
            except FileNotFoundError as e:
                tkinter.messagebox.showerror("FileNotFoundError", e, parent=customerWindow)
                return