import random
from WriteMapToFile import write_2d_map_to_file


def generate_map(depth, resolution, percentage_occupied_cells, seed, file_name):

    width = 2**depth
    num_of_objects = int(width * width * percentage_occupied_cells / 100)
    random.seed(seed)

    object_pos = []

    for i in range(num_of_objects):
        x = random.randrange(width)
        y = random.randrange(width)

        while (x, y) in object_pos:
            x = random.randrange(width)
            y = random.randrange(width)

        object_pos.append((x, y))

    map = generate_free_map(depth)

    for obj in object_pos:
        map[obj[0]][obj[1]] = 1

    write_2d_map_to_file(map, resolution, file_name)


def generate_free_map(depth):
    width = 2**depth
    map = [[0 for i in range(width)] for i in range(width)]
    return map


def main():
    # generate a free map
    depth = 6
    generate_map(depth, (1, 1), 60, 1, "mapdepth6obs60")


if __name__ == '__main__':
    main()
