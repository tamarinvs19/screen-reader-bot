import time
import requests

import parse_text
import img_to_text
import get_answer
import config as cfg


def main() -> [dict]:
    img_to_text.read_all(cfg.DIR_NAME, cfg.OUTPUT_DIR)
    questions = parse_text.parse_all(cfg.OUTPUT_DIR)
    res = []
    for question in questions:
        res += get_answer.get_answer(question)
    return res


if __name__ == '__main__':
    print(main())
