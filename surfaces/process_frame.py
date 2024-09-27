from PyQt5.Qt import QFrame, QLabel, QMovie, QSize
from PyQt5.QtCore import Qt
from tools import custom_qwidget
from tools import backend_function


class ProcessFrame:

    def __init__(self, main_surface):
        self.main_surface = main_surface

    def _setup_work_process_frame_widgets(self):
        # work_process_frame
        self.work_process_frame = QFrame(self.main_surface.work_frame)
        self.work_process_frame.setGeometry(0, 15, 800, 585)
        self.work_process_frame.setStyleSheet("background-color: white")
        # work_process_label
        self.work_process_label = QLabel(self.work_process_frame)
        self.work_process_label.setGeometry(300, 70, 200, 200)
        self.process_gif = QMovie("./resources/process.gif")
        self.process_gif.setScaledSize(QSize(200, 200))
        self.work_process_label.setMovie(self.process_gif)
        self.process_gif.start()
        # process_cancel_button
        self.process_cancel_button = custom_qwidget.MyQLabel(self.work_process_frame)
        self.process_cancel_button.setGeometry(0, 490, 800, 40)
        self.process_cancel_button.setText("取消")
        self.process_cancel_button.setStyleSheet("""
                                                    QLabel{
                                                    font-family: "微软雅黑";
                                                    font-size: 25px;
                                                    background-color: black;
                                                    color: white;}
                                                    QLabel::hover{
                                                    color: grey;}
                                                    """)
        self.process_cancel_button.setAlignment(Qt.AlignCenter)
        self.process_cancel_button.clicked.connect(self.cancel_process)
        # process_cancel_label
        self.process_cancel_label = custom_qwidget.MyQLabel(self.work_process_frame)
        self.process_cancel_label.setGeometry(0, 490, 800, 40)
        self.process_cancel_label.setText("取消中......")
        self.process_cancel_label.setStyleSheet("""
                                                            QLabel{
                                                            font-family: "微软雅黑";
                                                            font-size: 25px;
                                                            background-color: black;
                                                            color: white;}
                                                            """)
        self.process_cancel_label.setAlignment(Qt.AlignCenter)
        self.process_cancel_label.hide()
        # show
        self.work_process_frame.show()

    def acquire_threading(self, threading, complete_frame):
        self.threading = threading
        self.complete_frame = complete_frame
        self.process_cancel_button.clicked.connect(self.cancel_process)

    def cancel_process(self):
        self.process_cancel_button.hide()
        self.process_cancel_label.show()
        self.complete_frame.work_complete_frame.deleteLater()

