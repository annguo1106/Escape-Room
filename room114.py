import arcade
import arcade.color
import arcade.color
import arcade.resources
import arcade.resources
import utils      # when run room114.py
# import room114.utils as utils   # when run game.py
import gc
import psutil
# from room022.room022.room022 import Game
from room022.room022.mainTheme import MainTheme 


SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "room 114"

CONTROL_SCALING = 0.8
CONTROL_ALPHA = 140     # the transparency of the img, range(0, 255)

CONTROL_COR = [[-100, -100], [540, 10], [140, 10], [940, 10]]

is_exist = False

# items that should show in backpack
# display: 0: 未拿取, 1: 已拿取, 2: 用完了(不可以重複拿取)
backpack = [
    {   'name': "rag",
        'sprite': None,
        'display': 0,
        'path': "img/backpack/backpack_rag.jpg"
    },
    {   'name': "phone",
        'sprite': None,
        'display': 0,
        'path': None
    },
    {   'name': "charger",
        'sprite': None,
        'display': 0,
        'path': "img/backpack/backpack_charger.jpg"
    },
    {   'name': "ladder",
        'sprite': None,
        'display': 0,
        'path': "img/backpack/backpack_ladder.jpg"
    },
    {   'name': "eraser",
        'sprite': None,
        'display': 0,
        'path': "img/backpack/backpack_eraser.jpg"
    },
    {   'name': "red pen",
        'sprite': None,
        'display': 0,
        'path': "img/backpack/backpack_red pen.jpg"
    }
]

# things that should display in the scene
# 0: not display, 1: display, 2: next state (ex: 批改過的考卷)
display_items = {
    'rag': 1,
    'phone': 1,             # 2: 已解密
    'charger': 0,
    'ladder': 0,
    'eraser': 0,            # 1: 已拿取
    'red pen': 0,           # 1: 已拿取
    'exam_paper': 1,        # 2: 已批改
    'dirty_blackboard': 1,
    'oj_box': 1,            # 2: 已解密開啟
    'door': 1,              # 2: 開門
    'mouse_computer': 1,    # 講台電腦
    'oj_computer': 1,       # 桌子電腦，2: 充電(顯示oj)，3: 已解鎖
    'name_list': 1,
    'drink': 1,             # 2: 擦乾
    'red_pen_box': 1
}

class MyGame(arcade.Window):
    def __init__(self):
        # set up window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        # go to the starting view: classroom
        current_view = Start_screen()
        self.show_view(current_view)

    def setup(self):
        pass

class Start_screen(arcade.View):
    def __init__(self):
        super().__init__()

    def setup(self):
        pass

    def on_show(self):
        self.setup()

    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.PINK_PEARL)
        arcade.draw_text("click here to start", 250, 325, arcade.color.BLACK, 50)
        arcade.finish_render()

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        nxt_view = Classroom()
        self.window.show_view(nxt_view)

class Middle_screen(arcade.View):
    def __init__(self):
        super().__init__()
        self.room = "114"
    def setup(self):
        pass

    def on_show(self):
        self.setup()

    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.PINK_PEARL)
        arcade.draw_text("click here to move to the next room", 30, 325, arcade.color.BLACK, 45)
        arcade.finish_render()

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        print("go to 022")
        nxt_view = MainTheme()
        self.window.show_view(nxt_view)

class Classroom(arcade.View):
    def __init__(self):
        super().__init__()
        self.scene = arcade.Scene()
        self.direction = [True, False, True, True]  # 紀錄前後左右是否可以到達別的場景
        self.sprite_list = arcade.SpriteList()

        self.backpack_list = [] # a list to store the data of the items in the backpack

        # previous action (click item, take from backpack...)
        self.pre_action = None
        self.has_backpack = False
        self.room = "114"

    def setup(self):
        # background
        init = "img/background/classroom_init.jpg"
        bg = arcade.Sprite(init, 0.77)
        bg.center_x = 560
        bg.center_y = 325
        self.scene.add_sprite("Background", bg)
        self.sprite_list.append(bg)

        # control
        arrow_left = arcade.Sprite("img/control/arrow_left.png", CONTROL_SCALING)
        arrow_left.center_x = 160
        arrow_left.center_y = 30
        arrow_left.alpha = CONTROL_ALPHA
        self.scene.add_sprite("Control", arrow_left)
        self.sprite_list.append(arrow_left)

        arrow_right = arcade.Sprite("img/control/arrow_right.png", CONTROL_SCALING)
        arrow_right.center_x = 960
        arrow_right.center_y = 30
        arrow_right.alpha = CONTROL_ALPHA
        self.scene.add_sprite("Control", arrow_right)
        self.sprite_list.append(arrow_right)

        # backpack
        y = 550
        for i in range(len(backpack)):
            item = backpack[i]
            # should show in backpack, create its sprite
            if(item["display"] == 1):
                sp = arcade.Sprite(item["path"], 0.08)
                sp.position = (60, y)
                y -= 90
                self.scene.add_sprite("Backpack", sp)
                self.has_backpack = True
                self.backpack_list.append({
                    "sprite": sp,
                    "name": item["name"],
                    "click": False
                })
                self.sprite_list.append(sp)

    def on_show(self):
        virtual_memory = psutil.virtual_memory()
        used_memory_percentage = virtual_memory.percent
        # print(f"in classroom, Current memory usage: {used_memory_percentage}%")
        self.setup()

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("classroom", 500, 325)
        # background
        utils.draw_background()

        # background and control
        self.scene["Background"].draw()
        self.scene["Control"].draw()

        # backpack
        if(self.has_backpack):
            self.scene["Backpack"].draw()

        arcade.finish_render()

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        click  = False

        # click item in backpack
        for i in range(len(self.backpack_list)):
            item = self.backpack_list[i]["sprite"]
            if(self.pre_action == "click " + self.backpack_list[i]["name"] and not item.collides_with_point((x, y))):
                item.scale = 0.08
                self.pre_action = None

            elif(item.collides_with_point((x, y))):
                if(self.pre_action and self.pre_action.startswith("click")):
                    for j in range(len(self.backpack_list)):
                        if("click " + self.backpack_list[j]["name"] == self.pre_action):
                            self.backpack_list[j]["sprite"].scale = 0.08
                            break
                item.scale = 0.1
                self.pre_action = "click " + self.backpack_list[i]["name"]

        # press control?
        is_ctl = utils.press_control(x, y, self.direction)
        if(not click and is_ctl != -1):
            # release resources
            for sp in self.sprite_list:
                del sp
            arcade.cleanup_texture_cache()
            gc.collect()
            virtual_memory = psutil.virtual_memory()
            used_memory_percentage = virtual_memory.percent
            # print(f"Current memory usage: {used_memory_percentage}%")
            # go left
            if(is_ctl == 2):
                nxt_view = Table()
                self.window.show_view(nxt_view)
            # go right
            elif(is_ctl == 3):
                # release resources
                nxt_view = Door()
                self.window.show_view(nxt_view)
            # default, should not happen
            else:
                print(f"in function on_mouse_press, control, x = {x}, y = {y}, dir = {is_ctl}")

        # click on scene
        scene_list = [[450, 410], [-9999, -9999], [120, 130], [770, 130]]     # U, D, L, R
        is_scene = utils.click_scene(x, y, scene_list, 1)
        if(not click and is_scene != -1):
            # release resources
            for sp in self.sprite_list:
                del sp
            arcade.cleanup_texture_cache()
            gc.collect()
            virtual_memory = psutil.virtual_memory()
            used_memory_percentage = virtual_memory.percent
            # print(f"Current memory usage: {used_memory_percentage}%")
            # go front
            if(is_scene == 0):
                nxt_view = Blackboard()
                self.window.show_view(nxt_view)
            # go left
            elif(is_scene == 2):
                nxt_view = Table()
                self.window.show_view(nxt_view)
            # go right
            elif(is_scene == 3):
                nxt_view = Door()
                self.window.show_view(nxt_view)
            # default, should not happen
            else:
                print(f"in function on_mouse_press, scene, x = {x}, y = {y}, dir = {is_scene}")

    def on_key_press(self, key: int, modifiers: int):
        if(key == arcade.key.A):
            nxt_view = Classroom()
            self.window.show_view(nxt_view)
        elif(key == arcade.key.B):
            nxt_view = Blackboard()
            self.window.show_view(nxt_view)
        elif(key == arcade.key.C):
            nxt_view = Door()
            self.window.show_view(nxt_view)
        elif(key == arcade.key.D):
            nxt_view = Stage()
            self.window.show_view(nxt_view)
        elif(key == arcade.key.E):
            nxt_view = Corner()
            self.window.show_view(nxt_view)
        elif(key == arcade.key.F):
            nxt_view = Table()
            self.window.show_view(nxt_view)

