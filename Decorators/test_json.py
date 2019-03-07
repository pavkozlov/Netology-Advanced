import json
from pprint import pprint
import datetime


def log_file(other_func):
    def write_log(*args, **kwargs):
        path = input('Path to file: ')
        with open(f'{path}.txt', 'w') as file:
            file.write(str(datetime.datetime.now()))
            file.write('\t')
            file.write(*args, **kwargs)
            file.write('\t')
            file.write(other_func.__name__)
        result = other_func(*args, **kwargs)
        return result

    return write_log


@log_file
def get_descriptions(filename):
    words_list = list()
    with open(filename, encoding='UTF-8') as file:
        result = json.load(file)

    for descriptions in result['rss']['channel']['items']:
        for words in descriptions['description'].strip().split():
            if len(words) > 6:
                words_list.append(words.lower())
    return words_list


def get_top(words_list, top):
    count_dict = dict()
    for words in words_list:
        count_dict[words] = words_list.count(words)
    count_dict = sorted(count_dict, key=count_dict.get, reverse=True)
    return count_dict[:top]


if __name__ == '__main__':
    pprint(get_top(get_descriptions('newsafr.json'), 10))
