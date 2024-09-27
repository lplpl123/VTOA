

class DenoiseFrame:

    def __init__(self):
        pass

    def _setup_work_denoise_frame_widgets(self):
        # work_denoise_frame
        self.work_denoise_frame = QFrame(self.work_frame)
        self.work_denoise_frame.setGeometry(0, 15, 800, 475)
        self.work_denoise_frame.setStyleSheet("background-color: white")
        self.work_denoise_frame.hide()
        # split_line
        self.work_split_line = QFrame(self.work_denoise_frame)
        self.work_split_line.setGeometry(0, 45, 800, 380)
        self.work_split_line.setStyleSheet("background-color: white;"
                                           "border-top: 2px solid black;"
                                           "border-bottom: 2px solid black;")
        self.work_split_line.lower()
        # work_selected_file_info
        self.work_selected_file_info = QLabel(self.work_split_line)
        self.work_selected_file_info.setGeometry(0, 150, 800, 40)
        self.work_selected_file_info.setStyleSheet("""
                                                    QLabel{
                                                    font-family: "微软雅黑";
                                                    font-size: 20px;
                                                    background-color: white;
                                                    color: black;
                                                    border: none;}
                                                    """)
        self.work_selected_file_info.setAlignment(Qt.AlignCenter)
        # work_select_button
        self.work_select_button = MyButton(self.work_denoise_frame)
        self.work_select_button.setGeometry(150, 425, 200, 60)
        self.work_select_button.setText("选择文件")
        self.work_select_button.clicked.connect(self.select_file)
        # work_denoise_button
        self.work_extract_button = MyButton(self.work_denoise_frame)
        self.work_extract_button.setGeometry(450, 425, 200, 60)
        self.work_extract_button.setText("音频降噪")
        self.work_extract_button.clicked.connect(self.audio_transfer)