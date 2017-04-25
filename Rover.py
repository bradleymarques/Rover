import math
import sys
import re


def location(dimensions, position, movement):
    """ Returns the location of the Rover after the execution of the commands received as arguments """
    pattern = re.compile("^([0-9]+) ([0-9]+)$")
    if not pattern.match(dimensions):
        raise ValueError("Error: incorrect specification of the zone boundary command: %s" % dimensions)
    pattern = re.compile("^([0-9]+) ([0-9]+) ([E,W,N,S])$")
    if not pattern.match(position):
        raise ValueError("Error: incorrect specification of the starting position: %s" % position)
    pattern = re.compile("^([M,L,R]*)$")
    if not pattern.match(movement):
        raise ValueError("Error: incorrect specification of the movement and rotation sequence: %s" % movement)

    size = dimensions.split(" ")
    pos = position.split(" ")
    x = int(pos[0])
    y = int(pos[1])
    # Angles in degrees are assigned to directions N = 90, W = 180, S = 270, E = 0.
    options = {'N': 90, 'W': 180, 'S': 270, 'E': 0}
    angle = options.get(pos[2])

    for c in movement:
        if c == 'M':
            x += int(1 * math.cos(math.radians(angle)))
            y += int(1 * math.sin(math.radians(angle)))
            # If the Rover moves outside the zone then something is wrong in the input command list.
            if x > int(size[0]) or x < 0 or y > int(size[1]) or y < 0:
                raise ValueError(
                    "Error: movement instructions resulted in the location outside the zone at coordinates [ %i, %i ]" % (
                        x, y))
        elif c == 'R':
            angle -= 90
            if (angle < 0): angle += 360
        elif c == 'L':
            angle += 90
            if (angle > 359): angle -= 360

    angle_str = list(options.keys())[list(options.values()).index(angle)]
    res = " ".join([str(x), str(y), angle_str])
    return res


if __name__ == "__main__":
    if len(sys.argv) == 4:
        # initialise from commandline
        dimensions = sys.argv[1]
        position = sys.argv[2]
        movement = sys.argv[3]
    else:
        # read input from file: this method is good to provide compatible input with the arguments' parsing
        lines = tuple(open("input.txt", 'r'))
        if len(lines) < 3:
            raise ValueError("Error: 3 lines are required in the command list, received %i" % len(lines))
        dimensions = str(lines[0]).rstrip("\n")
        position = lines[1].rstrip("\n")
        movement = lines[2].rstrip("\n")
    try:
        result = location(dimensions=dimensions, position=position, movement=movement)
        print(result)
    except ValueError as msg:
        print(msg)
