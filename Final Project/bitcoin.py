import json
import requests
import sys
import re  

def main():
    if check_command_line():
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        print(json.dumps(response.json(), indent=2))

def is_decimal_number(input_string):
    pattern = re.compile(r'^[-+]?[0-9]*\.?[0-9]+$')
    return bool(pattern.match(input_string))

def check_command_line():
    if len(sys.argv) != 2:
        sys.exit("Command-line argument is not a number")
    elif is_decimal_number(sys.argv[1]):
        return True
    else:
        sys.exit("Command-line argument is not a number")
main()
