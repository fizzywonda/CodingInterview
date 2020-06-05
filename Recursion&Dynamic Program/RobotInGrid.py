"""
Robot in a Grid: Imagine a robot sitting on the upper left corner of grid with r rows and c columns.
The robot can only move in two directions, right and down, but certain cells are "off limits" such that
the robot cannot step on them. Design an algorithm to find a path for the robot from the top left to
the bottom right.
"""


def find_path1(maze):
    path = []
    if find_path(maze, 0, 0, path):
        return path
    return None


def find_path(maze, row, col, path):
    if row > len(maze) - 1 or col > len(maze[0]) - 1 or not maze[row][col]:
        return False

    end = row == len(maze) - 1 and col == len(maze[0]) -1
    if end or find_path(maze, row + 1, col, path) or find_path(maze, row, col + 1, path):
        p = [row, col]
        path.append(p)
        return True
    return False

"""
Dynamic programming approach
"""


def find_path_2(maze):
    path = []
    visited_point = set()
    if find_path2(maze, 0, 0, path, visited_point):
        return path
    return None


def find_path2(maze, row, col, path, visited_point):
    if row > len(maze) - 1 or col > len(maze[0]) - 1 or not maze[row][col]:
        return False

    p = (row, col)

    if p in visited_point:
        return False

    end = row == len(maze) - 1 and col == len(maze[0]) -1
    if end or find_path2(maze, row + 1, col, path, visited_point) or find_path2(maze, row, col + 1, path, visited_point):
        path.append(p)
        return True

    visited_point.add(p)
    return False

if __name__ == '__main__':
    maze = []
    maze.append(["s", False, False])
    maze.append([True, False, False])
    maze.append([True, True, False])
    maze.append([False, True, "e"])

    path = find_path1(maze)
    print(path)



