import arcade
import sceneUtil
import os
from itemList import item_list

class DoorRight(sceneUtil.Scenes):
    def __init__(self):
        super().__init__()
        self.direction = ["MainTheme", "Back", "None", "None"]
        self.scene_name = "doorRight"
        
    def setBackground(self):
        current_path = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(current_path, '..', "img/background/doorRight.png")
        background = arcade.Sprite(path, 1.02)
        background.center_x = 561
        background.center_y = 325
        self.scene.add_sprite("Background", background)
    
    def on_mouse_press(self, x: int, y: int, button: int, modifires: int):
        super().on_mouse_press(x, y, button, modifires)
        current_path = os.path.dirname(os.path.abspath(__file__))
        
        # init
        professorYen = self.items["professorYen"]["sprite"]
        vase = self.items["vase"]["sprite"]
        
        # click on professorYen
        # print("in doorRight -> check professor sprite", professorYen["name"])
        if(professorYen.collides_with_point((x, y))):
            path = os.path.join(current_path, '..', item_list["doorRight"][1]["pathShow"])
            professorYen.texture = arcade.load_texture(path)
            professorYen.scale = 0.5
            professorYen.position = (550, 325)
            self.pre_action = "click professorYen"
        
        # exist professor Yen
        elif(self.pre_action == "click professorYen" and not professorYen.collides_with_point((x, y))):
            path = os.path.join(current_path, '..', item_list["doorRight"][1]["pathSmall"])
            professorYen.texture = arcade.load_texture(path)
            professorYen.scale = item_list["doorRight"][1]["scale"]
            professorYen.position = (item_list["doorRight"][1]["x"], item_list["doorRight"][1]["y"])
            self.pre_action = None            
        
        # click on vase
        elif(vase.collides_with_point((x, y))):
            print(item_list["doorRight"][0]["pathShow"])
            path = os.path.join(current_path, '..', item_list["doorRight"][0]["pathShow"])
            vase.texture = arcade.load_texture(path)
            vase.scale = 0.05
            vase.position = (550, 325)
            self.pre_action = "click vase"
        
        # exist vase
        elif(self.pre_action == "click vase" and not vase.collides_with_point((x, y))):
            path = os.path.join(current_path, '..', item_list["doorRight"][0]["pathSmall"])
            vase.texture = arcade.load_texture(path)
            vase.scale = item_list["doorRight"][0]["scale"]
            vase.position = (item_list["doorRight"][0]["x"], item_list["doorRight"][0]["y"])
            self.pre_action = None
