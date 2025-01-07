from PyQt5.Qt import *
from PyQt5.QtCore import Qt
from tools import custom_qwidget
from tools.storage import Storage


class Frame:

    def __init__(self, main_surface):
        self.main_surface = main_surface
        # 存储器
        self.storage = Storage()

        self.button_qss = """
                        QWidget{
                            font-family: "微软雅黑";
                            font-size: 20px;
                            color: white;
                            border-radius:5px;
                            border-image:none;
                            background-color:black;}
                            """

    def _setup_work_frame_frame_widgets(self):
        # work_frame_frame
        self.work_frame_frame = QFrame(self.main_surface.work_frame)

        self.extract_up_frame = QFrame(self.work_frame_frame)
        self.extract_down_frame = QFrame(self.work_frame_frame)

        self.extract_layout = QVBoxLayout(self.work_frame_frame)
        self.extract_layout.addWidget(self.extract_up_frame)
        self.extract_layout.addWidget(self.extract_down_frame)
        self.extract_layout.setStretch(0, 10)
        self.extract_layout.setStretch(1, 2)

        # extract up frame
        self.extract_selected_file_info = custom_qwidget.DragFileLabel(self.extract_up_frame, page_index=0)
        self.extract_selected_file_info.setStyleSheet("""
                                                        QLabel{
                                                        font-family: "微软雅黑";
                                                        font-size: 25px;
                                                        background-color: rgba(255, 255, 255, 0);
                                                        color: red;
                                                        border: 3px Solid black;
                                                        border-radius: 15px;}
                                                    """)
        self.extract_selected_file_info.setAlignment(Qt.AlignCenter)
        self.extract_selected_file_info.setWordWrap(True)
        self.extract_selected_file_info.setCursor(Qt.PointingHandCursor)

        self.up_layout = QVBoxLayout(self.extract_up_frame)
        self.up_layout.addWidget(self.extract_selected_file_info)

        # extract down frame
        self.select_frame = QFrame(self.extract_down_frame)
        self.format_frame = QFrame(self.extract_down_frame)

        self.down_layout = QVBoxLayout(self.extract_down_frame)
        self.down_layout.addWidget(self.select_frame)
        self.down_layout.addWidget(self.format_frame)
        self.down_layout.setAlignment(Qt.AlignLeft)
        self.down_layout.setContentsMargins(0, 0, 0, 0)

        # select frame
        self.select_output_label = custom_qwidget.MyQLabel(self.select_frame)
        self.select_output_label.setText("输出位置 :")
        self.select_output_label.setStyleSheet(self.button_qss)
        self.select_output_label.setMinimumSize(150, 30)

        self.select_output_button = custom_qwidget.MyQLabel(self.select_frame)
        self.select_output_button.setText(self.storage.get_info("default_output_folder"))
        self.select_output_button.setMaximumWidth(400)
        self.select_output_button.setMinimumWidth(400)
        self.select_output_button.setStyleSheet("""
                                                            QLabel{
                                                            font-family: "微软雅黑";
                                                            color: black;
                                                            border: 3px solid black;}""")


        # progress bar
        self.select_process_bar = QProgressBar(self.select_frame)
        self.select_process_bar.setAlignment(Qt.AlignCenter)
        self.select_process_bar.setMaximumWidth(160)
        self.select_process_bar.setStyleSheet("QProgressBar { border: 2px solid grey; border-radius: 5px; color: white;  background-color: #FFFFFF; text-align: center;}QProgressBar::chunk {background-color: rgb(0,0,0); border-radius: 5px; margin: 0.1px;  width: 1px;}")
        font = QFont()
        font.setBold(True)
        font.setFamily("微软雅黑")
        font.setWeight(30)
        self.select_process_bar.setFont(font)

        self.bar_timer = QTimer()

        self.complete_number = 0
        self.select_process_bar.setMaximum(100)
        self.select_process_bar.setMinimum(0)
        self.select_process_bar.setValue(self.complete_number)
        self.select_process_bar.setFormat('Loaded  %p%'.format(self.select_process_bar.value()-self.select_process_bar.minimum()))

        self.select_layout = QHBoxLayout(self.select_frame)
        self.select_layout.addWidget(self.select_output_label)
        self.select_layout.addWidget(self.select_output_button)
        self.select_layout.addWidget(self.select_process_bar)


        # format frame
        self.format_label = custom_qwidget.MyQLabel(self.format_frame)
        self.format_label.setText("输出格式 :")
        self.format_label.setStyleSheet(self.button_qss)
        self.format_label.setMinimumHeight(30)

        self.format_button = custom_qwidget.MyQLabel()
        self.format_button.setText(self.storage.get_info("default_output_audio_format"))
        self.format_button.setMaximumWidth(400)
        self.format_button.setMinimumWidth(400)
        self.format_button.setStyleSheet("""
                                                            QLabel{
                                                            font-family: "微软雅黑";
                                                            color: black;
                                                            border: 3px solid black;}""")


        self.format_extract_button = custom_qwidget.MyQLabel(self.format_frame)
        self.format_extract_button.setText("开始转换")
        self.format_extract_button.setStyleSheet("""
                                                        QLabel{
                                                        font-family: "微软雅黑";
                                                        font-size: 20px;
                                                        background-color: black;
                                                        border-radius:15px;
                                                        color: gray;}
                                                    """)
        self.format_extract_button.setAlignment(Qt.AlignCenter)
        self.format_extract_button.setMaximumWidth(200)

        self.format_layout = QHBoxLayout(self.format_frame)
        self.format_layout.addWidget(self.format_label)
        self.format_layout.addWidget(self.format_button)
        self.format_layout.addWidget(self.format_extract_button)

        # show
        self.work_frame_frame.show()


