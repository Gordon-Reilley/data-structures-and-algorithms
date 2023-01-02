# Stacks and Queues
<!-- Short summary or background information -->
Stack is a container of objects that are inserted and removed according to the last-in first-out (LIFO) principle. Queue is a container of objects (a linear collection) that are inserted and removed according to the first-in first-out (FIFO) principle.
## Challenge
<!-- Description of the challenge -->
### Stack
- Create a Stack class that has a top property. It creates an empty Stack when instantiated.
  - This object should be aware of a default empty value assigned to top when the stack is created.
  - The class should contain the following methods:
  - push
    - Arguments: value
    - adds a new node with that value to the top of the stack with an O(1) Time performance.
  - pop
    - Arguments: none
    - Returns: the value from node from the top of the stack
    - Removes the node from the top of the stack
    - Should raise exception when called on empty stack
  - peek
    - Arguments: none
    - Returns: Value of the node located at the top of the stack
    - Should raise exception when called on empty stack
  - is empty
    - Arguments: none
    - Returns: Boolean indicating whether or not the stack is empty.
### Queue
- Create a Queue class that has a front property. It creates an empty Queue when instantiated.
  - This object should be aware of a default empty value assigned to front when the queue is created.
  - The class should contain the following methods:
  - enqueue
    - Arguments: value
    - adds a new node with that value to the back of the queue with an O(1) Time performance.
  - dequeue
    - Arguments: none
    - Returns: the value from node from the front of the queue
    - Removes the node from the front of the queue
    - Should raise exception when called on empty queue
  - peek
    - Arguments: none
    - Returns: Value of the node located at the front of the queue
    - Should raise exception when called on empty stack
  - is empty
    - Arguments: none
    - Returns: Boolean indicating whether or not the queue is empty
## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
#### Stack

- init - creates an empty stack with a top of None.
- push - Requires a value input and adds a new node with that value to the top of the stack with an O(1) Time performance.
- pop - Removes the node from the top of the stack and returns the value from that node or raises an exception when called on empty stack.
- peek - Returns the value of the node located at the top of the stack or raises an exception when called on an empty stack.
- is-empty - Returns a Boolean indicating whether the stack is empty.

#### Queue

- init - creates an empty queue with a front and back of None.- enqueue - Requires a value input and adds a new node with that value to the back of the queue with an O(1) Time performance.
- dequeue - Removes and returns the value from node from the front of the queue or raises an exception when called on empty queue.
- peek - Returns a value of the node located at the front of the queue or raises an exception when called on an empty queue.
- is_empty - Returns a Boolean indicating whether the queue is empty.
## API
<!-- Description of each method publicly available to your Stack and Queue-->
#### Stack

- init - creates an empty stack with a top of None.
- push - Requires a value input and adds a new node with that value to the top of the stack with an O(1) Time performance.
- pop - Removes the node from the top of the stack and returns the value from that node or raises an exception when called on empty stack.
- peek - Returns the value of the node located at the top of the stack or raises an exception when called on an empty stack.
- is-empty - Returns a Boolean indicating whether the stack is empty.

#### Queue

- init - creates an empty queue with a front and back of None.- enqueue - Requires a value input and adds a new node with that value to the back of the queue with an O(1) Time performance.
- dequeue - Removes and returns the value from node from the front of the queue or raises an exception when called on empty queue.
- peek - Returns a value of the node located at the front of the queue or raises an exception when called on an empty queue.
- is_empty - Returns a Boolean indicating whether the queue is empty.
