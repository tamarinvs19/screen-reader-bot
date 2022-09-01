import csv
import re


def parse_business(text_file_name: str, csv_file_name: str) -> None:
    table_dict: list[dict] = []
    question: str = ''
    answer: str = ''
    flag: str = ''
    with open(text_file_name, 'rt') as fin:
        for line in fin.readlines():
            if re.search(r'\d+\. [^\n]', line):
                if flag == 'answer' and answer != '':
                    table_dict.append({'answer': answer, 'question': question})
                elif flag == 'answer':
                    answer += line.strip()
                elif flag == 'question':
                    question += line.strip()
                flag = 'question'
                question = line.strip().split('. ')[1]
            elif re.search(r'Ответ:', line):
                flag = 'answer'
                answer = line.strip().split('Ответ: ')[1]
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
    parse_business('data/business1.txt', 'data/business1.csv')
