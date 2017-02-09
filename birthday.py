#!/usr/bin/env

"""
Class for keeping track of user objects
"""
class Contact:
    def __init__(self,name,birthday=None,address=None):
        self.name = name
        self.birthday = birthday
        self.address = address

    def setAddress(self,address):
        self.address = address

    def setName(self,name):
        self.name = name

    def setAddress(self,address):
        self.address = address



def main():
    #read in birthdays from csv
    print 'birthday' 


if __name__ == "__main__":
    main()
