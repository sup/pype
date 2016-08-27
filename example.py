from pype.pype import p
# from pype import pipe as p

def hello_world_example():
    def echo(x):
        print x

    'This is a simple pipe to echo.' |p| echo

def multiple_pipe_example():
    # Curry a mapper function
    def create_mapper(fn):
        return lambda lst: map(fn, lst)
    mult = lambda n: n * 2
    print [n for n in range(0,100)] |p| (mult |p| create_mapper) |p| sum

if __name__ == '__main__':
    hello_world_example()
    multiple_pipe_example()
