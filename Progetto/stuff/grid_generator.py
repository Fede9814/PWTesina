import arcade
import path
import random

boundaries = 0
roads = 3
inputs = 1
outputs = 2
traffic_lights = 4


def grid_creator(map_heigth, map_width):
    #map is an array
    Terrain_grid = []
    #iterate for heigth
    for row in range(map_heigth):
        #and append
        Terrain_grid.append([])
        #iterate for length
        for column in range(map_width):
            #if value in i[value] for row AND column is EVEN then: 
            if column % 2 == 1 and row % 2 == 1:

                Terrain_grid[row].append(boundaries)
            elif column == 0 or row == 0 or column == map_width - 1 or row == map_heigth - 1:
                Terrain_grid[row].append(roads)
            else:
                Terrain_grid[row].append(roads)
        return Terrain_grid


def make_maze_depth_first(maze_width, maze_height):

#maze diventa un array, dove applico la logica di 
    maze = grid_creator(maze_width, maze_height)

    w = (len(maze[0]) - 1) // 2
    h = (len(maze) - 1) // 2
    vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]

    def walk(x: int, y: int):
        vis[y][x] = 1

        d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        random.shuffle(d)
        for (xx, yy) in d:
            if vis[yy][xx]:
                continue
            if xx == x:
                maze[max(y, yy) * 2][x * 2 + 1] = boundaries
            if yy == y:
                maze[y * 2 + 1][max(x, xx) * 2] = boundaries

            walk(xx, yy)

    walk(random.randrange(w), random.randrange(h))

    return maze