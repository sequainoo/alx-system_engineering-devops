#!/usr/bin/python3
"""Makes an API request to return the todo list progress of an employee.
Takes in an argument asthe employee ID.
"""
import json
from requests import get
import sys

if __name__ == '__main__':
    endpoint = 'https://jsonplaceholder.typicode.com/todos'
    response = get(endpoint)
    data = response.json()
    id_ = int(sys.argv[1])

    # get user name
    name = get('https://jsonplaceholder.typicode.com/users/{}'.format(id_))
    name = name.json().get('username')

    # filter todos for employee id
    todos = [todo for todo in data if todo.get('userId') == id_]
    dict_ = {}
    list_ = []
    for todo in todos:
        d_ = {'task': todo.get('title'),
              'completed': todo.get('completed'),
              'username': name}
        list_.append(d_)
    dict_.update({'{}'.format(id_): list_})

    # json
    filename = '{}.json'.format(id_)
    with open(filename, mode='w', encoding='utf-8') as f:
        json.dump(dict_, f)
