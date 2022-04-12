#!/usr/bin/python3
"""Makes an API request to return the todo list progress of an employee.
Takes in an argument asthe employee ID.
"""
import json
from requests import get

if __name__ == '__main__':
    # get all todos
    todos = get('https://jsonplaceholder.typicode.com/todos')
    todos = todos.json()

    # get all users
    users = get('https://jsonplaceholder.typicode.com/users')
    users = users.json()

    # user id and username mapping
    user_names = {
            user.get('id'): user.get('username') for user in users
            }
    tmp_dict = {
            user_id:
            [
                todo for todo in todos
                if todo.get('userId') == user_id
                ] for user_id in user_names.keys()
            }
    items = tmp_dict.items()
    # reorganize the dictionary
    dict_ = {}
    for id_, tmp_list in items:
        new_list = []
        for todo in tmp_list:
            new_todo = {
                    'username': user_names[id_],
                    'task': todo.get('title'),
                    'completed': todo.get('completed')
                    }
            new_list.append(new_todo)
        dict_.update({id_: new_list})

    with open('todo_all_employees.json', mode='w', encoding='utf-8') as f:
        json.dump(dict_, f)
