#!/usr/bin/python3
"""
extend your Python script to export data in the JSON format
"""
from json import dumps
import requests
from sys import argv

if __name__ == '__main__':
    try:
        emp_id = int(argv[1])
    except ValueError:
        exit()

    api_url = 'https://jsonplaceholder.typicode.com'
    user_uri = '{api}/users/{id}'.format(api=api_url, id=emp_id)
    todo_uri = '{user_uri}/todos'.format(user_uri=user_uri)
    filename = '{emp_id}.json'.format(emp_id=emp_id)

    u_res = requests.get(user_uri).json()
    t_res = requests.get(todo_uri).json()

    # A list of all tasks of an user
    user_tasks = list()

    for elem in t_res:
        data = {
            'task': elem.get('title'),
            'completed': elem.get('completed'),
            'username': u_res.get('username')
        }
        user_tasks.append(data)

    with open(filename, 'w', encoding='utf-8') as jsonfile:
        jsonfile.write(dumps({emp_id: user_tasks}))
