import math
import cv2 as cv
import numpy as np

fileName = "minion.ppm" #input("Enter file name and extension: ")
"""
file = open("Creating My Own IView/" + fileName)
format = file.readline()[:-1]
createdBy = file.readline()[:-1]
dim = file.readline()[:-1].split(" ")
colorRange = file.readline()[:-1]
pixelValues = file.readlines()

print(format)
print(createdBy)
print(dim)
print(colorRange)
print("\n")
print(pixelValues)
"""
img = cv.imread("Creating My Own IView/minion.ppm")
cv.imshow(img)