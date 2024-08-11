# states: 0: not display, 1: display, 2: used
item_list = {
    "mainTheme": [
        {
        "name": "drawer",
        "sprite": None,
        "state": 0, # 0: small, 1: solved
        "display": False,
        "pathShow": "img/items/mainTheme/drawerShow.png",
        "pathEnd": "img/items/mainTheme/drawerEnd.png",
        "scale": 0.8,
        "place": "mainTheme",
        "x": 550,
        "y": 350
        },
        {
        "name": "rag",
        "sprite": None,
        "state": 0,
        "display": True,
        "pathSmall": "img/items/mainTheme/ragSmall.png",
        # "pathShow": "img/items/mainTheme/ragShow.png",
        "scale": 0.05,
        "place": "mainTheme",
        "x": 250,
        "y": 350
        },
    ],
    "doorRight": [
        {
        "name": "vase",
        "sprite": None,
        "state": 0, # 0: small, 1: break, 2: solved
        "display": True,
        "pathSmall": "img/items/doorRight/vaseSmall.png",
        "pathShow": "img/items/doorRight/vaseShow.png",
        "pathRes": "img/items/doorRight/vaseRes.png",
        "pathEnd": "img/items/doorRight/vaseEnd.png",
        "scale": 0.2,
        "place": "doorRight",
        "x": 185,
        "y": 170
        },
        {
        "name": "professorYen",
        "sprite": None,
        "state": 0,  # 0: small, 1: solved
        "display": True,
        "pathSmall": "img/items/doorRight/professorYenSmall.png",
        "pathShow": "img/items/doorRight/professorYenShow.jpg",
        "pathEnd": "img/items/doorRight/professorYenEnd.png",
        "scale": 0.2,
        "place": "doorRight",
        "x": 286,
        "y": 352}
    ],
    "doorLeft": [
        {
        "name": "box",
        "sprite": None,
        "state": 0,  # 0: small, 1: decoding, 2: finished decoding 3: get hammer
        "display": True,
        "pathSmall": "img/items/doorLeft/boxSmall.png",
        "pathShow": "img/items/doorLeft/boxShow.jpg",
        "pathRes": "img/items/doorLeft/hammer.png",
        "pathEnd": "img/items/doorLeft/boxShow.png",
        "scale": 0.1,
        "place": "doorLeft",
        "x": 250,
        "y": 200
        }
    ],
    "back": [
        {
        "name": "shell",
        "sprite": None,
        "state": 0,  # 0: small, 1: decoding, 2: finished decoding
        "display": True,
        "pathSmall": "img/items/back/shellSmall.png",
        "pathShow": "img/items/back/shellShow.png",
        "pathEnd": "img/items/back/shellEnd.png",
        "scale": 0.4,
        "place": "doorLeft",
        "x": 330,
        "y": 325
        }
    ],
    "front": [
    ]
}

backpack_list = [
    {
        "name": "flashlight",  # need to be changed into flashlight
        "sprite": None,
        "state": 0,
        "scale": 0.3,
        "display": False,
        "path": "img/items/doorRight/flashlight.png"
    },
    {
        "name": "hammer",
        "sprite": None,
        "state": 0,  # 0: not used, 1: used CURRENTLY NO USE
        "scale": 0.18,
        "display": False,
        "path": "img/items/doorLeft/hammer.png"
    }
]

control_list = [
    {
        "dir": "left",
        "path": "img/control/left.png",
        "x": 160,
        "y": 30
    },
    {
        "dir": "right",
        "path": "img/control/right.png",
        "x": 960,
        "y": 30
    },
    {
        "dir": "up",
        "path": "img/control/up.png",
        "x": 560,
        "y": 625
    },
    {
        "dir": "down",
        "path": "img/control/down.png",
        "x": 560,
        "y": 30
    }    
]

code_list = {
    "bookCode": [
        {
            "name": "book1",
            "path": "img/items/back/book1.png",
            "sp": None,
            "scale": 0.8
        },
        {
            "name": "book2",
            "path": "img/items/back/book2.png",
            "sp": None,
            "scale": 0.8
        },
        {
            "name": "book3",
            "path": "img/items/back/book3.png",
            "sp": None,
            "scale": 0.8
        },
        {
            "name": "book4",
            "path": "img/items/back/book4.png",
            "sp": None,
            "scale": 0.8
        },
        {
            "name": "book5",
            "path": "img/items/back/book5.png",
            "sp": None,
            "scale": 0.8
        },
    ],
}
