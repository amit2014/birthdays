Automated Birthday Card Sender

To run, type "python birthday.py <your_lob_key>"
The first time you run, you will need to input your name and address.
Next, enter the name, birthdays, and addresses of your friends that you wish to send birthday postcards to.
Finally, open a crontab and set a new cronjob for this file to be run every day at noon:
0 12 * * * python birthday.py <your_lob_key> -f


TODO:
- input checking and correcting for zip code, birthday
- address verification via lob
- postcard creation
- send SMS or email to user letting them know that message was sent



