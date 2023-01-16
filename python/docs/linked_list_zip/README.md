# Challenge Summary
<!-- Description of the challenge -->
- Write a function called zip lists
- Arguments: 2 linked lists
- Return: New Linked List, zipped as noted below
- Zip the two linked lists together into one so that the nodes alternate between the two lists and return a reference to the the zipped list.
- Try and keep additional space down to O(1)
- You have access to the Node class and all the properties on the Linked List class as well as the methods created in previous challenges.-
## Whiteboard Process
<!-- Embedded whiteboard image -->
![Whiteboard](./code_challeng08_wb.png)
## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
-  Create a new linked list and iterate over the zipped lists, adding each element to the new linked list.

Efficiency:

- Time: O(n^2) - quadratic time with nested loops
- Space: O(n) - linear space
## Solution
<!-- Show how to run your code, and examples of it in action -->
- [solution code](../../../python/code_challenges/linked_list_zip.py)

click link above for solution.
