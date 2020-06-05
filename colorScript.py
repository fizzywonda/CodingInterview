
color = ["c1", "c2", "c3", "c4", "c5", "c6"]
node = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"]
edges = ["a-b", "b-c", "b-d", "a-c", "c-h", "c-d", "d-h", "d-e", "d-f", "e-f", "e-g", "e-h",
         "f-g", "g-j", "j-k", "h-g", "h-i"]

print("min ", end="")
for i in range(len(color)):
    if i == len(color)-1:
        print(color[i])
    else:
        print(color[i] + "+", end="")

print("st")

for i in range(len(node)):
    print("\t", end="")
    for j in range(1, len(color)+1):
        if j == len(color):
            print(node[i] + str(j) + "=1")
        else:
            print(node[i]+str(j) + "+", end="")
print("")

for i in edges:
    node1, node2 = tuple(i.split("-"))
    print("\t" + "!Edge " + node1 + " - " + node2)
    for j in color:
        print("\t" + node1 + j + "+" + node2 + j + "<=1")
    print("")

x = 1
for i in color:
    for j in node:
        print("\t" + i + ">=" + str(x) + j)
    x += 1

print("end")
print("inte 6")