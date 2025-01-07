from PyQt5.Qt import *
from PyQt5.QtCore import Qt, pyqtSignal
from tools import custom_qwidget


class MainSurface:
    def __init__(self, main_window):
        # init params
        self.main_window = main_window
        self.file_path = ""
        self._create_surface()

    def _create_surface(self):
        self._setup_main_frame()
        self._setup_frames()
        self._setup_title_frame_widgets()
        self._setup_work_frame_widgets()

    def _setup_main_frame(self):
        self.main_frame = QFrame(self.main_window)
        self.tol_layout = QVBoxLayout(self.main_window)
        self.tol_layout.setContentsMargins(0, 0, 0, 0)
        self.tol_layout.addWidget(self.main_frame)

    def _setup_frames(self):
        # title_frame
        self.title_frame = QFrame(self.main_frame)
        self.title_frame.setStyleSheet("""
                                        background-color: black;
                                        """)
        # work_frame
        self.work_frame = custom_qwidget.MyWorkFrame(self.main_frame)
        self.work_frame.setStyleSheet("""
                                        background-color: white;
                                    """)
        # layout
        self.tol_vertical_layout = QVBoxLayout(self.main_frame)
        self.tol_vertical_layout.setSpacing(0)
        self.tol_vertical_layout.setContentsMargins(0, 0, 0, 0)
        self.tol_vertical_layout.addWidget(self.title_frame)
        self.tol_vertical_layout.addWidget(self.work_frame)
        self.tol_vertical_layout.setStretch(0, 1)
        self.tol_vertical_layout.setStretch(1, 11)

    def _setup_title_frame_widgets(self):
        """init title frame widgets"""
        # title_task_text
        self.title_task_text = custom_qwidget.MyQLabel(self.title_frame)
        self.title_task_text.setText("音频视频编辑工具")
        self.title_task_text.setAlignment(Qt.AlignCenter)
        self.title_task_text.setStyleSheet("""
                                            QLabel{
                                            font-family: "微软雅黑";
                                            font-size: 30px;
                                            background-color: black;
                                            color: white;}
                                            """)
        # title_exit_button
        self.title_exit_button = QPushButton(self.title_frame)
        self.title_exit_button.setFocusPolicy(Qt.NoFocus)
        self.title_exit_button.setFlat(True)
        self.title_exit_button.setFixedHeight(40)
        self.title_exit_button.setStyleSheet("""
                                            QWidget{
                                            background-color: black;
                                            image:url(./resources/exit_1.png);
                                            border: none;
                                            }
                                            QPushButton::hover{
                                            image:url(./resources/exit_1_hover.png);}
                                            """)
        # layout
        self.title_horizontal_layout = QHBoxLayout(self.title_frame)
        self.title_horizontal_layout.addWidget(self.title_task_text)
        self.title_horizontal_layout.addWidget(self.title_exit_button)
        self.title_horizontal_layout.setStretch(0, 16)
        self.title_horizontal_layout.setStretch(1, 1)
        self.title_horizontal_layout.setSpacing(0)
        self.title_horizontal_layout.setContentsMargins(0, 0, 0, 0)

    def _setup_work_frame_widgets(self):
        # work_background_lable
        self.background = QLabel(self.work_frame)
        self.background.setStyleSheet("border-image:url(./resources/background.png);")
        self.background_layout = QVBoxLayout(self.work_frame)
        self.background_layout.addWidget(self.background)
        self.background_layout.setContentsMargins(0, 0, 0, 0)
        # work_start_button
        self.start_button = custom_qwidget.MyQLabel(self.background)
        self.start_button.setText("开始")
        self.start_button.setMinimumSize(200, 50)
        # layout
        self.blank_vertical_layout = QVBoxLayout(self.background)
        self.blank_vertical_layout.addWidget(self.start_button)
        self.blank_vertical_layout.setAlignment(Qt.AlignCenter)

