import os
class PipeObject:
    def __init__(self, obj, x, y):
        self.object = obj
        self.xCoord = x
        self.yCoord = y

def get_connected_sinks(filename):
    objects = read_objects(filename)
    connects_up = ["║", "╚", "╝", "╠", "╣", "╩", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
                   "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    connects_down = ["║", "╔", "╗", "╠", "╣", "╦", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
                     "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    connects_left = ["═", "╗", "╝", "╣", "╦", "╩", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
                     "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    connects_right = ["═", "╔", "╚", "╠", "╦", "╩", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
                      "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    connected_sinks = []
    for i in range(len(objects) - 1):
        if objects[i].object.isalpha():
            checked_objects = []
            if is_connected(objects, connects_up, connects_down, connects_left, connects_right, objects[i], "",
                            checked_objects):
                connected_sinks.append(objects[i].object)
    connected_sinks.sort()
    return ''.join(connected_sinks)

def read_objects(filename):
    objects = []
    with open(filename, encoding="utf8") as file:
        for line in file:
            parts = line.strip().split(' ', 2)
            if len(parts) == 3:
                x = int(parts[1])
                y = int(parts[2])
                objects.append(PipeObject(parts[0], x, y))
    objects.append(PipeObject("null", 0, 0))
    return objects

def is_connected(objects, up, down, left, right, obj, direction_checked, checked_objects):
    if obj.object == "null":
        return False
    if obj.object == "*":
        return True
    if obj in checked_objects:
        return False
    checked_objects.append(obj)
    connect_left = connect_right = connect_up = connect_down = False

    if obj.object in left and direction_checked != "left":
        connect_left = is_connected(objects, up, down, left, right, get_left_of(objects, right, obj), "right",
                                    checked_objects)

    if obj.object in right and direction_checked != "right":
        connect_right = is_connected(objects, up, down, left, right, get_right_of(objects, left, obj), "left",
                                     checked_objects)

    if obj.object in up and direction_checked != "up":
        connect_up = is_connected(objects, up, down, left, right, get_top_of(objects, down, obj), "down",
                                  checked_objects)

    if obj.object in down and direction_checked != "down":
        connect_down = is_connected(objects, up, down, left, right, get_bottom_of(objects, up, obj), "up",
                                    checked_objects)

    return connect_left or connect_right or connect_up or connect_down

def get_left_of(objects, right, obj):
    for o in objects:
        if (o.object == "*" or o.object in right) and o.xCoord == obj.xCoord - 1 and o.yCoord == obj.yCoord:
            return o
    return objects[-1]

def get_right_of(objects, left, obj):
    for o in objects:
        if (o.object == "*" or o.object in left) and o.xCoord == obj.xCoord + 1 and o.yCoord == obj.yCoord:
            return o
    return objects[-1]

def get_top_of(objects, down, obj):
    for o in objects:
        if (o.object == "*" or o.object in down) and o.xCoord == obj.xCoord and o.yCoord == obj.yCoord + 1:
            return o
    return objects[-1]

def get_bottom_of(objects, up, obj):
    for o in objects:
        if (o.object == "*" or o.object in up) and o.xCoord == obj.xCoord and o.yCoord == obj.yCoord - 1:
            return o
    return objects[-1]

if __name__ == "__main__":
    filename = "input.txt"
    if os.path.isfile(filename):
        print(get_connected_sinks(filename))
    else:
        print(f"File {filename} not found.")


