
import threading
from tools import backend_function
from tools.storage import Storage


class FrameFunctions:

    def __init__(self, frame_dict):
        self.tools_frame = frame_dict["tools_frame"]

        self.can_transfer = False


    def work_extract_button_function(self):

        # 加一个线程
        threading_get_api = threading.Thread(target=self.get_api_backend)
        threading_get_api.start()

    def get_api_backend(self):
        pass

    def update_bar(self):
        pass

    def output_path_function(self):
        pass

    def output_type_function(self):

        pass






