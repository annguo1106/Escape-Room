import arcade

class maintheme(arcade.View):
    def __init__(self):
        self.scene = arcade.Scene()
        self.direction = [True, False, True, True]
        
        self.backpack_list = []
        
    def setup(self):
        pass