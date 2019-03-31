import csv
from pymongo import MongoClient
import re
from pprint import pprint
from datetime import datetime

client = MongoClient()
tickets_db = client.ticket_db


def read_data(filename):
    with open(filename, encoding='utf8') as f:
        res = []
        reader = csv.reader(f)
        next(reader)
        for line in reader:
            name, price, place, date = line
            tickets_db.tickets.insert_one({
                'name': name,
                'price': int(price),
                'place': place,
                'date': date
            })


def find_cheapest():
    result = list()
    for ticket in tickets_db.tickets.find({}).sort('price', 1):
        result.append(f"{ticket['name']} - ({ticket['price']} руб.). По адресу: {ticket['place']} ({ticket['date']})")
    return result


def find_by_name(name):
    result = list()
    pattern = f'(.*{name}.*)'
    for ticket in tickets_db.tickets.find({}):
        z = re.search(pattern, ticket['name'], flags=re.IGNORECASE)
        if z:
            result.append(z.group())
    return result


def date_search(needed_data: datetime):
    result = list()
    for ticket in tickets_db.tickets.find({}):
        try:
            date = datetime(year=2019, month=int(ticket['date'][3:]), day=int(ticket['date'][:2]))
        except ValueError:
            date = datetime(year=2019, month=int(ticket['date'][3:]), day=int(ticket['date'][:1]))
        datetime_object = datetime.strptime(needed_data, '%d.%m.%Y')
        if date == datetime_object:
            result.append(
                f"{ticket['name']} - ({ticket['price']} руб.). По адресу: {ticket['place']} ({ticket['date']}.2019)")
    return result


def run():
    if tickets_db.tickets.count_documents({}) == 0:
        read_data('artists.csv')
    else:
        print('Данные уже в базе')
    print(find_by_name('К'))
    pprint(find_cheapest())
    print(date_search('13.07.2019'))


if __name__ == '__main__':
    run()
