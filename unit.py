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

    def testContactCreate(self):
        self.assertEqual(self.user.name,"Harry")
        self.assertEqual(self.user.birthday,"07-31-1980")
        self.assertEqual(self.user.address,"4 Privet Drive, Little Whinging, Surrey")


if __name__ == '__main__':
    unittest.main()
