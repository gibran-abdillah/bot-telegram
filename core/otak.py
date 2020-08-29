import re 
import random,difflib

deskripsi_bot = """
dalam pengembangan.

"""

help_menu = """
tahap pengembangan

"""

def coba_coba(message):
    try:
      # you can add some feature here ...
       data_logic = {'description':deskripsi_bot,
                     'help':help_menu, 
                     'p':'Ga sopan anjing, salam yang bener',
                     'randquotes':str(random.choice(open('core/txt/quotes.txt').readlines())) # mengambil quotes random 
                     }
       return data_logic[message]
    except KeyError:
        simi = difflib.get_close_matches(message,list(data_logic.keys()))
        if len(simi) == 0:return 'not found bro, /help'
        else:return 'similiar command {}'.format(simi[0])

def membersihkan(message):
    parsing_math = re.findall('([\d\+\-\:]+)',message)
    if len(parsing_math) > 2:
        return eval(parsing_math[0])
    hasil = re.findall('(\w+)',str(message).lower())
    
    return coba_coba(hasil[0])