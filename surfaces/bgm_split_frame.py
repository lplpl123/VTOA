from surfaces.frame import Frame

class BgmSplitFrame(Frame):

    def __init__(self, main_surface):
        super().__init__(main_surface)

    def _setup_work_frame_frame_widgets(self):

        super()._setup_work_frame_frame_widgets()

        self.extract_selected_file_info.setText("伴奏提取，请选择文件")





