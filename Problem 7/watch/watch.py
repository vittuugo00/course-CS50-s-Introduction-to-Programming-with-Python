import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    try:
        src = re.search(r'^.+src="https?://(?:www\.)?youtube.com/embed/([^"]+)".+$', s)
        url = src.groups()
        return f"https://youtu.be/{url[0]}"
    except:
        return None

if __name__ == "__main__":
    main()
