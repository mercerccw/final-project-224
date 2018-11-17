#!/usr/bin/python3

import unittest
import math
from queue import *

class Node():
	""" A tree element.

	:ivar key: the key value
	:ivar left: reference to the left child
	:ivar right: reference to the right child
	:ivar parent: reference to the parent
	:ivar depth: depth of the node

	"""

	def __init__(self, key=None, left=None, right=None, parent=None,depth=0):
		""" Initializes a new node """
		self.key = key
		self.left = left
		self.right = right
		self.parent = parent
		self.depth=depth


	def add_left(self, left ):
		""" Helper function: create a L child  """
		self.left = left
		left.parent = self
		left.depth = self.depth + 1

	def add_right(self, right ):
		""" Helper function: create a R child  """
		self.right = right
		right.parent = self
		right.depth = self.depth + 1

	def __str__(self):
		return str(self.key)


class BinaryTree():
	"""
	A binary tree implementation.
	
	.. _root:

	:ivar root: a reference to the root node
	:ivar height: the height of the tree (length of a path from the root to a leaf)

	.. _description:

	The methods to be implemented in this module  (preorder_walk_, postorder_walk_, is_bst_) essentially use recursion to accomplish their task, but the purely recursive part is nested into the method, that takes care of bootstrapping  the inner procedure, providing the actual parameters for the top call. The general outline of these functions follows.


	.. code-block:: python

		def my_method( self, ... ):
		
			def inner_recursive_procedure( node, ... ):
				# recursive blah
		
			return inner_recursive_procedure( self.root, ... )

	Note that the nested procedure "captures" any variable created in the scope of the wrapper procedure. If you need to update a data structure across the recursive calls, the following is valid.

	.. code-block:: python

		def my_method( self, ... ):
		
			lst = []
		
			def inner_recursive_procedure( node, ... ):
				# recursive stuff that modifies lst
			
			inner_recursive_procedure( self.root, ... )
			
			return lst


	You can accomplish the same thing in a cleaner, more functional style, where the data structure is constructed, and returned by the recursive procedure:

	.. code-block:: python
		
		def my_method( self, ...):
			
			def inner_recursive_procedure( node, lst, ... ):
				# recursive stuff build a new list from lst, and return a new list

			return inner_recursive_procedure(self.root, [], ...)

	"""

	def __init__(self, root=None, array=None):
		""" Initializes an empty tree
		
		:param root: the root node reference
		:type root: Node
		:param array: (optional) if provided, a tree, in the form of nested lists
		:type array:  tuple
		"""
		self.root = root
		self.height=-1

		if array is not None:
			self.update_from_array( array )


	################## TODO #####################################

	def preorder_walk(self):
		"""
		.. _preorder_walk:

		Perform a preorder tree walk.

		.. todo::
			Implement the method, using CLRS3, 12.1 as an inspiration. Do not simply print the nodes, but return a list with the node keys in the desired order.

			1. In this function, write a nested, recursive procedure, that takes a node as a parameter and walks the tree rooted at this node preorder.
			2. In a second step, *call* the inner procedure, with the root_ of this tree as the actual parameter. Do not forget to return the list

			There are 2 ways to populate the list. See this class' description_.

		:return: list of all visited nodes, preorder
		:rtype: list
		"""

		def walkPreorder(node, list):
			if node != None:
				list.append(node.key)
				walkPreorder(node.left, list)
				walkPreorder(node.right, list)
			return list

		return walkPreorder(self.root, [])

	def postorder_walk(self):
		"""
		.. _postorder_walk:

		Perform a postorder tree walk.

		.. todo::
			Implement the method, using CLRS3, 12.1 as an inspiration. Do not simply print the node, but return a list with the node keys in the desired order.

			1. In this function, write a nested, recursive procedure, that takes a node as a parameter and walks the tree rooted at this node postorder.
			2. In a second step, *call* the inner procedure, with the root_ of this tree as the actual parameter. Do not forget to return the list

			There are 2 ways to populate the list. See this class' description_.

		:return: list of all visited nodes, postorder
		:rtype: list
		"""

		def walkPostorder(node, list):
			if node != None:
				walkPostorder(node.left, list)
				walkPostorder(node.right, list)
				list.append(node.key)
			return list

		return walkPostorder(self.root, [])

	def is_bst( self ):
		"""
		.. _is_bst:

		Check for BST property, recursively.

		.. todo::

			Write the procedure. The following is a common programming pattern when using recursion:

			1. In this function, write a nested, recursive procedure, that takes a node `n` as a parameter and returns `True` if the tree rooted at `n` meets the BST property, and `False` otherwise.
			2. In a second step, *call* the inner procedure, with the root_ of this tree as the first actual parameter, and other parameters as needed. Do not forget to return!

			CLRS3, Exercise 12.2.1 might be a good starting point: when you walk down the tree recursively, what should you keep track of in order to check whether the BST property holds for the current node?

		:return: True if this tree is a Binary Search Tree; False otherwise.
		:rtype: bool
		"""
		def checkBST(node, min, max):
			if node == None:
				return True
			left = True
			right = True
			if node.key >= min and node.key <= max:
				if node.left != None:
					left = checkBST(node.left, min, node.key)
				if node.right != None:
					right = checkBST(node.right, node.key, max)
				return left and right
			else:
				return False

		return checkBST(self.root,-10000000,10000000)

	#############################################################

	## NON-ESSENTIAL FUNCTIONS: FOR TEACHING/TESTING PURPOSE

	def update_from_array(self, array  ):
		""" Build a binary tree from nested tuples

		Ex. BinaryTree().update_from_array( ( 1,(2,3,4),(5,None,6) ) yields the following tree::

					1
			     __________/\________
			    2                   5
			  _/\                    \
			 3   4                    6


		:param array: a list of the form ( key, ( left subtree ), (right subtree ))
		:type array: tuple
		"""
	
		def read_rec( triplet ):
			""" Inner function: build a (node,depth) pair from a triplet (parenet,left,right) """
			# base case: a leaf
			if triplet is None:
				return None
			if type(triplet) is not list and type(triplet) is not tuple:
				return (Node(triplet), 0)
			# parent node
			n = Node( triplet[0] )
			# children
			data_left = read_rec( triplet[1] )
			data_right = read_rec( triplet[2] )
			if data_left is not None: n.add_left ( data_left[0])
			if data_right is not None: n.add_right ( data_right[0])
			# returning a pair:
			# - current node pointer
			# - height, as computed from children's heights
			if data_left is None:
				if data_right is None:
					return (n,0)
				return (n,data_right[1]+1)
			elif data_right is None:
				return (n,data_left[1]+1)
			return (n, max(data_left[1],data_right[1])+1)

		data = read_rec( array )
		self.root, self.height = data
		self.update_depth( self.root, 0)

		return self
		
	def update_depth(self, node, depth):
		""" Update the depth attribute on the given node, and all its
		descendants

		:param node: root of the subtree to be updated
		:param depth: value of the new depth attribute
		:type node: Node
		:type depth: int
		"""
		if node is not None:
			node.depth=depth
			self.update_depth(node.left, depth+1)
			self.update_depth(node.right, depth+1)

	def display(self):
		"""
		Breadth-first tree-walking, displaying the nodes on the console
		"""
		if self.root is None:
			return
		q = Queue(200)
		
		# overall width is function of the height of the tree
		root_pos = ((1<<(self.height+1))-1)
		
		prev_depth=0
		prev_pos=0
		edge_def=[]
		label_offset=0
		consumed=0
		q.enqueue((self.root,root_pos))
		while not q.is_empty():
			(n, n_pos) = q.dequeue()

			# starting a row: using absolute position for offset
			if n.depth != prev_depth or n is self.root:
				print('')
				prev_depth=n.depth
				offset = n_pos-1
				label_offset=0

				# converting edge boundaries into a string
				print( self.edge_string(edge_def) )
				edge_def=[]

			# in a row: computing an offset from last position
			# -2 takes care of label already entered
			else:
				offset = n_pos - prev_pos - label_offset

			prev_pos = n_pos
			label_offset=len(str(n.key))

			# display the node
			print('{}{}'.format(offset*' ',n.key),end="")

			
			# enqueue children, computing edge boundaries at the same time
			edge_length = int(math.ceil(root_pos/(2**(n.depth+1))))
			if n.left is not None:
				q.enqueue( (n.left, int(n_pos - edge_length)) )
				edge_def.append( ('L', int(n_pos - edge_length),n_pos) )
			if n.right is not None:
				q.enqueue( (n.right, int(n_pos + edge_length)) )
				edge_def.append(  ('R', n_pos+1,int(n_pos + edge_length)) )
		print('')			
		
	def edge_string( self, definition ):
		""" Build a string according to edge specs """
		last = 0
		string_arr = []
		for pair in definition:

			string_arr.append(' '*(pair[1]-last-1))
			if pair[0]=='L':
				string_arr.append(' ')
			else:
				string_arr.append( '\\' )
			string_arr.append( '_'*(pair[2]-pair[1]-1))
			if pair[0]=='L':
				string_arr.append( '/' )
			else:
				string_arr.append( ' ' )
			last = pair[2]
		return ''.join( string_arr )
			
					
