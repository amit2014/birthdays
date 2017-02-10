#!/usr/bin/env

#libraries
from datetime import datetime, timedelta
import unittest
import pytz #timezone
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




if __name__ == '__main__':
    unittest.main()
