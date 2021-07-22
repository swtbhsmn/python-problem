# Q7. Assuming that we have some email addresses in the "username@companyname.com"
#     format, write a program to print the company name of a given email address. Both user
#     names and company names are composed of letters only.

import re

email_address = "username@companyname.com"

split_email_address = re.split('\@|\.',email_address)

print(split_email_address) #['username', 'companyname', 'com']
