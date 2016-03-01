from WriteMapToFile import write_3d_map_to_file
import math


def generate_free_map(depth):
    width = 2**depth
    map = [[[0 for i in range(width)] for i in range(width)] for i in range(width)]
    return map


def main():
    write_3d_map_to_file(generate_free_map(1), (1000, 1000, 1000), 'test_freemapdepth1.txt')

    map = generate_free_map(2)
    freeCells = [(3, 2, 1), (2, 2, 1), (2, 1, 1), (1, 1, 0), (1, 0, 0), (0, 0, 0)]
    for x in range(len(map)):
        for y in range(len(map[0])):
            for z in range(len(map[0][0])):
                if (x, y, z) not in freeCells:
                    map[x][y][z] = 1

    write_3d_map_to_file(map, (1000, 1000, 1000), 'test_3Dlineofsightcase1.txt')


if __name__ == '__main__':
    main()