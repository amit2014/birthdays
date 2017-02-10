#!/usr/bin/env

#libraries
from datetime import datetime, timedelta
import unittest
import lob
#my modules
import birthday


##################
# Tests for Lib  #
##################

class TestContactClass(unittest.TestCase):

    def setUp(self):
        self.user = birthday.Contact("Harry Potter","07-31","4 Privet Drive","Little Whinging","Surrey","55555")

    def testCreateContact(self):
        self.assertEqual(self.user.name,"Harry Potter")
        self.assertEqual(self.user.birthday,"07-31")
        self.assertEqual(self.user.street,"4 Privet Drive")
        self.assertEqual(self.user.city,"Little Whinging")
        self.assertEqual(self.user.state,"Surrey")


class TestDataRead(unittest.TestCase):

    def setUp(self):
        self.birthdays = birthday.getBirthdays("contacts.csv")

    def testDictionaryCreate(self):
        self.assertTrue(self.birthdays)

    def testBirthdayInDict(self):
        self.assertTrue("02-23" in self.birthdays)

    def testBirthdayNotInDict(self):
        self.assertFalse("02-22" in self.birthdays)


class Test3DayDate(unittest.TestCase):

    def testDate(self):
        #test with an old date
        date = datetime.strptime("02-09","%m-%d") #create datetime object from chosen date string
        future = birthday.futureBirthdays(date)
        self.assertEqual(future,"02-12")

#class TestLobAddress(unittest.TestCase):
#
#    def setUp(self):
#        self.user = birthday.Contact("Harry Potter","07-31","4 Privet Drive","Little Whinging","Surrey","55555")
#    
#    def testCreateLobAddress(self):
#        address = birthday.createLobAddress(self.user)
#        self.user.setAdr_(address.id)
#        self.assertEqual(address.id,lob.Address.retrieve(friend.adr_).id)
#
#    def tearDown(self):
#        lob.Address.delete(self.user.adr_)


if __name__ == '__main__':
    unittest.main()
