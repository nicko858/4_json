import json
import sys


def load_data(filepath):
    source_file = open(filepath, 'r')
    return source_file.read()
    pass


def pretty_print_json(source_data):
    parsed = json.loads(source_data)
    print(json.dumps(parsed, indent=4, ensure_ascii=False, sort_keys=True))
    pass


if __name__ == '__main__':
    json_file = load_data(sys.argv[1])
    pretty_print_json(json_file)
    pass
