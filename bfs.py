direction = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 模拟上下左右四个搜索方向
matrix = [[],[]]
i, j = 0, 0  # 搜索的起始位置

def bfs(i, j):

    if i, j 满足某种条件:    # 有明确终点时使用，可有可无
        return

    queue = [[i, j]]  #本轮搜索的所有父端点的序列，一开始是(i,j)

    while len(queue) > 0:  #探索所有父端点序列
        x, y = queue.pop(0)

        for direction_X, direction_Y in direction:   #对于一个父端点下的所有子端点
            new_X = x + direction_X
            new_Y = y + direction_Y

            # 可通过改变和筛选matrix[new_X, new_Y]的值来避免重复或逆向搜索
            if new_X, new_Y, matrix[new_X, new_Y] 满足某种条件:
                #进行操作
                queue.append([new_X, new_Y])  # 将合适的子端点放入搜索序列

bfs(i, j)
