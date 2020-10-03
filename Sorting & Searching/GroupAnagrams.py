"""
Group Anagrams: Write a method to sort an array ot strings so that all tne anagrnms are next to
each other.
"""

def group_anagram(array):
    mydict = {}
    for word in array:
        key = "".join(sorted(word))
        if mydict.get(key) is None:
            mydict[key] = [word]
        else:
            mydict[key].append(word)
    index = 0
    for key  in mydict.keys():
        mylist = mydict[key]
        for word in mylist:
            array[index] = word
            index += 1

if __name__ == '__main__':
    array = ["race","boy","acre"]
    group_anagram(array)
    print(array)
