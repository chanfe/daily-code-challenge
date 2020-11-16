# This problem was asked by Microsoft.

# Implement a URL shortener with the following methods:

# shorten(url), which shortens the url into a six-character alphanumeric string, such as zLg6wl.

# restore(short), which expands the shortened string into the original url. If no such shortened string exists, return null.

# Hint: What if we enter the same URL twice?

import random
import string
import hashlib 


def get_random_alphanumeric_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
    return result_str

dict_url = {}
dict_code = {}

def shorten(url):
    if url in dict_url:
        print("url have been used")
        return dict_url[url]

    while True:
        temp = get_random_alphanumeric_string(6)
        if temp in dict_code:
            continue
        else:
            dict_url[url] = temp 
            dict_code[temp] = url
            print("sucess")       
        return temp

def restore(short):
    if short in dict_code:
        return dict_code[short]
    else:
        return "code not in system"

google = shorten("https://www.google.com/")
print("google:", google)
amazon = shorten("https://www.amazon.com/")
print("amazon:", amazon)

google = shorten("https://www.google.com/")
print(restore(google))
print(restore(amazon))
print(restore("jansur"))