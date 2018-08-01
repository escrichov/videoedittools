import sys
import os
from subprocess import call


def usage(program_name):
    print("Usage: {} [video_file] (speed). Default speed=4".format(
        program_name,

    ))
    sys.exit(1)


def execute(command):
    call(command.split())


def ffmpeg_speed_up(input_file, output_file, speed):
    ffmpeg_speed = 1.0/speed
    command = 'ffmpeg -y -i {input_f} -filter:v "setpts={speed}*PTS" {output_f}'.format(
        input_f=input_file,
        speed=ffmpeg_speed,
        output_f=output_file
    )
    call(command, shell=True)


def ffmpeg_remove_audio(input_file, output_file):
    command = 'ffmpeg -y -i {input_f} -c copy -an {output_f}'.format(
        input_f=input_file,
        output_f=output_file,
    )
    execute(command)


def process_file(input_video, speed):
    video_name = input_video.split('.')[0]
    video_extension = input_video.split('.')[1]

    video_no_audio = "{name}_noaudio.{extension}".format(
        name=video_name,
        extension=video_extension
    )
    video_speedup = "{name}_fast.{extension}".format(
        name=video_name,
        extension=video_extension
    )

    ffmpeg_remove_audio(input_video, video_no_audio)
    ffmpeg_speed_up(video_no_audio, video_speedup, speed)
    os.remove(video_no_audio)


def filter_hidden_files(files):
    return [f for f in files if f[0] != '.' ]


if __name__ == "__main__":
    if len(sys.argv) != 2 and len(sys.argv) != 2:
        usage(sys.argv[0])

    input_video=sys.argv[1]
    if len(sys.argv) == 3:
        speed=float(sys.argv[2])
    else:
        speed = 4

    if os.path.isfile(input_video):
        process_file(input_video, speed)
    elif os.path.isdir(input_video):
        files = os.listdir(input_video)
        files = filter_hidden_files(files)
        print files
        files.sort()
        for f in files:
            video_file = '{directory}/{f}'.format(directory=input_video, f=f)
            process_file(video_file, speed)
