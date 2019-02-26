#!/usr/bin/python3

import unittest

from Main6 import read_graph, Digraph


class TreeSetTests(unittest.TestCase):

    def test_size(self):
        g = read_graph('g1.txt')
        self.assertEqual(5, g.order)
        self.assertEqual(6, g.size)
        self.validate_equality(read_graph('g1.txt'), g)

    def test_insert_arc(self):
        g = read_graph('g1.txt')
        g.insert_arc(2, 4, 3.5)
        self.assertEqual(5, g.order)
        self.assertEqual(7, g.size)
        g.insert_arc(2, 4, 2.5)
        self.assertEqual(5, g.order)
        self.assertEqual(7, g.size)
        self.assertRaises(IndexError, g.insert_arc, 2, 7, 1.0)
        self.assertRaises(IndexError, g.insert_arc, 7, 1, 1.0)

    def test_out_degree(self):
        g = read_graph('g1.txt')
        self.assertEqual(2, g.out_degree(0))
        self.assertEqual(1, g.out_degree(1))
        self.assertEqual(0, g.out_degree(3))
        self.assertRaises(IndexError, g.out_degree, 7)
        self.validate_equality(read_graph('g1.txt'), g)

    def test_are_connected(self):
        g = read_graph('g1.txt')
        self.assertTrue(g.are_connected(0, 1))
        self.assertTrue(g.are_connected(4, 1))
        self.assertFalse(g.are_connected(1, 0))
        self.assertFalse(g.are_connected(1, 4))
        self.assertRaises(IndexError, g.are_connected, 2, 7)
        self.assertRaises(IndexError, g.are_connected, 7, 1)
        self.validate_equality(read_graph('g1.txt'), g)

    def test_is_path_valid(self):
        g = read_graph('g1.txt')
        self.assertTrue(g.is_path_valid([0, 2]))
        self.assertTrue(g.is_path_valid([2, 3]))
        self.assertTrue(g.is_path_valid([0, 2, 3]))
        self.assertFalse(g.is_path_valid([3, 2, 0]))
        self.assertTrue(g.is_path_valid([1]))
        self.assertRaises(IndexError, g.is_path_valid, [0, 7, 1])
        self.validate_equality(read_graph('g1.txt'), g)

    def test_arc_weight(self):
        import math
        g = read_graph('g1.txt')
        self.assertAlmostEqual(5.0, g.arc_weight(0, 1))
        self.assertAlmostEqual(2.5, g.arc_weight(4, 1))
        self.assertAlmostEqual(math.inf, g.arc_weight(1, 0))
        self.assertAlmostEqual(math.inf, g.arc_weight(1, 4))
        self.assertRaises(IndexError, g.arc_weight, 2, 7)
        self.assertRaises(IndexError, g.arc_weight, 7, 1)
        self.validate_equality(read_graph('g1.txt'), g)

    def test_path_weight(self):
        import math
        g = read_graph('g1.txt')
        self.assertAlmostEqual(2.0, g.path_weight([0, 2]))
        self.assertAlmostEqual(2.0, g.path_weight([2, 3]))
        self.assertAlmostEqual(4.0, g.path_weight([0, 2, 3]))
        self.assertAlmostEqual(math.inf, g.path_weight([3, 2, 0]))
        self.assertAlmostEqual(0, g.path_weight([1]))
        self.assertRaises(IndexError, g.path_weight, [0, 7, 1])
        self.validate_equality(read_graph('g1.txt'), g)

    def test_path_exists(self):
        g = read_graph('g1.txt')
        for v in range(g.order):
            self.assertTrue(g.does_path_exist(v, v))
        self.assertTrue(g.does_path_exist(0, 2))
        self.assertTrue(g.does_path_exist(2, 3))
        self.assertTrue(g.does_path_exist(0, 3))
        self.assertFalse(g.does_path_exist(1, 0))
        self.assertFalse(g.does_path_exist(3, 2))
        self.assertFalse(g.does_path_exist(2, 0))
        self.assertRaises(IndexError, g.does_path_exist, 0, 7)
        self.assertRaises(IndexError, g.does_path_exist, 7, 0)
        self.validate_equality(read_graph('g1.txt'), g)

    def test_find_min_path(self):
        g = read_graph('g1.txt')
        for v in range(g.order):
            self.assertAlmostEqual(0.0, g.path_weight(g.find_min_weight_path(v, v)))
        self.assertAlmostEqual(5.0, g.path_weight(g.find_min_weight_path(0, 1)))
        self.assertAlmostEqual(2.0, g.path_weight(g.find_min_weight_path(0, 2)))
        self.assertAlmostEqual(4.0, g.path_weight(g.find_min_weight_path(0, 3)))
        self.validate_equality(read_graph('g1.txt'), g)

    def test_large_graph(self):
        g = Digraph(101)
        # Path
        for i in range(100):
            g.insert_arc(i, (i + 1), i + 1)

        # Validate
        for i in range(101):
            for j in range(i + 1, 101):
                self.assertEqual((i + 1) == j, g.are_connected(i, j), '{0} -> {1}'.format(i, j))
                self.assertFalse(g.are_connected(j, i), '{1} -> {0}'.format(i, j))
                self.assertTrue(g.does_path_exist(i, j), '{0} -> {1}'.format(i, j))
                self.assertFalse(g.does_path_exist(j, i), '{1} -> {0}'.format(i, j))
                p = g.find_min_weight_path(i, j)
                self.assertEqual(j - i, len(p) - 1, '{0} -> {1}'.format(i, j))
        self.assertEqual(5050, g.path_weight(g.find_min_weight_path(0, 100)))

    def validate_equality(self, g1, g2):
        self.assertEqual(g1.order, g2.order)
        self.assertEqual(g1.size, g2.size)
        for i in range(g1.order):
            for j in range(g2.order):
                self.assertEqual(g1.are_connected(i, j), g2.are_connected(i, j), '{0}->{1}'.format(i, j))
                if g1.are_connected(i, j):
                    self.assertEqual(g1.arc_weight(i, j), g2.arc_weight(i, j), '{0}->{1}'.format(i, j))


if __name__ == '__main__':
    unittest.main()
