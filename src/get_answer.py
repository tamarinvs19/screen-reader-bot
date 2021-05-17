import csv


def get_answer(question: str) -> [str]:
    with open('data/answers.csv', 'r') as table:
        cin = csv.DictReader(table, fieldnames=['question', 'answer'])
        data = [row for row in cin]
    
    def pattern0(x):
        return x[:15] == question[:15]
    def pattern1(x):
        return x[:60] == question[:60]
    def pattern2(x):
        return x[-60:] == question[-60:]
    def pattern3(x):
        return x[3:60] in question
    def pattern4(x):
        return question[3:60] in x
    def pattern(x):
        return (pattern1(x) or pattern2(x) or pattern3(x) or pattern4(x)) or (pattern0(x))
    filtred_data = [row for row in data if pattern(row['question'])]
    if len(filtred_data) == 0:
        filtred_data = [{'question': 'Не удалось распознать, попробуй еще раз', 'answer': 'I do not know ((('}]
    return filtred_data


if __name__ == '__main__':
    get_answer('')
