import os
import sys
import shutil
import subprocess
from moviepy.editor import VideoFileClip
from PyQt5.Qt import QFileDialog


def read_file_path(file_type):
    file_path = QFileDialog.getOpenFileName(None, "请从本地上传完成的任务......",
                                            "./", f"(*.*);;(*.{file_type})")
    file_path = file_path[0]
    file_name = file_path.split("/")[-1]
    return file_path, file_name

def get_temp_file_info():
    file_list = os.listdir("./temp/")
    file_name = file_list[0]
    source_path = "./temp/" + file_name
    return file_name, source_path

def get_default_output_path():
    default_output_path = os.path.join(os.path.expanduser("~"), f"Downloads\\")
    default_output_path = os.path.normpath(default_output_path)
    return default_output_path

def save_file(source_path, output_path):
    shutil.copy(source_path, output_path)

def custom_save_file(source_path, output_path):
    try:
        shutil.copy(source_path, output_path)
    except Exception as e:
        print(e)

def transfer_video2audio(file_path, output_type, file_name):
    # 视频转音频
    file_name = file_name[:-4]
    # 默认视频转mp3
    video2audio_output_file = "./temp/" + file_name + ".mp3"
    audio_clip = VideoFileClip(file_path)
    audio_clip.audio.write_audiofile(video2audio_output_file)
    audio_clip.close()
    if output_type != "mp3":
    # 音频如果用户输入了格式，就进行转换
        # setting ffmpeg
        project_dir = os.path.dirname(sys.argv[0])
        project_dir = os.path.normpath(project_dir)
        ffmpeg_path = os.path.join(project_dir, "ffmpeg/bin/ffmpeg")
        ffmpeg_path = os.path.normpath(ffmpeg_path)
        # setting file path
        input_file_path = project_dir + "\\temp\\" + file_name + ".mp3"
        output_file_path = project_dir + "\\temp\\" + file_name + "." + output_type
        # run
        subprocess.run(f'{ffmpeg_path} -i "{input_file_path}" "{output_file_path}"', shell=True,
                       stdout=subprocess.PIPE, text=True)

def audio_transfer(file_path, output_type, file_name):
    file_name = file_name.rsplit(".", 1)[0]
    # setting  ffmpeg
    project_dir = os.path.dirname(sys.argv[0])
    project_dir = os.path.normpath(project_dir)
    ffmpeg_path = os.path.join(project_dir, "ffmpeg/bin/ffmpeg")
    ffmpeg_path = os.path.normpath(ffmpeg_path)
    # setting file path
    input_file_path = os.path.normpath(file_path)
    output_file_path = project_dir + "\\temp\\" + file_name + "." + output_type
    # run
    subprocess.run(f'{ffmpeg_path} -i "{input_file_path}" "{output_file_path}"', shell=True,
                   stdout=subprocess.PIPE, text=True)

def noise_reduce(file_path, output_path):
    project_dir = os.path.dirname(sys.argv[0])
    project_dir = os.path.normpath(project_dir)
    ffmpeg_path = os.path.join(project_dir, "ffmpeg/bin/ffmpeg")
    ffmpeg_path = os.path.normpath(ffmpeg_path)
    subprocess.run(f'{ffmpeg_path} -i "{file_path}" -af "afftdn=nr=30" "{output_path}"', shell=True,
                   stdout=subprocess.PIPE, text=True)

def check_if_file_exists(output_path):
    return os.path.exists(output_path)

def clear_cache():
    # 删除临时文件
    shutil.rmtree("./temp")
    os.mkdir("./temp")

def reset_pre_frame(current_frame):
    current_frame.work_select_label_index = 0
    current_frame.work_tip_label_index = 0
    current_frame.work_select_label.hide()
    current_frame.work_outputs_selection.hide()



