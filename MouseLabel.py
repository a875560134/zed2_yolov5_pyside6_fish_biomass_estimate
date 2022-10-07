# -*- coding: utf-8 -*-
from PySide6.QtCore import Signal as pyqtSignal
from PySide6.QtWidgets import *


class LabelMouse(QLabel):
    double_clicked = pyqtSignal()

    # 鼠标双击事件
    def mouseDoubleClickEvent(self, event):
        """
        """
        self.double_clicked.emit()

    def mouseMoveEvent(self):
        """
        当鼠标划过标签label2时触发事件
        :return:
        """
        print('当鼠标划过标签label2时触发事件')


class Label_click_Mouse(QLabel):
    clicked = pyqtSignal()

    # 鼠标点击事件
    def mousePressEvent(self, event):
        """
        """
        self.clicked.emit()
