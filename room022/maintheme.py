import arcade
import sceneUtil
import os

class MainTheme(sceneUtil.Scenes):
    def __init__(self):
        super().__init__()
        self.direction = ["DoorLeft", "DoorRight", "Front", "None"]
        self.scene_name = "mainTheme"
    
    def setBackground(self):
        path = os.path.join(self.current_path, '..', "img/background/mainTheme.png")
        background = arcade.Sprite(path, 1.02)
        background.center_x = 561
        background.center_y = 325
        self.scene.add_sprite("Background", background)
        
    def setup(self):
        super().setup()
    
    def on_draw(self):
        super().on_draw()
        arcade.finish_render()
