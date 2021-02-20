import sys

def hello(name):
    if name == "there":
        print("Hello yourself!")
    else:
        reversed_name = ''.join(reversed(name))
        print("Hello " + reversed_name + "!")


if __name__ == '__main__':
    name = sys.argv[1] if len(sys.argv) > 1 else 'there'
    hello(name)