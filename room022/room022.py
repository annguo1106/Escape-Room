import arcade
from sceneUtil import Scene
from itemUtil import Item
from dialogueUtil import DialogueBox
from constants import SCREEN_WIDTH, SCREEN_HEIGHT 

class Game(arcade.Window):
	def __init__(self):
		super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "ROOM 022")
		self.current_scene = None
		self.dialogue_box = None
		self.scenes = {}
		self.setup()

	def setup(self):
		Room_1 = Scene("images/Room_1.jpg")
		item_cabinet = Item("images/cabinet_close.png", 0.5, "cabinet", "this is a cabinet")
		# item_cabinet.position((400, 200))
		item_cabinet.center_x = 400
		item_cabinet.center_y = 400
		item_cabinet.show()

		item_cabinet_open = Item("images/cabinet_open.png", 0.5, "cabinet_open", "open the cabinet")
		# item_cabinet_open.position((400, 200))
		item_cabinet_open.center_x = 400
		item_cabinet_open.center_y = 400

		item_key = Item("images/key.png", 0.5, "key", "You found a key!")
		# item_key.position((400, 300))
		item_key.center_x = 400
		item_key.center_y = 500

		Room_1.items.append(item_cabinet)
		Room_1.items.append(item_cabinet_open)
		Room_1.items.append(item_key)

		Room_1.items_dict["cabinet"] = item_cabinet
		Room_1.items_dict["cabinet_open"] = item_cabinet_open
		Room_1.items_dict["key"] = item_key

		self.scenes["Room_1"] = Room_1

		self.current_scene = self.scenes["Room_1"]
		self.dialogue_box = DialogueBox("")

	def on_draw(self):
		arcade.start_render()
		self.current_scene.draw()
		self.dialogue_box.draw()

	def on_mouse_press(self, x, y, button, modifiers):
		if self.dialogue_box.visible:
			self.dialogue_box.hide()
		else:
			item = self.current_scene.on_click(x, y)
			if item:
				if item.name == "cabinet":
					if item.visible:              
						self.dialogue_box.text = item.dialogue
						self.dialogue_box.show()
						item.hide()
						item = self.current_scene.items_dict["cabinet_open"]
						item.show()
						item = self.current_scene.items_dict["key"]
						item.show()
				if item.name == "cabinet_open":
					if item.visible:
						self.dialogue_box.text = item.dialogue
						self.dialogue_box.show()
						item.visible = False
						item = self.current_scene.items_dict["cabinet"]
						item.show()
						item = self.current_scene.items_dict["key"]
						item.hide()
				if item.name == "key":
					if item.visible:
						self.dialogue_box.text = item.dialogue
						self.dialogue_box.show()
						item.visible = False
	def on_key_press(self, key, modifires):
		if key == arcade.key.SPACE:
			pass

	def update(self, delta_time):
		self.current_scene.update()

if __name__ == "__main__":
	window = Game()
	arcade.run()
