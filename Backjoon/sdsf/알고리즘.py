n, m = map(int, input().split())

board = []
for i in range(n):
    board.append(input())

list = []
for i in range(m-7):
    for j in range(n-7):
        index1 = 0
        index2 = 0
        for x in range(i, i+8):
            for y in range(j, j+8):
                if (i+y)%2 == 0:
                    if board[x][y] != "W":
                        index1 += 1
                    else:
                        index2 += 1
                else:
                    if board[x][y] != "B":
                        index1 += 1
                    else:
                        index2 += 1
        list.append(index1, index2)
print(min(list))
