#!/usr/bin/python3
"""Makes an API request to return the todo list progress of an employee.
Takes in an argument asthe employee ID.
"""
import sys

from requests import get

endpoint = 'https://jsonplaceholder.typicode.com/todos'
response = get(endpoint)
data = response.json()
id_ = int(sys.argv[1])

# get user name
name = get('https://jsonplaceholder.typicode.com/users/{}'.format(id_))
name = name.json()['name']

# filter todos for employee id
todos = [todo for todo in data if todo['userId'] == id_]
total = len(todos)
completed = 0
titles = ''

for todo in todos:
    if todo['completed']:
        completed += 1
        titles += '\t ' + todo['title'] + '\n'

print('Employee {} is done with tasks({}/{}):'.format(name, completed, total))
print(titles, end='')
