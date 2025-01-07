import os
import shutil
import subprocess
from moviepy.editor import VideoFileClip
from PyQt5.Qt import QFileDialog
from tools.storage import Storage


def get_default_output_path():
    default_output_path = os.path.join(os.path.expanduser("~"), f"Downloads\\")
    default_output_path = os.path.normpath(default_output_path)
    return default_output_path

def get_temp_output_folder():
    temp_output_folder = os.path.normpath(".\\cache")
    temp_output_folder = os.path.normpath(temp_output_folder)
    return  temp_output_folder



def select_file_path(select_type):

    video_file_types = Storage().get_info("video_file_types")
    audio_file_types = Storage().get_info("audio_file_types")
    can_select_formats = ""

    if select_type == "video":
        for can_select_format in video_file_types:
            can_select_formats += f"(*.{can_select_format});;"

    elif select_type == "audio":
        for can_select_format in audio_file_types:
            can_select_formats += f"(*.{can_select_format});;"


    file_path = QFileDialog.getOpenFileName(None, "请从本地上传完成的任务......",
                                            "./", can_select_formats)
    file_path = file_path[0]

    if file_path != '':
        file_path = os.path.normpath(file_path)
        file_total_name = file_path.split("\\")[-1]
        file_name = file_total_name.rsplit(".", 1)[0]

        Storage().store_info("selected_file_path", file_path)
        Storage().store_info("selected_file_total_name", file_total_name)
        Storage().store_info("selected_file_name", file_name)

        return True
    return False


def clear_store_info():
    try:
        Storage().clear_info("selected_file_path")
        Storage().clear_info("final_output_folder")
        Storage().clear_info("final_output_format")
        Storage().clear_info("final_output_path")
        Storage().clear_info("temp_output_path")
        Storage().clear_info("selected_file_path")
        Storage().clear_info("selected_file_total_name")
        Storage().clear_info("selected_file_name")
        print("clear completed")

    except Exception as E:
        print(E)

def check_if_output_file_exists():
    output_path = Storage().get_info("final_output_path")
    return os.path.exists(output_path)

"""
    后端函数
"""
def transfer_video2audio():

    original_file_path = Storage().get_info("selected_file_path")
    audio_clip = VideoFileClip(original_file_path)
    output_file_path = Storage().get_info("final_output_path")
    temp_file_path = Storage().get_info("temp_output_path")
    temp_output_path_mp3 = Storage().get_info("temp_output_path_mp3")


    if Storage().get_info("final_output_format") == "mp3":

        audio_clip.audio.write_audiofile(temp_file_path)

    else:
        ffmpeg_path = Storage().get_info("ffmpeg_path")

        audio_clip.audio.write_audiofile(temp_output_path_mp3)

        subprocess.run(f'{ffmpeg_path} -i "{temp_output_path_mp3}" "{temp_file_path}"', shell=True,
                       stdout=subprocess.PIPE, text=True)

        os.remove(temp_output_path_mp3)

    shutil.move(temp_file_path, output_file_path)
    audio_clip.close()

def audio_transfer():

    original_file_path = Storage().get_info("selected_file_path")
    output_file_path = Storage().get_info("final_output_path")

    ffmpeg_path = Storage().get_info("ffmpeg_path")

    temp_file_path = Storage().get_info("temp_output_path")

    subprocess.run(f'{ffmpeg_path} -i "{original_file_path}" "{temp_file_path}"', shell=True,
                   stdout=subprocess.PIPE, text=True)

    shutil.move(temp_file_path, output_file_path)


def voice_split():
    original_file_path = Storage().get_info("selected_file_path")
    output_file_path = Storage().get_info("final_output_path")

    spleeter_path = Storage().get_info("spleeter_path")

    subprocess.run(f'{spleeter_path} "{original_file_path}"', shell=True,
                   stdout=subprocess.PIPE, text=True)

    path_list = original_file_path.rsplit(".", 1)
    temp_output_path = path_list[0] + ".vocals.mp3"
    other_path_file = path_list[0] + ".accompaniment.mp3"
    os.remove(other_path_file)
    shutil.move(temp_output_path, output_file_path)

def bgm_split():
    original_file_path = Storage().get_info("selected_file_path")
    output_file_path = Storage().get_info("final_output_path")

    spleeter_path = Storage().get_info("spleeter_path")

    subprocess.run(f'{spleeter_path} "{original_file_path}"', shell=True,
                   stdout=subprocess.PIPE, text=True)

    path_list = original_file_path.rsplit(".", 1)
    temp_output_path = path_list[0] + ".accompaniment.mp3"
    other_path_file = path_list[0] + ".vocals.mp3"
    os.remove(other_path_file)
    shutil.move(temp_output_path, output_file_path)


"""end"""







