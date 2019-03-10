def adv_print(*args, start=0, **kwargs):
    args_list = list()
    for item in args:
        args_list.append(str(item))
    result = ' '.join(args_list)

    if start > 0:
        result = result[start:]

    if kwargs.get('max_line'):
        counter = 0
        res = ''
        for symbol in result:
            if counter < kwargs['max_line']:
                res += symbol
            else:
                res += '\n'
                res += symbol
                counter = 0
            counter += 1
        result = res
        del kwargs['max_line']

    if kwargs.get('in_file'):
        with open('text_file.txt', 'w') as file:
            file.write(result)
        del kwargs['in_file']

    print(*result.split(' '), **kwargs)