class BinaryTree_UnitTest(unittest.TestCase):


	def test_preorder_walk(self):
		" Test pre-order tree walk """
		bst=BinaryTree( array = (15, (7, (3,2,3), (10,8,(14,12,None))), (21, 19 ,(24,24,67))))
		print("test pre-order walk")
		bst.display()
		self.assertEqual( bst.preorder_walk(),  [15, 7, 3, 2, 3, 10, 8, 14, 12, 21, 19, 24, 24, 67])

	def test_postorder_walk(self):
		" Test post-order tree walk """
		bst=BinaryTree( array = (15, (7, (3,2,3), (10,8,(14,12,None))), (21, 19 ,(24,24,67))))
		print("test post-order walk")
		bst.display()
		self.assertEqual( bst.postorder_walk(),  [2, 3, 3, 8, 12, 14, 10, 7, 19, 24, 67, 24, 21, 15])


	def test_is_bst_true_1(self):
		""" Test BST property true: note that keys might be equal """
		bst=BinaryTree( array = (15, (7, (3,2,3), (10,8,(14,12,None))), (21, 19 ,(24,24,67))))
		print("test BST true")
		bst.display()
		self.assertTrue( bst.is_bst() )


	def test_is_bst_true_2(self):
		""" Test BST property: leaf """
		bst=BinaryTree( array = (15,None,None))
		print("test BST true: testing leaf")
		bst.display()
		self.assertTrue( bst.is_bst() )


	def test_is_bst_false_1(self):
		""" Test BST property false: property is broken between R child and parent
		"""
		bst=BinaryTree( array = (15, (7, (3,2,4), (10,8,(12,None,None))), (21, 19 ,(24,None,23))))
		print("test BST false: R child/parent")
		bst.display()
		self.assertFalse( bst.is_bst() )

	def test_is_bst_false_2(self):
		""" Test BST property false: property is broken between L child and parent
		"""
		bst=BinaryTree( array = (15, (7, (3,2,4), (10,8,(12,14,None))), (21, 19 ,(24,25,None))))
		print("test BST false: L child/parent")
		bst.display()
		self.assertFalse( bst.is_bst() )

	def test_is_bst_false_3(self):
		""" Test BST property false: property is broken between R descendant and ancestor
		"""
		bst=BinaryTree( array = (15, (7, (3,2,4), (10,8,(12,9,None))), (21, 19 ,(24,None,25))))
		print("test BST false: R descendant/ancestor")
		bst.display()
		self.assertFalse( bst.is_bst() )


	def test_is_bst_false_4(self):
		""" Test BST property false: property is broken between R descendant and ancestor
		"""
		bst=BinaryTree( array = (15, (7, (3,2,4), (10,8,(16,11,None))), (21, 19 ,(24,None,25))))
		print("test BST false: L descendant/ancestor")
		bst.display()
		self.assertFalse( bst.is_bst() )


def main():
        unittest.main()

if __name__ == '__main__':
        main()



