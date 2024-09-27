import sys
from tools import backend_function


class MainSurfaceFunctions:

    def __init__(self, chuang, main_surface, frame_dict):
        self.chuang = chuang
        self.main_surface = main_surface
        self.tools_frame = frame_dict["tools_frame"]

    def _bind_functions(self, main_surface_functions):
        self.main_surface.title_exit_button.clicked.connect(lambda: self.title_exit_button_function())

    def title_exit_button_function(self):
        # 清空temp文件夹
        backend_function.clear_cache()
        sys.exit(self.chuang.exec_())
