import re
import random
import string

class Str:

    @staticmethod
    def is_a_string(data):
        return type(data) == str

    @staticmethod
    def ends_with(data, ending, ignoreCase = False):
        
        if not Str.is_a_string(data) or not Str.is_a_string(ending):
            Str.__throw_not_string_exception()

        case = 0
        if(ignoreCase == True):
            case = re.IGNORECASE
        
        regex = re.compile(str(ending) + '$', case)

        return regex.search(str(data)) != None

    @staticmethod
    def starts_with(data, start, ignoreCase = False):

        if not Str.is_a_string(data) or not Str.is_a_string(start):
            Str.__throw_not_string_exception()

        case = 0
        if(ignoreCase == True):
            case = re.IGNORECASE
        
        regex = re.compile('^' + str(start), case)

        return regex.search(str(data)) != None

    @staticmethod
    def after(string, limit):

        if not Str.is_a_string(string) or not Str.is_a_string(limit):
            Str.__throw_not_string_exception()

        if limit.strip() == '':
            return string

        stringToList = string.split(limit, 2)
        stringToList.reverse()
        
        return stringToList[0].strip()

    @staticmethod
    def before(string, limit):

        if not Str.is_a_string(string) or not Str.is_a_string(limit):
            Str.__throw_not_string_exception()

        if limit.strip() == '':
            return string

        return string.split(limit, 2)[0].strip()

    @staticmethod
    def contains(string, search, ignoreCase = False):

        if not Str.is_a_string(string) or not Str.is_a_string(search):
            Str.__throw_not_string_exception()

        case = 0
        if(ignoreCase == True):
            case = re.IGNORECASE
        regex = re.compile(str(search), case)

        return regex.search(str(string)) != None


    @staticmethod
    def limit(string, limit, ellipses = True):

        if not Str.is_a_string(string):
            Str.__throw_not_string_exception()

        if Str.__is_not_an_integer(limit):
            Str.__throw_not_an_integer_exception(limit)

        if len(string) <= limit:
            return string

        result = string[:limit]

        if ellipses == True:
            result += '...'

        return result

    @staticmethod
    def random(length):   

        if Str.__is_not_an_integer(length):
            Str.__throw_not_an_integer_exception(length)

        return ''.join(random.choices(string.ascii_letters, k = length))

    @staticmethod
    def __throw_not_string_exception():
        raise TypeError('Some of the given args are not a string')

    @staticmethod
    def __throw_not_an_integer_exception(arg):
        raise TypeError(f'{arg} is not an integer')

    @staticmethod
    def __is_not_an_integer(integer):
        return type(integer) != int
