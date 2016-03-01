from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


def main():
    data = read_map_from_file('3dmapdepth4.txt')
    map = data[0]
    res = data[1]
    visualize_map(map, res)


def read_map_from_file(file_name):
    f = open(file_name, 'r')
    line = f.readline()

    # read depth
    depth = int(line)
    width = 2**depth

    # read resolution
    line = f.readline()
    resolution = [int(i) for i in line.split()]

    map = [[[0 for i in range(width)] for i in range(width)] for i in range(width)]
    line = f.readline()
    while line:
        data = [int(i) for i in line.split()]
        map[data[0]][data[1]][data[2]] = data[3]
        line = f.readline()

    f.close()

    return map, resolution


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


if __name__ == '__main__':
    main()