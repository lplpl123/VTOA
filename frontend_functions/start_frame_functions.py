from PyQt5.QtCore import QTimer
from frontend_functions.tools_frame_functions import ToolsFrameFunctions


class StartFrameFunctions:

    def __init__(self, frame_dict):
        self.start_frame = frame_dict["start_frame"]
        self.tools_frame = frame_dict["tools_frame"]
        self.tools_frame_functions = ToolsFrameFunctions(frame_dict)

    def _bind_functions(self):
        self.start_frame.start_button.clicked.connect(lambda: self.start_button_function())
        self.start_frame.music_image.clicked.connect(self.start_button_function)

    def start_button_function(self):
        self.start_frame.blank_widget.show()
        self.widget_opacity = 0
        self.mytimer = QTimer(self.start_frame.blank_widget)
        self.mytimer.timeout.connect(self.change_opacity)
        self.mytimer.start(30)

    def change_opacity(self):
        if self.widget_opacity >= 9:
            self.mytimer.stop()
            self.start_frame.start_frame.hide()
            self.tools_frame._setup_tools_frame_widgets()
            self.tools_frame_functions._bind_functions()
        self.widget_opacity += 1
        self.start_frame.blank_widget.setStyleSheet("background-color: rgb(255, 255, 255, {});".format(self.widget_opacity/10))