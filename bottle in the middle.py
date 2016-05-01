import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
import cv2
np.set_printoptions(threshold=np.nan)

fotofile = "uithetmidden.jpg" #"20160217_130858.jpg" 
fotopath = "C:/Users/Jelle/Google Drive/Int. VISION/Vision foto's/Bottles/"
picture = cv2.imread(fotopath + fotofile)
foto = cv2.resize(picture, (480, 700))
vertical, horizontal = foto.shape[:2]
kernel = np.ones((5,5),np.uint8)

cv2.namedWindow('Origineel',cv2.WINDOW_AUTOSIZE)
cv2.moveWindow('Origineel',0,0)
cv2.imshow('Origineel',foto)

foto_gray = cv2.cvtColor(foto, cv2.COLOR_BGR2GRAY)
cv2.namedWindow('Grijs',cv2.WINDOW_AUTOSIZE)
cv2.moveWindow('Grijs',250,0)
cv2.imshow('Grijs',foto_gray)

thresh = 70
foto_bin = cv2.threshold(foto_gray, thresh, 255, cv2.THRESH_BINARY)[1]
cv2.namedWindow('Binary',cv2.WINDOW_AUTOSIZE)
cv2.moveWindow('Binary',500,0)
cv2.imshow('Binary',foto_bin)

foto_linkerzijde = foto_bin[0:vertical, 0:(horizontal/2)]
foto_rechterzijde = foto_bin[0:vertical, horizontal/2:horizontal]

cv2.namedWindow('Linkerzijde',cv2.WINDOW_AUTOSIZE)
cv2.moveWindow('Linkerzijde',800,0)
cv2.imshow('Linkerzijde',foto_linkerzijde)

cv2.namedWindow('Rechterzijde',cv2.WINDOW_AUTOSIZE)
cv2.moveWindow('Rechterzijde',900,0)
cv2.imshow('Rechterzijde',foto_rechterzijde)

total_pix_helft = (horizontal/2) * vertical # Totaal aantal pixels van de helft van de foto
pixels_links  = total_pix_helft - cv2.countNonZero(foto_linkerzijde)
pixels_rechts = total_pix_helft - cv2.countNonZero(foto_rechterzijde)
print('Pixels links: ', pixels_links)
print('Pixels rechts: ', pixels_rechts)

if(pixels_links > pixels_rechts-1000 and pixels_links < pixels_rechts+1000):
    print("In het midden")
else:
    print("Uit het midden") 
