from checks import Checks


class Input(Checks):
    def __init__(self, loc):
        self.loc = loc
        super(Input, self).__init__(self.loc)


search = Input('input#searh')

print(search.check_text())