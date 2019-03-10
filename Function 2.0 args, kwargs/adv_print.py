def adv_print(text, start=0, **kwargs):
    result = str(text)[start:]
    if kwargs.get('max_line'):
        res = ''
        counter = 0
        for symbol in result:
            if counter < kwargs['max_line']:
                res += symbol
            else:
                res += '\n'
                res += symbol
                counter = 0
            counter += 1
        result = res
    if kwargs.get('in_file'):
        with open(f'{text}.txt', 'w') as file:
            file.write(result)
    print(result)
    return result


adv_print('I Love Netology', max_line=4, in_file=True)
adv_print('Python')
adv_print(139595, start=2)
