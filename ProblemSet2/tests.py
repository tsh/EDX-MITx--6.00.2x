from ps2 import RectangularRoom, Position

room = RectangularRoom(4,5)
print "len: ",len(room.room)
room.cleanTileAtPosition(Position(1,2))
print "cleanTiles: ", room.getNumCleanedTiles()
print "randomPos: ", room.getRandomPosition()