import os
import shutil


def copy_directory(source, destination):
    if os.path.exists(destination):
        shutil.rmtree(destination)
    os.mkdir(destination)

    for item in os.listdir(source):
        source_path = os.path.join(source, item)
        destination_path = os.path.join(destination, item)

        if os.path.isdir(source_path):
            copy_directory(source_path, destination_path)
        else:
            shutil.copy(source_path, destination_path)
            print(f"Copied file: {destination_path}")