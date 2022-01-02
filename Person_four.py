

def P_toWin(chessboard):
    #横方向
    for i in range(15):
        for j in range(0,10):
            if chessboard[i][j]== 0 and chessboard[i][j+1]==chessboard[i][j+2]==chessboard[i][j+3]==chessboard[i][j+4]==1 and chessboard[i][j+5]== 0:
                return i,j
            if chessboard[i][j]== 0 and chessboard[i][j+1]==chessboard[i][j+2]==chessboard[i][j+3]==chessboard[i][j+4]==1 and chessboard[i][j+5]== 2:
                return i,j
            if chessboard[i][j]== 2 and chessboard[i][j+1]==chessboard[i][j+2]==chessboard[i][j+3]==chessboard[i][j+4]==1 and chessboard[i][j+5]== 0:
                return i,j+5


    #竖方向
    for j in range(15):
        for i in range(0, 10):
            if chessboard[i][j] == 0 and chessboard[i+1][j]==chessboard[i+2][j]==chessboard[i+3][j]==chessboard[i+4][j] ==1 and chessboard[i+5][j] == 0 :
                return i+5,j
            if chessboard[i][j] == 2 and chessboard[i+1][j]==chessboard[i+2][j]==chessboard[i+3][j]==chessboard[i+4][j] ==1 and chessboard[i+5][j] == 0 :
                return i+5,j
            if chessboard[i][j] == 0 and chessboard[i+1][j]==chessboard[i+2][j]==chessboard[i+3][j]==chessboard[i+4][j] ==1 and chessboard[i+5][j] == 2 :
                return i,j

    #右斜
    for  i in range(5,15):
        for j in range(10):
            if chessboard[i][j] == 0 and chessboard[i -1][j+1] == chessboard[i -2][j+2] == chessboard[i - 3][j+3] == \
                    chessboard[i - 4][j+4] == 1 and chessboard[i-5][j+5] == 0:
                return i,j
            if chessboard[i][j] == 0 and chessboard[i -1][j+1] == chessboard[i -2][j+2] == chessboard[i - 3][j+3] == \
                    chessboard[i - 4][j+4] == 1 and chessboard[i-5][j+5] == 2:
                return i,j
            if chessboard[i][j] == 2 and chessboard[i -1][j+1] == chessboard[i -2][j+2] == chessboard[i - 3][j+3] == \
                    chessboard[i - 4][j+4] == 1 and chessboard[i-5][j+5] == 0:
                return i-5,j+5


    # 左斜
    for i in range(9,-1,-1):
        for j in range(10):
            if chessboard[i][j] ==0 and chessboard[i + 1][j + 1] == chessboard[i + 2][j + 2] == chessboard[i + 3][j + 3] == \
                    chessboard[i + 4][j + 4] == 1 and chessboard[i+5][j+5] ==0:
                return i+5,j+5
            if chessboard[i][j] ==2 and chessboard[i + 1][j + 1] == chessboard[i + 2][j + 2] == chessboard[i + 3][j + 3] == \
                    chessboard[i + 4][j + 4] == 1 and chessboard[i+5][j+5] ==0:
                return i+5,j+5
            if chessboard[i][j] ==0 and chessboard[i + 1][j + 1] == chessboard[i + 2][j + 2] == chessboard[i + 3][j + 3] == \
                    chessboard[i + 4][j + 4] == 1 and chessboard[i+5][j+5] ==2:
                return i,j

    return -1,-1

def AI_toWin(chessboard):
    #横方向
    for i in range(15):
        for j in range(0,10):
            if chessboard[i][j]== 0 and chessboard[i][j+1]==chessboard[i][j+2]==chessboard[i][j+3]==chessboard[i][j+4]==2 and chessboard[i][j+5]== 0:
                return i,j
            if chessboard[i][j]== 1 and chessboard[i][j+1]==chessboard[i][j+2]==chessboard[i][j+3]==chessboard[i][j+4]==2 and chessboard[i][j+5]== 0:
                return i,j+5
            if chessboard[i][j]== 0 and chessboard[i][j+1]==chessboard[i][j+2]==chessboard[i][j+3]==chessboard[i][j+4]==2 and chessboard[i][j+5]== 1:
                return i,j


    #竖方向
    for j in range(15):
        for i in range(0, 10):
            if chessboard[i][j] == 0 and chessboard[i+1][j]==chessboard[i+2][j]==chessboard[i+3][j]==chessboard[i+4][j] ==2 and chessboard[i+5][j] == 0 :
                return i+5,j
            if chessboard[i][j] == 1 and chessboard[i+1][j]==chessboard[i+2][j]==chessboard[i+3][j]==chessboard[i+4][j] ==2 and chessboard[i+5][j] == 0 :
                return i+5,j
            if chessboard[i][j] == 0 and chessboard[i+1][j]==chessboard[i+2][j]==chessboard[i+3][j]==chessboard[i+4][j] ==2 and chessboard[i+5][j] == 1 :
                return i,j

    #右斜
    for  i in range(5,15):
        for j in range(10):
            if chessboard[i][j] == 0 and chessboard[i -1][j+1] == chessboard[i -2][j+2] == chessboard[i - 3][j+3] == \
                    chessboard[i - 4][j+4] == 2 and chessboard[i-5][j+5] == 0:
                return i,j
            if chessboard[i][j] == 0 and chessboard[i -1][j+1] == chessboard[i -2][j+2] == chessboard[i - 3][j+3] == \
                    chessboard[i - 4][j+4] == 2 and chessboard[i-5][j+5] == 1:
                return i,j
            if chessboard[i][j] == 1 and chessboard[i -1][j+1] == chessboard[i -2][j+2] == chessboard[i - 3][j+3] == \
                    chessboard[i - 4][j+4] == 2 and chessboard[i-5][j+5] == 0:

                return i-5,j+5


    # 左斜
    for i in range(9,-1,-1):
        for j in range(10):
            if chessboard[i][j] ==0 and chessboard[i + 1][j + 1] == chessboard[i + 2][j + 2] == chessboard[i + 3][j + 3] == \
                    chessboard[i + 4][j + 4] == 2 and chessboard[i+5][j+5] ==0:
                return i+5,j+5
            if chessboard[i][j] ==1 and chessboard[i + 1][j + 1] == chessboard[i + 2][j + 2] == chessboard[i + 3][j + 3] == \
                    chessboard[i + 4][j + 4] == 2 and chessboard[i+5][j+5] ==0:
                return i+5,j+5
            if chessboard[i][j] ==0 and chessboard[i + 1][j + 1] == chessboard[i + 2][j + 2] == chessboard[i + 3][j + 3] == \
                    chessboard[i + 4][j + 4] == 2 and chessboard[i+5][j+5] ==1:

                return i,j

    return -1,-1