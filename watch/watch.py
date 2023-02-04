import re
import sys


def main():
    site = input("HTML: ")
    print(parse(site))


def parse(site):
    youtube = re.search(r"^\<.+src=(\".+\/\/(.+\.)?youtube\..+\").+\>$", site)
    if youtube:
        webs = re.search(r"\"(.+)\/embed(\/.+)\"", youtube[1])
        URL = "https://youtu.be" + webs[2]
        return URL
    else:
        return None


if __name__ == "__main__":
    main()