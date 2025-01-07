import sys
from frontend_functions.tools_frame_functions import ToolsFrameFunctions


class MainSurfaceFunctions:

    def __init__(self, chuang, main_surface, frame_dict):
        self.chuang = chuang
        self.main_surface = main_surface
        self.tools_frame = frame_dict["tools_frame"]
        self.tools_frame_functions = ToolsFrameFunctions(frame_dict)

    def _bind_functions(self):
        self.main_surface.title_exit_button.clicked.connect(lambda: self.title_exit_button_function())
        self.main_surface.start_button.clicked.connect(self.start_button_function)

    def title_exit_button_function(self):
        sys.exit(self.chuang.exec_())
        
    def start_button_function(self):
        self.tools_frame._setup_tools_frame_widgets()
        self.tools_frame_functions._bind_functions()
        print(2)
