import math


def write_3d_map_to_file(map, resolution, file_name):
    f = open(file_name, 'w')

    content = ""

    content += '%d\n' % int(math.log(len(map), 2))
    content += '%d %d %d\n' % (resolution[0], resolution[1], resolution[2])

    for x in range(len(map)):
        for y in range(len(map[0])):
            for z in range(len(map[0][0])):
                content += '%d %d %d %d\n' % (x, y, z, map[x][y][z])

    f.write(content)

    f.close()


def write_2d_map_to_file(map, resolution, file_name):
    f = open(file_name, 'w')

    content = ""

    content += '%d\n' % int(math.log(len(map), 2))
    content += '%d %d\n' % (resolution[0], resolution[1])

    for x in range(len(map)):
        for y in range(len(map[0])):
                content += '%d %d %d\n' % (x, y, map[x][y])

    f.write(content)
    f.close()
