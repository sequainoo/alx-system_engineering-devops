#!/usr/bin/python3
"""Extends on prevoius task api reqest and export to csv
"""
from requests import get
import sys

if __name__ == '__main__':
    endpoint = 'https://jsonplaceholder.typicode.com/todos'
    response = get(endpoint)
    data = response.json()
    id_ = int(sys.argv[1])

    # get user name
    name = get('https://jsonplaceholder.typicode.com/users/{}'.format(id_))
    name = name.json().get('name')

    # filter todos for employee id
    todos = [todo for todo in data if todo.get('userId') == id_]
    total = len(todos)
    done = 0
    titles = ''
    file_name = '{}.csv'.format(id_)

    with open(file_name, 'w', encoding='utf-8') as f:
        for todo in todos:
            status = todo.get('completed')
            title = todo.get('title')
            line = '"{}","{}","{}","{}"\n'.format(id_, name, status, title)
            f.write(line)

            if todo.get('completed'):
                done += 1
                titles += '\t ' + todo.get('title') + '\n'

    #print('Employee {} is done with tasks({}/{}):'.format(name, done, total))
    #print(titles, end='')
