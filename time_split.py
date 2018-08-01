import sys
from subprocess import call


def usage(program_name):
    print("Usage: {} [video_file] [timing_file]".format(
        program_name,

    ))
    sys.exit(1)


def execute(command):
    call(command.split())


def ffmpeg(input_file, output_file, from_time, to_time):
    command = 'ffmpeg -y -i {input_f} -ss {i} -to {t} {output_f}'.format(
        input_f=input_file,
        output_f=output_file,
        i=from_time,
        t=to_time
    )
    execute(command)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        usage(sys.argv[0])

    input_video=sys.argv[1]
    input_file=sys.argv[2]

    with open(input_file) as f:
        content = f.readlines()
        times = [x.strip().split(',') for x in content]
        for counter, time in enumerate(times):
            output_file = "scene_{}.mp4".format(counter)
            from_time=time[0].strip()
            to_time=time[1].strip()

            ffmpeg(input_video, output_file, from_time, to_time)
