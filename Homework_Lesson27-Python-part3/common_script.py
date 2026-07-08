import os

def multiply_numbers(a, b):
    return(a*b)
print(multiply_numbers(8, 13))

with open('test.txt', 'r', encoding='utf-8') as f:
    print(f.read())

files = os.listdir('./mydir')
for files in files:
    print(files)

from jinja2 import Template
with open('template.html') as file:
    template = Template(file.read())
output = template.render(title='Список пользователей и их email', users=[
    {"name": "Tomas", "email": "tomas@yandex.ru"},
    {"name": "Kat", "email": "kat@yandex.ru"},
    {"name": "William", "email": "william@yandex.ru"},
    {"name": "Anastasia", "email": "anastasia@yandex.ru"}
    ])
print(output)