class Blackboard(arcade.View):
    def __init__(self):
        super().__init__()
        self.scene = arcade.Scene()
        self.direction = [False, True, True, True]  # 紀錄前後左右是否可以到達別的場景
        self.sprite_list = arcade.SpriteList()
        
        # record item's data
        self.item_list = []     # a list to store the data of the items in the scene
        self.backpack_list = [] # a list to store the data of the items in the backpack

        # previous action (click item, take from backpack...)
        self.pre_action = None
        self.has_backpack = False
        self.room = "114"

    def setup(self):
        # background
        init = "img/background/blackboard_init.jpg"
        bg = arcade.Sprite(init, 0.7)
        bg.center_x = 560
        bg.center_y = 325
        self.scene.add_sprite("Background", bg)
        self.sprite_list.append(bg)

        # control
        arrow_left = arcade.Sprite("img/control/arrow_left.png", CONTROL_SCALING)
        arrow_left.center_x = 160
        arrow_left.center_y = 30
        arrow_left.alpha = CONTROL_ALPHA
        self.scene.add_sprite("Control", arrow_left)
        self.sprite_list.append(arrow_left)

        arrow_right = arcade.Sprite("img/control/arrow_right.png", CONTROL_SCALING)
        arrow_right.center_x = 960
        arrow_right.center_y = 30
        arrow_right.alpha = CONTROL_ALPHA
        self.scene.add_sprite("Control", arrow_right)
        self.sprite_list.append(arrow_right)

        arrow_down = arcade.Sprite("img/control/arrow_down.png", CONTROL_SCALING)
        arrow_down.center_x = 560
        arrow_down.center_y = 30
        arrow_down.alpha = CONTROL_ALPHA
        self.scene.add_sprite("Control", arrow_down)
        self.sprite_list.append(arrow_down)

        # items
        exam_paper = arcade.Sprite("img/items/blackboard_考卷.jpg", 0.1)
        exam_paper.center_x = 690
        exam_paper.center_y = 70
        self.scene.add_sprite("Items", exam_paper)
        self.item_list.append({
            "sprite": exam_paper,
            "name": "exam_paper",
            "show big": False
        })
        self.sprite_list.append(exam_paper)

        dirty_blcakboard = arcade.Sprite("img/items/blackboard_髒黑板.jpg", 0.18)
        dirty_blcakboard.center_x = 454
        dirty_blcakboard.center_y = 538
        self.scene.add_sprite("Items", dirty_blcakboard)
        self.item_list.append({
            "sprite": dirty_blcakboard,
            "name": "dirty_blackboard",
            "show big": False
        })
        self.sprite_list.append(dirty_blcakboard)

        ladder = arcade.Sprite("img/items/blackboard_ladder.jpg", 0.245)
        ladder.position = (390, 220)
        self.scene.add_sprite("Items", ladder)
        self.item_list.append({
            "sprite": ladder,
            "name": "ladder",
            "show big": False
        })
        self.sprite_list.append(ladder)

        # backpack
        y = 550
        for i in range(len(backpack)):
            item = backpack[i]
            # should show in backpack, create its sprite
            if(item["display"] == 1):
                sp = arcade.Sprite(item["path"], 0.08)
                sp.position = (60, y)
                y -= 90
                if(item["name"] == "ladder"):
                    self.scene.add_sprite("ladder", sp)
                elif(item["name"] == "red pen"):
                    self.scene.add_sprite("red pen", sp)
                elif(item["name"] == "eraser"):
                    self.scene.add_sprite("eraser", sp)
                else:
                    self.scene.add_sprite("Backpack", sp)
                    self.has_backpack = True
                self.backpack_list.append({
                    "sprite": sp,
                    "name": item["name"],
                    "click": False
                })
                self.sprite_list.append(sp)

    def on_show(self):
        self.setup()
        virtual_memory = psutil.virtual_memory()
        used_memory_percentage = virtual_memory.percent
        # print(f"in blackboard, Current memory usage: {used_memory_percentage}%")
        
    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("blackboard", 500, 325)
        # background
        utils.draw_background()
        
        # background and control
        self.scene["Background"].draw()
        self.scene["Control"].draw()
        
        # items
        last_draw = None
        for i in range(len(self.item_list)):
            item = self.item_list[i]["sprite"]
            name = self.item_list[i]["name"]
            if(self.item_list[i]["show big"]):
                last_draw = item
            elif(display_items[name]):
                item.draw()
        if(last_draw):
            last_draw.draw()
        
        # backpack
        if(self.has_backpack):
            self.scene["Backpack"].draw()
        if(backpack[3]["display"] == 1):
            self.scene["ladder"].draw()
        if(backpack[4]["display"] == 1):
            self.scene["eraser"].draw()
        if(backpack[5]["display"] == 1):
            self.scene["red pen"].draw()

        # debug
        # for i in range(len(self.item_list)):
        #     item = self.item_list[i]["sprite"]
        #     name = self.item_list[i]["name"]
        #     if(display_items[name]):
        #         item.draw_hit_box(arcade.color.BLUE, 2)
        #         arcade.draw_point(item.left, item.top, arcade.color.RED, 10)
        #         arcade.draw_point(item.right, item.bottom, arcade.color.RED, 10)

        arcade.finish_render()

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        click = False
        # click item in scene
        exam_paper = self.item_list[0]["sprite"]
        dirty_blackboard = self.item_list[1]["sprite"]


        # exist big exam_paper
        if(self.pre_action == "click exam paper" and not exam_paper.collides_with_point((x, y))):
            ori = arcade.load_texture("img/items/blackboard_考卷.jpg")
            exam_paper.texture = ori
            exam_paper.hit_box = exam_paper.texture.hit_box_points
            exam_paper.scale = 0.1
            exam_paper.position = (690, 70)
            self.pre_action = None
            click = True
            self.item_list[0]["show big"] = False
        
        # exist big dirty_blackboard
        elif(self.pre_action == "click dirty blackboard" and not dirty_blackboard.collides_with_point((x, y))):
            ori = arcade.load_texture("img/items/blackboard_髒黑板.jpg")
            dirty_blackboard.texture = ori
            dirty_blackboard.hit_box = dirty_blackboard.texture.hit_box_points
            dirty_blackboard.scale = 0.18
            dirty_blackboard.position = (454, 538)
            self.pre_action = None
            click = True
            self.item_list[1]["show big"] = False

        # click exam_paper
        elif(exam_paper.collides_with_point((x, y))):
            # 有拿紅筆，顯示批改，背包移除紅筆
            if(self.pre_action == "click red pen"):
                big = arcade.load_texture("img/items/blackboard_考卷_放大批改.jpg")
                display_items["exam_paper"] = 2     # 紀錄為已批改
                backpack[5]["display"] = 2
            # 批改過了，顯示批改
            elif(display_items["exam_paper"] == 2):
                big = arcade.load_texture("img/items/blackboard_考卷_放大批改.jpg")
            # 初始，顯示未批改
            else:
                big = arcade.load_texture("img/items/blackboard_考卷_放大未批改.jpg")
            exam_paper.texture = big
            exam_paper.hit_box = exam_paper.texture.hit_box_points
            exam_paper.scale = 0.55
            exam_paper.position = (560, 325)
            self.pre_action = "click exam paper"
            self.item_list[0]["show big"] = True
        
        # click dirty_blackboard
        elif(dirty_blackboard.collides_with_point((x, y))):
            # 有梯子，有拿板擦，顯示乾淨黑板
            if(display_items["ladder"] and self.pre_action == "click eraser"):
                big = arcade.load_texture("img/items/blackboard_髒黑板_放大乾淨.jpg")
                display_items["eraser"] = True
                backpack[4]["display"] = 2
                display_items["dirty_blackboard"] = 2
                self.pre_action = None
            # 之前擦乾淨了
            elif(display_items["dirty_blackboard"] == 2):
                big = arcade.load_texture("img/items/blackboard_髒黑板_放大乾淨.jpg")
            # 拿梯子，把梯子放上去
            elif(self.pre_action == "click ladder"):
                display_items["ladder"] = True
                backpack[3]["display"] = 2
                display_items["dirty_blackboard"] = 1
                self.pre_action = None
                return
            # 有梯子，無板擦，顯示髒黑板
            elif(display_items["ladder"]):
                big = arcade.load_texture("img/items/blackboard_髒黑板_放大髒.jpg")
            # 初始，無梯子無法點選
            else:
                return
            dirty_blackboard.texture = big
            dirty_blackboard.hit_box = dirty_blackboard.texture.hit_box_points
            dirty_blackboard.scale = 0.55
            dirty_blackboard.position = (560, 325)
            self.pre_action = "click dirty blackboard"
            self.item_list[1]["show big"] = True
        
        # click item in backpack
        for i in range(len(self.backpack_list)):
            item = self.backpack_list[i]["sprite"]
            name = self.backpack_list[i]["name"]
            # click ladder
            if(name == "ladder" and item.collides_with_point((x, y))):
                item.scale = 0.1
                self.pre_action = "click ladder"
            # click eraser
            elif(name == "eraser" and item.collides_with_point((x, y))):
                item.scale = 0.1
                self.pre_action = "click eraser"
            # other
            else:
                if(self.pre_action == "click " + self.backpack_list[i]["name"] and not item.collides_with_point((x, y))):
                    item.scale = 0.08
                    self.pre_action = None

                elif(item.collides_with_point((x, y))):
                    if(self.pre_action and self.pre_action.startswith("click")):
                        for j in range(len(self.backpack_list)):
                            if("click " + self.backpack_list[j]["name"] == self.pre_action):
                                self.backpack_list[j]["sprite"].scale = 0.08
                                break
                    item.scale = 0.1
                    self.pre_action = "click " + self.backpack_list[i]["name"]

        # press control?
        is_ctl = utils.press_control(x, y, self.direction)
        if(not click and is_ctl != -1):
            # release resources
            for sp in self.sprite_list:
                del sp
            arcade.cleanup_texture_cache()
            gc.collect()
            virtual_memory = psutil.virtual_memory()
            used_memory_percentage = virtual_memory.percent
            # print(f"Current memory usage: {used_memory_percentage}%")
            # go left
            if(is_ctl == 2):
                nxt_view = Stage()
                self.window.show_view(nxt_view)
            # go right
            elif(is_ctl == 3):
                nxt_view = Corner()
                self.window.show_view(nxt_view)
            # go back
            elif(is_ctl == 1):
                nxt_view = Classroom()
                self.window.show_view(nxt_view)
            # default, should not happend
            else:
                print(f"in function on_mouse_press, x = {x}, y = {y}, dir = {is_ctl}")
        
        # click on scene
        scene_list = [[-9999, -9999], [-9999, -9999], [120, 50], [850, 50]]     # U, D, L, R
        is_scene = utils.click_scene(x, y, scene_list, 2)
        if(not click and is_scene != -1):
            # release resources
            for sp in self.sprite_list:
                del sp
            arcade.cleanup_texture_cache()
            gc.collect()
            # go left
            if(is_scene == 2):
                nxt_view = Stage()
                self.window.show_view(nxt_view)
            # go right
            elif(is_scene == 3):
                nxt_view = Corner()
                self.window.show_view(nxt_view)
            # default, should not happen
            else:
                print(f"in function on_mouse_press, scene, x = {x}, y = {y}, dir = {is_scene}")

    def on_key_press(self, key: int, modifiers: int):
        if(key == arcade.key.A):
            nxt_view = Classroom()
            self.window.show_view(nxt_view)
        elif(key == arcade.key.B):
            nxt_view = Blackboard()
            self.window.show_view(nxt_view)
        elif(key == arcade.key.C):
            nxt_view = Door()
            self.window.show_view(nxt_view)
        elif(key == arcade.key.D):
            nxt_view = Stage()
            self.window.show_view(nxt_view)
        elif(key == arcade.key.E):
            nxt_view = Corner()
            self.window.show_view(nxt_view)
        elif(key == arcade.key.F):
            nxt_view = Table()
            self.window.show_view(nxt_view)

