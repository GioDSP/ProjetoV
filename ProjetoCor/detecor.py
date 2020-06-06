import cv2
import csv
import numpy

img = cv2.imread("red.jpg")

arq = open("colors.csv.txt")
colors = csv.DictReader(arq,["nome", "Name", "Código","Red", "Green", "Blue"], delimiter=',')

for row in colors:
    if list(img[0,0]) == list(map(int, [row["Blue"], row["Green"], row["Red"]])):
        print(row["Name"])
        break
    else:
        continue

arq.close()