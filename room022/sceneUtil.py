import arcade
import arcade.csscolor
import arcade.csscolor
import os
from itemList import backpack_list, item_list, control_list

class Scenes(arcade.View):
	def __init__(self):
		super().__init__()
		self.scene = arcade.Scene()
		self.code = arcade.Scene()
		self.direction = []  # left, right, up, down
		self.items = {}
		self.backpack = []
		self.pre_action = None
		self.scene_name = None
		# self.has_backpack = False
	
	def setBackground(self):
		pass

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
		current_path = os.path.dirname(os.path.abspath(__file__))
		# print("current_path:", current_path)
		# print("sceneUtil -> item_list ")
		# print(item_list[self.scene_name])
		for item in item_list[self.scene_name]:
			path = os.path.join(current_path, '..', item["pathSmall"])
			sp = arcade.Sprite(path, item["scale"])
			sp.set_position(item["x"], item["y"])
			self.scene.add_sprite("Items", sp)
			self.items[item["name"]] = {
				"sprite": sp,
				"name": item["name"],
				"show_big": False
			}
		# control
		current_path = os.path.dirname(os.path.abspath(__file__))
		# print("check -> sceneUtil-setup", "self direction")
		# print(self.direction)
		for i in range(4):
			if self.direction[i] != "None":
				path = os.path.join(current_path, '..', control_list[i]["path"])
				sp = arcade.Sprite(path, 0.8)
				sp.set_position(control_list[i]["x"], control_list[i]["y"])
				self.scene.add_sprite("Control", sp)
				
		# scene name, direction and control in child
    
	def on_show(self):
		self.setBackground()
		self.setup()
	
	def on_draw(self):
		arcade.start_render()
		
		# draw background
		arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)
		arcade.draw_rectangle_filled(60, 325, 120, 650, arcade.color.ARMY_GREEN)
		arcade.draw_rectangle_filled(60, 320, 100, 650, arcade.color.AVOCADO)
		arcade.draw_rectangle_filled(60, 620, 80, 30, arcade.color.APPLE_GREEN)
		arcade.draw_text("背包", 35, 610, arcade.color.BLACK, 16)
		
		# draw items
		self.scene.draw()

		# arcade.finish_render()
	
	def on_mouse_press(self, x: int, y: int, button: int, modifires: int):
		click = False
  		# click items in backpack
		if x >= 60 and x <= 320 and y >= 100 and y <= 650:
			for item in self.backpack:
				sp = item["sprite"]
				if(self.pre_action == "click " + item["name"] and not sp.collides_with_ppint((x, y))):
					sp.scale = 0.08
					self.pre_action = None
				elif(item.collides_with_point((x, y))):
					if(self.pre_action and self.pre_action.startwith("click")):
						for j in range(len(self.backpack)):
							if("click " + self.backpack[j]["name"] == self.pre_action):
								self.backpack[j]["sprite"].scale = 0.08
								break
					sp.scale = 0.1
					self.pre_action = "click " + item["name"]