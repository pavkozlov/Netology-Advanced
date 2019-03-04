import hashlib


class ToMd5:
    def __init__(self, filename):
        self.res = list()
        self.filename = filename

    def get_md5(self, list):
        start = 0
        stop = len(list)
        while start < stop:
            yield hashlib.md5(list[start].encode('utf-8')).hexdigest()
            start += 1

    def print_hash(self):
        with open(self.filename, 'r') as file:
            for row in file:
                self.res.append(row)

        for item in self.get_md5(self.res):
            print(item)


ToMd5('out.txt').print_hash()
