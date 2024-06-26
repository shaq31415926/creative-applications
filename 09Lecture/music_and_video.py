import os
os.environ['IMAGEIO_FFMPEG_EXE'] = '/opt/homebrew/bin/ffmpeg'
import moviepy.editor as mp

video1 = mp.VideoFileClip("video/example.mp4")
final = video1.set_audio(mp.AudioFileClip("music/trimmed_file.mp3"))

final.write_videofile("video/example_w_sound.mp4",
                      fps=30,
                      audio_codec="aac",
                      audio_bitrate="192k")