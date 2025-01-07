from surfaces.frame import Frame

class VoiceSplitFrame(Frame):

    def __init__(self, main_surface):
        super().__init__(main_surface)

    def _setup_work_frame_frame_widgets(self):

        super()._setup_work_frame_frame_widgets()

        self.extract_selected_file_info.setText("人声提取，请选择文件")





