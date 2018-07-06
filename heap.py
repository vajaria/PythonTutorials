import numpy as np
import cv2
import matplotlib as plt
import math
len = 9
filled = 9


def parent(k):
    global filled
    # should never happen
    if k > filled-1:
        return None
    n = int(math.floor((k-1)/2))
    # happens when parent of root is called
    if n < 0:
        return None
    return n


def leftchild(k):
    global filled
    n = 2*k+1
    if n > filled-1:
        return None
    return n


def rightchild(k):
    global filled
    n = 2*k+2
    if n > filled-1:
        return None
    return n


def heapifyup(a,i):
    if i <= 0:
        return
    p = parent(i)
    if a[i] > a[p]:
        t = a[p]
        a[p] = a[i]
        a[i] = t
    heapifyup(a, p)


def heapifydown(a,i):
    P = None
    if i < 0:
        return
    if i>filled:
        return
    L = leftchild(i)
    # if Left child is empty - nothing to do
    if (L==None or a[L] == None):
        return
    else:
        P = L

    # if valid right child, test with left child
    R = rightchild(i)
    if not(R == None or a[R] == None):
       if (a[R] > a[L]):
            P = R

    if a[i] < a[P]:
        t = a[P]
        a[P] = a[i]
        a[i] = t
        heapifydown(a, P)


def pop(ar):
    global filled
    global len
    global a
    if (filled==0):
        return None
    else:
        top  = ar[0]
        ar[0] = ar[filled-1]
        ar[filled - 1] = None
        filled = filled - 1
        heapifydown(ar, 0)
        b = [None] * int(len / 2)
        if filled <= len/4:
            b[0:filled]=ar[0:filled]
            a = b
            len = int(len/2)
            return top
        else:
            a = ar
            return top

def insert(ar,i):
    global len
    global filled
    global a
    b = [None] * len * 2
    if (len == filled):
        b[0:len]=ar[0:len]
        a=b
        len = len * 2

    a[filled] = i
    filled = filled + 1
    heapifyup(a, filled-1)

a = [2, 3, 5, 10, 1, 17, 23, 6, 0]
print(a)

## For testing Parent and Child access
# for i in range(0, len):
#     print(i)
#     if (parent(i) != None):
#         print('           parent {0}'.format(a[parent(i)]))
#     print('               node {0}'.format(a[i]))
#     if (leftchild(i) != None):
#         print('left{0}'.format(a[leftchild(i)]))
#     if (rightchild(i) != None):
#         print('                    right{0}'.format(a[rightchild(i)]))

## test heapify call - 23 should rise to top
# heapifyup(a, 6)
# print(a)

# Heapify the entire array
for i in range(0, filled-1, 1):
    heapifyup(a,i)
    print(a)

# test repeated insertions
insert(a,100)
print(a)
print('len {0} filled {1}').format(len, filled)

insert(a,200)
print(a)
print('len {0} filled {1}').format(len, filled)

insert(a,50)
print(a)
print('len {0} filled {1}').format(len, filled)

# test repeated deletions
for i in range(0, 13):
    x = pop(a)

# test reinsertions
print("Re-insertions")

insert(a,1)
print(a)
print('filled {0} len {1}'.format(filled, len))

insert(a,2)
print(a)
print('filled {0} len {1}'.format(filled, len))

insert(a,50)
print(a)
print('filled {0} len {1}'.format(filled, len))

insert(a,5)
print(a)
print('filled {0} len {1}'.format(filled, len))

insert(a,3)
print(a)
print('filled {0} len {1}'.format(filled, len))