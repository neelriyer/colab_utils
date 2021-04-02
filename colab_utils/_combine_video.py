import os
from pathlib import Path
import glob

def _write_to_txt(file, video_path):
  with open(file, 'a') as f:
      f.write("file  '%s'\n" % video_path)

def _write_videos_to_txt(merge_file, folder):
  if Path(merge_file).exists():
    os.remove(merge_file)

  # write videos to txt
  for i, file in enumerate(glob.glob(str(Path(folder)/'*.*'))):
    new_name = os.path.dirname(file) + '/' +str(i) + Path(file).suffix
    os.rename(file, new_name)
    print(new_name)
    _write_to_txt(merge_file, new_name)

