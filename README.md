# Video Edit Tools

Tools for generate best scenes of a movie.

## Requirements

* ffmpeg installed in the system.

 
### Time split 

Parses a file containing times per each and generate a video for each scenes.

The format of file is one scene per line and each line is in this format {begin_time},{end_time}. Example:
00:01:03,00:03:13

```
python time_split.py movie.mp4 times.txt
```

### Speed up

Generate a video speed up from each video in scenes_folder. The generated video has a speed up of 4 by default.

```
python speed_up.py scenes_folder
python speed_up.py speed scenes_folder
```

