import arcade

'''
draw the background
'''
def draw_background():
    # background
    arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    # 背包背景
    arcade.draw_rectangle_filled(60, 325, 120, 650, arcade.color.ARMY_GREEN)
    arcade.draw_rectangle_filled(60, 325, 100, 630, arcade.color.AVOCADO)
    arcade.draw_rectangle_filled(60, 620, 80, 30, arcade.color.APPLE_GREEN)
    arcade.draw_text("背包", 35, 610, arcade.color.BLACK, 16)

'''
Tell which control img is clicked
Parameter:
    x, y: the position of the mouse
    direction: the bool list that record whether this scene can go to each direction
Return:
    (int) dir: which direction is clicked
    0: should not happen
    1: down(back)
    2: left
    3: right
    -1: doesn't click on control
'''
def press_control(x, y, direction):
    CONTROL_COR = [[-100, -100], [540, 10], [140, 10], [940, 10]]
    for i in range(4):
        if( direction[i] and                                            # can go this direction
            x >= CONTROL_COR[i][0] and x <= CONTROL_COR[i][0]+40 and
            y >= CONTROL_COR[i][1] and y<= CONTROL_COR[i][1]+40):
            return i
    return -1    # doesn't click on control