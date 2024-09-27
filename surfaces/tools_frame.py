from PyQt5.Qt import QFrame, QWidget
from PyQt5.QtCore import Qt, QTimer
from tools import custom_qwidget


class ToolsFrame():

    def __init__(self, main_surface):
        self.main_surface = main_surface

    def _setup_tools_frame_widgets(self):
        # tools_frame
        self.tools_frame = QFrame(self.main_surface.work_frame)
        self.tools_frame.setGeometry(0, 15, 800, 585)
        self.tools_frame.setStyleSheet("background-color: white")
        # work_extract_button
        self.work_extract_button = custom_qwidget.MyButton(self.tools_frame)
        self.work_extract_button.setGeometry(200, 150, 200, 60)
        self.work_extract_button.setText("音频提取")
        # work_audio_transfer_button
        self.work_audio_transfer_button = custom_qwidget.MyButton(self.tools_frame)
        self.work_audio_transfer_button.setGeometry(400, 150, 200, 60)
        self.work_audio_transfer_button.setText("格式转换")
        # work_voice_transfer_button
        self.work_voice_transfer_button = custom_qwidget.MyButton(self.tools_frame)
        self.work_voice_transfer_button.setGeometry(200, 50, 200, 60)
        self.work_voice_transfer_button.setText("人声转换")
        self.work_voice_transfer_button.hide()
        # 3
        self.work_audio_cut_button = custom_qwidget.MyButton(self.tools_frame)
        self.work_audio_cut_button.setGeometry(400, 50, 200, 60)
        self.work_audio_cut_button.setText("音频剪裁")
        self.work_audio_cut_button.hide()
        # 4
        self.work_video_cut_button = custom_qwidget.MyButton(self.tools_frame)
        self.work_video_cut_button.setGeometry(600, 50, 200, 60)
        self.work_video_cut_button.setText("视频剪裁")
        self.work_video_cut_button.hide()
        # work_video_transfer_button
        self.work_video_transfer_button = custom_qwidget.MyButton(self.tools_frame)
        self.work_video_transfer_button.setGeometry(200, 150, 200, 60)
        self.work_video_transfer_button.setText("视频转换")
        self.work_video_transfer_button.hide()
        # work_denoise_button
        self.work_denoise_button = custom_qwidget.MyButton(self.tools_frame)
        self.work_denoise_button.setGeometry(400, 150, 200, 60)
        self.work_denoise_button.setText("降噪处理")
        self.work_denoise_button.hide()
        # work_split_button
        self.work_split_button = custom_qwidget.MyButton(self.tools_frame)
        self.work_split_button.setGeometry(600, 150, 200, 60)
        self.work_split_button.setText("提取伴奏")
        self.work_split_button.hide()
        # work_back_button
        self.work_back_button = custom_qwidget.MyQLabel(self.tools_frame)
        self.work_back_button.setGeometry(0, 490, 800, 40)
        self.work_back_button.setText("返回")
        self.work_back_button.setStyleSheet("""
                                                    QLabel{
                                                    font-family: "微软雅黑";
                                                    font-size: 25px;
                                                    background-color: black;
                                                    color: white;}
                                                    QLabel::hover{
                                                    color: grey;}
                                                    """)
        self.work_back_button.setAlignment(Qt.AlignCenter)
        # blank_widget
        self.blank_widget = QWidget(self.main_surface.work_frame)
        self.blank_widget.setGeometry(0, 0, 800, 600)
        self.blank_widget.setStyleSheet("""
                                        background-color: rgb(255, 255, 255, 1);
                                        """)
        self.blank_widget.show()
        # show
        self.tools_frame.show()
        self.widget_opacity = 10
        self.mytimer = QTimer(self.blank_widget)
        self.mytimer.timeout.connect(self.change_opacity)
        self.mytimer.start(30)

    def change_opacity(self):
        if self.widget_opacity <= 1:
            self.mytimer.stop()
            self.blank_widget.hide()
        self.widget_opacity -= 1
        self.blank_widget.setStyleSheet("background-color: rgb(255, 255, 255, {});".format(self.widget_opacity/10))
