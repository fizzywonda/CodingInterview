"""
Permutations with Duplicates: Write a method to compute all permutations of a string whose
characters are not necessarily unique. The list of permutations should not have duplicates.
"""


def permdwithDup(string):
    result = set()
    return perm(string, 0, result)

def perm(string, index, result):
    if index == len(string):
        return result
    result = getnextperm(string, index, result)
    return perm(string, index + 1, result)


def getnextperm(string, index, result):
    if index == 0:
        result.add(string[0])
        return result
    else:
        temp_result = set()
        new_char = string[index]
        for word in result:
            for i in range(len(word) + 1):
                new_word = insertchar(word, i, new_char)
                if new_word not in temp_result:
                    temp_result.add(new_word)
    return temp_result


def insertchar(word, index, char):
    start = word[:index]
    end = word[index :]
    return start + char + end

if __name__ == '__main__':
    string = "abca"
    permutations = permdwithDup(string)
    print(permutations)