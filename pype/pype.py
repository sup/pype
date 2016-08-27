class Infix:
    """
    Generic class that lets us define various fake infix operators
    """
    def __init__(self, function):
        self.function = function
    def __ror__(self, other):
        return Infix(lambda x, self=self, other=other: self.function(other, x))
    def __or__(self, other):
        return self.function(other)

# Generic Pipe Infix Operator
p=Infix(lambda x,f: f(x))
pipe=Infix(lambda x,f: f(x))
