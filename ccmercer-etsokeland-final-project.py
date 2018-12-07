#!/usr/bin/python3
#Eli Sokeland and Clayton Mercer
import unittest

#Create the Fox class for all atributes
class Fox:
    def __init__(self, id, sex, weight):
        self.id = id
        self.sex = sex
        self.weight = weight

    def __le__(self, fox):
        return self.weight <= fox.weight

    def __ge__(self, fox):
        return self.weight >= fox.weight

    def __eq__(self, fox):
        return self.weight == fox.weight

    def __gt__(self, fox):
        return self.weight > fox.weight

    def __lt__(self, fox):
        return self.weight < fox.weight

#Create the Node class to store the Fox class
class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

#Create the BinaryFoxTree from Fox Nodes
class BinaryFoxTree:
    def __init__(self, root):
        self.root = Node(root)

    def postorder(self):
        return self.postorderTree(self.root)

    def postorderTree(self, fox):
        if (fox):
            return self.postorderTree(fox.right) + [fox.data] + self.postorderTree(fox.left)
        else:
            return []

    def findFox(self, fox, weight):
        if (weight == fox.weight):
            return fox
        elif (weight < fox.weight):
            return self.findFox(fox.left, weight)
        else:
            return self.findFox(fox.right, weight)

    def foxInTree(self, weight):
        fox = self.findFox(self.root, weight)

    def deleteFox(self, weight):
        fox = self.findFox(self.root, weight)

    def insertFox(self, fox, weight):
        if (weight <= fox.data):
            if (fox.left):
                self.insertFox(fox.left, weight)
            else:
                fox.left = Node(weight)
        elif (weight > fox.data):
            if (fox.right):
                self.insertFox(fox.right, weight)
            else:
                fox.right = Node(weight)

    def insert(self, weight):
        self.insertFox(self.root, weight)


class Test(unittest.TestCase):

    #Tests the BST property through postorder traversal (should return true)
    def test_tree(self):
        postorder = [3, 4, 5, 10, 9, 8, 6]
        tree = BinaryFoxTree(6)
        tree.insert(8)
        tree.insert(3)
        tree.insert(10)
        tree.insert(5)
        tree.insert(4)
        tree.insert(9)
        self.assertEqual(tree.postorder(), postorder)

    #Tests to see if fox node is within tree (should return true)
    def test_find_fox(self):
        fox = Fox(19, "F", 13.0)
        tree = BinaryFoxTree(fox)
        tree.insert(Fox(7, "F", 15.678))
        tree.insert(Fox(2, "F", 2.56))
        tree.insert(Fox(5, "M", 8.96))
        tree.insert(Fox(6, "F", 7.65))
        tree.insert(Fox(11, "M", 10.78))
        self.assertTrue(tree.foxInTree(Fox(11, "M", 10.78)))

    #Tests to see if fox node is within tree (should return false)
    def test_fox_in_tree(self):
        postorder = [Fox(8, "M", 12.5), Fox(11, "F", 13.0), Fox(1, "M", 25.56), Fox(2, "M", 24.3), Fox(1, "F", 20.11)]
        tree = BinaryFoxTree(Fox(1, "F", 20.11))
        tree.insert(Fox(8, "M", 12.5))
        tree.insert(Fox(11, "F", 13.0))
        tree.insert(Fox(1, "M", 25.56))
        tree.insert(Fox(2, "M", 24.3))
        self.assertEqual(tree.foxInTree(Fox(11, "M", 10.78)))

    #Tests the difference between the weights of foxes (should return true)
    def test_fox_greater(self):
        fox_1 = Fox(7, "F", 25.001)
        fox_2 = Fox(4, "M", 9.25)
        fox_3 = Fox(6, "F", 25.001)
        self.assertTrue((fox_1 > fox_2) and not fox_1 > fox_3)

    #Tests the difference between the weights of foxes (should return true)
    def test_fox_equal(self):
        fox_1 = Fox(5, "F", 13.87)
        fox_2 = Fox(7, "M", 13.87)
        fox_3 = Fox(6, "F", 13.5)
        self.assertTrue(fox_1 == fox_2 and fox_1 != fox_3)

    #Tests the difference between the weights of foxes (should return true)
    def test_fox_less(self):
        fox_1 = Fox(10, "M", 16.3)
        fox_2 = Fox(6, "M", 1.4)
        fox_3 = Fox(9, "F", 16.3)
        self.assertTrue( (fox_2 < fox_1) and not fox_1 < fox_3)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
