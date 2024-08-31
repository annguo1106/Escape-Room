import arcade
from room022.room022.constants import SCREEN_WIDTH, SCREEN_HEIGHT 
from room022.room022.mainTheme import MainTheme
from room022.room022.doorLeft import DoorLeft
from room022.room022.doorRight import DoorRight
from room022.room022.back import Back
from room022.room022.front import Front
from room114 import Classroom

class StartScreen(arcade.View):
    def __init__(self):
        super().__init__()

    def setup(self):
        pass

    def on_show(self):
        self.setup()

    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.PINK_PEARL)
        arcade.draw_text("click here to start", 250, 325, arcade.color.BLACK, 50)
        arcade.finish_render()

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        nxt_view = Classroom()
        self.window.show_view(nxt_view)

class MiddleScreen(arcade.View):
    def __init__(self):
        super().__init__()
        
    def setup(self):
        pass
    
    def on_show(self):
        self.setup()
    
    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.PINK_PEARL)
        arcade.draw_text("click here to move to the next room", 250, 325, arcade.color.BLACK, 50)
        arcade.finish_render()
        
    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        nxt_view = MainTheme()
        self.window.show_view(nxt_view)

class EndScreen(arcade.View):
    def __init__(self):
        super().__init__()
        
    def setup(self):
        pass
    
    def on_show(self):
        self.setup()
    
    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.PINK_PEARL)
        arcade.draw_text("congratulations!", 250, 325, arcade.color.BLACK, 50)
        arcade.finish_render()
        

class Game(arcade.Window):
	def __init__(self):
		super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "ROOM 022")
		self.current_name = "start screen"
		current_view = StartScreen()
		self.show_view(current_view)


	def setup(self):
		pass

	def on_mouse_press(self, x, y, button, modifiers):
		if self.current_name == "start screen":
			next_view = Classroom()
			self.current_name = "room 114"
			self.show_view(next_view)
		elif self.current_name == "middle screen":
			self.current_name = "room 022"
			next_view = MainTheme()
			self.show_view(next_view)
			
		elif self.current_name == "room022":
			# do control
		# left and right control position done
			CONTROL_COR = [[140, 10], [940, 10], [540, 605], [540, 10]]
			next = "-1"
			# print("check -> room022-on_mouse_press", "x", x, "y", y)
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
		elif self.current_name == "room 022" and self.current_view.name == "doorRight" and self.current_view.exist:
			next_view = EndScreen()
			self.show_view(next_view)
