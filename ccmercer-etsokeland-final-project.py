#!/usr/bin/python3
import unittest


class Fox:
    def __init__(self, id=0, sex=None, weight=0.0, left=None, right=None, parent=None, depth=0):
        self.id = id
        self.sex = sex
        self.weight = weight
        self.left = left
        self.right = right
        self.parent = parent
        self.depth = depth

    def add_left(self, left):
        pass

    def add_right(self, right):
        pass

    def insert(self, fox):
        pass

    def delete(self, fox):
        pass


class BinaryFoxTree():
    def __init__(self, root=None, array=None):
        pass

    def insert(self, fox):
        pass

    def delete(self, fox):
        pass

    def search(self, fox):
        pass

    def minimum(self):
        pass

    def maximum(self):
        pass

    def is_bst(self):
        return True


class FoxTreeUnitTest(unittest.TestCase):

    def test_is_FoxTree_bst_true(self):

        fox1 = Fox(1, "M", 14.7)
        fox2 = Fox(2, "F", 8.5)
        fox3 = Fox(3, "F", 22.5)
        fox4 = Fox(4, "F", 4.2)
        fox5 = Fox(5, "M", 11.2)
        fox6 = Fox(6, "M", 17.6)
        fox7 = Fox(7, "F", 25.1)
        fox8 = Fox(8, "M", 2.1)
        fox9 = Fox(9, "F", 4.2)
        fox10 = Fox(10, "M", 8.7)
        fox11 = Fox(11, "M", 13.3)
        fox12 = Fox(12, "M", 25.1)
        fox13 = Fox(13, "M", 76.3)
        fox14 = Fox(14, "M", 12.0)
        foxes = (fox1.weight, (fox2.weight, (fox4.weight, fox8.weight, fox9.weight),
                               (fox5.weight, fox10.weight, (fox11.weight, fox14.weight, None))),
                 (fox3.weight, fox6.weight, (fox7.weight, fox12.weight, fox13.weight)))
        fox_tree = BinaryFoxTree(foxes)
        self.assertTrue(fox_tree.is_bst())

    def test_is_FoxTree_bst_false(self):
        fox1 = Fox(1, "M", 1.7)
        fox2 = Fox(2, "F", 8.5)
        fox3 = Fox(3, "F", 22.5)
        fox4 = Fox(4, "F", 4.2)
        fox5 = Fox(5, "M", 11.2)
        fox6 = Fox(6, "M", 17.6)
        fox7 = Fox(7, "F", 25.1)
        fox8 = Fox(8, "M", 2.1)
        fox9 = Fox(9, "F", 4.2)
        fox10 = Fox(10, "M", 8.7)
        fox11 = Fox(11, "M", 13.3)
        fox12 = Fox(12, "M", 25.1)
        fox13 = Fox(13, "M", 76.3)
        fox14 = Fox(14, "M", 12.0)
        foxes = (fox1.weight, (fox2.weight, (fox4.weight, fox8.weight, fox9.weight),
                               (fox5.weight, fox10.weight, (fox11.weight, fox14.weight, None))),
                 (fox3.weight, fox6.weight, (fox7.weight, fox12.weight, fox13.weight)))
        fox_tree = BinaryFoxTree(foxes)
        self.assertFalse(fox_tree.is_bst())


    def test_insert_fox15(self):
        # Insert fox into tree with only root
        # Insert fox into empty tree
        fox1 = Fox(1, "M", 14.7)
        fox2 = Fox(2, "F", 8.5)
        fox3 = Fox(3, "F", 22.5)
        fox4 = Fox(4, "F", 4.2)
        fox5 = Fox(5, "M", 11.2)
        fox6 = Fox(6, "M", 17.6)
        fox7 = Fox(7, "F", 25.1)
        fox8 = Fox(8, "M", 2.1)
        fox9 = Fox(9, "F", 4.2)
        fox10 = Fox(10, "M", 8.7)
        fox11 = Fox(11, "M", 13.3)
        fox12 = Fox(12, "M", 25.1)
        fox13 = Fox(13, "M", 76.3)
        fox14 = Fox(14, "M", 12.0)
        foxes = (fox1.weight, (fox2.weight, (fox4.weight, fox8.weight, fox9.weight),
                               (fox5.weight, fox10.weight, (fox11.weight, fox14.weight, None))),
                 (fox3.weight, fox6.weight, (fox7.weight, fox12.weight, fox13.weight)))
        fox_tree = BinaryFoxTree(foxes)
        self.assertTrue(fox_tree.insert(Fox(15, "M", 13.6)))




def main():
    unittest.main()


if __name__ == '__main__':
    main()
