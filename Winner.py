

def winner(chessboard):
    #横方向
    for i in range(15):
        for j in range(0,11):
            if chessboard[i][j]==chessboard[i][j+1]==chessboard[i][j+2]==chessboard[i][j+3]==chessboard[i][j+4]==1:
                return 1
            if chessboard[i][j]==chessboard[i][j+1]==chessboard[i][j+2]==chessboard[i][j+3]==chessboard[i][j+4]==2:
                return 2

    #竖方向
    for j in range(15):
        for i in range(0, 11):
            if chessboard[i][j] ==chessboard[i+1][j]==chessboard[i+2][j]==chessboard[i+3][j]==chessboard[i+4][j] ==1:
                return 1
            if chessboard[i][j] ==chessboard[i+1][j]==chessboard[i+2][j]==chessboard[i+3][j]==chessboard[i+4][j] ==2:
                return 2
    #右斜
    for  i in range(4,15):
        for j in range(11):
            if chessboard[i][j] == chessboard[i -1][j+1] == chessboard[i -2][j+2] == chessboard[i - 3][j+3] == \
                    chessboard[i - 4][j+4] == 1:
                return 1
            if chessboard[i][j] == chessboard[i -1][j+1] == chessboard[i -2][j+2] == chessboard[i - 3][j+3] == \
                    chessboard[i - 4][j+4] == 2:
                return 2

    # 左斜
    for i in range(10,-1,-1):
        for j in range(11):
            if chessboard[i][j] == chessboard[i + 1][j + 1] == chessboard[i + 2][j + 2] == chessboard[i + 3][j + 3] == \
                    chessboard[i + 4][j + 4] == 1:
                return 1
            if chessboard[i][j] == chessboard[i + 1][j + 1] == chessboard[i + 2][j + 2] == chessboard[i + 3][j + 3] == \
                    chessboard[i + 4][j + 4] == 2:
                return 2
    return 0