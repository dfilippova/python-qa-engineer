import json
from csv import DictReader

with open('files/users.json', 'r') as file:
    users_info = json.loads(file.read())

with open('files/books.csv', newline='') as file:
    reader = DictReader(file)

    books_info = [{
        'title': book['Title'],
        'author': book['Author'],
        'pages': book['Pages'],
        'genre': book['Genre']
    } for book in reader]

users_list = []
users_count = len(users_info)
books_count = len(books_info)

for index in range(0, users_count):
    users_list.append({
        'name': users_info[index]['name'],
        'gender': users_info[index]['gender'],
        'address': users_info[index]['address'],
        'age': users_info[index]['age'],
        'books': [books_info[i] for i in list(range(0, books_count))[index::users_count]]
    })

with open('result2.json', 'w') as file:
    s = json.dumps(users_list, indent=4)
    file.write(s)
