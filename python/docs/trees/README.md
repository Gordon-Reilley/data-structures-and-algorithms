# Trees
<!-- Short summary or background information -->
A Binary tree is represented by a pointer to the topmost node or root of the tree. If the tree is empty, then the value of the root is None. Each Node in the tree has a value, left, and right value that help when traversing the tree.
## Challenge
<!-- Description of the challenge -->
- Node
   - Create a Node class that has properties for the value stored in the node, the left child node, and the right child node.
- Binary Tree
   - Create a Binary Tree class
   - Define a method for each of the depth first traversals:
   - pre order
   - in order
   - post order
   - Each depth first traversal method should return an array of values, ordered appropriately.
- Binary Search Tree
   - Create a Binary Search Tree class
   - This class should be a sub-class (or your languages equivalent) of the Binary Tree Class, with the following additional methods:
   - Add
   - Arguments: value
   - Return: nothing
   - Adds a new node with that value in the correct location in the binary search tree.
   - Contains
   - Argument: value
   - Returns: boolean indicating whether or not the value is in the tree at least once.
## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
- Time

  - The Big O time complexity for inserting a new node is O(n). Searching for a specific node will also be O(n). If we assume that a tree has n nodes, then in the worst case we will have to look at n items, hence the O(n) complexity.
- Space

  - The Big O space complexity for a node insertion using breadth first insertion will be O(w), where w is the largest width of the tree.
  - The Big O space complexity of a BST search would be O(1).
## API
<!-- Description of each method publicly available in each of your trees -->
- Binary Tree

  - pre_order - starts at the top of the tree and works left, then right returning values in pre-order.
  - n_order - starts at the right-most leaf, works up to the parent, then the left leaf returning values in in-order.
  - post_order - starts at the bottom of the tree and works right at the current level, then up one level and works left to right, until it finally reaches the root returning values in post-order.
- Binary Search Tree

  - add - takes in a value adds a new node with that value in the correct location in the binary search tree.
  - contains - takes in a value and returns a boolean indicating whether the value is in the tree at least once.-
