#task1
def get_summ(one, two, delimiter='&'):
    return f'{one}{delimiter}{two}'

result_line = get_summ('Learn', 'python')
print(result_line.upper())
#task2
def format_price(price):
    price = int(price)
    return f'Цена: {price} руб.'
result = format_price(56.24)
print(result)
