class Disc:
    def __init__(self, value):
        self.radius = value
        self.under = None

    def putOnTopOf(self, topOfExistingStack):
        self.under = topOfExistingStack
        return self

    def height(self):
        if self.under is not None:
            return 1 + self.under.height()
        else:
            return 1

    def asList(self):
        if self.under is None:
            return [self.radius]
        else:
            return [self.radius] + self.under.asList()

    def graphicalRepresentation(self, baseRadius):
        if self.under is None:
            return '_|*-*|\n'.replace('*', '-'*self.radius).replace('_',' '*(baseRadius - self.radius))
        else:
            return '_|*-*|\n'.replace('*', '-'*self.radius).replace('_',' '*(baseRadius - self.radius)) + self.under.graphicalRepresentation(baseRadius)