a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
accumstring=[]

def leftchild(i):
    global a
    n = 2*i+1
    if n >= len(a):
        return None
    return n

def rightchild(i):
    global a
    n = 2*i+2
    if n >= len(a):
        return None
    return n

# Testing left and right child access
# for i in range(0, len(a)):
#     #print(a[i], a[leftchild(i)])
#     print(a[i], a[rightchild(i)])

def VisitNode(i):
    global a
    if i <len(a):
        # print(a[i])
        accumstring.append(a[i])

        if (leftchild(i) == None) and (rightchild(i) == None):
            print (accumstring)
            accumstring.pop(len(accumstring) - 1)
            # print("Leaf reached")
            return

        if (leftchild(i) != None):
            VisitNode(leftchild(i))

        if (rightchild(i) != None):
            VisitNode(rightchild(i))

        accumstring.pop(len(accumstring) - 1)
        # print(accumstring)
        # print("Both visited")

# A is an unfilled  binary tree.
print(a)
# Print all paths from root to leaves
VisitNode(0)