#!/usr/bin/env

import sys
import csv
from datetime import date
from datetime import timedelta

"""
Class for keeping track of user objects
"""
class Contact:
    def __init__(self,name,birthday=None,address=None,adr_=None):
        self.name = name
        self.birthday = birthday
        self.address = address
        self.adr_ = adr_

    def setName(self,name):
        self.name = name

    def setBirthday(self,birthday):
        self.birthday = birthday

    def setAddress(self,address):
        self.address = address

    def setAdr_(self,adr_):
        self.adr_ = adr_


"""
open csv file, read in data
return dictionary of Contact objects with birthday date keys
"""
def getBirthdays(contacts_file):
    #read in birthdays from csv
    with open(contacts_file,"r") as csvfile:
        reader = csv.reader(csvfile)

        #create dictionary to hold dates as keys, user objs as values
        birthdays = {}

        for row in reader:
            #gather data
            name = row[0]
            birthday = row[1] 
            address = row[2]+', '+row[3]+', '+row[4]+' '+row[5] #street address, city, state, zipcode
            
            #create user object with data from csv
            user = Contact(name,birthday,address) 

            #add date to birthdays dictionary
            if birthday in birthdays:
                birthdays[birthday].append(user)
            else:
                birthdays[birthday] = [user]
             
    return birthdays

"""
return string of today+3 days
"""
def futureBirthdays(today):
    three_days = today + timedelta(days=3) #get date of 3 days from today
    return three_days.strftime("%m-%d-%Y")


def main():
    ###
    # pass contact file name if you want specific file
    # default to contacts.csv
    ###
    if len(sys.argv)>1:
        contacts_file = sys.argv[1] 
    else:
        contacts_file = "contacts.csv"
    birthdays = getBirthdays(contacts_file)

    #get date 3 days in future; will send out cards today for people with birthdays in 3 days
    today = date.today() #get current date as date object 
    birthday_date = futureBirthdays(today)


    



#(format is MM-DD-YYYY)
    
    #if current date == 3 days before friend's birthday
    #   if address object id not part of Contact object
    #       access lob
    #       create address via lob
    #       save adr_ to user object
    #   else:
    #       access user's adr_ from address book
    #   send postcard
    

    for k,v in birthdays.items():
        print k
        for friend in v:
            print friend.name
    
        

if __name__ == "__main__":
    main()
