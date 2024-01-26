direction = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 模拟上下左右四个搜索方向
matrix = [[],[]]
i, j = 0, 0  # 搜索的起始位置

def bfs(i, j):

    queue = [[i, j]]  # 起点入队

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



迷宫问题答案：
n, m = list(map(int, input().split()))
maze = []
for i in range(n):
    maze.append(input().split())

path = {}
d = ((1,0),(-1,0),(0,1),(0,-1))
p = []

def bfs():
    maze[0][0] = '1'
    queue = [(0,0)]
    path[(0,0)] = None
    while len(queue) > 0:
        if queue[0] == (n-1,m-1):
            i = queue[0]
            p.append(i)
            while path[i]:
                p.append(path[i])
                i = path[i]
            while p:
                a = p.pop()
                print('({},{})'.format(a[0],a[1]))
            return
        x,y = queue.pop(0)
        for x_d, y_d in d:
            new_x = x + x_d
            new_y = y + y_d
            if 0 <= new_x < n and 0 <= new_y < m and maze[new_x][new_y] == '0':
                queue.append((new_x,new_y))
                maze[new_x][new_y] = '1'
                path[(new_x,new_y)] = (x,y)
bfs()
