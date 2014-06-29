import json
import sys
if __name__ == '__main__':
    dict=json.loads(open(sys.argv[2],'r').read())
    print(sys.argv[1].format(**dict))