class Door(arcade.View):
    def __init__(self):
        super().__init__()
        self.scene = arcade.Scene()
        self.direction = [False, True, False, False]  # 紀錄前後左右是否可以到達別的場景
        self.sprite_list = arcade.SpriteList()

        # record item's data
        self.item_list = []     # a list to store the data of the items in the scene
        self.backpack_list = [] # a list to store the data of the items in the backpack
        self.btn_list = []      # a list to store btn sprite (for door password)
        self.color_list = []    # a list to store color sprite (for oj box password)

        self.pre_action = None          # previous action (click item, take from backpack...)
        self.has_backpack = False       # 背包中是否有東西
        self.has_rag = False            # 背包裡是否有抹布(還是在場景中)
        self.has_ladder = False         # 背包裡是否有梯子(還是在場景中)
        self.door_pw = ""               # string to record player's password
        self.ojbox_pw = [0, 0, 0, 0]    # list to record player's password

        self.last_draw = "none"
        self.is_exist = False
        self.room = "114"

    def setup(self):
        # background
        init = "img/background/door_init.jpg"
        bg = arcade.Sprite(init, 0.68)
        bg.center_x = 560
        bg.center_y = 325
        self.scene.add_sprite("Background", bg)
        self.sprite_list.append(bg)

        # control
        arrow_down = arcade.Sprite("img/control/arrow_down.png", CONTROL_SCALING)
        arrow_down.center_x = 560
        arrow_down.center_y = 30
        arrow_down.alpha = CONTROL_ALPHA
        self.scene.add_sprite("Control", arrow_down)
        self.sprite_list.append(arrow_down)

        # items
        oj_box = arcade.Sprite("img/items/door_oj 寶箱.jpg", 0.135)
        oj_box.position = (230, 349)
        self.scene.add_sprite("Items", oj_box)
        self.item_list.append({
            "sprite": oj_box,
            "name": "oj_box",
            "show big": False
        })
        self.sprite_list.append(oj_box)

        door = arcade.Sprite("img/items/door.jpg", 0.27)
        door.position = (640, 225)
        self.scene.add_sprite("Items", door)
        self.item_list.append({
            "sprite": door,
            "name": "door",
            "show big": False
        })
        self.sprite_list.append(door)

        rag = arcade.Sprite("img/items/door_抹布.jpg", 0.1)
        rag.position = (190, 150)
        self.scene.add_sprite("rag", rag)
        self.item_list.append({
            "sprite": rag,
            "name": "rag",
            "show big": False
        })
        self.sprite_list.append(rag)

        # 解謎
        # door
        x = 460
        for i in range(2):
            btn = arcade.Sprite("img/items/door_門口密碼放.jpg", 0.18)
            btn.position = (x, 280)
            x += 200
            self.scene.add_sprite("door_password", btn)
            self.btn_list.append({
                "sprite": btn,
                "click": False,
                "time": 0
            })
            self.sprite_list.append(btn)

        
        # oj box
        x = 374
        for i in range(4):
            color = arcade.Sprite("img/items/door_oj 寶箱0.jpg", 0.117)
            color.position = (x, 227)
            x += 115
            self.scene.add_sprite("ojbox_password", color)
            self.color_list.append({
                "sprite": color,
                "color": 0
            })
            self.sprite_list.append(color)
        
        # backpack
        y = 550
        for i in range(len(backpack)):
            item = backpack[i]
            # should show in backpack, create its sprite
            if(item["display"] == 1):
                sp = arcade.Sprite(item["path"], 0.08)
                sp.position = (60, y)
                y -= 90
                self.scene.add_sprite("Backpack", sp)
                self.sprite_list.append(sp)
                self.backpack_list.append({
                    "sprite": sp,
                    "name": item["name"],
                    "click": False
                })
                self.has_backpack = True
                if(item["name"] == "rag"):
                    self.has_rag = True
                if(item["name"] == "ladder"):
                    self.has_ladder = True

        # rag is in scene, may be added to backpack
        if(not backpack[0]["display"]):
            backpack_rag = arcade.Sprite("img/backpack/backpack_rag.jpg", 0.08)
            backpack_rag.position = (60, y)
            y -= 90
            self.scene.add_sprite("backpack_rag", backpack_rag)
            self.backpack_list.append({
                "sprite": backpack_rag,
                "name": "backpack_rag",
                "click": False
            })
            self.sprite_list.append(backpack_rag)

        # ladder in scene(oj box), may be added to backpack
        if(not backpack[3]["display"]):
            backpack_ladder = arcade.Sprite("img/backpack/backpack_ladder.jpg", 0.08)
            backpack_ladder.position = (60, y)
            self.scene.add_sprite("backpack_ladder", backpack_ladder)
            self.backpack_list.append({
                "sprite": backpack_ladder,
                "name": "backpack_ladder",
                "click": False
            })
            self.sprite_list.append(backpack_ladder)

    def on_show(self):
        self.setup()
        virtual_memory = psutil.virtual_memory()
        used_memory_percentage = virtual_memory.percent
        # print(f"in door, Current memory usage: {used_memory_percentage}%")

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("door", 500, 325)
        # background
        utils.draw_background()
        
        # background
        self.scene["Background"].draw()
        
        # items
        # scene rag
        if(display_items["rag"]):
            self.scene["rag"].draw()

        # other items
        last_draw = None
        for i in range(len(self.item_list)):
            item = self.item_list[i]["sprite"]
            name = self.item_list[i]["name"]
            if(self.item_list[i]["show big"]):
                last_draw = item
                self.last_draw = name
            elif(display_items[name]):
                item.draw()

        if(last_draw):
            last_draw.draw()

        # debug
        # for i in range(len(self.item_list)):
        #     item = self.item_list[i]["sprite"]
        #     name = self.item_list[i]["name"]
        #     if(display_items[name]):
        #         item.draw_hit_box(arcade.color.BLUE, 2)
        #         arcade.draw_point(item.left, item.top, arcade.color.RED, 10)
        #         arcade.draw_point(item.right, item.bottom, arcade.color.RED, 10)
        
        # 門口解謎
        if(self.item_list[1]["show big"] and display_items["door"] == 1):
            self.scene["door_password"].draw()
        
        # oj 寶箱解謎
        # if(self.item_list[0]["show big"]):
        if(self.pre_action == "click oj_box" and display_items["oj_box"] != 2):
            self.scene["ojbox_password"].draw()
        
        # backpack
        if(self.has_backpack):
            self.scene["Backpack"].draw()
        # backpack rag
        if(backpack[0]["display"] == 1 and not self.has_rag):
            self.scene["backpack_rag"].draw()
        # backpack ladder
        if(backpack[3]["display"] == 1 and not self.has_ladder):
            self.scene["backpack_ladder"].draw()
        # control
        self.scene["Control"].draw()

        arcade.finish_render()

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        click = False
        is_ctl = utils.press_control(x, y, self.direction)

        # click item
        oj_box = self.item_list[0]["sprite"]
        door = self.item_list[1]["sprite"]
        rag = self.item_list[2]["sprite"]
        
        # click rag, add to backpack
        if(backpack[0]["display"] == 0 and rag.collides_with_point((x, y))):
            display_items["rag"] = False
            backpack[0]["display"] = True
        
        # click items in scene
        # exist big oj_box
        if(self.item_list[0]["show big"] and not oj_box.collides_with_point((x, y))):
            # # print("exist big oj box")
            ori = arcade.load_texture("img/items/door_oj 寶箱.jpg")
            oj_box.texture = ori
            oj_box.hit_box = oj_box.texture.hit_box_points
            oj_box.scale = 0.135
            oj_box.position = (230, 349)

            self.pre_action = None
            self.ojbox_pw = [0, 0, 0, 0]
            click  = True
            self.item_list[0]["show big"] = False

            # init colors
            for i in range(4):
                self.color_list[i]["sprite"].texture = arcade.load_texture("img/items/door_oj 寶箱0.jpg")

            # if box open, add ladder to backpack
            if(backpack[3]["display"] == 0 and display_items["oj_box"] == 2):
                backpack[3]["display"] = True
            
            return

        # exist big door
        elif(self.item_list[1]["show big"] and not door.collides_with_point((x, y))):
            ori = arcade.load_texture("img/items/door.jpg")
            door.texture = ori
            door.hit_box = door.texture.hit_box_points
            door.scale = 0.27
            door.position = (640, 225)
            self.pre_action = None
            self.door_pw = ""
            click  = True
            self.item_list[1]["show big"] = False
            if(self.is_exist):
                nxt_view = Middle_screen()
                self.window.show_view(nxt_view)
            return
        
        # press control?
        elif(is_ctl != -1):
            # go back
            if(is_ctl == 1):
                # release resources
                for sp in self.sprite_list:
                    del sp
                arcade.cleanup_texture_cache()
                gc.collect()
                virtual_memory = psutil.virtual_memory()
                used_memory_percentage = virtual_memory.percent
                # print(f"Current memory usage: {used_memory_percentage}%")
                nxt_view = Classroom()
                self.window.show_view(nxt_view)
            # default, should not happend
            else:
                print(f"in function on_mouse_press, x = {x}, y = {y}, dir = {is_ctl}")

        # click oj box, show big (password or open)
        elif(oj_box.collides_with_point((x, y))):
            click  = True
            # 解謎中
            if(self.item_list[0]["show big"]):
                for i in range(4):
                    color = self.color_list[i]
                    # 點擊顏色，變顏色 紀錄玩家密碼
                    if(color["sprite"].collides_with_point((x, y))):
                        color_id = (color["color"] + 1)%3
                        color["color"] = color_id
                        color["sprite"].texture = arcade.load_texture(f"img/items/door_oj 寶箱{color_id}.jpg")
                        self.ojbox_pw[i] = color_id
                
                # check whether the password is correct
                ans = [0, 2, 1, 2]
                correct  = True
                for i in range(4):
                    if(self.ojbox_pw[i] != ans[i]):
                        correct = False
                        break
                if(correct):
                    oj_box.texture = arcade.load_texture("img/items/door_oj 寶箱_大開.jpg")
                    oj_box.scale = 0.55
                    oj_box.position = (560, 325)
                    display_items["oj_box"] = 2

            else:
                if(display_items["oj_box"] == 2):   # 已解密
                    big = arcade.load_texture("img/items/door_oj 寶箱_大開.jpg")
                else:                               # 待解密
                    big = arcade.load_texture("img/items/door_oj 寶箱_大關.jpg")
                oj_box.texture = big
                oj_box.hit_box = oj_box.texture.hit_box_points
                oj_box.scale = 0.55
                oj_box.position = (560, 325)
                self.pre_action = "click oj_box"
                self.item_list[0]["show big"] = True

            return
            
        # click door, show big (password) or open
        elif(door.collides_with_point((x, y))):
            # 解密中，when click btn, record order and change texture
            if(self.item_list[1]["show big"]):
                # click on right/left btn
                if(self.btn_list[0]["sprite"].collides_with_point((x, y))):
                    self.door_pw += '0'
                    self.btn_list[0]["click"] = True
                elif(self.btn_list[1]["sprite"].collides_with_point((x, y))):
                    self.door_pw += '1'
                    self.btn_list[1]["click"] = True

                # password correct, open
                if(self.door_pw == "1011"):
                    big = arcade.load_texture("img/items/door_門口開門.jpg")
                    display_items["door"] = 2
                    print("correct")
                    self.is_exist = True
                else:
                    return
            # 未解密
            elif(display_items["door"] == 1):
                big = arcade.load_texture("img/items/door_門口密碼.jpg")
            # 解密，開門
            else:
                big = arcade.load_texture("img/items/door_門口開門.jpg")
            door.texture = big
            door.hit_box = door.texture.hit_box_points
            door.scale = 0.55
            door.position = (560, 325)
            self.pre_action = "click door"
            self.item_list[1]["show big"] = True
            return

        # click item in backpack
        for i in range(len(self.backpack_list)):
            item = self.backpack_list[i]["sprite"]
            if(self.pre_action == "click " + self.backpack_list[i]["name"] and not item.collides_with_point((x, y))):
                item.scale = 0.08
                self.pre_action = None

            elif(item.collides_with_point((x, y))):
                if(self.pre_action and self.pre_action.startswith("click")):
                    for j in range(len(self.backpack_list)):
                        if("click " + self.backpack_list[j]["name"] == self.pre_action):
                            self.backpack_list[j]["sprite"].scale = 0.08
                            break
                item.scale = 0.1
                self.pre_action = "click " + self.backpack_list[i]["name"]

    def update(self, delta_time: float):
        # door password btn
        for i in range(2):
            btn = self.btn_list[i]
            if(btn["click"]):
                btn["time"] += delta_time
                if(btn["time"] < 0.2):
                    btn["sprite"].texture = arcade.load_texture("img/items/door_門口密碼按.jpg")
                else:
                    btn["sprite"].texture = arcade.load_texture("img/items/door_門口密碼放.jpg")
                    btn["time"] = 0
                    btn["click"] = False

    def on_key_press(self, key: int, modifiers: int):
        if(key == arcade.key.A):
            nxt_view = Classroom()
            self.window.show_view(nxt_view)
        elif(key == arcade.key.B):
            nxt_view = Blackboard()
            self.window.show_view(nxt_view)
        elif(key == arcade.key.C):
            nxt_view = Door()
            self.window.show_view(nxt_view)
        elif(key == arcade.key.D):
            nxt_view = Stage()
            self.window.show_view(nxt_view)
        elif(key == arcade.key.E):
            nxt_view = Corner()
            self.window.show_view(nxt_view)
        elif(key == arcade.key.F):
            nxt_view = Table()
            self.window.show_view(nxt_view)

