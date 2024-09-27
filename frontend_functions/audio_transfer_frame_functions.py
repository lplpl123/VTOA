import threading
from tools import backend_function
from frontend_functions.complete_frame_functions import CompleteFrameFunctions


class AudioTransferFrameFunctions:

    def __init__(self, frame_dict):
        self.file_path = None
        self.tools_frame = frame_dict["tools_frame"]
        self.audio_transfer_frame = frame_dict["audio_transfer_frame"]
        self.process_frame = frame_dict["process_frame"]
        self.complete_frame = frame_dict["complete_frame"]
        self.complete_frame_functions = CompleteFrameFunctions(frame_dict, 1)

    def _bind_functions(self):
        self.audio_transfer_frame.audio_transfer_music_image_01.clicked.connect(lambda: self.work_select_button_function())
        self.audio_transfer_frame.audio_transfer_music_image_02.clicked.connect(self.work_select_button_function)
        self.audio_transfer_frame.work_select_button.clicked.connect(self.work_select_button_function)
        self.audio_transfer_frame.work_extract_button.clicked.connect(self.work_audio_transfer_button_function)
        self.audio_transfer_frame.audio_transfer_back_button.clicked.connect(self.work_back_button_function)
        self.audio_transfer_frame.work_select_label.clicked.connect(self.work_select_label_function)
        self.audio_transfer_frame.work_tip_label.clicked.connect(self.work_tip_label_function)

    def work_select_button_function(self):
        temp_file_path, self.file_name = backend_function.read_file_path("mp3")
        if self.file_name:
            file_type = self.file_name.rsplit(".", 1)[1]
        if temp_file_path and file_type in ["mp3", "flac", "avi"]:
            self.file_path = temp_file_path
            self.audio_transfer_frame.audio_transfer_selected_file_info.show()
            self.audio_transfer_frame.audio_transfer_selected_file_info.raise_()
            self.audio_transfer_frame.audio_transfer_selected_file_info.setText(self.file_name)

    def work_audio_transfer_button_function(self):
        backend_function.clear_cache()
        if self.file_path:
            self.output_type = self.audio_transfer_frame.work_outputs_selection.currentText()
            self.process_frame._setup_work_process_frame_widgets()
            # 加一个线程
            threading_get_api = threading.Thread(target=self.get_api_audio_transfer)
            self.process_frame.acquire_threading(threading_get_api, self.complete_frame)
            threading_get_api.start()
            self.audio_transfer_frame.audio_transfer_selected_file_info.setText("")
            self.complete_frame._setup_work_complete_frame_widgets()
            self.complete_frame_functions._bind_functions()
        else:
            self.audio_transfer_frame.audio_transfer_selected_file_info.show()
            self.audio_transfer_frame.audio_transfer_selected_file_info.setText("请选择文件......")

    def get_api_audio_transfer(self):
        backend_function.audio_transfer(self.file_path, self.output_type, self.file_name)
        self.complete_frame_functions._get_info()
        self.file_path = None
        self.process_frame.work_process_frame.deleteLater()
        try:
            self.complete_frame.work_complete_frame.show()
        except:
            pass

    def work_back_button_function(self):
        self.audio_transfer_frame.work_audio_transfer_frame.deleteLater()
        self.tools_frame.tools_frame.show()

    def work_select_label_function(self):
        if self.audio_transfer_frame.work_select_label_index == 0:
            self.audio_transfer_frame.work_outputs_selection.show()
            self.audio_transfer_frame.work_select_label_index = 1
        else:
            self.audio_transfer_frame.work_outputs_selection.hide()
            self.audio_transfer_frame.work_select_label_index = 0

    def work_tip_label_function(self):
        if self.audio_transfer_frame.work_tip_label_index == 0:
            self.audio_transfer_frame.work_select_label.show()
            self.audio_transfer_frame.work_tip_label_index = 1
        else:
            self.audio_transfer_frame.work_select_label.hide()
            self.audio_transfer_frame.work_select_label_index = 0
            self.audio_transfer_frame.work_outputs_selection.hide()
            self.audio_transfer_frame.work_tip_label_index = 0