#!/usr/bin/python3
"""0th task file"""

import requests
from sys import argv

employeeID = argv[1]
employeeData = requests.get(f'https://jsonplaceholder.typicode.com/users/{employeeID}')
employeeTODOs = requests.get(f'https://jsonplaceholder.typicode.com/users/{employeeID}/todos').json()
employeeName = employeeData.json()["name"]
completedTasks = []
countCompletedTasks = 0
totalTasks = len(employeeTODOs)
for todo in employeeTODOs:
    if todo["completed"] == True:
        countCompletedTasks += 1
        completedTasks.append(todo["title"])
print("Employee {} is done with tasks({}/{}):".format(employeeName, countCompletedTasks, totalTasks))
for task in completedTasks:
    print("\t{}".format(task))

