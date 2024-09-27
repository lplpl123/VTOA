from PyQt5.Qt import QFrame, QLabel, QHBoxLayout, QWidget
from PyQt5.QtCore import Qt
from tools import custom_qwidget


class StartFrame():

    def __init__(self, main_surface):
        self.main_surface = main_surface

    def _setup_start_frame_widgets(self):
        """init work frame widgets"""
        self.start_frame = QFrame(self.main_surface.work_frame)
        self.start_frame.setGeometry(0, 15, 800, 585)
        self.start_frame.setStyleSheet("background-color: white")
        # work_start_button
        self.start_button = custom_qwidget.MyButton(self.start_frame)
        self.start_button.setGeometry(300, 400, 200, 60)
        self.start_button.setText("开始")
        # work_music_image
        self.music_image = custom_qwidget.MyQLabel(self.start_frame)
        self.music_image.setGeometry(280, 80, 240, 240)
        self.music_image.setStyleSheet("""
                                            QWidget{
                                                image:url(./resources/music01.png)}
                                            """)
        self.music_image.setCursor(Qt.PointingHandCursor)
        # work_background_label
        self.work_background_img = QLabel(self.main_surface.work_frame)
        self.work_background_img.lower()
        self.work_background_img.setStyleSheet("""
                                                background-color: white;
                                                """)
        # layout
        self.work_horizontal_layout = QHBoxLayout(self.main_surface.work_frame)
        self.work_horizontal_layout.addWidget(self.work_background_img)
        self.work_horizontal_layout.setContentsMargins(0, 0, 0, 0)
        # blank_widget
        self.blank_widget = QWidget(self.main_surface.work_frame)
        self.blank_widget.setGeometry(0, 0, 800, 600)
        self.blank_widget.setStyleSheet("""
                                        background-color: rgb(255, 255, 255, 0);
                                        """)
        self.blank_widget.hide()
