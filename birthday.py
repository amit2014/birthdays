#!/usr/bin/env

import sys
import csv
import lob
from datetime import date
from datetime import timedelta

#GLOBAL
key = sys.argv[1]
lob.api_key = key

"""
Class for keeping track of user objects
"""
class Contact:
    def __init__(self,name,birthday=None,street=None,city=None,state=None,zipcode=None):
        self.name = name
        self.birthday = birthday
        self.street = street
        self.city = city
        self.state = state
        self.zipcode = zipcode


"""
Receive a string name of a state
Return the abbreviation
"""
def state_abbreviation(state):
    states = {
        'alabama':'AL',
        'alaska':'AK',
        'arizona':'AZ',
        'arkansas':'AR',
        'california':'CA',
        'colorado':'CO',
        'connecticut':'CT',
        'delaware':'DE',
        'florida':'FL',
        'georgia':'GA',
        'hawaii':'HI',
        'idaho':'ID',
        'illinois':'IL',
        'indiana':'IN',
        'iowa':'IA',
        'kansas':'KS',
        'kentucky':'KY',
        'louisiana':'LA',
        'maine':'ME',
        'maryland':'MD',
        'massachusetts':'MA',
        'michigan':'MI',
        'minnesota':'MN',
        'mississippi':'MS',
        'missouri':'MO',
        'montana':'MT',
        'nebraska':'NE',
        'nevada':'NV',
        'new':'Hampshire   NH',
        'new':'Jersey  NJ',
        'new':'Mexico  NM',
        'new':'York    NY',
        'north':'Carolina  NC',
        'north':'Dakota    ND',
        'ohio':'OH',
        'oklahoma':'OK',
        'oregon':'OR',
        'pennsylvania':'PA',
        'rhode':'Island    RI',
        'south':'Carolina  SC',
        'south':'Dakota    SD',
        'tennessee':'TN',
        'texas':'TX',
        'utah':'UT',
        'vermont':'VT',
        'virginia':'VA',
        'washington':'WA',
        'west':'Virginia   WV',
        'wisconsin':'WI',
        'wyoming':'WY'
    }
    if state.lower() in states:
        return states[state.lower()]
    else:
        return False


"""
Prompt user to enter state
Send data to function that will find abbreviation if user entered full name
If data does not appear, prompt user again
return state
"""
def get_state():
    state = raw_input("State: ")
    if len(state)>2:
        state = state_abbreviation(state)
        if not state: #likely case: user spelled state wrong
            print "Please enter the name of the state again (check spelling!)."
            return get_state()
        else:
            return state
    else:
        return state
            

"""
"""
def get_user_address():
    name = raw_input("\nName: ")
    street = raw_input("Street Address: ")
    city = raw_input("City: ")
    state = get_state()
    zipcode = raw_input("Zip Code: ")
    print "\nPlease verify the your address: "
    print name
    print street + ", "+city+", "+state+" "+zipcode
    if (raw_input("\nIs this correct? ").lower()=="yes"):
        lob_address = lob.Address.create(
            name=name,
            address_line1=street,
            address_city=city,
            address_state=state,
            address_zip=zipcode,
            metadata={"user":True}
        )
    else:
        print "Please re-enter your information."
        get_user_address()


"""
Prompt user to enter info about contacts
Return a list of Contact objects
"""
def get_contacts():
    contacts = []
    more_contacts = True
    while more_contacts:
        name = raw_input("\nName: ")
        street = raw_input("Street Address: ")
        city = raw_input("City: ")
        state = get_state()
        zipcode = raw_input("Zip Code: ")
        birthday = raw_input("Birthday: ")
        #TODO: check user input
        print "\nPlease verify the following contact: "
        print name
        print birthday
        print street + ", "+city+", "+state+" "+zipcode
        if (raw_input("\nIs this correct? ").lower()=="yes"):
            friend = Contact(name,birthday,street,city,state,zipcode)
            contacts.append(friend)
            more = raw_input("\nDo you have more contacts to add? [Yes|No] ")
            if more.lower()=='no':
                more_contacts = False
        else:
            print "Please re-enter that contact's information."
    return contacts


"""
return string of today+3 days
"""
def futureBirthdays(today):
    three_days = today + timedelta(days=3) #get date of 3 days from today
    return three_days.strftime("%m-%d")


def main():
    if len(sys.argv)==2: #person is manually running program 
        print """Welcome to the Automated Birthday Card Sender!\nEnter your contacts at the prompt. Please stick to the following guidelines when entering contacts:
    Name: Dennis Reynolds
    Street Address: 2253 Bastin Drive
    City: Philadelphia
    State: PA (Pennsylvania is also acceptable)
    Zip Code: 19108
    Birthday: 01-31-2001"""
        if (raw_input("\nAre you a new user? ").lower()=="yes"):
            print "First, please enter your name and address below."
            get_user_address()
        print "Please enter the information for each contact you wish to send a birthday card to."
        contacts = get_contacts()
        for friend in contacts: #add contacts to lob address book
            lob_address = lob.Address.create(
                name=friend.name,
                address_line1=friend.street,
                address_city=friend.city,
                address_state=friend.state,
                address_zip=friend.zipcode,
                metadata={"birthday":friend.birthday}
            )

        print "Please set this script to run every day with the command:"
        print "python birthday.py <lob_api_key> -f"
    else:   #if flag specified at end, this is being run by cron; don't add new users
        #get date 3 days in future; will send out cards today for people with birthdays in 3 days
        birthday_date = futureBirthdays(date.today()) #get string of date 3 days from today (format is MM-DD)

        #use list all addresses function in lob api to search for addresses that have matching metadata for birthday
        birthdays = lob.Address.list(metadata={'birthday':birthday_date}) 
        my_address = lob.Address.list(metadata={'user':True})
        if birthdays.count:
            for birthday in birthdays.data:
                lob.Postcard.create(
                    to_address = birthday,
                    from_address = my_address.data[0],
                    front = '<html style="padding: 1in; font-size: 50;">Front HTML for {{name}}</html>',
                    back = '<html style="padding: 1in; font-size: 20;">Back HTML for {{name}}</html>',
                    data = {"name":birthday.name}
                )
                print "Birthday postcard sent to "+birthday.name
        else:
            print 'no birthdays'
        
        
        


if __name__ == "__main__":
    main()


