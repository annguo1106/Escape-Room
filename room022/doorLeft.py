import arcade
import sceneUtil
import os
from itemList import item_list
class DoorLeft(sceneUtil.Scenes):
    def __init__(self):
        super().__init__()
        self.direction = ["Back", "MainTheme", "None", "None"]
        self.scene_name = "doorLeft"
    
    def setBackground(self):
        current_path = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(current_path, '..', "img/background/doorLeft.png")
        background = arcade.Sprite(path, 1.02)
        background.center_x = 561
        background.center_y = 325
        self.scene.add_sprite("Background", background)
        
    def on_mouse_press(self, x: int, y: int, button: int, modifires: int):
        super().on_mouse_press(x, y, button, modifires)
        current_path = os.path.dirname(os.path.abspath(__file__))
        
        # init
        box = self.items["box"]["sprite"]
        
        # click on box
        if(box.collides_with_point((x, y))):
            path = os.path.join(current_path, '..', item_list["doorLeft"][0]["pathShow"])
            box.texture = arcade.load_texture(path)
            box.scale = 0.5
            box.position = (550, 325)
            self.pre_action = "click box"
            item_list["doorLeft"][0]["state"] = 1
            
            
        # exist professor Yen
        elif(self.pre_action == "click box" and not box.collides_with_point((x, y))):
            path = os.path.join(current_path, '..', item_list["doorLeft"][0]["pathSmall"])
            box.texture = arcade.load_texture(path)
            box.scale = item_list["doorLeft"][0]["scale"]
            box.position = (item_list["doorLeft"][0]["x"], item_list["doorLeft"][0]["y"])
            self.pre_action = None
        
