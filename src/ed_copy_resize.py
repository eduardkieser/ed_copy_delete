from pathlib import Path
import subprocess
from PIL import Image
import sys

def resize_image(input_path, output_path, max_size=2048):
    if input_path.suffix.lower() == '.arw':
        # Using ffmpeg to convert and resize the ARW file
        cmd = f"magick '{input_path}' -resize '{max_size}x{max_size}>' '{output_path}'"
        subprocess.run(cmd, shell=True, check=True)
    else:
        # Existing code for other image formats
        img = Image.open(input_path)
        ratio = min(max_size / img.size[0], max_size / img.size[1])
        new_size = (int(img.size[0] * ratio), int(img.size[1] * ratio))
        img = img.resize(new_size, Image.ANTIALIAS)
        img.save(output_path, 'JPEG')

def resize_and_convert_directory(input_dir, output_dir, max_size=1024):
    input_dir = Path(input_dir)
    output_dir = Path(output_dir)

    if not output_dir.exists():
        output_dir.mkdir(parents=True)

    file_path_list = list(input_dir.rglob('*'))
    num_files = len(file_path_list)

    for ix, file_path in enumerate(file_path_list):

        if file_path.is_file() and file_path.suffix.lower() in ['.png', '.jpg', '.jpeg', '.arw']:
            relative_path = file_path.relative_to(input_dir)
            new_output_path = output_dir.joinpath(relative_path).with_suffix('.jpeg')
            if new_output_path.exists():
                print(f"Skipping {new_output_path} as it already exists")
                continue
            else:
                print(f"Processing {ix}/{num_files}: {file_path}")
            new_output_path.parent.mkdir(parents=True, exist_ok=True)
            resize_image(file_path, new_output_path, max_size)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <folder_name>")
        sys.exit(1)

    folder_name = sys.argv[1]
    base_dir = Path.cwd()
    input_directory = base_dir / folder_name
    output_directory = base_dir / (folder_name + '_small')
    resize_and_convert_directory(input_directory, output_directory)
