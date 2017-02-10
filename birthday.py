#!/usr/bin/env

import sys
import csv
import lob
from datetime import date
from datetime import timedelta

"""
Class for keeping track of user objects
"""
class Contact:
    def __init__(self,name,birthday=None,street=None,city=None,state=None,zipcode=None,adr_=None):
        self.name = name
        self.birthday = birthday
        self.street = street
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.adr_ = adr_

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
            #create user object with data from csv
            #0=>name, 1=>birthday (MM-DD), 2=>street address
            #3=>city, 4=>state, 5=>zipcode
            birthday = row[1]
            user = Contact(row[0],row[1],row[2],row[3],row[4],row[5]) 

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
    return three_days.strftime("%m-%d")

"""
Calls Lob API to create a new address object
Saves new adr_ id to given Contact object
Returns lob_address
"""
def createLobAddress(friend):
    lob_address = lob.Address.create(
        name=friend.name,
        address_line1=friend.street,
        address_city=friend.city,
        address_state=friend.state,
        address_zip=friend.zipcode
    )
    friend.setAdr_(lob_address.id)
    return lob_address

def main():
    #collect command line arguments
    key = sys.argv[1]
    # pass contact file name if you want specific file, default to contacts.csv
    if len(sys.argv)>2:
        contacts_file = sys.argv[2] 
    else:
        contacts_file = "contacts.csv"

    birthdays = getBirthdays(contacts_file)

    #get date 3 days in future; will send out cards today for people with birthdays in 3 days
    birthday_date = futureBirthdays(date.today()) #get string of date 3 days from today (format is MM-DD)

    #check birthdays dict for birthday_date
    if birthday_date in birthdays:
        lob.api_key = key
        for friend in birthdays[birthday_date]: #loop through list of Contact objects
            if friend.adr_: #if user has a Lob address ID assigned to them (already in Lob address book)
                lob_address = lob.Address.retrieve(friend.adr_)
            else:
                #create new address in Lob
                lob_address = createLobAddress(friend)
                #TODO: Save to CSV file or database
        #send postcard


if __name__ == "__main__":
    main()
