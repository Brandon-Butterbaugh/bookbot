import sys
from stats import stats

def main():
    if(len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    stats(sys.argv[1])

main()