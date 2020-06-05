"""
Given a string of lowercase ASCII characters, find all distinct continuous palindromic sub-strings of it.
"""
def countSubstrings(s):
    def manachers(s):
        helper_string = '@#' + '#'.join(s) + '#$'
        pal_length = [0] * len(helper_string)
        m = set()
        center = right = 0
        for i in range(1, len(helper_string) - 1):
            if i < right:
                pal_length[i] = min(right - i, pal_length[2 * center - i])
            while helper_string[i + pal_length[i] + 1] == helper_string[i - pal_length[i] - 1]:
                pal_length[i] += 1
                c = pal_length[i]
                w = helper_string[(i - c) : (i + c +1)]
                w = w.split("#")
                w = "".join(w)
                m.add(w)

            if i + pal_length[i] > right:
                center, right = i, i + pal_length[i]
        print(m)
        return m

    #return sum((v+1)/2 for v in manachers(s))

    print(len(manachers(s)))

countSubstrings("mokkori")