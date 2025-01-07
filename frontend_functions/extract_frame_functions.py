import os
from tools import backend_function
from tools import custom_qwidget
from tools.storage import Storage
from frontend_functions.frame_functions import FrameFunctions
from PyQt5.Qt import QFileDialog


class ExtractFrameFunctions(FrameFunctions):

    def __init__(self, frame_dict):
        super().__init__(frame_dict)
        self.extract_frame = frame_dict["extract_frame"]

    def _bind_functions(self):
        self.extract_frame.extract_selected_file_info.clicked.connect(self.work_select_button_function)
        self.extract_frame.bar_timer.timeout.connect(self.update_bar)

        self.extract_frame.select_output_button.clicked.connect(self.output_path_function)
        self.extract_frame.format_button.clicked.connect(self.output_type_function)

        self.extract_frame.format_extract_button.clicked.connect(self.work_extract_button_function)

        custom_qwidget.change_process_button_style(0, True)

    def work_select_button_function(self):

        if backend_function.select_file_path("video"):

            selected_file_path = Storage().get_info("selected_file_path")
            self.extract_frame.extract_selected_file_info.setText(selected_file_path)

            self.can_transfer = True

            self.extract_frame.complete_number = 0
            self.extract_frame.select_process_bar.setValue(self.extract_frame.complete_number)


    def work_extract_button_function(self):

        if not self.can_transfer:
            return

        self.can_transfer = False

        final_output_folder = self.extract_frame.select_output_button.text()
        Storage().store_info("final_output_folder", final_output_folder)

        file_name = Storage().get_info("selected_file_name")
        temp_output_folder = Storage().get_info("temp_output_folder")

        final_output_format = self.extract_frame.format_button.text()
        Storage().store_info("final_output_format", final_output_format)

        final_output_path = os.path.join(final_output_folder, file_name + '.' + final_output_format)
        Storage().store_info("final_output_path", final_output_path)

        temp_output_path_mp3 = os.path.join(temp_output_folder, file_name + '.mp3')
        Storage().store_info("temp_output_path_mp3", temp_output_path_mp3)


        temp_output_path = os.path.join(temp_output_folder, file_name + '.' + final_output_format)
        Storage().store_info("temp_output_path", temp_output_path)

        if backend_function.check_if_output_file_exists():
            self.extract_frame.extract_selected_file_info.setText("目标路径文件已存在")
            return

        self.extract_frame.bar_timer.start(50)

        super().work_extract_button_function()


    def get_api_backend(self):
        backend_function.transfer_video2audio()

    def update_bar(self):

        self.extract_frame.complete_number += 1
        self.extract_frame.select_process_bar.setValue(self.extract_frame.complete_number)

        if self.extract_frame.complete_number >= 99:

            import time

            start_time = time.time()

            while True:

                if backend_function.check_if_output_file_exists():

                    self.extract_frame.complete_number += 1
                    self.extract_frame.select_process_bar.setValue(self.extract_frame.complete_number)
                    self.extract_frame.bar_timer.stop()

                    self.extract_frame.extract_selected_file_info.setText("转换成功，请继续选择文件")
                    backend_function.clear_store_info()

                    break

                end_time = time.time()

                if end_time - start_time > 30:
                    self.extract_frame.extract_selected_file_info.setText("转换失败")
                    break



    def output_path_function(self):

        if not self.can_transfer:
            return

        custome_output_folder = QFileDialog.getExistingDirectory(None, "输出位置")
        custome_output_folder = os.path.normpath(custome_output_folder)

        if custome_output_folder != ".":
            self.extract_frame.select_output_button.setText(custome_output_folder)



    def output_type_function(self):

        if not self.can_transfer:
            return

        select_format_frame = Storage().get_info("frame_dict")["select_format_frame"]

        window_size = Storage().get_info("window_size")

        format_frame_x = float(window_size[0]) * 0.3
        format_frame_y = float(window_size[1]) * 0.55

        try:
            select_format_frame.back_label.show()
        except:
            select_format_frame._setup_frame_widgets(int(format_frame_x), int(format_frame_y), self.extract_frame.format_button)

