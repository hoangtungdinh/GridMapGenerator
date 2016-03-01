import random
from WriteMapToFile import write_3d_map_to_file
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


def generate_map(depth, percentage_occupied_cells, seed):

    width = 2**depth
    num_of_objects = int(width**3 * percentage_occupied_cells / 100)
    random.seed(seed)

    object_pos = []

    for i in range(num_of_objects):
        x = random.randrange(width)
        y = random.randrange(width)
        z = random.randrange(width)

        while (x, y, z) in object_pos:
            x = random.randrange(width)
            y = random.randrange(width)
            z = random.randrange(width)

        object_pos.append((x, y, z))

    map = generate_free_map(depth)

    for obj in object_pos:
        map[obj[0]][obj[1]][obj[2]] = 1

    return map


def generate_free_map(depth):
    width = 2**depth
    map = [[[0 for i in range(width)] for i in range(width)] for i in range(width)]
    return map


def visualize_map(map, res):
    width = len(map)
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.set_aspect("equal")

    for x in range(width):
        for y in range(width):
            for z in range(width):
                if map[x][y][z] == 1:
                    draw_cube(ax, (x * res[0], y * res[1], z * res[2]), res[0], res[1], res[2])

    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')

    plt.show()


def draw_cube(ax, pos, size_x, size_y, size_z):
    X, Y = np.meshgrid([pos[0], pos[0] + size_x], [pos[1], pos[1] + size_x])
    ax.plot_surface(X, Y, pos[2], alpha=0.2)
    ax.plot_surface(X, Y, pos[2] + size_z, alpha=0.2)

    Y, Z = np.meshgrid([pos[1], pos[1] + size_y], [pos[2], pos[2] + size_z])
    ax.plot_surface(pos[0], Y, Z, alpha=0.2)
    ax.plot_surface(pos[0] + size_x, Y, Z, alpha=0.2)

    X, Z = np.meshgrid([pos[0], pos[0] + size_x], [pos[2], pos[2] + size_z])
    ax.plot_surface(X, pos[1], Z, alpha=0.2)
    ax.plot_surface(X, pos[1] + size_y, Z, alpha=0.2)


def main():
    # generate a free map
    depth = 8
    resolution = (1000, 1000, 1000)
    write_3d_map_to_file(generate_map(depth, 0, 1), resolution, "map/map0obs.txt")
    random.seed(1)
    seed_list = random.sample(range(1, 1000000), 180)
    percentage = [5, 10, 15, 20, 25, 30]

    for percent in percentage:
        for i in range(30):
            seed = seed_list.pop(0)
            file_name = 'map/map' + str(percent) + 'percent' + str(i) + '.txt'
            write_3d_map_to_file(generate_map(depth, percent, seed), resolution, file_name)


if __name__ == '__main__':
    main()
