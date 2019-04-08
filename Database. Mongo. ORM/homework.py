import csv
from pymongo import MongoClient
import re
from pprint import pprint
from datetime import datetime

client = MongoClient()
tickets_db = client.ticket_db


def read_data(filename):
    with open(filename, encoding='utf8') as f:
        reader = csv.reader(f)
        next(reader)
        my_dict_list = list()
        for line in reader:
            name, price, place, date = line
            my_dict = {
                'name': name,
                'price': int(price),
                'place': place,
                'date': date
            }
            my_dict_list.append(my_dict)
        tickets_db.tickets.insert_many(d for d in my_dict_list)


def find_cheapest():
    result = list()
    for ticket in tickets_db.tickets.find({}).sort('price', 1):
        result.append(f"{ticket['name']} - ({ticket['price']} руб.). По адресу: {ticket['place']} ({ticket['date']})")
    return result


def find_by_name(name):
    escaped_name = re.escape(name)
    pattern = re.compile(r'(.*?{}.*?)'.format(escaped_name), re.IGNORECASE)
    res = tickets_db.tickets.find({'name': pattern})
    result = list()
    for item in res:
        result.append(item['name'])
    return result


def date_search(needed_data):
    needed_data = re.escape(needed_data)
    pattern = re.compile(r'({}.*?)'.format(needed_data), re.IGNORECASE)
    res = tickets_db.tickets.find({'date': pattern})
    result = list()
    for item in res:
        result.append(item['name'])
    return result


def run():
    if tickets_db.tickets.count_documents({}) == 0:
        read_data('artists.csv')
    else:
        print('Данные уже в базе')
    print(find_by_name('К'))
    pprint(find_cheapest())
    print(date_search('13.07'))


if __name__ == '__main__':
    run()
