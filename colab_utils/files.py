from pathlib import Path
import shutil

__all__ = ['copy_file_to_drive']

def copy_file_to_drive(file, output_folder, overwrite = False):
  drive_path = Path('/content/drive/MyDrive/')
  if not drive_path.exists(): raise 'drive not found. please mount drive.'
  base_path = drive_path/output_folder
  base_path.mkdir(parents = True, exist_ok = True)
  if (base_path/Path(file).name).exists() and overwrite: os.remove(base_path/Path(file).name)
  shutil.copyfile(file, str(base_path/Path(file).name))



