from PyQt5.Qt import *
from tools import custom_qwidget
from tools.storage import Storage


class SelectFormatFrame:

    def __init__(self, chuang):
        self.chuang = chuang
        self.window = self.chuang.topLevelWidgets()[0]

    def _setup_frame_widgets(self, x, y, format_button):
        self.format_button = format_button

        self.back_label = custom_qwidget.MyQLabel(self.window)
        self.back_label.setStyleSheet("background-color:rgb(255, 255, 255, 0);")
        self.back_label.clicked.connect(self.close_format_frame)

        self.format_layout = QVBoxLayout(self.window)
        self.format_layout.addWidget(self.back_label)
        self.format_layout.setContentsMargins(0, 0, 0, 0)

        self.format_frame = QFrame(self.back_label)
        self.format_frame.setGeometry(x, y, 200, 200)
        self.format_frame.setStyleSheet("background:rgb(255, 255, 255, 1);"
                                        "border: 1px solid black;")


        # formats
        self.mp3_button = custom_qwidget.MyQLabelFormat(self.format_frame)
        self.mp3_button.setText("mp3")
        self.mp3_button.clicked.connect(lambda: self.button_f("mp3"))

        self.avi_button = custom_qwidget.MyQLabelFormat(self.format_frame)
        self.avi_button.setText("avi")
        self.avi_button.clicked.connect(lambda: self.button_f("avi"))


        self.flac_button = custom_qwidget.MyQLabelFormat(self.format_frame)
        self.flac_button.setText("flac")
        self.flac_button.clicked.connect(lambda: self.button_f("flac"))


        self.grid_layout = QGridLayout(self.format_frame)
        self.grid_layout.addWidget(self.mp3_button)
        self.grid_layout.addWidget(self.avi_button)
        self.grid_layout.addWidget(self.flac_button)

        self.back_label.raise_()
        self.back_label.show()

    def button_f(self, format):
        self.format_button.setText(format)
        self.close_format_frame()

    def close_format_frame(self):
        self.back_label.hide()

