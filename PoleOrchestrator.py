import os

from Disc import Disc
from Pole import Pole


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


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

    def moveDisc(self, src, dest):
        if self.pole(dest).top is None or self.pole(src).top.radius < self.pole(dest).top.radius:
            return self.pole(dest).addDisc(self.pole(src).removeDisc())
        else:
            return False

    def prompt(self):
        print("choose an operation:")
        print("m: move a disc from one pole to another")
        print("s: solve the game according to the recursive algorithm")
        choice = ""
        while choice not in ["m", "s"]:
            choice = input("(m, s) > ")
        if choice == "m":
            self.moveDisc(int(input("src pole: ")), int(input("dest pole: ")))
        elif choice == "s":
            self.solve()

    def makeLegalMove(self, pole1, pole2):
        if self.pole(pole1).height() > 0 and self.pole(pole2).height() > 0:
            if self.pole(pole2).top is None or self.pole(pole1).top.radius < self.pole(pole2).top.radius:
                if self.moveDisc(pole1, pole2):
                    print("Moved disc of size " + str(self.pole(pole2).top.radius) + " from pole " + str(
                        pole1) + " -> " + str(pole2))
            else:
                if self.moveDisc(pole2, pole1):
                    print("Moved disc of size " + str(self.pole(pole1).top.radius) + " from pole " + str(
                        pole2) + " -> " + str(pole1))
        elif self.pole(pole1).height() > 0 or self.pole(pole2).height() > 0:
            if self.pole(pole1).height() == 0 and self.pole(pole2).height() != 0:
                if self.moveDisc(pole2, pole1):
                    print("Moved disc of size " + str(self.pole(pole1).top.radius) + " from pole " + str(
                        pole2) + " -> " + str(pole1))
            else:
                if self.moveDisc(pole1, pole2):
                    print("Moved disc of size " + str(self.pole(pole2).top.radius) + " from pole " + str(
                        pole1) + " -> " + str(pole2))

    def printPoles(self):
        for i in range(0, 3):
            print("Pole " + str(i))
            print(self.pole(i).graphicalRepresentation(
                max((self.pole(0).base or Disc(1)).radius, (self.pole(1).base or Disc(1)).radius,
                    (self.pole(2).base or Disc(1)).radius)))

    def solve(self):
        totalDiscs = self.pole(0).height() + self.pole(1).height() + self.pole(2).height()
        even = totalDiscs % 2 == 0
        while self.pole(2).height() != totalDiscs:
            if self.solveBreak() is False:
                clear()
                self.makeLegalMove(0, 1 if even else 2)
                self.printPoles()
            else:
                break
            if self.solveBreak() is False:
                clear()
                self.makeLegalMove(0, 2 if even else 1)
                self.printPoles()
            else:
                break
            if self.solveBreak() is False:
                clear()
                self.makeLegalMove(1, 2)
                self.printPoles()
            else:
                break
        if self.pole(2).height() != totalDiscs:
            print("Solving complete!")
            self.printPoles()

    @staticmethod
    def solveBreak():
        interrupt = input("Enter to continue. Enter any character to stop solving and return manual control: ")
        if interrupt is None or interrupt == "":
            return False
        else:
            return True

    def run(self):
        while True:
            clear()
            self.printPoles()
            self.prompt()
