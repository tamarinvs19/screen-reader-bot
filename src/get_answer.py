import csv

import config as cfg


def get_answer(question: str) -> [str]:
    def pattern(row):
        return any([
            row[:12] == question[3:15],
            row[:57] == question[3:60],
            row[-60:] == question[-60:],
            row[3:60] in question,
            question[5:60] in row if len(question) > 12 else question in row,
            ])

    with open(cfg.ANSWERS_TABLE, 'r') as table:
        cin = csv.DictReader(table, fieldnames=['question', 'answer'])

        filtred_data = [row for row in cin if pattern(row['question'])]

    if len(filtred_data) == 0:
        filtred_data = [
            {
                'question': question,
                'answer': 'Не удалось распознать, попробуй еще раз',
                },
            ]

    return filtred_data


def find_answer(answer: str) -> [str]:
    def pattern(row):
        return answer in row

    with open(cfg.ANSWERS_TABLE, 'r') as table:
        cin = csv.DictReader(table, fieldnames=['question', 'answer'])
        filtred_data = [row for row in cin if pattern(row['answer'])]

    if len(filtred_data) == 0:
        filtred_data = [
            {
                'question': 'Не удалось распознать ответ, попробуй еще раз',
                'answer': 'I do not know (((',
                },
            ]

    return filtred_data


if __name__ == '__main__':
    get_answer('Random question')
