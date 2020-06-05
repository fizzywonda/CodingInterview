"""G(v)"""

for i in vertices:
    numberOfVistedNode = 0
    while i has child:
        depthFirstSearch(i)
        i = childof(i)
        numberOfVistedNode += 1
    if vertices.length == numberOfVistedNode:
        return getPath(i)

def getPath(x):
    path= [x]
    while x.parent != None:
        path.insert(0,x.parent)
        x = x.parent

    return path