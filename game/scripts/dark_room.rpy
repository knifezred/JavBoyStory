label dark_room:
    scene bg room
    "这是一间小黑屋"
    "你快要冻死了"
    menu optional_name:
        "你决定去寻找木材"
        "四处翻找":
            "你找到了一些木材"
            jump game_end_good
            #block of code to run
        "出门查看":
            "你被冻死了"
            jump game_end
            #block of code to run
