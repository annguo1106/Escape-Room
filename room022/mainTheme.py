import arcade
import sceneUtil
import os
from itemList import item_list, backpack_list

class MainTheme(sceneUtil.Scenes):
    def __init__(self):
        super().__init__()
        self.direction = ["DoorLeft", "DoorRight", "Front", "None"]
        self.scene_name = "mainTheme"
        self.drawer = None
        
    def setBackground(self):
        path = os.path.join(self.current_path, '..', "img/background/mainTheme.jpg")
        background = arcade.Sprite(path, 1.02)
        background.center_x = 561
        background.center_y = 325
        self.scene.add_sprite("Background", background)
        
    def setup(self):
        super().setup()
    
    def on_draw(self):
        super().on_draw()
        arcade.finish_render()
        
    def on_mouse_press(self, x: int, y: int, button: int, modifires: int):
        super().on_mouse_press(x, y, button, modifires)
        
        # init
        
        # click on rag
        
        # click on drawer  
        if 418 <= x and x <= 537 and 271 <= y and y <= 303:
            self.drawer = item_list["mainTheme"][0]
            if self.drawer["state"] == 0:
                self.pre_action = "click drawer"
                path = os.path.join(self.current_path, '..', self.drawer["pathShow"])
                self.drawer["sprite"] = arcade.Sprite(path, self.drawer["scale"])
                self.drawer["sprite"].set_position(self.drawer["x"], self.drawer["y"])
                self.scene.add_sprite("Itmes", self.drawer["sprite"])
            elif self.drawer["state"] == 1:
                self.pre_action = "click drawer"
                path = os.path.join(self.current_path, '..', self.drawer["pathEnd"])
                self.drawer["sprite"] = arcade.Sprite(path, self.drawer["scale"])
                self.drawer["sprite"].set_position(self.drawer["x"], self.drawer["y"])
                self.scene.add_sprite("Items", self.drawer["sprite"])
        # exist drawer
        elif(self.pre_action == "click drawer" and (self.drawer != None and not self.drawer["sprite"].collides_with_point((x, y)))):
            self.drawer["sprite"].remove_from_sprite_lists()
            self.drawer = None
                