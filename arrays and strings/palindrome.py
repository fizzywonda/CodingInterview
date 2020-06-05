"""
Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome.
A palindrome is a word or phrase that is the same forwards and backwards. A permutation
is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
1.5
1.6
EXAMPLE
Input: Tact Coa
Output: True (permutations: "taco cat", "atco eta", etc.)
"""

def palindrome(string):


    def getCharFreq(string):
        charfreq= {}
        for i in string:
                if i != " ":
                    if i in charfreq.keys():
                        charfreq[i] += 1
                    else:
                        charfreq[i] = 1
        return charfreq

    def checkmaxOdd(charfreq):
        NumOfOddString = 0
        for i in charfreq.values():
            if i % 2 == 1:
                if NumOfOddString < 1:
                    NumOfOddString += 1
                else:
                    return False
        return True

    charfreq = getCharFreq(string)
    return checkmaxOdd(charfreq)

def main():
    x = "tact coa"
    print(palindrome(x))

main()

