"""Text extracting script

This script run `tesseract` and
extract the text from the picture to the new file."""

import os
import time


def run_tesseract(img_name: str, output_name: str) -> None:
    os.system('tesseract {} {} -l rus --psm 4'.format(img_name, output_name))
    time.sleep(1)
    os.system('rm {}'.format(img_name))


def read_all(dir_name: str, output_dir: str) -> None:
    files: [str] = os.popen('ls {}'.format(dir_name)).read().split('\n')[:-1]
    file_name: str
    for file_name in files:
        run_tesseract(dir_name + file_name, output_dir + file_name)

