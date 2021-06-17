import re
import os
import random

class Email:

    @staticmethod
    def is_valid(email):
        regex = re.compile("(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", re.IGNORECASE)
        return regex.search(email) != None

    @staticmethod
    def random():        
        file = open(os.path.realpath('dummy/emails.txt'))
        print(file.readlines()[random.randint(0, 499)].strip())
    