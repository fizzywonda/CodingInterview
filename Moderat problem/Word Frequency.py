"""
Word Frequencies: Design a method to find the frequency of occurrences of any given word in a
book. What if we were running this algorithm multiple times?
"""

def wordfreq(book,word):
    word = word.lower().strip()
    count = 0
    book = book.split()
    for w in book:
        if w == word:
            count += 1
    return count

"for repitive calls put it in a dictionary "

def dicSetup(book):
    bookdict = {}
    for word in book:
        if word not in bookdict:
            bookdict[word] = 1
        else:
            bookdict[word] += 1

def getFreq(bookdict, word):
    word = word.lower().trim
    if word not in bookdict.keys():
        return False
    else:
        return bookdict[word]