class Stage(arcade.View):
    def __init__(self):
        super().__init__()
        self.scene = arcade.Scene()
        self.direction = [False, True, False, False]  # 紀錄前後左右是否可以到達別的場景
        self.sprite_list = arcade.SpriteList()

        self.item_list = []         # items sprites
        self.backpack_list = []     # backpack items sprite
        self.block_list = []        # drawer password sprites(0: white, 1:black)
        self.mouse_sprite = []      # record data of the mouse sprite
        self.digit_list = []        # computer password sprites

        self.has_backpack = False
        self.pre_action = None
        self.show_drawer = 0                        # 1: 解謎, 2: 打開獲得板擦, 0: leave
        if(display_items["eraser"] == 0):
            self.show_drawer = 0
        else:
            self.show_drawer = 3
        self.drawer_pw = [[0]*4 for _ in range(4)]  # drawer's password
        self.has_eraser = False
        self.computer_pw = [8] * 5
        self.room = "114"

    def setup(self):
        # background
        init = "img/background/stage_init.jpg"
        bg = arcade.Sprite(init, 0.69)
        bg.center_x = 563
        bg.center_y = 325
        self.scene.add_sprite("Background", bg)
        self.sprite_list.append(bg)

        # control
        arrow_down = arcade.Sprite("img/control/arrow_down.png", CONTROL_SCALING)
        arrow_down.center_x = 560
        arrow_down.center_y = 30
        arrow_down.alpha = CONTROL_ALPHA
        self.scene.add_sprite("Control", arrow_down)
        self.sprite_list.append(arrow_down)

        # items
        computer = arcade.Sprite("img/items/stage_computer.jpg", 0.208)
        computer.position = (501, 370.5)
        self.scene.add_sprite("Items", computer)
        self.item_list.append({
            "sprite": computer,
            "name": "mouse_computer",
            "show big": False
        })
        self.sprite_list.append(computer)

        if(self.show_drawer == 0):
            drawer_big = arcade.Sprite("img/items/stage_drawer_大解謎.jpg", 0.55)
        else:
            drawer_big = arcade.Sprite("img/items/stage_drawer_大開.jpg", 0.55)
        drawer_big.position = (560, 325)
        self.scene.add_sprite("drawer", drawer_big)
        self.sprite_list.append(drawer_big)

        # 解謎
        # 電腦密碼
        x = 425
        for i in range(5):
            digit = arcade.Sprite("img/items/stage_computer8.jpg", 0.25)
            digit.position = (x, 235)
            x += 65
            self.scene.add_sprite("digit", digit)
            self.digit_list.append({
                "sprite": digit,
                "val": 8
            })
            self.sprite_list.append(digit)

        # 電腦滑鼠軌跡
        mouse = arcade.Sprite("img/control/mouse.png")
        mouse.position = (560, 325)
        self.scene.add_sprite("mouse", mouse)
        self.mouse_sprite.append({
            "sprite": mouse,
            "time": 0
        })
        self.sprite_list.append(mouse)

        # 抽屜
        y = 475
        for _ in range(4):
            x = 410
            for _ in range(4):
                block = arcade.Sprite("img/items/stage_drawer0.jpg", 0.1)
                block.position = (x, y)
                x += 100
                self.scene.add_sprite("block", block)
                self.block_list.append({
                    "sprite": block,
                    "state": 0
                })
                self.sprite_list.append(block)
            y -= 100

        # backpack
        y = 550
        for i in range(len(backpack)):
            item = backpack[i]
            # should show in backpack, create its sprite
            if(item["display"] == 1):
                sp = arcade.Sprite(item["path"], 0.08)
                sp.position = (60, y)
                y -= 90
                self.scene.add_sprite("Backpack", sp)
                self.backpack_list.append({
                    "sprite": sp,
                    "name": item["name"],
                    "click": False
                })
                self.sprite_list.append(sp)
                self.has_backpack = True
                if(item["name"] == "eraser"):
                    self.has_eraser = True
        
        if(not backpack[4]["display"]):
            eraser = arcade.Sprite("img/backpack/backpack_eraser.jpg", 0.08)
            eraser.position = (60, y)
            y -= 90
            self.scene.add_sprite("eraser", eraser)
            self.backpack_list.append({
                "sprite": eraser,
                "name": "eraser",
                "click": False
            })
            self.sprite_list.append(eraser)

    def on_show(self):
        self.setup()
        virtual_memory = psutil.virtual_memory()
        used_memory_percentage = virtual_memory.percent
        # print(f"in stage, Current memory usage: {used_memory_percentage}%")

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("stage", 500, 325)
        # background
        utils.draw_background()

        # background and control
        self.scene["Background"].draw()
        self.scene["Control"].draw()

        # items
        last_draw = None
        for i in range(len(self.item_list)):
            item = self.item_list[i]["sprite"]
            name = self.item_list[i]["name"]
            if(self.item_list[i]["show big"]):
                last_draw = item
            elif(display_items[name]):
                item.draw()
        if(last_draw):
            last_draw.draw()

        # backpack
        if(self.has_backpack):
            self.scene["Backpack"].draw()

        if(backpack[4]["display"] == 1 and not self.has_eraser):
            self.scene["eraser"].draw()

        # 解謎
        if(self.show_drawer == 1 or self.show_drawer == 2):
            self.scene["drawer"].draw()
        if(self.show_drawer == 1):
            self.scene["block"].draw()

        if(self.item_list[0]["show big"] and display_items["mouse_computer"] == 1):
            self.scene["digit"].draw()
            arcade.draw_text("密碼:", 320, 230, arcade.color.CADET_GREY, 15)
        elif(self.item_list[0]["show big"] and display_items["mouse_computer"] == 2):
            self.scene["mouse"].draw()

        # debug
        # for i in range(len(self.item_list)):
        #     item = self.item_list[i]["sprite"]
        #     name = self.item_list[i]["name"]
        #     if(display_items[name]):
        #         item.draw_hit_box(arcade.color.BLUE, 2)
        #         arcade.draw_point(item.left, item.top, arcade.color.RED, 10)
        #         arcade.draw_point(item.right, item.bottom, arcade.color.RED, 10)

        arcade.finish_render()

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        is_ctl = utils.press_control(x, y, self.direction)

        computer = self.item_list[0]["sprite"]
        
        # exist computer
        if(self.item_list[0]["show big"] and not computer.collides_with_point((x, y))):
            computer.texture = arcade.load_texture("img/items/stage_computer.jpg")
            computer.hit_box = computer.texture.hit_box_points
            computer.scale = 0.208
            computer.position = (501, 370.5)
            self.item_list[0]["show big"] = False
            self.mouse_sprite[0]["time"] = 0
            # init password
            for i in range(5):
                self.digit_list[i]["sprite"].texture = arcade.load_texture("img/items/stage_computer8.jpg")
                self.computer_pw[i] = 8

        # exist drawer
        elif(self.pre_action == "click drawer" and not self.scene["drawer"][0].collides_with_point((x, y))):
            self.show_drawer = 0 if self.show_drawer == 1 else 3
            self.pre_action = None
            # init password
            for i in range(16):
                self.block_list[i]["state"] = 0
                self.block_list[i]["sprite"].texture = arcade.load_texture("img/items/stage_drawer0.jpg")
                self.drawer_pw[int(i/4)][i%4] = 0
            if(backpack[4]["display"] == 0 and display_items["eraser"] == 1):
                backpack[4]["display"] = True
        
        # click computer
        elif(not self.pre_action == "click drawer" and computer.collides_with_point((x, y))):
            # 解謎
            if(display_items["mouse_computer"] == 1):
                big = arcade.load_texture("img/items/stage_computer_大密碼.jpg")
                for i in range(5):
                    digit = self.digit_list[i]["sprite"]
                    if(digit.collides_with_point((x, y))):
                        val = (self.digit_list[i]["val"] + 1) % 10
                        self.digit_list[i]["val"] = val
                        digit.texture = arcade.load_texture(f"img/items/stage_computer{val}.jpg")
                        self.computer_pw[i] = val
                correct = True
                ans = [7, 1, 6, 5, 0]
                for i in range(5):
                    if(self.computer_pw[i] != ans[i]):
                        correct = False
                        break
                if(correct):
                    big = arcade.load_texture("img/items/stage_computer_大.jpg")
                    display_items["mouse_computer"] = 2
                        
            # 已解謎，顯示滑鼠軌跡
            else:
                big = arcade.load_texture("img/items/stage_computer_大.jpg")
            computer.texture = big
            computer.hit_box = computer.texture.hit_box_points
            computer.scale = 0.55
            computer.position = (560, 325)
            self.item_list[0]["show big"] = True
        
        # 抽屜解謎
        elif(self.pre_action == "click drawer" and self.scene["drawer"][0].collides_with_point((x, y)) and self.show_drawer == 1):
            for i in range(16):
                if(self.block_list[i]["sprite"].collides_with_point((x, y))):
                    idx = (self.block_list[i]["state"] + 1) % 2
                    self.block_list[i]["state"] = idx
                    self.block_list[i]["sprite"].texture = arcade.load_texture(f"img/items/stage_drawer{idx}.jpg")
                    self.drawer_pw[int(i/4)][i%4] = idx
            # check valid
            correct = True
            ans = [[1, 0, 0, 0],
                    [0, 0, 0, 1],
                    [0, 1, 0, 0],
                    [0, 0, 1, 0]]
            for i in range(4):
                for j in range(4):
                    if(self.drawer_pw[i][j] != ans[i][j]):
                        correct = False
                        break
            if(correct):
                self.show_drawer = 2
                self.scene["drawer"][0].texture = arcade.load_texture("img/items/stage_drawer_大開.jpg")
                self.pre_action = "click drawer"
                display_items["eraser"] = 1
        
        # click 抽屜
        elif(x>=350 and x<=810 and y>=160 and y<=230):
            self.pre_action = "click drawer"
            # case 1. 解謎
            if(self.show_drawer == 0):
                self.show_drawer = 1

            # case 2. 已打開獲得板擦
            else:
                self.show_drawer = 2
                self.scene["drawer"][0].texture = arcade.load_texture("img/items/stage_drawer_大開.jpg")
        
        # press control?
        elif(is_ctl != -1):
            # go back
            if(is_ctl == 1):
                # release resources
                for sp in self.sprite_list:
                    del sp
                arcade.cleanup_texture_cache()
                gc.collect()
                virtual_memory = psutil.virtual_memory()
                used_memory_percentage = virtual_memory.percent
                # print(f"Current memory usage: {used_memory_percentage}%")
                nxt_view = Blackboard()
                self.window.show_view(nxt_view)
            # default, should not happend
            else:
                print(f"in function on_mouse_press, x = {x}, y = {y}, dir = {is_ctl}")

        # click item in backpack
        for i in range(len(self.backpack_list)):
            item = self.backpack_list[i]["sprite"]
            if(self.pre_action == "click " + self.backpack_list[i]["name"] and not item.collides_with_point((x, y))):
                item.scale = 0.08
                self.pre_action = None

            elif(item.collides_with_point((x, y))):
                if(self.pre_action and self.pre_action.startswith("click")):
                    for j in range(len(self.backpack_list)):
                        if("click " + self.backpack_list[j]["name"] == self.pre_action):
                            self.backpack_list[j]["sprite"].scale = 0.08
                            break
                item.scale = 0.1
                self.pre_action = "click " + self.backpack_list[i]["name"]

    def update(self, delta_time: float):
        # 電腦滑鼠軌跡 (RLRR)
        if(self.item_list[0]["show big"]):
            mouse = self.mouse_sprite[0]
            mouse["time"] += delta_time
            middle = (560, 300)
            left = (400, 350)
            right = (720, 350)
            if(mouse["time"] < 1):
                mouse["sprite"].position = middle
            elif(mouse["time"] < 2):
                mouse["sprite"].position = right
            elif(mouse["time"] < 3):
                mouse["sprite"].position = middle
            elif(mouse["time"] < 4):
                mouse["sprite"].position = left
            elif(mouse["time"] < 5):
                mouse["sprite"].position = middle
            elif(mouse["time"] < 6):
                mouse["sprite"].position = right
            elif(mouse["time"] < 7):
                mouse["sprite"].position = middle
            elif(mouse["time"] < 8):
                mouse["sprite"].position = right
            elif(mouse["time"] < 10):
                mouse["sprite"].position = middle
            else:
                mouse["time"] = 0
    
    def on_key_press(self, key: int, modifiers: int):
        if(key == arcade.key.A):
            nxt_view = Classroom()
            self.window.show_view(nxt_view)
        elif(key == arcade.key.B):
            nxt_view = Blackboard()
            self.window.show_view(nxt_view)
        elif(key == arcade.key.C):
            nxt_view = Door()
            self.window.show_view(nxt_view)
        elif(key == arcade.key.D):
            nxt_view = Stage()
            self.window.show_view(nxt_view)
        elif(key == arcade.key.E):
            nxt_view = Corner()
            self.window.show_view(nxt_view)
        elif(key == arcade.key.F):
            nxt_view = Table()
            self.window.show_view(nxt_view)

