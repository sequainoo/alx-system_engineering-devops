#!/usr/bin/python3
"""Extends on prevoius task api reqest and export to csv
"""
import csv
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
        # create a csv dictionationary writer
        fieldnames = ['USER_ID', 'USERNAME',
                      'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        writer = csv.DictWriter(f, fieldnames=fieldnames,
                                quoting=csv.QUOTE_ALL)
        for todo in todos:
            dict_ = {'USER_ID': id_, 'USERNAME': name,
                     'TASK_COMPLETED_STATUS': todo.get('completed'),
                     'TASK_TITLE': todo.get('title')}
            writer.writerow(dict_)

            if todo.get('completed'):
                done += 1
                titles += '\t ' + todo.get('title') + '\n'
