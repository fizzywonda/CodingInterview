"""
Paint Fill: Implement the "paint fill" function that one might see on many image editing programs.
That is, given a screen (represented by a two-dimensional array of colors), a point, and a new color,
fill in the surrounding area until the color changes from the original color.
"""

def paint_fill(screen, r, c, color):
    if r < 0 or r > len(screen) or c < 0 or c > len(screen[0]):
        return False
    screen[r][c] = color
    paint_fill(screen, r -1, c, color)  # up
    paint_fill(screen, r, c -1, color)  # left
    paint_fill(screen, r + 1, c, color)  # down
    paint_fill(screen, r, c + 1, color)  # right

    return True


