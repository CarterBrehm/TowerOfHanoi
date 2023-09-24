# CSCI 2030 Final Project - Tower of Hanoi
This repository documents my efforts towards a final project in Dr. Ricks' Data Structures course (CSCI 3320).

### What?
Tower of Hanoi is a mathematical game involving three Poles and a number of Discs with various radii. These discs can be added and removed from the top of each pole, stacking on top of another disc _only if the disc beneath it is smaller_. The game begins with all of the discs stacked on top of each other in order on the first Pole, and the game is completed when all of these discs have been moved to the third Pole. The second Pole is required to play the game, as it functions as a spare Pole.

The [Wikipedia Page](https://en.wikipedia.org/wiki/Tower_of_Hanoi) has more information, as well as the recursive method for solving this game.

### Why?
I chose this game for no other reason than my own curiosity. I used to work as a "Code Sensei" at a hybrid daycare/coding bootcamp. The technologies used were mostly simple, with our own in-house game development suite relying mostly on Javascript, with provided libraries used to draw shapes, apply physics, and anything else the kids might need to develop their games. The games were developed as a response to challenges, a set of requirements (& sometimes starter code) that were given to the student. Most of these challenges were simple, usually focusing more on the game/physics portion than any specific game behavior.

There was one challenge, however, that did not fit this mold. One of the challenges given was to implement the Tower of Hanoi, with animations, drag & drop, and a whole host of other bells and whistles. These, of course, were no challenge to Blue Belt students who encountered it, having just finished up another project using mouse movement & animations to control and maneuver a character. However, one thing that was almost always an issue was the question of keeping track of the Discs and Poles, especially with the restrictions placed on how the Discs can be positioned.

I never got a chance to implement it (as solving the challenges for the students was usually frowned upon) but I had always wondered: what would a data structure _designed for Hanoi_ look like?

### How?
There are a couple goals that this implementation of the Tower of Hanoi hopes to fulfill:
- Rather than relying on "checking" the state of the Poles to determine if moves are valid, the data structure should inherently hold that all data saved in it is valid.
  - To put it in other words, adding a new disc to a Pole should __NEVER__ require recursively checking or looping through a Pole, and should instead make one comparison.
- The program should be able to use this data structure to recursively solve the game in the most efficient manner, no matter the size or current configuration (ie: the user can solve half, and let the computer solve the other half).