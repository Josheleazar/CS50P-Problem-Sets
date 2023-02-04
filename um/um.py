import re
import sys

def main():
    s = input("Text: ")
    print(count(s))

def count(s):
    word = re.findall(r"\bum\b", s, re.IGNORECASE)
    cnt = len(word)
    return cnt

if __name__ == "__main__":
    main()