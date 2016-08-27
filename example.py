from pype.pype import p
# from pype import pipe as p

def hello_world_example():
    def echo(x):
        print x
    # Simple pipe application
    'This is a simple pipe to echo.' |p| echo

def multiple_pipe_example():
    # Create a curried mapper function
    create_mapper = lambda (fn): lambda (lst): map(fn, lst)
    mult = lambda n: n * 2
    # Application of multiple pipes
    print [n for n in range(0,100)] |p| (mult |p| create_mapper) |p| sum

if __name__ == '__main__':
    hello_world_example()
    multiple_pipe_example()
