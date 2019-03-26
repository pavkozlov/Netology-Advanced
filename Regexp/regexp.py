import re
import csv


class PhoneBook:
    def __init__(self, filename, outfile_name='phonebook.csv'):
        self.pattern = '(^[А-Яа-яёЁ]*)\s?\,?([а-яА-Я]*)\s?\,?([А-Яа-я]*)?,*[а-яА-Я,\s–]*(\+7|8)?\s?\(?(\d{3})?\)?\s?\-?(\d{3})?\-?(\d{2})?\-?(\d{2})?\s?\(?[А-Яа-я. ]*(\d*)?.*'
        self.filename = filename
        self.contact_list = self.open_and_read()
        self.info_list = self.find_info()
        self.result = self.format_info()
        self.outfile_name = outfile_name
        self.write_to_file()

    def open_and_read(self):
        with open(self.filename, encoding='utf8') as f:
            rows = csv.reader(f, delimiter="\n")
            contact_list = list(rows)
        return contact_list

    def find_info(self):
        info_list = list()
        for i in self.contact_list[1:]:
            info_list.append(re.sub(self.pattern, r'\1 \2 \3 +7(\5)\6-\7-\8 (доб.\9)', ''.join(i)))
        return info_list

    def format_info(self):
        result = list()
        for contact in self.info_list:
            contact = contact.split()
            if len(contact[3]) < 16:
                pass
            else:
                if len(contact[4]) > 6:
                    result.append(contact)
                else:
                    result.append(contact[:4])
        return result

    def write_to_file(self):
        with open(self.outfile_name, "w", encoding='utf8') as f:
            for items in self.result:
                f.write(' '.join(items) + ',\n')


if __name__ == '__main__':
    PhoneBook('phonebook_raw.csv')
