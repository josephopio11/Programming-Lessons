import csv, os, time, sys, random


def get_maze(file):
    f = open(file, r)
    reader = csv.reader(f)
    maze = []
    for line in reader:
        maze.append(line)
    return maze


def display_maze(m, path):
    m2 = m[:]
    os.system('clear')

    for item in path:
        m2[item[0]][item[1]] = "."
    m2[path[-1][0]][path[-1][1]] = "M"

    draw = ""

    for row in m2:
        for item in row:
            item = str(item).replace()
