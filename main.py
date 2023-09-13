import sys
import os
from PyQt5 import QtWidgets, QtCore, QtGui
import tkinter as tk

from skimage.metrics import structural_similarity as ssim

from typing import List
from numpy.core.numeric import _tensordot_dispatcher
from numpy.core.numerictypes import sctype2char



import cv2 as cv
import numpy as np
from PIL import ImageGrab, Image, ImageChops

import time

from threading import Timer



global listingy
listingy = []


global testor
testor = 1

global x1
# x1 = 0
global y1
# y1 = 0
global x2
# x2 = 0
global y2
# y2 = 0


dodad = 0

test1 = "yonska"


global score1
score1 = 1

def namechange():
    global dodad
    dodad = dodad + 1
    global test2
    test2 = str(dodad)
    global output
    output = test1 + test2
    global outputfinal
    outputfinal = output + ".png"


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        root = tk.Tk()
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        self.setGeometry(0, 0, screen_width, screen_height)
        self.setWindowTitle(' ')
        self.begin = QtCore.QPoint()
        self.end = QtCore.QPoint()
        self.setWindowOpacity(0.3)
        QtWidgets.QApplication.setOverrideCursor(
            QtGui.QCursor(QtCore.Qt.CrossCursor)
        )
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        print('Capture the screen...')
        self.show()

    def paintEvent(self, event):
        qp = QtGui.QPainter(self)
        qp.setPen(QtGui.QPen(QtGui.QColor('black'), 3))
        qp.setBrush(QtGui.QColor(128, 128, 255, 128))
        qp.drawRect(QtCore.QRect(self.begin, self.end))

    def mousePressEvent(self, event):
        self.begin = event.pos()
        self.end = self.begin
        self.update()

    def mouseMoveEvent(self, event):
        self.end = event.pos()
        self.update()

    def mouseReleaseEvent(self, event):
        self.close()


        global x1
        # x1 = 0
        global y1
        # y1 = 0
        global x2

        global y2
      



        x1 = min(self.begin.x(), self.end.x())
        y1 = min(self.begin.y(), self.end.y())
        x2 = max(self.begin.x(), self.end.x())
        y2 = max(self.begin.y(), self.end.y())

        print(x1)
        print(y1)
        print(x2)
        print(y2)
        testothing()


def imgGrab():
    pass

def comparasonthing():

        global imgt
        global img1_np
        global score1

        resized_orig = cv.resize(img1_np, (300, 200))
        resized_mod = cv.resize(img_npt, (300, 200))

        gray_orig = cv.cvtColor(resized_orig, cv.COLOR_BGR2GRAY)
        gray_mod = cv.cvtColor(resized_mod, cv.COLOR_BGR2GRAY)
        

        (score, diff) = ssim(gray_orig, gray_mod, full=True)
        diff = (diff * 255).astype("uint8")

        if score >= 0.98:
            pass

        elif (abs(score1-score)) >= 0.01:
            print("this is score 1: " + format(score1))
            print("this is score: " + format(score))
            print("this is the difference between them: " + format(abs(score1-score)))
            score1 = score
            namechange()
            global outputfinal
            cv.imwrite(outputfinal, img_npt)
            img1_np = img_npt
        else:
            pass



def testothing():
    global img1
    img1 = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    global img1_np
    img1_np = np.array(img1)
    # frame1 = cv.cvtColor(img1_np, cv.COLOR_BGR2GRAY)
    # cv.imshow("frame", frame1)
    cv.imwrite("firstyonk.png", img1_np)
    key1 = cv.waitKey(1)



    if key1 == 27:
        pass

    while(True):
        # imgGrab()


        global imgt
        imgt = ImageGrab.grab(bbox=(x1, y1, x2, y2))
        global img_npt
        img_npt = np.array(imgt)
        # frame = cv.cvtColor(img_npt, cv.COLOR_BGR2GRAY)
        # cv.imshow('frame', frame)



        comparasonthing()
        time.sleep(2)
        key = cv.waitKey(1)
        if key == 27:
            break

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    app.aboutToQuit.connect(app.deleteLater)
    sys.exit(app.exec_())

    
cv.waitKey(0)
cv.destroyAllWindows