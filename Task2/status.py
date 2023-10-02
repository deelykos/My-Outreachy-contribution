#!/usr/bin/python3
# A python code that gets urls from a csv file and print their status code

import csv
import requests

def get_status_code(url):
    # The function to get the urls and print status code

    try:
        response = requests.get(url)
        status_code = response.status_code
        print("({}) {}".format(status_code, url))
    except Exception as err:
        print("(Error: {}) {}".format(err, url))

    # Reading csv file
with open("Intern.csv", "r") as f:
    read_csv = csv.reader(f)
    next(read_csv)

    # looping over the urls
    for row in read_csv:
        if len(row) > 0:
            url = row[0]
            get_status_code(url)
