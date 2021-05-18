"""Text parser

This script can parse text and found exercises."""

import os


def parse_text(file_name: str, patterns: [str]) -> str:
    with open(file_name, 'r') as text_file:
        text: [str] = text_file.readlines()
    flag: int = 0
    result_text: str = ''
    line: str
    for line in text:
        # print('-----> ', line)
        if any(pattern in line for pattern in patterns):
            flag = 1
        elif line not in {'', '\n'} and 'Вопрос' not in line and 'Показать ответ' not in line:
            if flag == 2:
                result_text += line.strip()
                break
            else: 
                flag += 1
    if result_text == '':
        result_text = 'kokokokokokokokokok'
    os.system('rm {}'.format(file_name))
    print(result_text)
    return result_text

def parse_all(dir_name: str, patterns: [str]) -> [str]:
    files: [str] = os.popen('ls {}'.format(dir_name)).read().split('\n')[:-1]
    file_name: str
    return [parse_text(dir_name + file_name, patterns) for file_name in files]
        

