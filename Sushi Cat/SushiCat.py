#Import the turtle module to utilize turtle graphics which will compose the game.
import turtle
#Import math specifically for use of the sqrt() function, used in calculations to determine distance between Turtle objects in the game.
import math

#Registering Shapes/Outside Graphics that will be used as skins for the Turtle Objects
#Graphic for Player object(s)
turtle.register_shape("images/CatHero.gif")
#Graphic for Treasure (the sushi) object(s)
turtle.register_shape("images/crab_meat.gif")
#Graphic for the wooden wall object(s)
turtle.register_shape("images/WoodWall1.gif")
#Graphic for the forest background of the Screen object(s)
turtle.register_shape("images/Background.gif")
#Graphic for the lamp/torches on the map
turtle.register_shape("images/Lamp.gif")
#Graphic for the Tree/Bushes on the map
turtle.register_shape("images/Tree.gif")

#Instantiate a Screen object, which is a subclass/child of TurtleScreen
window = turtle.Screen()
#Set the background color of the Screen, takes color string arguments and other colorvalues (i.e. RGB per Turtle documentation)
window.bgcolor("black")
#Set the background image of the Screen
window.bgpic("images/Background.gif")
#Set the title of the Screen
window.title("Sushi Cat")
#Specify the dimensions of the Screen, in this case, 700px x 700px
window.setup(700, 700)

#Create a List object in which each element is a singular list of strings. Said list of strings represents a single map in the game. If more than one map is created in the future, they can be added in subsequent indices.
levels = []

#Create List object that will contain a string representation of the map in a 25 x 25 element multidimensional array, corresponding to 25 x 25 pixels.
level_1 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XL           LXXL   T  LX",
"X  *   P *    XX        X",
"X  XXXXXXXX   XX*     * X",
"X  XXT        XXXXX   XXX",
"X  XXXXXXXXXXXXXXXX   XXX",
"X                     XXX",
"X  XXXX XXXX  XXXXXXXXXXX",
"X  XXXX XXXX  XXL  T  LXX",
"X      T   *  XX       XX",
"X  XXXX XXXX  XXXXX  XXXX",
"X  XXXX XXXX  XXXXX  XXXX",
"X                   *   X",
"X   XXX*XXX   XXX*XXX   X",
"X   XX***XX   XXX*XXX   X",
"X * XX***XX   XXX*XXX   X",
"X   XXX*XXX   XXX*XXX   X",
"X                       X",
"XL            *        LX",
"XXXXX*XXXXXX  XXXXXXXXXXX",
"XL     XXXXX  X       *XX",
"X T X         XT       XX",
"X   X         XXXXXL  LXX",
"XL     XXXXX           XX",
"XXXXXXXXXXXXXXXXXXXXXXXXX"]

#Add the string representation of the map above to the array named "levels" which was initialized earlier to be empty. "levels" helps to organize the maps sequentially, since each index of "levels" contains a single map.
levels.append(level_1)

#This list will be populated by Treasure objects
treasures = []

#This list will be populated by the coordinates of every "wall" aka index in the multidimensional array representation of the map wherein movement is not allow to by the Player.
walls = []

#This list will be populated by the coordinates of every tree in the multidimensional array representation of the map wherein movement is not allow to by the Player.
trees = []

#This list will be populated by the coordinates of every lamp in the multidimensional array representation of the map wherein movement is not allow to by the Player.
lamps = []

#Pen class is a Turtle class, instantiate Pen Class and initialize members shape, color, speed, and penup, which toggles tracing on and off. Pen is used to draw/designate the walls in the map.
class Pen(turtle.Turtle):
	def __init__(self):
		turtle.Turtle.__init__(self)
		#Let the speed of the Pen object drawing the walls be 0, which is the fastest speed available to a Turtle object.
		self.speed(0)
		#Disable tracing of the Pen by calling the penup method, this allows the program to populate the walls/terrain of the game without tracing lines appearing that "walk along" each iteration of the Pen across the playable area of the Screen  
		self.penup()

