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
Prompt user to enter info about contacts
Return a list of Contact objects
"""
def get_contacts():
    print """Welcome to the Automated Birthday Card Sender!\nEnter your contacts at the prompt. Please stick to the following guidelines when entering contacts:
    Name: Dennis Reynolds
    Street Address: 2253 Bastin Drive
    City: Philadelphia
    State: PA (Pennsylvania is also acceptable)
    Zip Code: 19108
    Birthday: 01-31-2001"""

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
    #TODO: Check for flag at runtime that indicates if this is run by user or cron
    key = sys.argv[1]
    #log into Lob
    lob.api_key = key
    
    if len(sys.argv)==3: #if flag specified at end, this is being run by cron; don't add new users
        contacts = get_contacts()
        for friend in contacts:
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
    #else:
        

    ##get date 3 days in future; will send out cards today for people with birthdays in 3 days
    #birthday_date = futureBirthdays(date.today()) #get string of date 3 days from today (format is MM-DD)

    ##check birthdays dict for birthday_date
    #if birthday_date in birthdays:
    #    lob.api_key = key
    #    for friend in birthdays[birthday_date]: #loop through list of Contact objects
    #        if friend.adr_: #if user has a Lob address ID assigned to them (already in Lob address book)
    #            lob_address = lob.Address.retrieve(friend.adr_)
    #        else:
    #            #create new address in Lob
    #            lob_address = createLobAddress(friend)
    #            #TODO: Save to CSV file or database
    #    #send postcard


if __name__ == "__main__":
    main()


