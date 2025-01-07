from tools.storage import Storage
from tools import backend_function
from frontend_functions.extract_frame_functions import ExtractFrameFunctions
from frontend_functions.audio_transfer_frame_functions import AudioTransferFrameFunctions
from frontend_functions.voice_split_frame_functions import VoiceSplitFrameFunctions
from frontend_functions.bgm_split_frame_functions import BgmSplitFrameFunctions


class ToolsFrameFunctions():

    def __init__(self, frame_dict):

        self.last_show_frame = None
        self.current_show_frame = None

        self.tools_frame = frame_dict["tools_frame"]
        self.extract_frame = frame_dict["extract_frame"]
        self.audio_transfer_frame = frame_dict["audio_transfer_frame"]
        self.voice_split_frame = frame_dict["voice_split_frame"]
        self.bgm_split_frame = frame_dict["bgm_split_frame"]

        storage = Storage()
        storage.store_info("frame_dict", frame_dict)

        self.extract_frame_functions = ExtractFrameFunctions(frame_dict)
        self.audio_transfer_frame_functions = AudioTransferFrameFunctions(frame_dict)
        self.voice_split_frame_functions = VoiceSplitFrameFunctions(frame_dict)
        self.bgm_split_frame_functions = BgmSplitFrameFunctions(frame_dict)

        # qss
        self.selected_qss = """
                    QWidget{
                            font-family: "微软雅黑";
                            font-size: 25px;
                            color: white;
                            border-radius:5px;
                            border-image:none;
                            background-color:black;
                            border:5px solid white;}
                            """
        self.origin_qss = """
                    QWidget{
                            font-family: "微软雅黑";
                            font-size: 25px;
                            color: white;
                            border-radius:5px;
                            border-image:none;
                            background-color:black;}
                            
                            QLabel:hover{
                            border:3px solid white;}
                            """

    def _bind_functions(self):

        self.tools_frame.tools_extract_button.clicked.connect(lambda: self.tools_extract_button_function())
        self.tools_frame.tools_audio_transfer_button.clicked.connect(self.work_audio_transfer_button_function)
        self.tools_frame.tools_voice_split_button.clicked.connect(self.work_voice_split_button_function)
        self.tools_frame.tools_bgm_split_button.clicked.connect(self.work_bgm_split_button_function)
        self.tools_frame.work_layout.removeWidget(self.tools_frame.work_blank_label)

        self.current_show_frame = None
        self.tools_extract_button_function()

#region
    def tools_extract_button_function(self):

        if self.current_show_frame == self.extract_frame:
            return

        backend_function.clear_store_info()

        self.change_frame(self.extract_frame, self.extract_frame_functions,
                          self.tools_frame.tools_extract_button)


    def work_audio_transfer_button_function(self):

        if self.current_show_frame == self.audio_transfer_frame:
            return

        backend_function.clear_store_info()
        self.change_frame(self.audio_transfer_frame, self.audio_transfer_frame_functions,
                          self.tools_frame.tools_audio_transfer_button)

    def work_voice_split_button_function(self):

        if self.current_show_frame == self.voice_split_frame:
            return

        backend_function.clear_store_info()
        self.change_frame(self.voice_split_frame, self.voice_split_frame_functions,
                          self.tools_frame.tools_voice_split_button)


    def work_bgm_split_button_function(self):

        if self.current_show_frame == self.bgm_split_frame:
            return

        backend_function.clear_store_info()
        self.change_frame(self.bgm_split_frame, self.bgm_split_frame_functions,
                          self.tools_frame.tools_bgm_split_button)

    #endRegion

    def reset_button_qss(self):
        self.tools_frame.tools_extract_button.setStyleSheet(self.origin_qss)
        self.tools_frame.tools_audio_transfer_button.setStyleSheet(self.origin_qss)
        self.tools_frame.tools_voice_split_button.setStyleSheet(self.origin_qss)
        self.tools_frame.tools_bgm_split_button.setStyleSheet(self.origin_qss)

    def change_frame(self, current_frame, current_frame_functions, tools_button):

        self.last_show_frame = self.current_show_frame # todo 不知道会不会同时改变
        self.current_show_frame = current_frame

        self.reset_button_qss()
        tools_button.setStyleSheet(self.selected_qss)

        current_frame._setup_work_frame_frame_widgets()

        if self.last_show_frame != None:
            self.tools_frame.work_layout.removeWidget(self.last_show_frame.work_frame_frame)
        self.tools_frame.work_layout.addWidget(current_frame.work_frame_frame)

        current_frame_functions._bind_functions()





