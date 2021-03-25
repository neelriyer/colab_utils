from pathlib import Path
from IPython.display import HTML
from base64 import b64encode
from ._video_to_frames import video_to_frames
import os
import cv2


__all__ = ['show_short_video', 'video_to_frames']

def show_short_video(file, seconds = 10):

  path = Path(file)

  new_file_name = path.stem + '_short' + path.suffix
  output_file = path.parents[0]/str(new_file_name)
  print(output_file)

  end_time = '00:00:'+str(seconds)
  cmd = 'ffmpeg -loglevel warning -y -ss 00:00:00 -i '+file+' -c copy -t '+end_time + ' ' + output_file
  os.system(cmd)
  
  mp4 = open(output_file,'rb').read()
  data_url = "data:video/mp4;base64," + b64encode(mp4).decode()
  return HTML("""
  <video width=400 controls>
        <source src="%s" type="video/mp4">
  </video>
  """ % data_url)


def frame_extractor(video_path, frames_dir, overwrite=False, every=1, chunk_size=1000):
  video_to_frames(video_path, frames_dir, overwrite, every, chunk_size)



