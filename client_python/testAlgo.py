import unittest

from GraphAlgo import GraphAlgo
from DiGraph import DiGraph


class TestDiGraph(unittest.TestCase):

    # def test_load_from_json(self):
    #     ga = GraphAlgo()
    #     self.assertTrue(ga.load_from_json("C:/Users/adi.fin45/PycharmProjects/Ex3/data/10000Nodes.json"))

    def test_save_from_json(self):
        graphAlgo = GraphAlgo(DiGraph())
        graphAlgo.load_from_json("C:/Users/adi.fin45/PycharmProjects/Ex3/data/A2.json")
        self.assertTrue(graphAlgo.save_to_json("temp.json"))

    def test_shortest_path(self):
        graphAlgo = GraphAlgo(DiGraph())
        graphAlgo.graph.add_node(0)
        graphAlgo.graph.add_node(1)
        graphAlgo.graph.add_node(2)
        graphAlgo.graph.add_edge(0, 1, 1)
        graphAlgo.graph.add_edge(1, 2, 4)
        self.assertEqual(graphAlgo.shortest_path(0, 1), (1, [0, 1]))
        self.assertEqual(graphAlgo.shortest_path(0, 2), (5, [0, 1, 2]))

    def test_all_in_edges_of_node(self):
        graphAlgo = GraphAlgo()
        graphAlgo.load_from_json("C:/Users/adi.fin45/PycharmProjects/Ex3/data/A1.json")
        self.assertEqual(len(graphAlgo.graph.all_in_edges_of_node(0)), 2)

    def test_all_out_edges_of_node(self):
        graphAlgo = GraphAlgo()
        graphAlgo.load_from_json("C:/Users/adi.fin45/PycharmProjects/Ex3/data/A1.json")
        self.assertEqual(len(graphAlgo.graph.all_out_edges_of_node(0)), 2)

    def test_get_mc(self):
        graphAlgo = GraphAlgo()
        graphAlgo.load_from_json("C:/Users/adi.fin45/PycharmProjects/Ex3/data/A1.json")
        self.assertEqual(graphAlgo.graph.get_mc(), 53)

    def test_dist(self):
        g_algo = GraphAlgo()
        x1 = 4.0
        y1 = 7.0
        x2 = 0.0
        y2 = 4.0
        self.assertEqual(g_algo.dist(x1, y1, x2, y2), 5.0)

    def test_closest(self):
        graphAlgo = GraphAlgo(DiGraph())
        graphAlgo.graph.add_node(0, (4.0, 6.0))
        graphAlgo.graph.add_node(1, (6.0, 2.0))
        graphAlgo.graph.add_node(2, (2.0, 1.0))
        graphAlgo.graph.add_edge(0, 1, 1)
        graphAlgo.graph.add_edge(1, 2, 4)
        self.assertEqual(graphAlgo.closest(5.0, 4.0), (0))
        self.assertEqual(graphAlgo.closest(3.0, 4.0), (0))








if __name__ == '__main__':
    unittest.main()
