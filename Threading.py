import threading
import time

val = 0

def workerAdd(i, p):
    global val
    for j in range(1,30):
        val = val + i
        print(val)
        time.sleep(p)


def workerSub(i, p):
    global val
    for j in range(1,30):
        val = val - i
        print(' ', val)
        time.sleep(p)
    return

t1 = threading.Thread(name='Pquick', target=workerAdd, args=(25, 0.2))
t2 = threading.Thread(name='Pslow', target=workerSub, args=(25, 0.225))

t1.start()
time.sleep(0.1)
t2.start()