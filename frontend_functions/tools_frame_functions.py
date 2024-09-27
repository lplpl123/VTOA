from PyQt5.QtCore import QTimer
from frontend_functions.extract_frame_functions import ExtractFrameFunctions
from frontend_functions.audio_transfer_frame_functions import AudioTransferFrameFunctions


class ToolsFrameFunctions():

    def __init__(self, frame_dict):
        self.start_frame = frame_dict["start_frame"]
        self.tools_frame = frame_dict["tools_frame"]
        self.audio_transfer_frame = frame_dict["audio_transfer_frame"]
        self.extract_frame = frame_dict["extract_frame"]
        self.extract_frame_functions = ExtractFrameFunctions(frame_dict)
        self.audio_transfer_frame_functions = AudioTransferFrameFunctions(frame_dict)

    def _bind_functions(self):
        self.tools_frame.work_extract_button.clicked.connect(lambda: self.work_extract_button_function())
        self.tools_frame.work_audio_transfer_button.clicked.connect(self.work_audio_transfer_button_function)
        self.tools_frame.work_voice_transfer_button.clicked.connect(self.work_extract_button_function)
        self.tools_frame.work_audio_cut_button.clicked.connect(self.work_extract_button_function)
        self.tools_frame.work_video_cut_button.clicked.connect(self.work_extract_button_function)
        self.tools_frame.work_video_transfer_button.clicked.connect(self.work_video_transfer_button_function)
        self.tools_frame.work_denoise_button.clicked.connect(self.work_denoise_button_function)
        self.tools_frame.work_split_button.clicked.connect(self.work_split_button_function)
        self.tools_frame.work_back_button.clicked.connect(self.work_back_button_function)

    def work_extract_button_function(self):
        self.tools_frame.tools_frame.hide()
        self.extract_frame._setup_work_extract_frame_widgets() # 应该包含了展示frame的作用
        self.extract_frame_functions._bind_functions()

    def work_audio_transfer_button_function(self):
        self.tools_frame.tools_frame.hide()
        self.audio_transfer_frame._setup_work_audio_transfer_frame_widgets()
        self.audio_transfer_frame_functions._bind_functions()

    def work_video_transfer_button_function(self):
        pass

    def work_denoise_button_function(self):
        pass
        # self.tools_frame.hide()
        # self.work_denoise_frame.show()

    def work_split_button_function(self):
        pass

    def work_back_button_function(self):
        self.tools_frame.blank_widget.show()
        self.widget_opacity = 0
        self.mytimer = QTimer(self.tools_frame.blank_widget)
        self.mytimer.timeout.connect(self.change_opacity)
        self.mytimer.start(30)

    def change_opacity(self):
        if self.widget_opacity >= 9:
            self.mytimer.stop()
            self.back_start_frame()
            self.tools_frame.tools_frame.deleteLater()
            self.tools_frame.blank_widget.deleteLater()
        self.widget_opacity += 1
        self.tools_frame.blank_widget.setStyleSheet("background-color: rgb(255, 255, 255, {});".format(self.widget_opacity/10))

    def back_start_frame(self):
        self.start_frame.blank_widget.setStyleSheet("""
                                                    background-color: rgb(255, 255, 255, 0);
                                                    """)
        self.start_frame.blank_widget.hide()
        self.start_frame.start_frame.show()


