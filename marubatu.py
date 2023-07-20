import numpy as np
import random
#変数宣言、初期化
table = np.array([[[0 , 0 , 0],
                   [0 , 0 , 0],
                   [0 , 0 , 0]],

                  [[0 , 0 , 0],
                   [0 , 0 , 0],
                   [0 , 0 , 0]],

                  [[0 , 0 , 0],
                   [0 , 0 , 0],
                   [0 , 0 , 0]]])

py = np.array([[[0 , 0 , 0],
                [0 , 0 , 0],
                [0 , 0 , 0]],

               [[0 , 0 , 0],
                [0 , 0 , 0],
                [0 , 0 , 0]],

               [[0 , 0 , 0],
                [0 , 0 , 0],
                [0 , 0 , 0]]])

cpu = np.array([[[0 , 0 , 0],
                 [0 , 0 , 0],
                 [0 , 0 , 0]],

                [[0 , 0 , 0],
                 [0 , 0 , 0],
                 [0 , 0 , 0]],

                [[0 , 0 , 0],
                 [0 , 0 , 0],
                 [0 , 0 , 0]]])

player():
    x = input("x座標(1~3)を入力")
    y = input("y座標(1~3)を入力")
    z = input("z座標(1~3)を入力")
    if(cpu == py):
        print("CPUと重なっています\n")
        print("もう一度やり直してください\n")
        player()

    if(1 <= x && x <= 3):
        if(1 <= y && y <= 3):
            if(1 <= z && z <= 3):
                py[x - 1][y - 1 ][z - 1] = 1
                table = py
    else:
        print("もう一度やり直してください\n")
        player()

return 0

computer():
    x = random.randrange(3)
    y = random.randrange(3)
    z = random.randrange(3)
    if(cpu != py):
        cpu[x][y][z] = 1
        table = cpu
    else:
        computer()

return 0