class Corner(arcade.View):
    def __init__(self):
        super().__init__()
        self.scene = arcade.Scene()
        self.direction = [False, True, False, False]  # 紀錄前後左右是否可以到達別的場景
        self.sprite_list = arcade.SpriteList()

        # record item's data
        self.item_list = []     # a list to store the data of the items in the scene
        self.backpack_list = [] # a list to store the data of the items in the backpack
        self.word_list = []     # a list to store the word's sprite (box)
        self.arrow_list = []    # a list to store the arrow's sprite (phone)

        self.pre_action = None      # previous action (click item, take from backpack...)
        self.has_backpack = False
        self.has_charger = False
        self.has_red_pen = False
        self.box_pw = [0, 0, 0]
        self.phone_pw = [180, 180, 180]
        self.room = "114"

    def setup(self):
        # background
        init = "img/background/corner_init.jpg"
        bg = arcade.Sprite(init, 0.678)
        bg.center_x = 560
        bg.center_y = 325
        self.scene.add_sprite("Background", bg)
        self.sprite_list.append(bg)

        # control
        arrow_down = arcade.Sprite("img/control/arrow_down.png", CONTROL_SCALING)
        arrow_down.center_x = 560
        arrow_down.center_y = 30
        arrow_down.alpha = CONTROL_ALPHA
        self.scene.add_sprite("Control", arrow_down)
        self.sprite_list.append(arrow_down)

        # items
        box = arcade.Sprite("img/items/corner_box.jpg", 0.24)
        box.position = (820, 314)
        self.scene.add_sprite("Items", box)
        self.item_list.append({
            "sprite": box,
            "name": "red_pen_box",
            "show big": False
        })
        self.sprite_list.append(box)

        phone = arcade.Sprite("img/items/corner_phone.jpg", 0.12)
        phone.position = (410, 240)
        self.scene.add_sprite("Items", phone)
        self.item_list.append({
            "sprite": phone,
            "name": "phone",
            "show big": False
        })
        self.sprite_list.append(phone)

        # 解謎
        x = 430
        for i in range(3):
            word = arcade.Sprite("img/items/corner_box0.jpg", 0.11)
            word.position = (x, 300)
            x += 120
            self.scene.add_sprite("word", word)
            self.word_list.append({
                "sprite": word,
                "char": 0
            })
            self.sprite_list.append(word)


        x = 430
        for i in range(3):
            arrow = arcade.Sprite("img/items/corner_phone_arrow.jpg", 0.1)
            arrow.position = (x, 300)
            arrow.angle = 180
            x += 120
            self.scene.add_sprite("arrow", arrow)
            self.arrow_list.append({
                "sprite": arrow,
            })
            self.sprite_list.append(arrow)


        # backpack
        y = 550
        for i in range(len(backpack)):
            item = backpack[i]
            # should show in backpack, create its sprite
            if(item["display"] == 1):
                sp = arcade.Sprite(item["path"], 0.08)
                sp.position = (60, y)
                y -= 90
                self.scene.add_sprite("Backpack", sp)
                self.has_backpack = True
                if(item["name"] == "charger"):
                    self.has_charger = True
                if(item["name"] == "red pen"):
                    self.has_red_pen = True
                self.backpack_list.append({
                    "sprite": sp,
                    "name": item["name"],
                    "click": False
                })
                self.sprite_list.append(sp)

        if(not backpack[2]["display"]):
            charger = arcade.Sprite("img/backpack/backpack_charger.jpg", 0.08)
            charger.position = (60, y)
            y -= 90
            self.scene.add_sprite("backpack_charger", charger)
            self.backpack_list.append({
                "sprite": charger,
                "name": "backpack_charger",
                "click": False
            })
            self.sprite_list.append(charger)

        if(not backpack[5]["display"]):
            red_pen = arcade.Sprite("img/backpack/backpack_red pen.jpg", 0.08)
            red_pen.position = (60, y)
            y -= 90
            self.scene.add_sprite("backpack_red_pen", red_pen)
            self.backpack_list.append({
                "sprite": red_pen,
                "name": "backpack_red_pen",
                "click": False
            })
            self.sprite_list.append(red_pen)

    def on_show(self):
        self.setup()
        virtual_memory = psutil.virtual_memory()
        used_memory_percentage = virtual_memory.percent
        # print(f"in corner, Current memory usage: {used_memory_percentage}%")

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("corner", 500, 325)
        # background
        utils.draw_background()
        
        # background and control
        self.scene["Background"].draw()
        self.scene["Control"].draw()
        
        # items
        last_draw = None
        for i in range(len(self.item_list)):
            item = self.item_list[i]["sprite"]
            name = self.item_list[i]["name"]
            if(self.item_list[i]["show big"]):
                last_draw = item
            elif(display_items[name]):
                item.draw()
        if(last_draw):
            last_draw.draw()

        if(self.item_list[0]["show big"] and display_items["red_pen_box"] == 1):
            self.scene["word"].draw()
        if(self.item_list[1]["show big"] and display_items["phone"] == 1):
            self.scene["arrow"].draw()

        # backpack
        if(self.has_backpack):
            self.scene["Backpack"].draw()

        if(not self.has_charger and backpack[2]["display"] == 1):
            self.scene["backpack_charger"].draw()

        if(not self.has_red_pen and backpack[5]["display"] == 1):
            self.scene["backpack_red_pen"].draw()

        # debug
        # for i in range(len(self.item_list)):
        #     item = self.item_list[i]["sprite"]
        #     name = self.item_list[i]["name"]
        #     if(display_items[name]):
        #         item.draw_hit_box(arcade.color.BLUE, 2)
        #         arcade.draw_point(item.left, item.top, arcade.color.RED, 10)
        #         arcade.draw_point(item.right, item.bottom, arcade.color.RED, 10)

        arcade.finish_render()

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        click = False
        box = self.item_list[0]["sprite"]
        phone = self.item_list[1]["sprite"]

        # exist box
        if(self.item_list[0]["show big"] and not box.collides_with_point((x, y))):
            box.texture = arcade.load_texture("img/items/corner_box.jpg")
            box.hit_box = box.texture.hit_box_points
            box.scale = 0.24
            box.position = (820, 314)
            self.pre_action = None
            self.item_list[0]["show big"] = False
            click  = True
            # init password
            for i in range(3):
                self.box_pw[i] = 0
                self.word_list[i]["sprite"].texture = arcade.load_texture("img/items/corner_box0.jpg")
            if(backpack[5]["display"] == 0 and display_items["red_pen_box"] == 2):
                backpack[5]["display"] = True
        
        # exist phone
        elif(self.item_list[1]["show big"] and not phone.collides_with_point((x, y))):
            phone.texture = arcade.load_texture("img/items/corner_phone.jpg")
            phone.hit_box = phone.texture.hit_box_points
            phone.scale = 0.12
            phone.position = (410, 240)
            self.pre_action = None
            self.item_list[1]["show big"] = False
            click  = True
            if(display_items["phone"] == 1):
                # init password
                for i in range(3):
                    self.arrow_list[i]["sprite"].angle = 180
                    self.phone_pw[i] = 180
            elif(backpack[2]["display"] == 0 and display_items["phone"] == 4):
                # get charger
                backpack[2]["display"] = True

        # click box (DFS open box, get red pen)
        elif(not self.item_list[1]["show big"] and box.collides_with_point((x, y))):
            # 解謎
            if(display_items["red_pen_box"] == 1):
                big = arcade.load_texture("img/items/corner_box_close.jpg")
                for i in range(3):
                    if(self.word_list[i]["sprite"].collides_with_point((x, y))):
                        idx = (self.word_list[i]["char"] + 1) % 5
                        self.word_list[i]["char"] = idx
                        self.box_pw[i] = idx
                        self.word_list[i]["sprite"].texture = arcade.load_texture(f"img/items/corner_box{idx}.jpg")

                correct = True
                ans = [1, 2, 4]
                for i in range(3):
                    if(self.box_pw[i] != ans[i]):
                        correct = False
                        break
                if(correct):
                    display_items["red_pen_box"] = 2
                    big = arcade.load_texture("img/items/corner_box_open.jpg")
            # 已解密
            else:
                big = arcade.load_texture("img/items/corner_box_open.jpg")
            box.texture = big
            box.hit_box = box.texture.hit_box_points
            box.scale = 0.55
            box.position = (560, 325)
            self.pre_action = "click box"
            self.item_list[0]["show big"] = True

        # phone 解謎
        elif(self.item_list[1]["show big"] and phone.collides_with_point((x, y))):
            # 解密
            if(display_items["phone"] == 1):
                for i in range(3):
                    arrow = self.arrow_list[i]["sprite"]
                    if(arrow.collides_with_point((x, y))):
                        arrow.angle = (arrow.angle - 90 ) % 360
                        self.phone_pw[i] = arrow.angle
                correct = True
                ans = [90, 0, 270]
                for i in range(3):
                    if(self.phone_pw[i] != ans[i]):
                        correct = False
                        break
                if(correct):
                    display_items["phone"] = 2
                    phone.texture = arcade.load_texture("img/items/corner_phone_1.jpg")

            elif(display_items["phone"] == 2):
                display_items["phone"] = 3
                phone.texture = arcade.load_texture("img/items/corner_phone_2.jpg")
            elif(display_items["phone"] == 3):
                display_items["phone"] = 4
                phone.texture = arcade.load_texture("img/items/corner_charger_big.jpg")

        # click phone
        elif(not self.item_list[0]["show big"] and phone.collides_with_point((x, y))):
            # 解密
            if(display_items["phone"] == 1):
                big = arcade.load_texture("img/items/corner_phone_lock.jpg")
            # 已解密
            elif(display_items["phone"] == 2):
                display_items["phone"] = 3
                big = arcade.load_texture("img/items/corner_phone_2.jpg")
            elif(display_items["phone"] == 3):
                display_items["phone"] = 4
                big = arcade.load_texture("img/items/corner_charger_big.jpg")
            else:
                big = arcade.load_texture("img/items/corner_charger_big.jpg")
            phone.texture = big
            phone.hit_box = phone.texture.hit_box_points
            phone.scale = 0.55
            phone.position = (560, 325)
            self.pre_action = "click phone"
            self.item_list[1]["show big"] = True

        # click item in backpack
        for i in range(len(self.backpack_list)):
            item = self.backpack_list[i]["sprite"]
            name = self.backpack_list[i]["name"]
            if(self.pre_action == "click " + self.backpack_list[i]["name"] and not item.collides_with_point((x, y))):
                item.scale = 0.08
                self.pre_action = None

            elif(item.collides_with_point((x, y))):
                if(self.pre_action and self.pre_action.startswith("click")):
                    for j in range(len(self.backpack_list)):
                        if("click " + self.backpack_list[j]["name"] == self.pre_action):
                            self.backpack_list[j]["sprite"].scale = 0.08
                            break
                item.scale = 0.1
                self.pre_action = "click " + self.backpack_list[i]["name"]

        # press control?
        is_ctl = utils.press_control(x, y, self.direction)
        if(not click and is_ctl != -1):
            # go back
            if(is_ctl == 1):
                # release resources
                for sp in self.sprite_list:
                    del sp
                arcade.cleanup_texture_cache()
                gc.collect()
                virtual_memory = psutil.virtual_memory()
                used_memory_percentage = virtual_memory.percent
                # print(f"Current memory usage: {used_memory_percentage}%")
                nxt_view = Blackboard()
                self.window.show_view(nxt_view)
            # default, should not happend
            else:
                print(f"in function on_mouse_press, x = {x}, y = {y}, dir = {is_ctl}")

    def on_key_press(self, key: int, modifiers: int):
        if(key == arcade.key.A):
            nxt_view = Classroom()
            self.window.show_view(nxt_view)
        elif(key == arcade.key.B):
            nxt_view = Blackboard()
            self.window.show_view(nxt_view)
        elif(key == arcade.key.C):
            nxt_view = Door()
            self.window.show_view(nxt_view)
        elif(key == arcade.key.D):
            nxt_view = Stage()
            self.window.show_view(nxt_view)
        elif(key == arcade.key.E):
            nxt_view = Corner()
            self.window.show_view(nxt_view)
        elif(key == arcade.key.F):
            nxt_view = Table()
            self.window.show_view(nxt_view)

