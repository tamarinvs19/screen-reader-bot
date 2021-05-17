import parse_text
import img_to_text
import get_answer

import time

dir_name: str = '~/Pictures/Screenshots/'
output_dir: str = 'data/texts/'
patterns: [str] = [
    'Вопрос',
    'Воnрос',
    'Вoпрос',
    'Bопрос',
    'Bоnрос',
    'Bonpoc'
    ]


def main() -> [dict]:
    img_to_text.read_all(dir_name, output_dir)
    questions = parse_text.parse_all(output_dir, patterns)
    res = []
    for question in questions:
        res += get_answer.get_answer(question)
    return res


if __name__ == '__main__':
    while True:
        print(main())
        time.sleep(5)
