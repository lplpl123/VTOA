from PyQt5.Qt import *
from PyQt5.QtCore import Qt, pyqtSignal
from tools.storage import Storage


class MyWindow(QWidget):
    clicked = pyqtSignal()


    def __init__(self, parent=None):
        super().__init__(parent)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag = True
            self.offset = event.globalPos() - self.pos()

    def mouseMoveEvent(self, event):
        if self.drag:
            new_pos = event.globalPos() - self.offset
            self.move(new_pos)

    def mouseReleaseEvent(self, event):
        if self.drag and event.button() == Qt.LeftButton:
            self.drag = False


class MyWorkFrame(QFrame):
    clicked = pyqtSignal()


    def __init__(self, parent=None):
        super().__init__(parent)

    def mousePressEvent(self, event):
        pass

    def mouseMoveEvent(self, event):
        pass

    def mouseReleaseEvent(self, event):
        pass

# 标题按钮
class MyQLabel(QLabel):
    clicked = pyqtSignal()

    def __init__(self, parent=None):
        super(MyQLabel, self).__init__(parent)
        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet("""
                            QWidget{
                            font-family: "微软雅黑";
                            font-size: 25px;
                            color: white;
                            border-radius:5px;
                            border-image:none;
                            background-color:black;}
                            
                            QLabel:hover{
                            border:3px solid white;}
                            """)

    def mouseReleaseEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:  # 判断左键按下
            self.clicked.emit()


class MyQLabelFormat(QLabel):
    clicked = pyqtSignal()

    def __init__(self, parent=None):
        super(MyQLabelFormat, self).__init__(parent)
        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet("""
                            QWidget{
                            font-family: "微软雅黑";
                            font-size: 20px;
                            color: black;
                            border-radius:5px;
                            border-image:none;
                            background-color:white;}
                            QLabel:hover{
                            border:3px solid black;}
                            """)

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
                            color: black;}
                            QWidget::pressed{
                            background-color: gray;}
                        """)

    def mouseReleaseEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:  # 判断左键按下
            self.clicked.emit()


class DragFileLabel(QLabel):
    clicked = pyqtSignal()

    def __init__(self, parent=None, page_index=0):
        super(DragFileLabel, self).__init__(parent)
        self.setAcceptDrops(True)
        self.page_index = page_index

    def mouseReleaseEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:  # 判断左键按下
            self.clicked.emit()

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        for url in event.mimeData().urls():
            file_path = url.toLocalFile()

            file_format = file_path.rsplit(".", 1)[1]
            file_list = Storage().get_info("video_file_types")
            if file_format not in file_list:
                self.setText("请上传正确的格式文件")
                return

            storage = Storage()
            storage.store_info("selected_file_path", file_path)
            self.setText(file_path)
            change_process_button_style(self.page_index, True)


def change_process_button_style(page_index, active):

    pages = ["extract_frame", "audio_transfer_frame", "voice_split_frame", "bgm_split_frame"]
    storage = Storage()

    frame_dict = storage.get_info("frame_dict")
    frame = frame_dict[pages[page_index]]

    qss_active_true = """QLabel{
                                    font-family: "微软雅黑";
                                    font-size: 20px;
                                    background-color: black;
                                    border-radius:15px;
                                    color: white;}
                                    QLabel::hover{
                                    color: grey;}"""

    qss_active_false = """
                            QLabel{
                                    font-family: "微软雅黑";
                                    font-size: 20px;
                                    background-color: black;
                                    border-radius:15px;
                                    color: gray;}"""

    qss_active_true_vice = """
                            QLabel{
                                    font-family: "微软雅黑";
                                    color: black;
                                    border: 3px solid black;}
                            QLabel:hover{
                                    background-color: gray;}
    """

    qss_active_false_vice = """
                            QLabel{
                                    font-family: "微软雅黑";
                                    color: black;
                                    border: 3px solid black;}
    """

    if active:
        frame.format_extract_button.setStyleSheet(qss_active_true)
        frame.select_output_button.setStyleSheet(qss_active_true_vice)
        frame.format_button.setStyleSheet(qss_active_true_vice)

    else:
        frame.format_extract_button.setStyleSheet(qss_active_false)
        frame.select_output_button.setStyleSheet(qss_active_false_vice)
        frame.format_button.setStyleSheet(qss_active_false_vice)




