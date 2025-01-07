import os
from tools import backend_function
from tools import custom_qwidget
from tools.storage import Storage
from frontend_functions.frame_functions import FrameFunctions
from PyQt5.Qt import QFileDialog


class BgmSplitFrameFunctions(FrameFunctions):

    def __init__(self, frame_dict):
        super().__init__(frame_dict)
        self.bgm_split_frame = frame_dict["bgm_split_frame"]

    def _bind_functions(self):
        self.bgm_split_frame.extract_selected_file_info.clicked.connect(self.work_select_button_function)
        self.bgm_split_frame.bar_timer.timeout.connect(self.update_bar)

        self.bgm_split_frame.select_output_button.clicked.connect(self.output_path_function)

        self.bgm_split_frame.format_extract_button.clicked.connect(self.work_extract_button_function)

        custom_qwidget.change_process_button_style(3, True)

    def work_select_button_function(self):
        if backend_function.select_file_path("audio"):

            selected_file_path = Storage().get_info("selected_file_path")
            self.bgm_split_frame.extract_selected_file_info.setText(selected_file_path)

            self.can_transfer = True

            self.bgm_split_frame.complete_number = 0
            self.bgm_split_frame.select_process_bar.setValue(self.bgm_split_frame.complete_number)

    def work_extract_button_function(self):

        if not self.can_transfer:
            return

        self.can_transfer = False

        final_output_folder = self.bgm_split_frame.select_output_button.text()
        Storage().store_info("final_output_folder", final_output_folder)

        final_output_format = self.bgm_split_frame.format_button.text()
        Storage().store_info("final_output_format", final_output_format)

        final_output_path = os.path.join(final_output_folder, 'accompany.' + final_output_format)
        Storage().store_info("final_output_path", final_output_path)

        if backend_function.check_if_output_file_exists():
            self.bgm_split_frame.extract_selected_file_info.setText("目标路径文件已存在")
            return

        self.bgm_split_frame.bar_timer.start(50)

        super().work_extract_button_function()

    def get_api_backend(self):
        backend_function.bgm_split()

    def update_bar(self):

        self.bgm_split_frame.complete_number += 1
        self.bgm_split_frame.select_process_bar.setValue(self.bgm_split_frame.complete_number)

        if self.bgm_split_frame.complete_number >= 99:

            import time

            start_time = time.time()

            while True:

                if backend_function.check_if_output_file_exists():

                    self.bgm_split_frame.complete_number += 1
                    self.bgm_split_frame.select_process_bar.setValue(self.bgm_split_frame.complete_number)
                    self.bgm_split_frame.bar_timer.stop()

                    self.bgm_split_frame.extract_selected_file_info.setText("转换成功，请继续选择文件")
                    backend_function.clear_store_info()
                    break

                end_time = time.time()

                if end_time - start_time > 30:
                    self.bgm_split_frame.extract_selected_file_info.setText("转换失败")
                    break

    def output_path_function(self):
        if not self.can_transfer:
            return

        custome_output_folder = QFileDialog.getExistingDirectory(None, "输出位置")
        custome_output_folder = os.path.normpath(custome_output_folder)

        if custome_output_folder != ".":
            self.bgm_split_frame.select_output_button.setText(custome_output_folder)

