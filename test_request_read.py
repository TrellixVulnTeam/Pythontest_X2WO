import sys

with open('filter_request.txt', 'r', encoding='utf-8' ) as f:
    for i in f:
        if sys.argv[1] in i:
            print(i)