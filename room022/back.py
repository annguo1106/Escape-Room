import arcade
import sceneUtil
import os
from itemList import item_list, code_list

class Back(sceneUtil.Scenes):
    def __init__(self):
        super().__init__()
        self.direction = ["DoorRight", "DoorLeft", "None", "None"]
        self.scene_name = "back"
        self.books = []
        self.book_place = [None, None, None, None, None]
        self.book_count = 0
        self.book_ans = ["click book1", "click book3", "click book2", "click book4", "click book5"]
        
    def setBackground(self):
        path = os.path.join(self.current_path, '..', "img/background/back.jpg")
        background = arcade.Sprite(path, 1.02)
        background.center_x = 561
        background.center_y = 325
        self.scene.add_sprite("Background", background)
    
    def set_code(self):
        self.books.clear()
        x = 550
        y = 330
        for book in code_list["bookCode"]:
            path = os.path.join(self.current_path, '..', book["path"])
            sp = arcade.Sprite(path, book["scale"])
            sp.set_position(x, y)
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
        if item_list["back"][0]["state"] == 1:
            self.code["book"].draw()
            
        arcade.finish_render()
        
    def on_mouse_press(self, x: int, y: int, button: int, modifires: int):
        super().on_mouse_press(x, y, button, modifires)
        print("self.preaction", self.pre_action)
        # init
        shell = self.items["shell"]["sprite"]
        
        # click on shell
        if(shell.collides_with_point((x, y))):
            # before decoding
            if item_list["back"][0]["state"] == 0:
                self.pre_action = "click shell"
                item_list["back"][0]["state"] = 1
                path = os.path.join(self.current_path, '..', item_list["back"][0]["pathShow"])
                shell.texture = arcade.load_texture(path)
                shell.hit_box = shell.texture.hit_box_points
                shell.scale = 0.8
                shell.position = (500, 350)
                self.set_code()
                
            # decoding
            elif item_list["back"][0]["state"] == 1:
                # init books
                # if click book -> book enlarge, and pre_action = click booki
                # if click book shell, check range -> fill range
                # when book shell is fill -> check ans. right books remain
                if 550 <= x and x <= 800:
                    for book in self.books:
                        if book["sprite"].collides_with_point((x, y)):
                            # print("in book preaction:", self.pre_action)
                            if(self.pre_action and self.pre_action.startswith("click")):
                                for j in range(len(self.books)):
                                    if(("click " + self.books[j]["name"]) == self.pre_action):
                                        self.books[j]["sprite"].scale = self.books[j]["scale"]
                                        break
                            self.pre_action = "click " + book["name"]
                            print("update pre action", self.pre_action)
                            self.hand_item = book
                            book["sprite"].scale = book["scale"] * 1.2
                else:  # didn't click on books
                    # start: x = 230 (+36)
                    if(self.pre_action.startswith("click book")):
                        print("in else:", self.pre_action)
                        place = 230
                        for i in range(5):
                            if place <= x and x <= place + 36:
                                if(self.book_place[i] == None):
                                    self.book_count += 1
                                    self.book_place[i] = self.pre_action
                                    self.hand_item["sprite"].scale = self.hand_item["scale"] * 0.8
                                    self.hand_item["sprite"].position = (place + 18, 340)
                                    self.hand_item = None
                            place += 36
                    self.pre_action = "click shell"
                if self.book_count == 5:  # check ans
                    if self.book_ans == self.book_place:
                        item_list["back"][0]["state"] = 2  # solved
                        print("correct!")
                        path = os.path.join(self.current_path, '..', item_list["back"][0]["pathEnd"])
                        shell.texture = arcade.load_texture(path)
                        shell.hit_box = shell.texture.hit_box_points
                        shell.scale = 0.5
                        shell.position = (565, 350)
                    else:
                        self.book_place = [None, None, None, None, None]
                        self.book_count = 0
                        place = 550
                        for book in self.books:
                            book["sprite"].set_position(place, 330)
                            book["sprite"].scale = book["scale"]
                            place += 50
                            
            
            # decoded
            elif item_list["back"][0]["state"] == 2:
                path = os.path.join(self.current_path, '..', item_list["back"][0]["pathEnd"])
                shell.texture = arcade.load_texture(path)
                shell.hit_box = shell.texture.hit_box_points
                shell.scale = 0.5
                shell.position = (565, 350)
                self.pre_action = "click shell"
        
        # exist shell
        elif((self.pre_action == "click shell" or (self.pre_action != None and self.pre_action.startswith("click book"))) and not shell.collides_with_point((x, y))):
            path = os.path.join(self.current_path, '..', item_list["back"][0]["pathSmall"])
            shell.texture = arcade.load_texture(path)
            shell.scale = item_list["back"][0]["scale"]
            shell.position = (item_list["back"][0]["x"], item_list["back"][0]["y"])
            self.book_place = [None, None, None, None, None]
            self.book_count = 0
            for book in self.books:
                book["sprite"].remove_from_sprite_lists()
            if item_list["back"][0]["state"] != 2:
                item_list["back"][0]["state"] = 0
            self.pre_action = None
        
        # at the click event end
        if self.hand_item:
            print("hand item:", self.hand_item["name"])
            if(self.hand_item["sprite"].scale != self.hand_item["scale"] and not self.hand_item["sprite"].collides_with_point((x, y))):
                # print("change scale")
                self.hand_item["sprite"].scale = self.hand_item["scale"]
                if(self.pre_action == ("click " + self.hand_item["name"])):
                    # print("change pre action")
                    self.pre_action = None

        # for book in self.books:
        #     print(book["name"])
        #     print(book["sprite"].visible)
        #     print(book["sprite"].scale)
        #     print(book["sprite"].position)