from tools import backend_function
from PyQt5.Qt import QFileDialog


class CompleteFrameFunctions:

    def __init__(self, frame_dict, index_page):
        self.index_page = index_page
        self.complete_frame = frame_dict["complete_frame"]
        self.extract_frame = frame_dict["extract_frame"]
        self.audio_transfer_frame = frame_dict["audio_transfer_frame"]

    def _get_info(self):
        self.file, self.source_path = backend_function.get_temp_file_info() # file Simyee陈芯怡 粤语版 《青花瓷》 ....mp3 source_path ./temp/Simyee陈芯怡 粤语版 《青花瓷》 ....mp3
        self.default_output_path = backend_function.get_default_output_path()

    def _bind_functions(self):
        self.complete_frame.work_save_button.clicked.connect(lambda: self.work_save_button_function())
        self.complete_frame.work_custom_save_button.clicked.connect(self.work_custom_save_button_function)
        self.complete_frame.complete_back_button.clicked.connect(self.complete_back_button_function)

    def work_save_button_function(self):
        default_output_path = self.default_output_path + f"\\{self.file}"
        # check
        if backend_function.check_if_file_exists(default_output_path):
            self.complete_frame.work_tip_info.setText("文件已存在")
            self.complete_frame.work_tip_info.show()
        # save
        else:
            backend_function.save_file(self.source_path, default_output_path)
            tip_info = "保存至" + str(default_output_path)
            self.complete_frame.work_tip_info.setText(tip_info)
            self.complete_frame.work_tip_info.show()

    def work_custom_save_button_function(self):
        default_output_path = self.default_output_path + f"\\{self.file}"
        # setting info
        tip_info = ""
        output_path_info = QFileDialog.getSaveFileName(None, "另存为", default_output_path.rsplit(".", 1)[0],
                                                       default_output_path.rsplit(".", 1)[1])
        # save
        if output_path_info[0]:
            output_path = output_path_info[0] + "." + output_path_info[1]
            if backend_function.check_if_file_exists(output_path):
                self.complete_frame.work_tip_info.setText("文件已存在")
            else:
                backend_function.custom_save_file(self.source_path, output_path)
                tip_info = "保存至" + str(output_path)
        # save
        self.complete_frame.work_tip_info.setText(tip_info)
        self.complete_frame.work_tip_info.show()

    def complete_back_button_function(self):
        # 删除临时文件
        backend_function.clear_cache()
        ######
        self.complete_frame.work_complete_frame.deleteLater()
        if self.index_page == 0:
            backend_function.reset_pre_frame(self.extract_frame)
            self.extract_frame.work_extract_frame.show()
        elif self.index_page == 1:
            backend_function.reset_pre_frame(self.audio_transfer_frame)
            self.audio_transfer_frame.work_audio_transfer_frame.show()