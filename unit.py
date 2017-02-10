#!/usr/bin/env

#libraries
from datetime import datetime, timedelta
import unittest
#my modules
import birthday


##################
# Tests for Lib  #
##################

class TestContactClass(unittest.TestCase):

    def setUp(self):
        self.user = birthday.Contact("Harry","07-31-1980","4 Privet Drive, Little Whinging, Surrey")

    def testCreateContact(self):
        self.assertEqual(self.user.name,"Harry")
        self.assertEqual(self.user.birthday,"07-31-1980")
        self.assertEqual(self.user.address,"4 Privet Drive, Little Whinging, Surrey")

    def testUpdateContact(self):
        self.user.setName("Ron")
        self.user.setBirthday("03-01-1980")
        self.user.setAddress("The Burrow, Ottery St. Catchpole, Devon")
        self.assertEqual(self.user.name,"Ron")
        self.assertEqual(self.user.birthday,"03-01-1980")
        self.assertEqual(self.user.address,"The Burrow, Ottery St. Catchpole, Devon")

    def tearDown(self):
        #need to make sure it goes back to the way it was when first set
        self.user = birthday.Contact("Harry","07-31-1980","4 Privet Drive, Little Whinging, Surrey")


class TestDataRead(unittest.TestCase):

    def setUp(self):
        self.birthdays = birthday.getBirthdays("contacts.csv")

    def testDictionaryCreate(self):
        self.assertTrue(self.birthdays)

    def testBirthdayInDict(self):
        self.assertTrue("02-23-1977" in self.birthdays)

    def testBirthdayNotInDict(self):
        self.assertFalse("02-22-1977" in self.birthdays)


class Test3DayDate(unittest.TestCase):

    def testDate(self):
        #test with an old date
        date = datetime.strptime("02-09-2017","%m-%d-%Y") #create datetime object from chosen date string
        future = birthday.futureBirthdays(date)
        self.assertEqual(future,"02-12-2017")



if __name__ == '__main__':
    unittest.main()
