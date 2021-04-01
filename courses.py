class Courses:

    def __init__(self, name, code):
        self.name = name
        self.code = code

    @property
    def naco(self):
        full = '{}({})'.format(self.name, self.code)
        return full
