class Pole:

    def __init__(self):
        self.top = None
        self.base = None

    def addDisc(self, disc):
        if self.top is not None:
            if self.top.radius > disc.radius:
                self.top = disc.putOnTopOf(self.top)
            else:
                return False
        else:
            self.top = disc
            self.base = disc

    def removeDisc(self):
        if self.top is not None:
            removedDisc = self.top
            self.top = self.top.under
            return removedDisc
        else:
            return None

    def height(self):
        return self.top.height() if self.top is not None else 0

    def asList(self):
        return self.top.asList() if self.top is not None else []

    def graphicalRepresentation(self):
        return self.top.graphicalRepresentation(self.base.radius) if self.top is not None else ""


