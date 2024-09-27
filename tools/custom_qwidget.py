import threading

from PyQt5.Qt import QLabel, QPushButton, QComboBox
from PyQt5.QtCore import Qt, pyqtSignal


# 标题按钮
class MyQLabel(QLabel):
    clicked = pyqtSignal()

    def __init__(self, parent=None):
        super(MyQLabel, self).__init__(parent)

    def mouseReleaseEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:  # 判断左键按下
            self.clicked.emit()

# 菜单按钮
class MyQLabel_01(QLabel):
    clicked = pyqtSignal()

    def __init__(self, parent=None):
        super(MyQLabel_01, self).__init__(parent)
        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet("""
                            QWidget{
                            font-family: "微软雅黑";
                            font-size: 20px;
                            background-color: white;
                            color: black;
                            border: none;}
                            QWidget::hover{
                            color: red;}
                        """)

    def mouseReleaseEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:  # 判断左键按下
            self.clicked.emit()

class MyButton(QPushButton):

    def __init__(self, parent=None):
        super(MyButton, self).__init__(parent)
        self.setFocusPolicy(Qt.NoFocus)
        self.setFlat(True)
        self.setStyleSheet("""
                            QPushButton{
                            color: black;
                            font-family: "微软雅黑";
                            font-size: 30px;
                            background-color: white;}

                            QPushButton::hover{
                            color: red;
                            font-size: 35px;}

                            QPushButton::pressed{
                            border: 0px solid white;}
                        """)