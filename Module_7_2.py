import io
from pprint import pprint

def custom_write(file_name, strings):
    file_name = 'test.txt'
    strings_positions = {}
    with open(file_name, 'w', encoding='utf-8') as file:
        for line_number, string in enumerate(strings, start=1):
            start_byte = file.tell()
            file.write(string + '\n')
            strings_positions[(line_number, start_byte)] = string
    return strings_positions
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for i in result.items():
  print(i)