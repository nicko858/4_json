import json
import sys


def load_data(filepath):
    with open(filepath, 'r') as source_file:
        return source_file.read()


def pretty_print_json(source_data):
    try:
        parsed_data = json.loads(source_data)
        result_data = json.dumps(parsed_data, indent=4, ensure_ascii=False, sort_keys=True)
        return result_data
    except:
        return None


if __name__ == '__main__':
    usage = "python pprint_json.py <path to file>"
    if len(sys.argv) != 2:
        print("Incorrect line argument!""\n" "Using: {}".format(usage))
        exit(1)
    json_content = load_data(sys.argv[1])
    try:
        content_to_print = pretty_print_json(json_content)
        if content_to_print:
            print(content_to_print)
        else:
            raise ValueError
    except ValueError:
        print("Decoding JSON has failed!")
        print('The source-file is not a valid JSON! Check the file content!')
