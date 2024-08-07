import arcade
from sceneUtil import Scene
from itemList import item_list, backpack_list
from dialogueUtil import DialogueBox
from constants import SCREEN_WIDTH, SCREEN_HEIGHT 
from mainTheme import MainTheme
class Game(arcade.Window):
	def __init__(self):
		super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "ROOM 022")
		self.current_view = MainTheme()
		self.show_view(self.current_view)
	def setup(self):
		pass

	def on_mouse_press(self, x, y, button, modifiers):
		# do control
		CONTROL_COR = [[-100, -100], [540, 10], [140, 10], [940, 10]]
		next = "-1"
		for i in range(4):
			if(self.current_view.direction[i] != "None" and
      			x >= CONTROL_COR[i][0] and x <= CONTROL_COR[i][0]+40 and
         		y >= CONTROL_COR[i][1] and y <= CONTROL_COR[i][1] + 40):
				next = self.current_view.direction[i]
				break
		if next != "-1":
			next_view = None
			if next == "mainTheme":
				next_view = MainTheme()
			
			self.show_view(next_view)


if __name__ == "__main__":
	window = Game()
	arcade.run()
