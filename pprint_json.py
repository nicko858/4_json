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


if __name__ == '__main__':
    data = load_data(sys.argv[1])
    pretty_print_json(data)
    pass
