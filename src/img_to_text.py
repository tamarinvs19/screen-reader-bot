"""Text extracting script

This script run `tesseract` and
extract the text from the picture to the new file."""

import config as cfg

import os
import sys
import time


def crop(img_name: str) -> None:
    img_info: str = os.popen('identify {}'.format(img_name)).read()
    img_formats = ['PNG', 'JPG', 'JPEG']
    for img_format in img_formats:
        if img_format in img_info:
            sizes: [int] = list(map(int, img_info.split(img_format)[1].strip().split()[0].split('x')))
            break
    height: int = sizes[0] - cfg.CROP_TOP
    width: int = sizes[1] - cfg.CROP_RIGHT - cfg.CROP_LEFT

    os.system('convert {} -crop {}x{}+{}+{} {}'.format(
        img_name, width, height, cfg.CROP_LEFT, cfg.CROP_TOP, img_name
        ))


def run_tesseract(img_name: str, output_name: str) -> None:
    os.system('tesseract {} {} -l rus+eng --psm 4'.format(img_name, output_name))
    time.sleep(1)
    os.system('rm {}'.format(img_name))


def backup_image(img_name: str) -> None:
    os.system('cp {dir_name}{name} {backup_dir}{name}'.format(name=img_name, backup_dir=cfg.BACKUP_DIR, dir_name=cfg.DIR_NAME))


def read_all(dir_name: str, output_dir: str) -> None:
    files: [str] = os.popen('ls {}'.format(dir_name)).read().split('\n')[:-1]
    file_name: str
    for file_name in files:
        crop(dir_name + file_name)
        backup_image(file_name)
        run_tesseract(dir_name + file_name, output_dir + file_name)


if __name__ == '__main__':
    file_name: str = sys.argv[1]
    run_tesseract(file_name, file_name)
    with open(file_name + '.txt', 'r') as f:
        print(''.join(f.readlines()))
