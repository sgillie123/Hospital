# loads the ui file and does the scalling

import os
from PyQt6 import QtCore
from PyQt6.QtWidgets import QDialog, QWidget
from PyQt6.QtCore import QRect
from PyQt6.uic import loadUi

# path to the ui folder
UI_DIR = os.path.join(os.path.dirname(__file__), "ui")

# this holds all the screens i think
state = {}

# go to a screen by number
def go(i): state["widget"].setCurrentIndex(i)

# making the screen class
class Screen(QDialog):
    def __init__(self, ui):
        super().__init__()
        # load the ui file from the ui folder
        loadUi(os.path.join(UI_DIR, ui), self)
        self._bw, self._bh = self.width(), self.height()
        # timer thing so it waits before snapshotting
        QtCore.QTimer.singleShot(0, self._snapshot)

    # saves original positions
    def _snapshot(self):
        for c in self.findChildren(QWidget):
            if c.parent() is self:
                g = c.geometry()
                # store x y w h
                c._g = (g.x(), g.y(), g.width(), g.height())

    # this makes it resize properly
    def resizeEvent(self, e):
        super().resizeEvent(e)
        # calculate the scale
        sx, sy = self.width() / self._bw, self.height() / self._bh
        for c in self.findChildren(QWidget):
            if c.parent() is self and hasattr(c, '_g'):
                x, y, w, h = c._g
                # set new geometry
                c.setGeometry(QRect(int(x*sx), int(y*sy), int(w*sx), int(h*sy)))