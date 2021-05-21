"""Text parser

This script can parse text and found exercises."""

import os


def parse_text(file_name: str) -> str:
    with open(file_name, 'r') as text_file:
        text: [str] = text_file.readlines()
    line: str
    for line in text:
        if len(line) > 5:
            result_text = line
            break
    if result_text == '':
        result_text = 'kokokokokokokokokok'
    os.system('rm {}'.format(file_name))
    print(result_text)
    return result_text

def parse_all(dir_name: str) -> [str]:
    files: [str] = os.popen('ls {}'.format(dir_name)).read().split('\n')[:-1]
    file_name: str
    return [parse_text(dir_name + file_name) for file_name in files]
        

