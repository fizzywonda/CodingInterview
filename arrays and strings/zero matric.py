"""
Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
"""
def zeromatrix(matrix):
    rowcol = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                rowcol.append((i, j))

    for row, col in rowcol:
        for i in range(len(matrix[row])):
            matrix[row][i] = 0

        for j in range(len(matrix)):
            if j == row:
                continue
            else:
                matrix[j][col] = 0

    return matrix

def printmatrix(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            print(matrix[row][col], end ='')
        print("\n")

if __name__ == '__main__':

    matrix = [[1,8,3],[2,4,0],[1,3,9]]

    zeroresult = zeromatrix(matrix)
    printmatrix(zeroresult)

