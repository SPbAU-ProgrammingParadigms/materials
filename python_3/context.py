#!/usr/bin/python3

class Closing:
    def __init__(self, resource):
        self.resource = resource

    def __enter__(self):
        return self.resource

    def __exit__(self, exc_type, exc_value, traceback):
        self.resource.close()

def main():
    class Closeable:
        def open(self):
            print('open')

        def close(self):
            print('close')

    def open():
        c = Closeable()
        c.open()
        return c

    with Closing(open()) as x:
        print('hello')
        pass

    try:
        with Closing(open()) as x:
            raise Exception()
    except Exception:
        pass

if __name__ == '__main__':
    main()
