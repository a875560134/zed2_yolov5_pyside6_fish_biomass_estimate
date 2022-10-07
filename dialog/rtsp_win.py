# -*- coding: utf-8 -*-
import sys

from PySide6.QtWidgets import *

from dialog.rtsp_dialog import Ui_Form


class Window(QWidget, Ui_Form):
    """
    """

    def __init__(self):
        super(Window, self).__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication()
    window = Window()
    window.show()
    sys.exit(app.exec_())
