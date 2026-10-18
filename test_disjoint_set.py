"""Regression tests for the connectivity structure used by HexGame."""

import unittest

from disjoint_set import DisjointSet


class TestDisjointSet(unittest.TestCase):
    def test_elements_start_in_separate_sets(self):
        sets = DisjointSet(['a', 'b'])
        self.assertTrue(sets.is_same_set('a', 'a'))
        self.assertFalse(sets.is_same_set('a', 'b'))

    def test_union_is_transitive_and_preserves_unrelated_elements(self):
        sets = DisjointSet(range(4))
        sets.union(0, 1)
        sets.union(1, 2)
        self.assertTrue(sets.is_same_set(0, 2))
        self.assertFalse(sets.is_same_set(0, 3))

    def test_repeated_and_self_union_do_not_increase_rank(self):
        sets = DisjointSet(range(2))
        sets.union(0, 1)
        ranks = sets.rank.copy()
        sets.union(1, 0)
        sets.union(0, 0)
        self.assertEqual(sets.rank, ranks)
        self.assertTrue(sets.is_same_set(0, 1))

    def test_find_compresses_a_multi_level_path(self):
        sets = DisjointSet(range(4))
        sets.union(0, 1)
        sets.union(2, 3)
        sets.union(0, 2)
        self.assertNotEqual(sets.parent[3], sets.find(0))
        root = sets.find(3)
        self.assertEqual(root, sets.find(0))
        self.assertEqual(sets.parent[3], root)

    def test_union_attaches_lower_rank_root_in_either_argument_order(self):
        for reverse in (False, True):
            with self.subTest(reverse=reverse):
                sets = DisjointSet(range(3))
                sets.union(0, 1)
                root = sets.find(0)
                if reverse:
                    sets.union(2, 0)
                else:
                    sets.union(0, 2)
                self.assertEqual(sets.find(2), root)
                self.assertEqual(sets.rank[root], 1)


if __name__ == '__main__':
    unittest.main()
