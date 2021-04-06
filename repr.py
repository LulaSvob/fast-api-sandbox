class Person:
    name = 'Adam'

    def __repr__(self):
        return repr('Hello ' + self.name)


test = 1

print(repr(Person()))
print(repr(test))
