#!/usr/local/bin/python
# -*- coding: utf-8 -*-

# see http://peaceandhilightandpython.hatenablog.com/entry/2016/02/18/194303
# see http://qiita.com/wwacky/items/98d8be2844fa1b778323

import cv2

faceCascade = cv2.CascadeClassifier('xml/haarcascade_frontalface_default.xml')

img = cv2.imread('img/face/000.jpg', cv2.IMREAD_COLOR)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face = faceCascade.detectMultiScale(gray, 1.1, 3)

if len(face) > 0:
    for rect in face:
        cv2.rectangle(img, tuple(rect[0:2]), tuple(rect[0:2]+rect[2:4]), (0, 0, 255), 2)
else:
    print "no face"

cv2.imwrite('result/detected.jpg', img)
