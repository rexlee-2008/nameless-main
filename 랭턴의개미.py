n = int(input())

maze = []

for i in range(10):
    maze.append([0] * 10)

color = [1, 0]
direct = [[0, 1], [-1, 0], [0, -1], [1, 0]]
ant_x = 5
ant_y = 5
v = 3

for i in range(1000):
    
    if maze[ant_x][ant_y] == 1:
        v -= 1
        if v == -1:
            v = 3
    else:
        v += 1
        if v == 4:
            v = 0
    now_color = maze[ant_x][ant_y]
    
    ant_x += direct[v][0]
    ant_y += direct[v][1]
    
    maze[ant_x][ant_y] = color[now_color]
    
    for i in maze:
        print(i)
    
    print()
    print()

    