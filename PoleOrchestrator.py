from Disc import Disc
from Pole import Pole
class PoleOrchestrator:
    def __init__(self, poles, discs):
        self.poles = []
        for i in range(0, poles):
            self.poles.append(Pole())
        for i in range(discs, 0, -1):
            self.poles[0].addDisc(Disc(i))

    def pole(self, index):
        if len(self.poles) < index:
            return None
        else:
            return self.poles[index]

