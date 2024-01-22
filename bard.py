from bardapi import BardCookies
import datetime

cookie_dict={
    "__Secure-1PSID": "fggkjdIZ1RczfSnFBgcZQmiMehpjRnWHmLwhkLETkh04jm6xCQ0ohEzNVy7q36cGQd2H3g.",
    "__Secure-1PSIDTS": "sidts-CjEBPVxjShjZvsqlcGqWOiv9rjRELGlUmSUBEEiIdB-FpKMuJgmc-kXTgu66HwZGPbunEAA",
    "__Secure-1PSIDCC": "ABTWhQHNZlvxgTJVctXQB6ubFsBiFc5NTELLhxPS4aFas1Z7tLjYF2yrQv2ZhwURJze1v9dj710",
    
}
bard=BardCookies(cookie_dict=cookie_dict)

while True:
     Query=input("Enter Your Query")
     Reply=bard.get_answer(Query)['content']
     print(Reply)
     