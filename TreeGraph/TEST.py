# Write your Python program in this editor
# 1) Press Run button to compile


def output(data):
    # your code goes here
    row = int(data.pop())
    col = int(data.pop())

    classroom = [["."] * col for i in range(row)]
    for i in range(row):
        line = data.pop()
        for j in range(len(line)):
            if line[j] == "+":
                classroom[i][j] = "+"

    return max_no_student(classroom)


def max_no_student(classroom):
    count = 0
    for row in range(len(classroom)):
        for col in range(len(classroom[row])):
            if (classroom[row][col] != False and classroom[row][col] != "+") and check_srnd(classroom, row, col):
                classroom[row][col] = True
                disable(classroom, row, col)
                count += 1
    return count


def check_srnd(classroom, row, col):
    # check top left
    if row - 1 >= 0 and col - 1 >= 0:
        if classroom[row - 1][col - 1] == True:
            return False

    # check top right
    if row - 1 >= 0 and col + 1 <= len(classroom[row]) - 1:
        if classroom[row - 1][col + 1] == True:
            return False

    # check left
    if col - 1 >= 0:
        if classroom[row][col - 1] == True:
            return False

    # check right
    if col + 1 <= len(classroom[row]) - 1:
        if classroom[row][col + 1] == True:
            return False

    # check down left
    if row + 1 <= len(classroom) - 1 and col - 1 >= 0:
        if classroom[row + 1][col - 1] is True:
            return False

    #  check down right
    if row + 1 <= len(classroom) - 1 and col + 1 <= len(classroom[row]) - 1:
        if classroom[row + 1][col + 1] is True:
            return False

    return True


def disable(classroom, row, col):
    # disable top left
    if row - 1 >= 0 and col - 1 >= 0:
        classroom[row - 1][col - 1] = False

    # disable top right
    if row - 1 >= 0 and col + 1 <= len(classroom[row]) - 1:
        classroom[row - 1][col + 1] = False

    # disable left
    if col - 1 >= 0:
        classroom[row][col - 1] = False

    # disable right
    if col + 1 <= len(classroom[row]) - 1:
        classroom[row][col + 1] = False

    # disable down left
    if row + 1 <= len(classroom) - 1 and col - 1 >= 0:
        classroom[row + 1][col - 1] = False

    #  disable down right
    if row + 1 <= len(classroom) - 1 and col + 1 <= len(classroom[row]) - 1:
        classroom[row + 1][col + 1] = False


data = []
data.append(str(input()))
rows = int(data[0])

while rows > -1:
    data.insert(0, str(input()))
    rows -= 1

print(output(data))