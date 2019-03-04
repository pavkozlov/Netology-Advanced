import json
import wikipedia


class WikiLink:
    def __init__(self, filename, to_file):
        self.filename = filename
        self.to_file = to_file
        self.create_list()

    class GetNames:
        def __init__(self, file):
            self.file = file
            self.start = -1
            self.stop = len(self.file)

        def __iter__(self):
            return self

        def __next__(self):
            self.start += 1
            if self.start == self.stop:
                raise StopIteration
            return self.file[self.start]['name']['common']

    def create_list(self):
        with open(self.filename) as file:
            my_file = json.load(file)
        res = list()
        for countries in self.GetNames(my_file):
            try:
                result = wikipedia.page(countries)
                res.append(f'{result.title} {result.url}')
            except wikipedia.exceptions.DisambiguationError:
                country = f'{countries} (country)'
                result = wikipedia.page(country)
                res.append(f'{result.title} {result.url}')
        with open(self.to_file, 'a', encoding='utf8') as file:
            for line in res:
                file.write(f'{line}\n')


WikiLink('countries.json', 'out.txt')
