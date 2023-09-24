from Disc import Disc
from Pole import Pole

pole = Pole()
pole.addDisc(Disc(7))
pole.addDisc(Disc(4))
pole.addDisc(Disc(3))
pole.addDisc(Disc(2))
pole.addDisc(Disc(1))
print(pole.graphicalRepresentation())