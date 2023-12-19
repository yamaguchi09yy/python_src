l = ['Mon','tue','Wed','Thu','Fri','sat','Sun']

def change_words(words, func):
    for word in words:
        print(func(word))
        
def sample_func(word):
    return word.capitalize() #大文字にする

change_words(l,sample_func)