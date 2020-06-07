import cv2, numpy, csv

img = cv2.imread("red.jpg")

arq = open("colors.txt")
colors = csv.DictReader(arq,["lilName", "Name", "Code","Red", "Green", "Blue"], delimiter=',')

'''
cv2.imshow('vermelho', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

for row in colors:
    if list(img[0,0]) == list(map(int, [row["Blue"], row["Green"], row["Red"]])):
        print(row["Name"])
        break
    else:
        continue

arq.close()
