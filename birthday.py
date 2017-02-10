#!/usr/bin/env

import csv

"""
Class for keeping track of user objects
"""
class Contact:
    def __init__(self,name,birthday=None,address=None):
        self.name = name
        self.birthday = birthday
        self.address = address

    def setName(self,name):
        self.name = name

    def setBirthday(self,birthday):
        self.birthday = birthday

    def setAddress(self,address):
        self.address = address


"""
open csv file, read in data
return dictionary of Contact objects with birthday date keys
"""
def getBirthdays():
    #read in birthdays from csv
    with open("contacts.csv","r") as csvfile:
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


def main():
    #TODO: allow user to input contact filename
    birthdays = getBirthdays()

    for k,v in birthdays.items():
        print k
        for friend in v:
            print friend.name
    
        

if __name__ == "__main__":
    main()
