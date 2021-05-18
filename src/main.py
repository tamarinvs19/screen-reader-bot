import parse_text
import img_to_text
import get_answer

import time
import requests

dir_name: str = '~/Pictures/Screenshots/'
output_dir: str = 'data/texts/'
patterns: [str] = [
    'Вопрос',
    'Воnрос',
    'Вoпрос',
    'Bопрос',
    'Bоnрос',
    'Bonpoc',
    'Отправить',
    ]
TOKEN = '1761503051:AAG74bLr09NDP03IlZ9nSMM6ySCloKQaqPg'


def main() -> [dict]:
    img_to_text.read_all(dir_name, output_dir)
    questions = parse_text.parse_all(output_dir, patterns)
    res = []
    for question in questions:
        res += get_answer.get_answer(question)
    return res


def send_telegram(text: str):
    url = "https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}"
    token = TOKEN
    channel_id = "-1001441669791"

    r = requests.get(url.format(token, channel_id, text))

    if r.status_code != 200:
        pass

def send_info():
    info = main()
    if len(info) < 10:
        for data in info:
            send_telegram('__Question__: {} \n\n__Answer__: {}'.format(str(data['question']), str(data['answer'])))


if __name__ == '__main__':
    while True:
        send_info()
        time.sleep(15)
