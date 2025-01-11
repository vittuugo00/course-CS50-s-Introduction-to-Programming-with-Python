import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    pattern_check_ip = r'^(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.' \
                       r'(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.' \
                       r'(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.' \
                       r'(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    if re.search(pattern_check_ip, ip):
        return True
    else:
        return False

if __name__ == "__main__":
    main()




# .   any character except a new line
# *   0 or more repetitions
# +   1 or more repetitions
# ?   0 or 1 repetition
# {m} m repetitions
# {m,n} m-n repetitions
