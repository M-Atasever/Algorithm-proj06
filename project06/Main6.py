#!/usr/bin/python3

from Digraph import Digraph


def read_graph(filename):
    with open(filename, 'r') as reader:
        g = Digraph(int(reader.readline()))
        for line in reader:
            (s, d, w) = line.split()
            g.insert_arc(int(s), int(d), float(w))
        return g


def main(filename):
    g = read_graph(filename)
    s = int(input('Source vertex?'))
    d = int(input('Dest vertex?'))
    print('Out degree(s):', g.out_degree(s))
    print('Out degree(d):', g.out_degree(d))
    if g.does_path_exist(s, d):
        p = g.find_min_weight_path(s, d)
        print('Path with', len(p) - 1, 'arcs exists')
        print(p)
        if g.is_path_valid(p):
            print('Path weight:', g.path_weight(p))
        else:
            print('But your path is no good!')
    else:
        print('No path exists')


if __name__ == '__main__':
    main('g1.txt')