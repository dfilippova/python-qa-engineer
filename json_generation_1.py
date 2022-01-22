import json
from csv import DictReader

with open('files/users.json', 'r') as file:
    users_info = json.loads(file.read())

users_list = []

for user in users_info:
    users_list.append({
        'name': user['name'],
        'gender': user['gender'],
        'address': user['address'],
        'age': user['age'],
        'books': []
    })

with open('files/books.csv', newline='') as file:
    books_info = DictReader(file)

    user_number = 0
    users_count = len(users_info)

    for book in books_info:
        if user_number >= users_count:
            user_number = 0

        users_list[user_number]['books'].append({
            'title': book['Title'],
            'author': book['Author'],
            'pages': book['Pages'],
            'genre': book['Genre']
        })

        user_number += 1

with open('result1.json', 'w') as file:
    result = json.dumps(users_list, indent=4)
    file.write(result)
