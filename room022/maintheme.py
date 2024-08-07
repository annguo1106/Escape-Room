import arcade
import sceneUtil

class MainTheme(sceneUtil.Scenes):
    def __init__(self):
        super().__init__()
        
    def setup(self):
        super().setup()
        self.direction = [True, False, False, False]
        self.scene_name = "mainTheme"

        
