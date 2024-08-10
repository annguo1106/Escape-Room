import arcade
import arcade.gui

class FInputBox(arcade.View):
    def __init__(self, y, length, ans):
        super().__init__()
        self.y = y
        self.max_length = length
        self.input_text = ""
        self.cursor_position = 0
        self.ans = ans
        self.result = None
    
    def on_draw(self):
        # center (x, y) = (561, 325)
        start_x = 550 - (self.max_length * 30) // 2
        y = self.y

        # Draw the underscores
        for i in range(self.max_length):
            arcade.draw_text("_", start_x + i * 30, y, arcade.color.BLACK, 24)

        # Draw the input text
        for i, char in enumerate(self.input_text):
            arcade.draw_text(char, start_x + i * 30, y + 5, arcade.color.BLACK, 24)
        # Draw the cursor
        if len(self.input_text) < self.max_length:
            arcade.draw_text("|", start_x + self.cursor_position * 30, y + 5, arcade.color.GRAY, 24)
            
    def on_key_press(self, key, modifiers: int):
        super().on_key_press(key, modifiers)
        if self.input_text == "WRONG":
            self.input_text = ""
        if key == arcade.key.BACKSPACE and self.input_text:
            self.input_text = self.input_text[:-1]
            self.cursor_position = max(self.cursor_position - 1, 0)
        elif len(self.input_text) < self.max_length:
            if key in range(arcade.key.A, arcade.key.Z+1):
                self.input_text += chr(key).upper()
            elif key in range(arcade.key.KEY_0, arcade.key.Z + 1):
                self.input_text += chr(key)
            self.cursor_position = len(self.input_text)
        if len(self.input_text) == self.max_length:
            print("check ans")
            if self.input_text == self.ans:
                self.result = True
            else:
                self.result = False
                self.input_text = "WRONG"
                self.cursor_position = 0
            