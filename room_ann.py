import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Room - 1"

class Scene:
		def __init__(self, background_image):
				self.background = arcade.load_texture(background_image)
				self.items = arcade.SpriteList()
				self.items_dict = {}
				self.dialogue = None

class Item(arcade.Sprite):
		def __init__(self, image, scale, name, dialogue):
				super().__init__(image, scale)
				self.dialogue = dialogue
				self.name = name
				self.visible = False
		def show(self):
				self.visible = True
		def hide(self):
				self.visible = False

class DialogueBox:
		def __init__(self, text):
				self.text = text
				self.visible = False
		def show(self):
				self.visible = True
		def hide(self):
				self.visible = False
		def draw(self):
				if self.visible:
						arcade.draw_rectangle_filled(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4, SCREEN_WIDTH - 100, 100, arcade.color.BLACK)
						arcade.draw_text(self.text, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4, arcade.color.WHITE, 16, width=SCREEN_WIDTH - 120, align="center", anchor_x="center", anchor_y="center")

class Game(arcade.Window):
		def __init__(self):
				super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
				self.current_scene = None
				self.dialoge_box = None
				self.scenes = {}
				self.setup()

		def setup(self):
				Room_1 = Scene("Room_1.jpg")
				item_cabinet = Item("images/cabinet_close.png", 0.5, "cabinet", None)
				item_cabinet.position(400, 200)
				item_cabinet.show()

				item_cabinet_open = Item("images/cabinet_open.png", 0.5, "cabinet_open", None)
				item_cabinet_open.position(400, 200)

				item_key = Item("images/key.png", 0.5, "key", "You found a key!")
				item_key.position(400, 300)

				Room_1.items.append(item_cabinet)
				Room_1.items.append(item_cabinet_open)
				Room_1.items.append(item_key)

				Room_1.items_dict["cabinet"] = item_cabinet
				Room_1.items_dict["cabinet_open"] = item_cabinet_open
				Room_1.items_dict["key"] = item_key

				self.scenes["Room_1"] = Room_1

				self.current_scene = self.scenes["Room_1"]
				self.dialoge_box = DialogueBox("")

		def on_draw(self):
				arcade.start_render()
				self.current_scene.draw()
				self.dialoge_box.draw()

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
												item.visible = False
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
