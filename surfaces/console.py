from surfaces.extract_frame import ExtractFrame
from surfaces.main_surface import MainSurface
from surfaces.audio_transfer_frame import AudioTransferFrame
from surfaces.voice_split_frame import VoiceSplitFrame
from surfaces.bgm_split_frame import BgmSplitFrame
from surfaces.tools_frame import ToolsFrame
from surfaces.select_format_frame import SelectFormatFrame
from frontend_functions.main_surface_functions import MainSurfaceFunctions
from tools import backend_function


class Console:

    def __init__(self, chuang, main_window):
        self.chuang = chuang
        self.main_window = main_window
        # 初始化各种框架的界面
        self.main_surface = MainSurface(self.main_window)
        self.tools_frame = ToolsFrame(self.main_surface)
        self.extract_frame = ExtractFrame(self.main_surface)
        self.audio_transfer_frame = AudioTransferFrame(self.main_surface)
        self.voice_split_frame = VoiceSplitFrame(self.main_surface)
        self.bgm_split_frame = BgmSplitFrame(self.main_surface)
        self.select_format_frame = SelectFormatFrame(self.chuang)
        self.frame_dict = {
            "tools_frame": self.tools_frame,
            "extract_frame": self.extract_frame,
            "audio_transfer_frame": self.audio_transfer_frame,
            "voice_split_frame": self.voice_split_frame,
            "bgm_split_frame": self.bgm_split_frame,
            "select_format_frame": self.select_format_frame
        }
        # 初始化前端函数
        self.main_surface_functions = MainSurfaceFunctions(self.chuang, self.main_surface, self.frame_dict)
        # 绑定函数
        self.main_surface_functions._bind_functions()