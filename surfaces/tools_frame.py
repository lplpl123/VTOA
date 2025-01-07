from PyQt5.Qt import *
from tools import custom_qwidget


class ToolsFrame():

    def __init__(self, main_surface):
        self.main_surface = main_surface

    def _setup_tools_frame_widgets(self):
        # tools_frame
        self.tools_frame = QFrame(self.main_surface.work_frame)
        self.tools_frame.setStyleSheet("background-color: white;")
        self.main_surface.background_layout.removeWidget(self.main_surface.background)
        self.main_surface.background_layout.addWidget(self.tools_frame)

        # function & work
        self.tools_function_frame = QFrame(self.tools_frame)
        self.tools_work_frame = QFrame(self.tools_frame)
        self.tools_layout = QVBoxLayout(self.tools_frame)
        self.tools_layout.addWidget(self.tools_function_frame)
        self.tools_layout.addWidget(self.tools_work_frame)
        self.tools_layout.setStretch(0, 1)
        self.tools_layout.setStretch(1, 9)


        # function frame
        self.tools_extract_button = custom_qwidget.MyQLabel(self.tools_function_frame)
        self.tools_extract_button.setText("音频提取")
        self.tools_extract_button.setMinimumHeight(45)
        self.tools_audio_transfer_button = custom_qwidget.MyQLabel(self.tools_function_frame)
        self.tools_audio_transfer_button.setText("格式转换")
        self.tools_voice_split_button = custom_qwidget.MyQLabel(self.tools_function_frame)
        self.tools_voice_split_button.setText("人声提取")
        self.tools_bgm_split_button = custom_qwidget.MyQLabel(self.tools_function_frame)
        self.tools_bgm_split_button.setText("伴奏提取")

        self.function_layout = QHBoxLayout(self.tools_function_frame)
        self.function_layout.addWidget(self.tools_extract_button)
        self.function_layout.addWidget(self.tools_audio_transfer_button)
        self.function_layout.addWidget(self.tools_voice_split_button)
        self.function_layout.addWidget(self.tools_bgm_split_button)

        # work frame
        self.work_blank_label = QLabel(self.tools_work_frame)
        self.work_layout = QVBoxLayout(self.tools_work_frame)
        self.work_layout.addWidget(self.work_blank_label)
        self.work_layout.setContentsMargins(0, 0, 0, 0)
