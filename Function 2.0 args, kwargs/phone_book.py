class Contact:
    def __init__(self, name, last_name, phone_number, *args, favorite=False, **kwargs):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.favorite = favorite
        if kwargs.get('email'):
            self.email = kwargs['email']
        else:
            self.email = ''
        if kwargs.get('telegram'):
            self.telegram = kwargs['telegram']
        else:
            self.telegram = ''
        self.other_numbers = args

    def __str__(self):
        print(f'Имя: {self.name}')
        print(f'Фамилия: {self.last_name}')
        print(f'Телефон: {self.phone_number}')
        if self.favorite:
            print('В избранных: Да')
        else:
            print('В избранных: Нет')
        if self.email or self.telegram:
            print('Дополнительная информация: ')
        if self.email:
            print(f'\tE-mail: {self.email}')
        if self.telegram:
            print(f'\tTelegram: {self.telegram}')
        if len(self.other_numbers) > 0:
            print('Дополнительные номера:')
            for number in self.other_numbers:
                print(f'\t{number}')


dima = Contact('Dima', 'Ivanov', '+89099099090', favorite=True, telegram='@dima', email='dima@dima.ru')
dima.__str__()

ivan = Contact('Ivan', 'Petrov', '+89099099090', '101', '102', '103')
ivan.__str__()


class PhoneBook:
    def __init__(self, name):
        self.name = name
        self.contact_list = list()

    def add_contact(self, contact):
        self.contact_list.append(contact)

    def del_contact(self, phone_num):
        for contact in self.contact_list:
            if contact.phone_number == phone_num:
                self.contact_list.remove(contact)

    def print_contacts(self):
        for contact in self.contact_list:
            print(f'{contact.name}  {contact.last_name} {contact.phone_number}')

    def get_favorite(self):
        for contact in self.contact_list:
            if contact.favorite:
                print(f'{contact.name}  {contact.last_name} {contact.phone_number}')

    def search(self, name, last_name):
        for contact in self.contact_list:
            if contact.name.lower() == name.lower() and contact.last_name.lower() == last_name.lower():
                print(f'{contact.name}  {contact.last_name} {contact.phone_number}')


friends = PhoneBook('friends')
friends.add_contact(dima)
friends.add_contact(ivan)
friends.print_contacts()

friends.get_favorite()

friends.search('Ivan', 'Petrov')

friends.del_contact('+89099099090')
friends.print_contacts()
