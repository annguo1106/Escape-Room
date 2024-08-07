import arcade
import arcade.csscolor
import arcade.csscolor
from itemList import backpack_list, item_list

class Scenes(arcade.View):
	def __init__(self):
		super.__init__()
		self.scene = arcade.Scene()
		self.direction = []
		self.items = []
		self.backpack = []
		self.pre_action = None
		self.scene_name = None
		# self.has_backpack = False
	
	def setup(self):
		# backpack
		y = 550
		for item in backpack_list:
			if(item["state"] == 1):
				sp = arcade.Sprite(item["path"], item["scale"])
				sp.position = (60, y)
				y -= 90
				self.scene.add_sprite("Backpack", sp)
				self.backpack.append({
					"sprite": sp,
					"name": item["name"],
					"click": False
				})
		
		# items
		for item in item_list:
			if item["place"] == self.scene_name:
				sp = arcade.Sprite(item["path"], item["scale"])
				sp.center_x = item["x"]
				sp.center_y = item["y"]
				self.scene.add_sprite("Items", sp)
				self.items.append({
					"sprite": sp,
					"name": item["name"],
					"show_big": False
				})

		# scene name, direction and control in child
    
	def on_show(self):
		self.setup()
	
	def on_draw(self):
		arcade.start_render()
		
		# draw background
		arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)
		arcade.draw_rectangle_filled(60, 325, 120, 650, arcade.color.ARMY_GREEN)
		arcade.draw_rectangle_filled(60, 320, 100, 650, arcade.color.AVOCADO)
		arcade.draw_rectangle_filled(60, 620, 80, 30, arcade.color.APPLE_GREEN)
		arcade.draw_text("backpack", 35, 610, arcade.color.BLACK, 16)
		
		# draw items
		for scene in self.scene:
			scene.draw()

		arcade.finish_render()
	
	def on_mouse_press(self, x: int, y: int, button: int, modifires: int):
		click = False
  		# click items in backpack
		for item in self.backpack_list:
			sp = item["sprite"]
			if(self.pre_action == "click " + item["name"] and not sp.collides_with_ppint((x, y))):
				item.scale = 0.08
				self.pre_action = None
			elif(item.collides_with_point((x, y))):
				if(self.pre_action and self.pre_action.startwith("click")):
					for j in range(len(self.backpack)):
						if("click " + self.backpack[j]["name"] == self.pre_action):
							self.backpack[j]["sprite"].scale = 0.08
							break
				item.scale = 0.1
				self.pre_action = "click " + item["name"]
			