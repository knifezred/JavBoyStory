# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

define sister = Character("姐姐")
define ai = Character("小爱")


# 游戏在此开始。

label start:

    jump dark_room

    # 显示一个背景。此处默认显示占位图，但您也可以在图片目录添加一个文件
    # （命名为 bg room.png 或 bg room.jpg）来显示。

    scene bg room

    # 显示角色立绘。此处使用了占位图，但您也可以在图片目录添加命名为
    # eileen happy.png 的文件来将其替换掉。


    # 此处显示各行对话。

    "一间寒冷的木屋"

    "火堆快要熄灭了"

    # show ai normal

    ai "您已创建一个新的 Ren'Py 游戏。"

    ai "当您完善了故事、图片和音乐之后，您就可以向全世界发布了！"

    # 此处为游戏结尾。
    jump game_end
    return

label game_end:
    jump game_end_bad
    return

label game_end_bad:

    "游戏结束了，显示你什么都没做"
    return

label game_end_good:

    "游戏结束了，你做的不错、撑过了一些时日"
    return