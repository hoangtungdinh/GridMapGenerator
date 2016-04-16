import random
from WriteMapToFile import write_3d_map_to_file


def generate_map(depth, percentage_occupied_cells, seed, all_pos):
    width = 2 ** depth
    num_of_objects = int(width ** 3 * percentage_occupied_cells / 100)

    random.seed(seed)
    object_pos = random.sample(all_pos, num_of_objects)

    map = generate_free_map(depth)

    for obj in object_pos:
        map[obj[0]][obj[1]][obj[2]] = 1

    return map


def generate_free_map(depth):
    width = 2 ** depth
    map = [[[0 for i in range(width)] for i in range(width)] for i in range(width)]
    return map


def main():
    # generate a free map
    depth = 8
    resolution = (1000, 1000, 1000)
    write_3d_map_to_file(generate_map(depth, 0, 1), resolution, "map/map0obs.txt")
    random.seed(1)
    seed_list = random.sample(range(1, 1000000), 180)
    percentage = [5, 10, 15, 20, 25, 30]

    width = 2 ** depth
    all_pos = set()
    for x in range(width):
        for y in range(width):
            for z in range(width):
                all_pos.add((x, y, z))

    for percent in percentage:
        for i in range(30):
            seed = seed_list.pop(0)
            file_name = 'map/map' + str(percent) + 'percent' + str(i) + '.txt'
            write_3d_map_to_file(generate_map(depth, percent, seed, all_pos), resolution, file_name)
            print("Done " + file_name)


if __name__ == '__main__':
    main()
