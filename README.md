# Prettify JSON

The code reads a file with arbitrary data in JSON format and displays its contents in the console in an easy-to-read form: adds line breaks, left padding and spaces.


# Quickstart

The program is represented by the module ```pprint_json.py```.
Module ```pprint_json.py``` contains the following functions:

- ```load_data()``` - accepts the input to a file with arbitrary data in json format and reads the file content
- ```pretty_print_json()``` - accepts the file content  from the previous function and makes it easy-to-read using ```json.dumps()```- function 

Here is example of source-code and how to use this functions:

```python
import json
import sys


def load_data(filepath):
    f = open(filepath, 'r')
    return f.read()
    pass


def pretty_print_json(data):
    parsed = json.loads(data)
    print(json.dumps(parsed, indent=4, ensure_ascii=False, sort_keys=True))
    pass

    data = load_data(sys.argv[1])
    pretty_print_json(data)
```

How in works:
- The program reads  the first command-line argument(path to json-file)
- loads it using  ```json.loads()``` -function
- With ```json.dumps()``` -function, parse content and print in easy-to-read form

Option ```ensure_ascii=False``` needs, to correct output cyrrilic symbols.

Example of script launch on Linux, Python 3.5:

```bash

$ python pprint_json.py <path to file>

```
in the console  output you will see something  like this:
```bash
[
    {
        "Cells": {
            "Address": "улица Академика Павлова, дом 10",
            "AdmArea": "Западный административный округ",
            "ClarificationOfWorkingHours": null,
            "District": "район Кунцево",
            "IsNetObject": "да",
            "Name": "Ароматный Мир",
            "OperatingCompany": "Ароматный Мир",
            "PublicPhone": [
                {
                    "PublicPhone": "(495) 777-51-95"
                }
            ],
            "TypeService": "реализация продовольственных товаров",
            "WorkingHours": [
                {
                    "DayOfWeek": "понедельник",
                    "Hours": "09:30-22:30"
                },
                {
                    "DayOfWeek": "вторник",
                    "Hours": "09:30-22:30"
                }

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
