from Disc import Disc
from Pole import Pole

def testPole(pole, height, top, base, list):
    assert pole.height() == height, "Pole height " + str(pole.height()) + " ≠ " + str(height)
    assert pole.top == top, "Pole top " + str(pole.top.radius) + " ≠ " + str(top.radius)
    assert pole.base == base, "Pole base " + str(pole.base.radius) + " ≠ " + str(base.radius)
    assert pole.asList() == list, "Pole list " + str(pole.asList()) + " ≠ " + str(list)

def testDisc(disc, radius):
    assert disc.radius == radius
    assert disc.graphicalRepresentation(0) == '|*-*|\n'.replace('*', '-'*radius)

# Instantiating a pole
pole = Pole()
assert isinstance(pole, Pole) is True

# Pole has no elements right now
testPole(pole, 0, None, None, [])

# Make some new discs
disc1 = Disc(1)
testDisc(disc1, 1)
disc5 = Disc(5)
testDisc(disc5, 5)
disc9 = Disc(9)
testDisc(disc9, 9)

# Stacking them legitimately should work
assert pole.addDisc(disc9) is True
testPole(pole, 1, disc9, disc9, [disc9.radius])
assert pole.addDisc(disc5) is True
testPole(pole, 2, disc5, disc9, [disc5.radius, disc9.radius])
assert pole.addDisc(disc1) is True
testPole(pole, 3, disc1, disc9, [disc1.radius, disc5.radius, disc9.radius])

# We can pluck them individually off the stack
assert pole.removeDisc() == disc1
testPole(pole, 2, disc5, disc9, [disc5.radius, disc9.radius])

# We can even pluck them right onto another pole
pole2 = Pole()
pole2.addDisc(pole.removeDisc())
# Our old pole doesn't have that anymore
testPole(pole, 1, disc9, disc9, [disc9.radius])
# Our new pole has only that
testPole(pole2, 1, disc5, disc5, [disc5.radius])

# Adding a larger disc on top of a smaller one doesn't work though
disc11 = Disc(11)
assert pole2.addDisc(disc11) is False
testPole(pole2, 1, disc5, disc5, [disc5.radius])

# But, we can temporarily move the smaller disc out of the way to put the larger disc on
pole.addDisc(pole2.removeDisc())
assert pole2.addDisc(disc11) is True
assert pole2.addDisc(pole.removeDisc()) is True

# At the end of these tests, we should have these two poles
testPole(pole, 1, disc9, disc9, [disc9.radius])
testPole(pole2, 2, disc5, disc11, [disc5.radius, disc11.radius])



