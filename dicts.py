#task1
my_dict = {
    'city': 'Москва',
    'temperature': '20'
}
print(my_dict['city'])
my_dict['temperature'] = int(my_dict['temperature']) - 5 
print(my_dict)
#task2
print(my_dict.get('country', 'Россия'))
my_dict['date'] = '27.05.2019'
print(len(my_dict))
