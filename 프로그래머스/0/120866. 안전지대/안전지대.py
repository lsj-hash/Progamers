def solution(board):
    n = len(board)
    m = len(board[0])
    danger = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                for x in range(max(0,i-1), min(n,i+2)):
                    for y in range(max(0,j-1), min(m,j+2)):
                        danger[x][y] = 1
    answer = sum(danger[i][j]==0 for i in range(n) for j in range(m))
    return answer
