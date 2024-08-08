import arcade
import sceneUtil
import os

class Back(sceneUtil.Scenes):
    def __init__(self):
        super().__init__()
        self.direction = ["DoorRight", "DoorLeft", "None", "None"]
        self.scene_name = "back"
    
    def setBackground(self):
        current_path = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(current_path, '..', "img/background/back.png")
        background = arcade.Sprite(path, 1.02)
        background.center_x = 561
        background.center_y = 325
        self.scene.add_sprite("Background", background)
        
    def setup(self):
        super().setup()
        

