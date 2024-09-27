from surfaces.extract_frame import ExtractFrame
from surfaces.main_surface import MainSurface
from surfaces.start_frame import StartFrame
from surfaces.audio_transfer_frame import AudioTransferFrame
from surfaces.tools_frame import ToolsFrame
from surfaces.process_frame import ProcessFrame
from surfaces.complete_frame import CompleteFrame
from frontend_functions.main_surface_functions import MainSurfaceFunctions
from frontend_functions.start_frame_functions import StartFrameFunctions
from tools import backend_function


class Console:

    def __init__(self, chuang, main_window):
        self.chuang = chuang
        self.main_window = main_window
        # 初始化各种框架的界面
        backend_function.clear_cache()
        self.main_surface = MainSurface(self.main_window)
        self.start_frame = StartFrame(self.main_surface)
        self.tools_frame = ToolsFrame(self.main_surface)
        self.extract_frame = ExtractFrame(self.main_surface)
        self.audio_transfer_frame = AudioTransferFrame(self.main_surface)
        self.process_frame = ProcessFrame(self.main_surface)
        self.complete_frame = CompleteFrame(self.main_surface)
        self.frame_dict = {
            "start_frame": self.start_frame,
            "tools_frame": self.tools_frame,
            "extract_frame": self.extract_frame,
            "audio_transfer_frame": self.audio_transfer_frame,
            "process_frame": self.process_frame,
            "complete_frame": self.complete_frame
        }
        # 初始化前端函数
        self.main_surface_functions = MainSurfaceFunctions(self.chuang, self.main_surface, self.frame_dict)
        self.start_frame_functions = StartFrameFunctions(self.frame_dict)
        # 绑定函数
        self.main_surface_functions._bind_functions(self.main_surface_functions)
        # 默认生成start_frame
        self.create_start_frame()

    def create_start_frame(self):
        self.start_frame._setup_start_frame_widgets()
        self.start_frame_functions._bind_functions()