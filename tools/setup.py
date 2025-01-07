import sys
import os
import ctypes
from PyQt5.Qt import *
from PyQt5 import QtCore, QtGui, QtWidgets
from config import app
from surfaces.console import Console
from tools.storage import Storage
from tools import backend_function
from tools import custom_qwidget


class Run():
    def __init__(self):
        self.setup()

    def setup(self):
        self.chuang = QApplication(sys.argv)
        desktop = QApplication.desktop()
        main_screen_rect = desktop.screenGeometry(0)
        x = int((main_screen_rect.width() - 800) / 2)
        y = int((main_screen_rect.height() - 600) / 2)
        # 阴影层
        self.effect_window = custom_qwidget.MyWindow()
        self.effect_window.setWindowTitle("Main")
        self.effect_window.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.effect_window.setGeometry(x-3, y-3, app["width"]+6, app["height"]+6)
        self.effect_window.setWindowFlags(Qt.FramelessWindowHint)
        self.effect_window.setWindowIcon(QIcon("./resources/icon.png"))
        ####
        self.effect_shadow = QtWidgets.QGraphicsDropShadowEffect(self.effect_window)
        self.effect_shadow.setOffset(0, 0)  # 偏移
        self.effect_shadow.setBlurRadius(10)  # 阴影半径
        self.effect_shadow.setColor(QtCore.Qt.gray)  # 阴影颜色
        # 主层
        self.main_window = QWidget(self.effect_window)
        self.main_window.setGeometry(3, 3, app["width"], app["height"])
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")
        self.main_window.setGraphicsEffect(self.effect_shadow)
        self.setup_console()

    def run(self):
        self.setup_vars()
        self.effect_window.show()
        self.main_window.show()
        sys.exit(self.chuang.exec_())

    def setup_console(self):
        Console(self.chuang, self.main_window)

    def setup_vars(self):
        storage = Storage()
        video_file_types = ["mp4", "avi", "mov", "mpeg", "flv", "wmv", "mkv", "webm"]
        audio_file_types = ["mp3", "flac", "wav", "m4a", "ogg", "wma"]
        Storage().store_info("video_file_types", video_file_types)
        Storage().store_info("audio_file_types", audio_file_types)

        Storage().store_info("chuang", self.chuang)

        window_width = self.main_window.width()
        window_height = self.main_window.height()
        Storage().store_info("window_size", [window_width, window_height])

        default_output_path = backend_function.get_default_output_path()
        storage.store_info("default_output_folder", default_output_path)

        temp_output_folder = backend_function.get_temp_output_folder()
        storage.store_info("temp_output_folder", temp_output_folder)

        default_output_audio_format = "mp3"
        storage.store_info("default_output_audio_format", default_output_audio_format)

        default_output_video_format = "mp4"
        storage.store_info("default_output_video_format", default_output_video_format)

        project_path = os.path.dirname(sys.argv[0])
        project_path = os.path.normpath(project_path)
        storage.store_info("project_path", project_path)

        ffmpeg_path = os.path.join(project_path, "ffmpeg/bin/ffmpeg")
        ffmpeg_path = os.path.normpath(ffmpeg_path)
        storage.store_info("ffmpeg_path", ffmpeg_path)

        spleeter_path = os.path.join(project_path, "SpleeterMsvcExe/Spleeter")
        spleeter_path = os.path.normpath(spleeter_path)
        storage.store_info("spleeter_path", spleeter_path)