class Table(arcade.View):
    def __init__(self):
        super().__init__()
        self.scene = arcade.Scene()
        self.direction = [False, True, False, False]  # 紀錄前後左右是否可以到達別的場景
        self.sprite_list = arcade.SpriteList()
        
        # record item's data
        self.item_list = []     # a list to store the data of the items in the scene
        self.backpack_list = [] # a list to store the data of the items in the backpack
        self.word_list = []         # computer password sprites (B, D, F, J, S)

        self.pre_action = None      # previous action (click item, take from backpack...)
        self.has_backpack = False
        self.password = [0, 0, 0]   # "B": 0, "D": 1, "F": 2, "J":3, "S":4
        self.room = "114"
        
    def setup(self):
        # background
        init = "img/background/table_init.jpg"
        bg = arcade.Sprite(init, 0.68)
        bg.center_x = 560
        bg.center_y = 325
        self.scene.add_sprite("Background", bg)
        self.sprite_list.append(bg)

        # control
        arrow_down = arcade.Sprite("img/control/arrow_down.png", CONTROL_SCALING)
        arrow_down.center_x = 560
        arrow_down.center_y = 30
        arrow_down.alpha = CONTROL_ALPHA
        self.scene.add_sprite("Control", arrow_down)
        self.sprite_list.append(arrow_down)

        # items
        computer = arcade.Sprite("img/items/table_computer.jpg", 0.33)
        computer.position = (358, 489)
        self.scene.add_sprite("Items", computer)
        self.item_list.append({
            "sprite": computer,
            "name": "oj_computer",
            "show big": False
        })
        self.sprite_list.append(computer)

        name_list = arcade.Sprite("img/items/table_點名表.jpg", 0.23)
        name_list.position = (655, 250)
        self.scene.add_sprite("Items", name_list)
        self.item_list.append({
            "sprite": name_list,
            "name": "name_list",
            "show big": False
        })
        self.sprite_list.append(name_list)

        if(display_items["drink"] == 2):
            drink = arcade.Sprite("img/items/table_打翻_密碼.jpg", 0.35)
            drink.position = (790, 470)
        else:
            drink = arcade.Sprite("img/items/table_打翻.jpg", 0.18)
            drink.position = (840, 470)
        self.scene.add_sprite("Items", drink)
        self.item_list.append({
            "sprite": drink,
            "name": "drink",
            "show big": False
        })
        self.sprite_list.append(drink)

        # backpack
        y = 550
        for i in range(len(backpack)):
            item = backpack[i]
            # should show in backpack, create its sprite
            if(item["display"] == 1):
                sp = arcade.Sprite(item["path"], 0.08)
                sp.position = (60, y)
                y -= 90
                if(item["name"] == "rag"):
                    self.scene.add_sprite("rag", sp)
                elif(item["name"] == "charger"):
                    self.scene.add_sprite("charger", sp)
                else:
                    self.scene.add_sprite("Backpack", sp)
                    self.has_backpack = True
                self.backpack_list.append({
                    "sprite": sp,
                    "name": item["name"],
                    "click": False
                })
                self.sprite_list.append(sp)

    def on_show(self):
        self.setup()
        virtual_memory = psutil.virtual_memory()
        used_memory_percentage = virtual_memory.percent
        # print(f"in table, Current memory usage: {used_memory_percentage}%")

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("table", 500, 325)
        # background
        utils.draw_background()

        # background and control
        self.scene["Background"].draw()
        self.scene["Control"].draw()
        
        # items
        last_draw = None
        for i in range(len(self.item_list)):
            item = self.item_list[i]["sprite"]
            name = self.item_list[i]["name"]
            if(self.item_list[i]["show big"]):
                last_draw = item
            elif(display_items[name]):
                item.draw()
        if(last_draw):
            last_draw.draw()

        # backpack
        if(self.has_backpack):
            self.scene["Backpack"].draw()
        if(backpack[0]["display"] == 1):
            self.scene["rag"].draw()
        if(backpack[2]["display"] == 1):
            self.scene["charger"].draw()

        # debug
        # for i in range(len(self.item_list)):
        #     item = self.item_list[i]["sprite"]
        #     name = self.item_list[i]["name"]
        #     if(display_items[name]):
        #         item.draw_hit_box(arcade.color.BLUE, 2)
        #         arcade.draw_point(item.left, item.top, arcade.color.RED, 10)
        #         arcade.draw_point(item.right, item.bottom, arcade.color.RED, 10)

        arcade.finish_render()

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        computer = self.item_list[0]["sprite"]
        name_list = self.item_list[1]["sprite"]
        drink = self.item_list[2]["sprite"]

        # exist computer
        if(self.item_list[0]["show big"] and not computer.collides_with_point((x, y))):
            computer.texture = arcade.load_texture("img/items/table_computer.jpg")
            computer.hit_box = computer.texture.hit_box_points
            computer.scale = 0.33
            computer.position = (358, 489)
            self.item_list[0]["show big"] = False

        # exist name_list
        elif(self.item_list[1]["show big"] and not name_list.collides_with_point((x, y))):
            name_list.texture = arcade.load_texture("img/items/table_點名表.jpg")
            name_list.hit_box = name_list.texture.hit_box_points
            name_list.scale = 0.23
            name_list.position = (655, 250)
            self.item_list[1]["show big"] = False

        # exist drink
        elif(self.item_list[2]["show big"] and not drink.collides_with_point((x, y))):
            if(display_items["drink"] == 2):
                drink.texture = arcade.load_texture("img/items/table_打翻_密碼.jpg")
                drink.scale = 0.35
                drink.position = (790, 470)
            else:
                drink.texture = arcade.load_texture("img/items/table_打翻.jpg")
                drink.scale = 0.18
                drink.position = (840, 470)
            drink.hit_box = drink.texture.hit_box_points
            self.item_list[2]["show big"] = False
            
        # click computer
        elif(computer.collides_with_point((x, y))):
            if(self.pre_action == "click charger"):
                big = arcade.load_texture("img/items/table_computer_大oj.jpg")
                display_items["oj_computer"] = 2
                backpack[2]["display"] = 2
            elif(display_items["oj_computer"] == 2):
                big = arcade.load_texture("img/items/table_computer_大oj.jpg")
            else:
                big = arcade.load_texture("img/items/table_computer_大沒電.jpg")

            computer.texture = big
            computer.hit_box = computer.texture.hit_box_points
            computer.scale = 0.55
            computer.position = (560, 325)
            self.item_list[0]["show big"] = True

        # click name_list
        elif(name_list.collides_with_point((x, y))):
            name_list.texture = arcade.load_texture("img/items/table_點名表_大.jpg")
            name_list.hit_box = name_list.texture.hit_box_points
            name_list.scale = 0.55
            name_list.position = (560, 325)
            self.item_list[1]["show big"] = True

        # click drink
        elif(drink.collides_with_point((x, y))):
            if(self.pre_action == "click rag"):
                big = arcade.load_texture("img/items/table_打翻_大乾.jpg")
                display_items["drink"] = 2
                backpack[0]["display"] = 2
            elif(display_items["drink"] == 2):
                big = arcade.load_texture("img/items/table_打翻_大乾.jpg")
            else:
                big = arcade.load_texture("img/items/table_打翻_大水.jpg")
            drink.texture = big
            drink.hit_box = drink.texture.hit_box_points
            drink.scale = 0.55
            drink.position = (560, 325)
            self.item_list[2]["show big"] = True

        # press control?
        is_ctl = utils.press_control(x, y, self.direction)
        if(is_ctl != -1):
            # go back
            if(is_ctl == 1):
                # release resources
                for sp in self.sprite_list:
                    del sp
                arcade.cleanup_texture_cache()
                gc.collect()
                virtual_memory = psutil.virtual_memory()
                used_memory_percentage = virtual_memory.percent
                # print(f"Current memory usage: {used_memory_percentage}%")
                nxt_view = Classroom()
                self.window.show_view(nxt_view)
            # default, should not happend
            else:
                print(f"in function on_mouse_press, x = {x}, y = {y}, dir = {is_ctl}")

        # click item in backpack
        for i in range(len(self.backpack_list)):
            item = self.backpack_list[i]["sprite"]
            if(self.pre_action == "click " + self.backpack_list[i]["name"] and not item.collides_with_point((x, y))):
                item.scale = 0.08
                self.pre_action = None

            elif(item.collides_with_point((x, y))):
                if(self.pre_action and self.pre_action.startswith("click")):
                    for j in range(len(self.backpack_list)):
                        if("click " + self.backpack_list[j]["name"] == self.pre_action):
                            self.backpack_list[j]["sprite"].scale = 0.08
                            break
                item.scale = 0.1
                self.pre_action = "click " + self.backpack_list[i]["name"]

    def on_key_press(self, key: int, modifiers: int):
        if(key == arcade.key.A):
            nxt_view = Classroom()
            self.window.show_view(nxt_view)
        elif(key == arcade.key.B):
            nxt_view = Blackboard()
            self.window.show_view(nxt_view)
        elif(key == arcade.key.C):
            nxt_view = Door()
            self.window.show_view(nxt_view)
        elif(key == arcade.key.D):
            nxt_view = Stage()
            self.window.show_view(nxt_view)
        elif(key == arcade.key.E):
            nxt_view = Corner()
            self.window.show_view(nxt_view)
        elif(key == arcade.key.F):
            nxt_view = Table()
            self.window.show_view(nxt_view)


def main114():
    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main114()