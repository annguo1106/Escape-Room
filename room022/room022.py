import arcade
from constants import SCREEN_WIDTH, SCREEN_HEIGHT 
from mainTheme import MainTheme
from doorLeft import DoorLeft
from doorRight import DoorRight
from back import Back
from front import Front


class Game(arcade.Window):
	def __init__(self):
		super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "ROOM 022")
		current_view = MainTheme()
		self.show_view(current_view)
  
	def setup(self):
		pass

	def on_mouse_press(self, x, y, button, modifiers):
		# do control
		# left and right control position done
		CONTROL_COR = [[140, 10], [940, 10], [540, 605], [540, 10]]
		next = "-1"
		print("check -> room022-on_mouse_press", "x", x, "y", y)
		for i in range(4):
			if(self.current_view.direction[i] != "None" and
      			x >= CONTROL_COR[i][0] and x <= CONTROL_COR[i][0] + 40 and
         		y >= CONTROL_COR[i][1] and y <= CONTROL_COR[i][1] + 40):
				next = self.current_view.direction[i]
				break

		if next != "-1":
			next_view = None
			if next == "MainTheme":
				next_view = MainTheme()
			elif next == "DoorLeft":
				next_view = DoorLeft()
			elif next == "DoorRight":
				next_view = DoorRight()
			elif next == "Back":
				next_view = Back()
			elif next == "Front":
				next_view = Front()
    
			self.show_view(next_view)


if __name__ == "__main__":
	window = Game()
	arcade.run()
