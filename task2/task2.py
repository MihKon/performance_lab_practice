import sys


circle_coords_file_path = sys.argv[1]
dot_coords_file_path = sys.argv[2]

with open(circle_coords_file_path, "r", encoding="UTF-8") as circle_file:
    circle_x_coord, circle_y_coord = [int(i) for i in circle_file.readline().split(" ")]
    circle_radius = int(circle_file.readline())

dot_coords = []
with open(dot_coords_file_path, "r", encoding="UTF-8") as dot_file:
    file_lines = dot_file.readlines()
    for dot_line in file_lines:
        current_line_dot_coords = [int(i) for i in dot_line.split(" ")]
        dot_coords.append(current_line_dot_coords)

result_arr = []
for coords in dot_coords:
    dot_x, dot_y = coords

    x_result = 2
    y_result = 2

    if circle_x_coord - circle_radius < dot_x < circle_x_coord + circle_radius:
        x_result = 1
    elif dot_x == circle_x_coord + circle_radius or dot_x == circle_x_coord - circle_radius:
        x_result = 0

    if circle_y_coord - circle_radius < dot_y < circle_y_coord + circle_radius:
        y_result = 1
    elif dot_y == circle_y_coord + circle_radius or dot_y == circle_y_coord - circle_radius:
        y_result = 0

    dot_result = 2
    if (x_result == 0 and dot_y == 0) or (y_result == 0 and dot_x == 0):
        dot_result = 0
    else:
        formulae_result = (dot_x - circle_x_coord) ** 2 + (dot_y - circle_y_coord) ** 2
        if formulae_result < circle_radius ** 2:
            dot_result = 1
        elif formulae_result > circle_radius ** 2:
            dot_result = 2
        else:
            dot_result = 0
    
    result_arr.append(dot_result)

print(*result_arr, sep="\n")
