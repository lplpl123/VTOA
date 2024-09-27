from PyQt5.Qt import QFrame, QLabel, QComboBox, QMovie, QSize
from PyQt5.QtCore import Qt
from tools import custom_qwidget


class ExtractFrame:

    def __init__(self, main_surface):
        self.main_surface = main_surface
        self.work_select_label_index = 0
        self.work_tip_label_index = 0

    def _setup_work_extract_frame_widgets(self):
        # work_extract_frame
        self.work_extract_frame = QFrame(self.main_surface.work_frame)
        self.work_extract_frame.setGeometry(0, 15, 800, 585)
        self.work_extract_frame.setStyleSheet("background-color: white")
        # work_tip_label
        self.work_tip_label = custom_qwidget.MyQLabel_01(self.work_extract_frame)
        work_tip_label_stylesheet = self.work_tip_label.styleSheet().replace("20px", "25px")
        self.work_tip_label.setStyleSheet(work_tip_label_stylesheet)
        self.work_tip_label.setGeometry(0, 0, 150, 35)
        self.work_tip_label.setText("音频提取")
        # work_select_label
        self.work_select_label = custom_qwidget.MyQLabel_01(self.work_extract_frame)
        self.work_select_label.setGeometry(0, 60, 120, 35)
        self.work_select_label.setText("输出格式")
        self.work_select_label.hide()
        # work_outputs_selection
        self.work_outputs_selection = QComboBox(self.work_extract_frame)
        self.work_outputs_selection.setGeometry(20, 100, 120, 35)
        self.work_outputs_selection.setStyleSheet("""
                                    QWidget{
                                    font-family: "微软雅黑";
                                    font-size: 20px;
                                    color: black;
                                    background-color: white;
                                    border: none;}
                                    QComboBox::drop-down{
                                    border: none;}
                                    """)
        self.work_outputs_selection.addItem("mp3")
        self.work_outputs_selection.addItem("avi")
        self.work_outputs_selection.addItem("flac")
        self.work_outputs_selection.hide()
        # work_music_image_01
        self.extract_music_image_01 = custom_qwidget.MyQLabel(self.work_extract_frame)
        self.extract_music_image_01.setGeometry(750, 0, 35, 35)
        self.extract_music_image_01.setStyleSheet("""
                                                QWidget{
                                                    image:url(./resources/music.png)}
                                                """)
        # work_music_image_02
        self.extract_music_image_02 = custom_qwidget.MyQLabel(self.work_extract_frame)
        self.extract_music_image_02.setGeometry(300, 100, 200, 200)
        self.extract_music_image_02.setStyleSheet("background-color: white;")
        self.extract_music_image_02_gif = QMovie("./resources/music02.gif")
        self.extract_music_image_02_gif.setScaledSize(QSize(200, 200))
        self.extract_music_image_02.setMovie(self.extract_music_image_02_gif)
        self.extract_music_image_02_gif.start()
        self.extract_music_image_02.raise_()
        # split_line
        self.work_split_line = QFrame(self.work_extract_frame)
        self.work_split_line.setGeometry(0, 45, 800, 445)
        self.work_split_line.setStyleSheet("background-color: white;"
                                           "border-top: 2px solid black;")
        self.work_split_line.lower()
        # work_selected_file_info
        self.extract_selected_file_info = QLabel(self.work_extract_frame)
        self.extract_selected_file_info.setGeometry(0, 280, 800, 30)
        self.extract_selected_file_info.setStyleSheet("""
                                                    QLabel{
                                                    font-family: "微软雅黑";
                                                    font-size: 15px;
                                                    background-color: rgba(255, 255, 255, 0);
                                                    color: red;
                                                    border: none;}
                                                    """)
        self.extract_selected_file_info.setAlignment(Qt.AlignCenter)
        self.extract_selected_file_info.setWordWrap(True)
        self.extract_selected_file_info.hide()
        # work_select_button
        self.work_select_button = custom_qwidget.MyButton(self.work_extract_frame)
        self.work_select_button.setGeometry(150, 375, 200, 60)
        self.work_select_button.setText("选择文件")
        # work_extract_button
        self.work_extract_button = custom_qwidget.MyButton(self.work_extract_frame)
        self.work_extract_button.setGeometry(450, 375, 200, 60)
        self.work_extract_button.setText("开始转换")
        # extract_back_button
        self.extract_back_button = custom_qwidget.MyQLabel(self.work_extract_frame)
        self.extract_back_button.setGeometry(0, 490, 800, 40)
        self.extract_back_button.setText("返回")
        self.extract_back_button.setStyleSheet("""
                                            QLabel{
                                            font-family: "微软雅黑";
                                            font-size: 25px;
                                            background-color: black;
                                            color: white;}
                                            QLabel::hover{
                                            color: grey;}
                                            """)
        self.extract_back_button.setAlignment(Qt.AlignCenter)
        # show
        self.work_extract_frame.show()



