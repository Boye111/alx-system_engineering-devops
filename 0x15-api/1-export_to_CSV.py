#!/usr/bin/python3
"""
extend your Python script to export data in the CSV format
"""
import csv
import requests
from sys import argv

if __name__ == '__main__':
    try:
        emp_id = int(argv[1])
    except ValueError:
        exit()

    # Main formatted names to API uris and filenames
    api_url = 'https://jsonplaceholder.typicode.com'
    user_uri = '{api}/users/{id}'.format(api=api_url, id=emp_id)
    todo_uri = '{user_uri}/todos'.format(user_uri=user_uri)
    filename = '{emp_id}.csv'.format(emp_id=emp_id)

    res = requests.get(user_uri).json()
    username = res.get('username')
    res = requests.get(todo_uri).json()

    # Create the new file for the user to save the information
    with open(filename, 'w', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)

        for elem in res:
            status = elem.get('completed')
            title = elem.get('title')
            writer.writerow([emp_id, username, status, title])
