import sys
import ctypes
from PyQt5.Qt import *
from PyQt5 import QtCore, QtGui, QtWidgets
from config import app
from surfaces.console import Console


class Run():
    def __init__(self):
        self.setup()

    def setup(self):
        self.chuang = QApplication(sys.argv)
        desktop = QApplication.desktop()
        main_screen_rect = desktop.screenGeometry(0)
        x = int((main_screen_rect.width() - 800) / 2)
        y = int((main_screen_rect.height() - 600) / 2)
        # 阴影层
        self.effect_window = QWidget()
        self.effect_window.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.effect_window.setGeometry(x-3, y-3, app["width"]+6, app["height"]+6)
        self.effect_window.setWindowFlags(Qt.FramelessWindowHint)
        self.effect_window.setWindowIcon(QIcon("./resources/icon.png"))
        ####
        self.effect_shadow = QtWidgets.QGraphicsDropShadowEffect(self.effect_window)
        self.effect_shadow.setOffset(0, 0)  # 偏移
        self.effect_shadow.setBlurRadius(10)  # 阴影半径
        self.effect_shadow.setColor(QtCore.Qt.gray)  # 阴影颜色
        # 主层
        self.main_window = QWidget(self.effect_window)
        self.main_window.setGeometry(3, 3, app["width"], app["height"])
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")
        self.main_window.setGraphicsEffect(self.effect_shadow)
        self.setup_console()

    def run(self):
        self.effect_window.show()
        self.main_window.show()
        sys.exit(self.chuang.exec_())

    def setup_console(self):
        Console(self.chuang, self.main_window)