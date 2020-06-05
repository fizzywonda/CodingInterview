"""
Power Set: Write a method to return all subsets of a set.
"""

def power_set(my_set):
    return power_set2(my_set, 0)


def power_set2(my_set, index, final_set):
    if index == len(my_set) - 1:
        return final_set
    temp_set = get_new_set(final_set, my_set[index])
    add_set(final_set, temp_set)
    return power_set2(my_set, index + 1, final_set)


def get_new_set(final_set, set_element):
    temp = final_set
    for i in temp:
        i.add(set_element)
    return temp


def add_set(final_set, temp_set):
    for i in temp_set:
        final_set.append(i)


def _true():
    print("second parameter")
    return True
def _false():
    print("first")
    return True


a = _false() and _true()
print(a)
