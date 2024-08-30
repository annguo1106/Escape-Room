import arcade
from . import sceneUtil
import os
from .itemList import item_list, code_list, backpack_list

class Back(sceneUtil.Scenes):
    def __init__(self):
        super().__init__()
        self.direction = ["DoorRight", "DoorLeft", "None", "None"]
        self.scene_name = "back"
        self.books = []
        self.book_place = [None, None, None, None, None]
        self.book_count = 0
        self.book_ans = ["click book3", "click book2", "click book5", "click book1", "click book4"]
        
    def setBackground(self):
        path = os.path.join(self.current_path, '..', "img/background/back.jpg")
        background = arcade.Sprite(path, 1.02)
        background.center_x = 561
        background.center_y = 325
        self.scene.add_sprite("Background", background)
    
    def set_code(self):
        self.books.clear()
        x = 590
        y = 240
        for book in code_list["bookCode"]:
            path = os.path.join(self.current_path, '..', book["path"])
            sp = arcade.Sprite(path, book["scale"])
            sp.set_position(x, y + sp.height/2)
            x += 50
            self.code.add_sprite("book", sp)
            self.books.append({
					"sprite": sp,
					"name": book["name"],
                    "scale": book["scale"]
				})
        

    def on_draw(self):
        super().on_draw()
        
        # decoding
        if item_list["back"][1]["state"] == 1:
            self.code["book"].draw()
            
        arcade.finish_render()
        
    def on_mouse_press(self, x: int, y: int, button: int, modifires: int):
        super().on_mouse_press(x, y, button, modifires)
                
        # click on lighter
        if item_list["back"][0]["display"]:
            lighter = self.items["lighter"]["sprite"]
            if lighter.collides_with_point((x, y)):
                lighter.remove_from_sprite_lists()
                item_list["back"][0]["display"] = False
                backpack_list[3]["display"] = True
                self.set_backpack()
                self.pre_action = None
                
        # click on shell
        shell = self.items["shell"]["sprite"]
        if(shell.collides_with_point((x, y))):
            # before decoding
            if item_list["back"][1]["state"] == 0:
                self.pre_action = "click shell"
                item_list["back"][1]["state"] = 1
                path = os.path.join(self.current_path, '..', item_list["back"][1]["pathShow"])
                self.load_sp(shell, 0.8, 550, 350, path)
                self.set_code()
                
            # decoding
            elif item_list["back"][1]["state"] == 1:
                # init books
                # if click book -> book enlarge, and pre_action = click booki
                # if click book shell, check range -> fill range
                # when book shell is fill -> check ans. right books remain
                flg_book = True
                for book in self.books:
                    if book["sprite"].collides_with_point((x, y)) and book["sprite"].scale == book["scale"]:
                        flg_book = False
                        if(self.pre_action and self.pre_action.startswith("click")):
                            for j in range(len(self.books)):
                                if(("click " + self.books[j]["name"]) == self.pre_action):
                                    self.books[j]["sprite"].scale = self.books[j]["scale"]
                                    break
                        self.pre_action = "click " + book["name"]
                        self.hand_item = {
                            "sprite": book["sprite"],
                            "name": book["name"],
                            "scale": book["scale"],
                        }
                        book["sprite"].scale = book["scale"] * 1.2
                if flg_book:  # didn't click on books
                    # start: x = 230 (+36)
                    if(self.pre_action.startswith("click book")):
                        place = 285
                        for i in range(5):
                            if place <= x and x <= place + 25:
                                if(self.book_place[i] == None):
                                    self.book_count += 1
                                    self.book_place[i] = self.pre_action
                                    self.hand_item["sprite"].scale = self.hand_item["scale"] * 0.65
                                    self.hand_item["sprite"].position = (place + 13, 276 + self.hand_item["sprite"].height / 2)
                                    self.hand_item = None
                            place += 25
                    self.pre_action = "click shell"
                    # print("hand item:", self.hand_item["name"])
                if self.book_count == 5:  # check ans
                    if self.book_ans != self.book_place:
                        self.book_place = [None, None, None, None, None]
                        self.book_count = 0
                        place = 590
                        for book in self.books:
                            book["sprite"].scale = book["scale"]
                            book["sprite"].set_position(place, 240 + book["sprite"].height/2)
                            place += 50
                            
            # decoded
            elif item_list["back"][1]["state"] == 2:
                path = os.path.join(self.current_path, '..', item_list["back"][1]["pathEnd"])
                self.load_sp(shell, item_list["back"][1]["scale"] * 1.8, 565, 350, path)
                self.pre_action = "click shell"
        
        # exist shell
        elif((self.pre_action == "click shell" or (self.pre_action != None and self.pre_action.startswith("click book"))) and not shell.collides_with_point((x, y))):
            path = os.path.join(self.current_path, '..', item_list["back"][1]["pathSmall"])
            self.load_sp(shell, item_list["back"][1]["scale"], item_list["back"][1]["x"], item_list["back"][1]["y"], path)
            if self.book_count == 5 and item_list["back"][1]["state"] == 1: # solved
                item_list["back"][1]["state"] = 2
            self.book_place = [None, None, None, None, None]
            self.book_count = 0
            for book in self.books:
                book["sprite"].remove_from_sprite_lists()
            if item_list["back"][1]["state"] != 2:
                item_list["back"][1]["state"] = 0
            self.pre_action = None
        
        # at the click event end
        if self.hand_item:
            if(self.hand_item["sprite"].scale != self.hand_item["scale"] and not self.hand_item["sprite"].collides_with_point((x, y))):
                self.hand_item["sprite"].scale = self.hand_item["scale"]
                if(self.pre_action == ("click " + self.hand_item["name"])):
                    # print("change pre action")
                    self.hand_item = None
                    self.pre_action = None
