import numpy as np
import cv2
import matplotlib as plt


drawing = False
mode = True
ix, iy = -1, -1
img2 = 0


# mouse callback function
def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x,y), 100, (255, 0, 0), -1)

def togglestate():
    togglestate.value = 1 ^ togglestate.value # xor value

togglestate.value = 0

def red():
    red.counter += 10
    if (red.counter>255):
        red.counter = 0

def green():
    green.counter += 10
    if (green.counter>255):
        green.counter = 0

def blue():
    blue.counter += 10
    if (blue.counter>255):
        blue.counter = 0

red.counter = 150
green.counter = 150
blue.counter = 150


def draw_color_circle(event, x, y, flags, param):

    global drawing, ix, iy, img2, img

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
        cv2.circle(img, (x, y), 10, (red.counter, green.counter, blue.counter), -1)
        img2 = img

    if event == cv2.EVENT_MOUSEMOVE:
        if drawing:
         cv2.imshow('I0', img2)
         cv2.rectangle(img2, (ix, iy), (x, y), (red.counter, green.counter, blue.counter), 1)

    if event == cv2.EVENT_RBUTTONDBLCLK:
        blue()
        cv2.rectangle(img, (ix, iy), (x, y), (red.counter, green.counter, blue.counter), 1)
        cv2.circle(img, (x, y), 50, (red.counter, green.counter, blue.counter), -1)

    # if event == cv2.EVENT_MBUTTONDBLCLK:
    #     green()
    #     cv2.circle(img, (x, y), 50, (red.counter, green.counter, blue.counter), -1)

    if event == cv2.EVENT_LBUTTONUP:
        drawing = False
        #cv2.rectangle(img, (ix, iy), (x, y), (red.counter, green.counter, blue.counter), 1)
        #cv2.circle(img, (x, y), 10, (red.counter, green.counter, blue.counter), -1)
        cv2.imshow('I0', img)


print("drawTest Start")
img = cv2.imread("C:\\users\\hvajaria\\Desktop\\girl2.jpg", cv2.IMREAD_COLOR)

cv2.namedWindow('I0')
cv2.setMouseCallback('I0', draw_color_circle)

while (1):
    cv2.imshow('I0', img)
    if cv2.waitKey(20) & 0xFF == 27:
        break;

cv2.destroyAllWindows()
# events = [i for i in dir(cv2) if 'EVENT' in i]
# print (events)

print("drawTest Done")