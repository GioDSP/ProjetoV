import cv2
#import numpy
import csv

img = cv2.imread("colorpic.jpg")


def euclidean_distance(color1, color2):
    x = color1[0] - color2[0]
    y = color1[1] - color2[1]
    z = color1[2] - color2[2]
    distance = (x**2 + y**2 + z**2)**0.5
    return distance


def mouse_handler(event, x, y, flags, param):
    global mouseX, mouseY
    if event == cv2.EVENT_LBUTTONDOWN:
        mouseX, mouseY = x, y


arq = open("colors.txt")
colors = list(csv.DictReader(arq, ["lilName", "Name", "Hex", "Red", "Green", "Blue"], delimiter=','))

cv2.imshow('image', img)
cv2.setMouseCallback('image', mouse_handler)

print("Press 'esc' to quit")

while True:

    key = cv2.waitKey(0) & 0xFF

    if key != 27:
        # print(mouseX, mouseY)
        # print(img[mouseY, mouseX])
        color_pix = img[mouseY, mouseX]
        guess = []
        min_dist = 0

        for row in colors:
            [B, G, R] = [int(row["Blue"]), int(row["Green"]), int(row["Red"])]
            dist = euclidean_distance(color_pix, [B, G, R])
            if len(guess) == 0:
                min_dist = dist
                guess.append(row["Name"])
            elif dist < min_dist:
                min_dist = dist
                guess = [row["Name"]]
            elif dist == min_dist:
                guess.append(row["Name"])
            else:
                continue
        print(min_dist)
        print(guess)

    else:
        print("exiting")
        break

cv2.destroyAllWindows()

arq.close()
