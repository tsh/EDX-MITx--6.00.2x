from ps2 import RectangularRoom

room = RectangularRoom(4,6)
print len(room.room)
print len(room.room[0])
print "clean tiles ",room.getNumCleanedTiles()
room.isTileCleaned(4,6)

