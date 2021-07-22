# Q7. Assuming that we have some email addresses in the "username@companyname.com"
#     format, write a program to print the company name of a given email address. Both user
#     names and company names are composed of letters only.

import re

def split_string():
    email_address = "username@companyname.com"
    split_email_address = re.split('\@|\.',email_address)
    #split_email_address -> ['username', 'companyname', 'com']
    return split_email_address[1] #['username', 'companyname', 'com']

print(split_string())