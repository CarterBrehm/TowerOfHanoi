from Disc import Disc
from Pole import Pole
from PoleOrchestrator import PoleOrchestrator

def testPole(pole, height, top, base, list):
    assert pole.height() == height, "Pole height " + str(pole.height()) + " ≠ " + str(height)

    if top is None:
        assert pole.top is None, "Top should be none, instead " + str(pole.top.radius)
    else:
        assert pole.top.radius == top.radius, "Pole top " + str(pole.top.radius) + " ≠ " + str(top.radius)

    if base is None:
        assert pole.base is None, "Base should be none, instead " + str(pole.base.radius)
    else:
        assert pole.base.radius == base.radius, "Pole base " + str(pole.base.radius) + " ≠ " + str(base.radius)

    assert pole.asList() == list, "Pole list " + str(pole.asList()) + " ≠ " + str(list)

def testDisc(disc, radius):
    assert disc.radius == radius

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

# introducing the mighty POLE ORCHESTRATOR
# we'll instantiate one with 3 poles and 10 discs
game = PoleOrchestrator(3, 10)
# this pole orchestrator will control 3 poles, and put 10 discs on the first one
assert len(game.poles) == 3
testPole(game.poles[0], 10, Disc(1), Disc(10), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
testPole(game.poles[1], 0, None, None, [])
testPole(game.poles[2], 0, None, None, [])

# let's play the game for a bit

game.moveDisc(0, 1)
game.moveDisc(0, 2)
game.moveDisc(1, 2)
game.moveDisc(0, 1)
game.moveDisc(2, 0)
game.moveDisc(2, 1)
game.moveDisc(0, 1)
game.moveDisc(0, 2)

# now check that we've done everything correctly

testPole(game.poles[0], 6, Disc(5), Disc(10), [5, 6, 7, 8, 9, 10])
testPole(game.poles[1], 3, Disc(1), Disc(3), [1, 2, 3])
testPole(game.poles[2], 1, Disc(4), Disc(4), [4])