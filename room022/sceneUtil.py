import arcade
from constants import SCREEN_HEIGHT, SCREEN_WIDTH

class Scene(arcade.View):
	def __init__(self):
		super.__init__()
		self.scene = arcade.Scene()
		self.direction = []
		self.backpack_list = []
		self.pre_action = None
		self.has_backpack = False
	
	def setup():
		pass
 
	def on_show(self):
		self.setup()
	
	def on_draw(self):
		arcade.start_render()
		arcade.draw_text()
	
	def on_click(self, x, y):
		for item in self.items:
			if item.collides_with_point((x, y)):
				return item
		return None