#The Player class contains all methods and members involved with the Turtle Object which the User controls, its movement in the x and y axis are updated and obtained from here, in addition to attributes such as the image/skin of the User's character
#as well as items/statistics that are relevant to the game, i.e. how many Treasure/Sushi items have been collected thus far.
class Player(turtle.Turtle):
	def __init__(self):
		turtle.Turtle.__init__(self)
		self.shape("images/CatHero.gif")
		self.penup()
		self.speed(0)
		self.sushi = 0

	#The following "go" methods extract the player's current coordinates in the graph represented by a multidimensional array. If a player uses the movement keys, WASD, the respective "go" methods are triggered i.e. go up if W is pressed.
	#The location that the player wishes to relocate to is then calculated and checked against valid coordinates on the map where the player is allowed to move. If the movement leads to a valid space, movement occurs, if it would lead to 
	#Terrain designated as a wall or impassable, the movement is not executed. The go methods act in conjunction with the is_collision method to determine this information. Each square on the grid is 24 pixels in both width and length.
	def go_up(self):
		move_to_x = player.xcor()
		move_to_y = player.ycor() + 24
		
		if (move_to_x, move_to_y) not in walls:
			self.goto(move_to_x, move_to_y)

	def go_down(self):
		move_to_x = player.xcor()
		move_to_y = player.ycor() - 24
		
		if (move_to_x, move_to_y) not in walls:
			self.goto(self.xcor(), self.ycor() - 24)

	def go_left(self):
		move_to_x = player.xcor() - 24
		move_to_y = player.ycor()
		
		if (move_to_x, move_to_y) not in walls:
			self.goto(self.xcor() - 24, self.ycor())

	def go_right(self):
		move_to_x = player.xcor() + 24
		move_to_y = player.ycor()

		if (move_to_x, move_to_y) not in walls:	
			self.goto(self.xcor() + 24, self.ycor())

	def is_collision(self, other):
		a = self.xcor()-other.xcor()
		b = self.ycor()-other.ycor()
		distance = math.sqrt((a**2) + (b**2))

		if distance < 5:
			return True
		else:
			return False

#The Treasure class is a Subclass of the Turtle class. It acts as a placeholder object for an item that can be collected. Each Treasure contains a member/attribute "sushi" with a value of 1. Whenevr the player moves over this object,
#The player class increases its own member/attribute named "sushi" by 1, and also causes the destroy method to be triggered by the Treasure object, which removes the object from the playable map.
class Treasure(turtle.Turtle):
	def __init__(self, x, y,):
		turtle.Turtle.__init__(self)
		self.shape("images/crab_meat.gif")
		self.penup()
		self.speed(0)
		self.sushi = 1
		self.goto(x, y)

	def destroy(self):
		self.goto(2000, 2000)
		self.hideturtle()

#Create function that initializes the maze on to the screen/window object. This function examines every index in the multidimensional array representation of the map. If the index contains a string designating that particular index as a "Wall" ("X") or impassable terrain,
# That index will be added to the list of "walls" and also have the graphic/skin/texture of a wall associated with it. Likewise if the index contains a string designating that particular index as containing the "P" or Player instace object that represents
#the user in the map, the Player object will be placed at that location at the beginning of the game. If the index contains "T" this represents the location where a Treasure object will be placed and subsequently associated with the list of Treasures.
def setup_maze(level):
	for y in range(0, len(level)):
		for x in range(0, len(level[y])):

			character = level[y][x]

			screen_x = -288 + (x * 24)
			screen_y = 288 - (y * 24)

			if character == "X":
				pen.goto(screen_x, screen_y)
				pen.shape("images/WoodWall1.gif")
				pen.stamp()
				walls.append((screen_x, screen_y))

			if character == "L":
				pen.goto(screen_x, screen_y)
				pen.shape("images/Lamp.gif")
				pen.stamp()
				lamps.append((screen_x, screen_y))

			if character == "*":
				pen.goto(screen_x, screen_y)
				pen.shape("images/Tree.gif")
				pen.stamp()
				trees.append((screen_x, screen_y))

			if character == "P":
				player.goto(screen_x, screen_y)

			if character == "T":
				treasures.append(Treasure(screen_x, screen_y))


#Instantiate a new Pen object and Player object to both draw the map and place the Player object after the map has been drawn
pen = Pen()
player = Player()

#Set up the map currently in the first index of the list of levels
setup_maze(levels[0])

#Player movement
turtle.listen()
turtle.onkey(player.go_left, "Left")
turtle.onkey(player.go_right, "Right")
turtle.onkey(player.go_up, "Up")
turtle.onkey(player.go_down, "Down")

#Disable screen notifications
window.tracer(0)

#Game Execution
while True:

	for treasure in treasures:
		#If the Player collides with treasure, increment the treasure/sushi attribute/member of the Player object and destroy the treasure while removing it from the playable area of the map.
		if player.is_collision(treasure):
			player.sushi+= treasure.sushi
			print("Player Sushi: {}".format(player.sushi))
			treasure.destroy()
			treasures.remove(treasure)

	#Update the visible objects on the map as the Player does or does not collide with various objects.
	window.update()


