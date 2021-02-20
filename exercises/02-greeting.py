import sys

def hello(name):
    # TODO: Implement this correctly according to the exercise
    print(name)

if __name__ == '__main__':
    name = sys.argv[1] if len(sys.argv) > 1 else 'there'
    hello(name)
