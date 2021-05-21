import csv
import re


def parse_philosophy(text_file_name: str, csv_file_name: str) -> None:
    table_dict: [dict] = []
    question: str = ''
    answer: str = ''
    flag: str = ''
    with open(text_file_name, 'rt') as fin:
        for line in fin.readlines():
            if re.search(r'\A\d*\. Вопрос:', line):
                if flag == 'answer' and answer != '':
                    table_dict.append({'answer': answer, 'question': question})
                flag = 'question'
                question = ''
            elif re.search(r'Ответ:', line):
                flag = 'answer'
                answer = ''
            elif flag == 'question':
                if question != '':
                    question += ' '
                question += line.strip()
            elif flag == 'answer':
                if answer != '':
                    answer += ' '
                answer += line.strip()

    with open(csv_file_name, 'wt') as fout:
        cout = csv.DictWriter(fout, ['question', 'answer'])
        cout.writeheader()
        cout.writerows(table_dict)


if __name__ == '__main__':
    parse_philosophy('data/philosophy.txt', 'data/philosophy.csv')
