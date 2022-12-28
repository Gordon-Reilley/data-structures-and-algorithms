# Singly Linked List
<!-- Short summary or background information -->
In Python, a linked list is a linear data structure that is made up of a sequence of nodes, where each node stores a reference to an object and a reference to the next node in the sequence. Linked lists are used to store data in a dynamic way, as the number of nodes in a linked list can grow or shrink as needed. Each node in a linked list is typically implemented as a separate Python class, with instance variables to store the data and the reference to the next node. The linked list class itself typically contains a reference to the head (first) node in the list and possibly a reference to the tail (last) node as well.
## Challenge
<!-- Description of the challenge -->
- Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node.
- Create a Linked List class
- Within your Linked List class, include a head property.
- Upon instantiation, an empty Linked List should be created.
## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
Linked lists have some advantages and disadvantages compared to other data structures such as arrays. One advantage is that it is easy to add and remove elements from a linked list, as you only need to update the references in the nodes. However, linked lists are not as efficient for indexing and searching as arrays, as you need to traverse the list from the beginning to access a specific element.
## API
<!-- Description of each method publicly available to your Linked List -->
- **Insert**
  - Arguments: value
  - Returns: nothing
  - Adds a new node with that value to the head of the list with an O(1) Time performance.
- **Includes**
  - Arguments: value
  - Returns: Boolean
  - Indicates whether that value exists as a Node’s value somewhere within the list.
- **To String**
  - Arguments: none
  - Returns: a string representing all the values in the Linked List, formatted as:
  - "{ a } -> { b } -> { c } -> NULL"
