
color = ["y1", "y2", "y3", "y4", "y5", "y6"]
node = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]
edges = ["a-b", "b-c", "b-d", "a-c", "c-h", "c-d", "d-h", "d-e", "d-f", "e-f", "e-g", "e-h",
         "f-g", "g-j", "j-k", "h-g", "h-i"]

print("min ", end="")
for i in range(len(node)):
    for j in range(len(color)):
        if i == len(node)-1 and j == len(color)-1:
            print(color[j]+node[i])
        else:
            print(color[j] + node[i] + "+", end="")
    print("")
print("st")

for i in range(len(node)):
    print("\t", end="")
    for j in range(len(color)):
        if j == len(color)-1:
            print(color[j] + node[i] + "=1")
        else:
            print(color[j] + node[i] + "+", end="")
print("")

for i in edges:
    node1, node2 = tuple(i.split("-"))
    print("\t" + "!Edge " + node1 + " - " + node2)
    for j in color:
        print("\t" + j + node1 + "+" + j + node2 + "<=1")
    print("")

# x = 1
# for i in color:
#     for j in node:
#         print("\t" + i + ">=" + str(x) + j)
#     x += 1

print("end")
print("inte 66")