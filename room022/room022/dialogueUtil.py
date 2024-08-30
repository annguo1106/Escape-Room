# not used
import arcade

class DialogueBox:
    def __init__(self, text):
        self.is_visible = False
        self.text = text
        # init background
        self.background = arcade.SpriteSolidColor(800, 600, arcade.color.BLACK)
        self.background.center_x = 550
        self.background.center_y = 50
        # init text
        self.dialogue = arcade.Text(
            text = self.text,
            start_x = 550,
            start_y = 50,
            color=arcade.color.WHEAT,
            font_size = 20,
            width = 800 - 2 * 10,
            align="left"
        )
        
    def on_draw(self):
        if self.is_visible:
            self.background.draw()
            self.dialogue.draw()
        
    def update_text(self, text):
        self.text = text
        self.dialogue.text = text
    
    def show(self):
        self.is_visible = True
        
    def hide(self):
        self.is_visible = False

    
