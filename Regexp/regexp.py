import re
import csv

with open("phonebook_raw.csv", encoding='utf8') as f:
    rows = csv.reader(f, delimiter=",")
    contact_list = list(rows)

pattern = '(^[А-Яа-яёЁ]*)\s?\,?([а-яА-Я]*)\s?\,?([А-Яа-я]*)?,*[а-яА-Я,\s–]*(\+7|8)?\s?\(?(\d{3})?\)?\s?\-?(\d{3})?\-?(\d{2})?\-?(\d{2})?\s?\(?[А-Яа-я. ]*(\d*)?'
pattern = re.compile(pattern)

result_list = list()

for i in contact_list[1:]:
    res = list(pattern.findall('\n'.join(i))[0])
    if res[4] and res[5]:
        if res[8]:
            if res[3] == '+7':
                result = (f'{res[0]} {res[1]} {res[2]} {res[3]}({res[4]}){res[5]}-{res[6]}-{res[7]} доб.{res[8]}')
                result_list.append(result)
            else:
                result = (f'{res[0]} {res[1]} {res[2]} +7({res[4]}){res[5]}-{res[6]}-{res[7]} доб.{res[8]}')
                result_list.append(result)
        else:
            if res[3] == '+7':
                result = (f'{res[0]} {res[1]} {res[2]} {res[3]}({res[4]}){res[5]}-{res[6]}-{res[7]}')
                result_list.append(result)
            else:
                result = (f'{res[0]} {res[1]} {res[2]} +7({res[4]}){res[5]}-{res[6]}-{res[7]}')
                result_list.append(result)

print(result_list)
with open("phonebook.csv", "w", encoding='utf8') as f:
    datawriter = csv.writer(f,)
    datawriter = csv.writer(f, delimiter=',')
    for row in result_list:
        columns = [c.strip() for c in row.strip(', ').split(',')]
        datawriter.writerow(columns)
