# Tree Max
<!-- Description of the challenge -->
Write the following method for the Binary Tree class

- find maximum value
- Arguments: none
- Returns: number
- Find the maximum value stored in the tree. You can assume that the values stored in the Binary Tree will be numeric.
## Whiteboard Process
<!-- Embedded whiteboard image -->

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
#### Approach

- Determine if the tree is empty.
  - If so, return None.
  - If not, use the “post_order” method to create a list of all the values.
  - Use the “max” method to find the max value and return it.

#### Efficiency

- Time: O(n) - “post_order” method will take linear time based on size of list
- Space: O(n) - list will grow linearly with number of nodes
## Solution
<!-- Show how to run your code, and examples of it in action -->
The solution code can be found here: [Solution Code](../../data_structures/binary_tree.py)
