from PyQt5.Qt import QFrame, QLabel
from PyQt5.QtCore import Qt
from tools import custom_qwidget


class CompleteFrame:

    def __init__(self, main_surface):
        self.main_surface = main_surface

    def _setup_work_complete_frame_widgets(self):
        # work_complete_frame
        self.work_complete_frame = QFrame(self.main_surface.work_frame)
        self.work_complete_frame.setGeometry(0, 15, 800, 585)
        self.work_complete_frame.setStyleSheet("background-color: white;")
        # work_complete_info
        self.work_complete_info = QLabel(self.work_complete_frame)
        self.work_complete_info.setGeometry(0, 140, 800, 50)
        self.work_complete_info.setText("转换完成")
        self.work_complete_info.setStyleSheet("""
                                                QLabel{
                                                font-family: "微软雅黑";
                                                font-size: 35px;
                                                background-color: rgba(255, 255, 255, 0);
                                                color: black;
                                                border: none;}
                                                """)
        self.work_complete_info.setAlignment(Qt.AlignCenter)
        # work_complete_info
        self.work_tip_info = QLabel(self.work_complete_frame)
        self.work_tip_info.setGeometry(0, 300, 800, 60)
        self.work_tip_info.setWordWrap(True)
        self.work_tip_info.setStyleSheet("""
                                        QLabel{
                                        font-family: "微软雅黑";
                                        font-size: 15px;
                                        background-color: rgba(255, 255, 255, 0);
                                        color: red;
                                        border: none;}
                                        """)
        self.work_tip_info.setAlignment(Qt.AlignCenter)
        self.work_tip_info.hide()
        # work_save_button
        self.work_save_button = custom_qwidget.MyButton(self.work_complete_frame)
        self.work_save_button.setGeometry(150, 350, 200, 60)
        self.work_save_button.setText("保存")
        # work_custom_save_button
        self.work_custom_save_button = custom_qwidget.MyButton(self.work_complete_frame)
        self.work_custom_save_button.setGeometry(450, 350, 200, 60)
        self.work_custom_save_button.setText("另存")
        # complete_back_button
        self.complete_back_button = custom_qwidget.MyQLabel(self.work_complete_frame)
        self.complete_back_button.setGeometry(0, 490, 800, 40)
        self.complete_back_button.setText("返回")
        self.complete_back_button.setStyleSheet("""
                                                    QLabel{
                                                    font-family: "微软雅黑";
                                                    font-size: 25px;
                                                    background-color: black;
                                                    color: white;}
                                                    QLabel::hover{
                                                    color: grey;}
                                                    """)
        self.complete_back_button.setAlignment(Qt.AlignCenter)