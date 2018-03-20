import json
import sys


def load_data(filepath):
    with open(filepath, "r") as source_file:
        return source_file.read()


def get_pretty_json(source_data):
        parsed_data = json.loads(source_data)
        result_data = json.dumps(parsed_data, indent=4, ensure_ascii=False, sort_keys=True)
        return result_data


if __name__ == "__main__":
    usage = "python pprint_json.py <path to file>"
    if len(sys.argv) != 2:
        exit("Incorrect line argument!""\n" "Using: {}".format(usage))
    else:
        json_content = load_data(sys.argv[1])
        try:
            content_to_print = get_pretty_json(json_content)
            print(content_to_print)
        except ValueError:
            print("Decoding JSON has failed!")
            print("The source-file is not a valid JSON or empty! Check the file content!")
