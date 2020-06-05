"""
String Compression: Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z).
"""


def stringcompression(string):
    consecutive = 1
    compressed = []
    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            consecutive += 1
        else:
            compressed.append(string[i -1])
            compressed.append(str(consecutive))
            consecutive = 1
        if i == len(string) - 1:
            compressed.append(string[i - 1])
            compressed.append(str(consecutive))
    result = "".join(compressed)
    return result if len(result) < len(string) else string

if __name__ == '__main__':

    string =  "aabcccccaaa"
    print(stringcompression(string))

