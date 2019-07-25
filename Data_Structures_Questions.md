Answer the following questions for each of the data structures you implemented
as part of this project.

## Queue

1. What is the runtime complexity of `enqueue`?

   Depends on a implementation.

   With queue based on linked list it is **O(1)**. With queue based on an array
   it may be **O(n)** when it needs to rewrite an entire array if there is no
   space left. We can enhance our queue with the max length/size parameter to
   prevent this.

2. What is the runtime complexity of `dequeue`?

   Depends on a implementation.

   With queue based on linked list it is **O(1)**. With queue based on an array
   it is **O(n)** as it needs to shift all elements by one position.

3. What is the runtime complexity of `len`?

   Depends on the implementation.

   Can be **O(1)** with some additional memory (one variable) but can be
   **O(n)** without storing that memory in the actual Queue object. Then the
   method needs to traverse an entire queue that leads to **O(n)**.

## Binary Search Tree

1.  What is the runtime complexity of `insert`?

    Depends on implementation. The average is **O(log n)** with the worst case
    of **O(n)** (for trees that are unbalanced, or just to be precise - linear).

2.  What is the runtime complexity of `contains`?

    Depends on implementation. The average is **O(log n)** with the worst case
    of **O(n)** (for trees that are unbalanced, or just to be precise - linear).

3.  What is the runtime complexity of `get_max`?

    Depends on some constraints. If the BST is built on top of the fixed-size
    array and we know that the array is full, then this method can be **O(1)**
    because we can just get the last element of this array and it's the deepest
    child on the very right. The average is **O(log n)** with the worst case of
    **O(n)** (for trees that are unbalanced, or just to be precise - linear).

## Heap

1. What is the runtime complexity of `_bubble_up`?

   It's **O(log n)**.

2. What is the runtime complexity of `_sift_down`? It's **O(log n)**.

3. What is the runtime complexity of `insert`? It's **O(1)** on average with
   **O(log n)** in the worst case.

4. What is the runtime complexity of `delete`?

   It's **O(log n)** for both average and the worst cases.

5. What is the runtime complexity of `get_max`?

   It's **O(1)** for the max heap as the max value is in the root. Otherwise,
   if we have min heap and search for the max value, then it's **O(n)**.

## Doubly Linked List

1.  What is the runtime complexity of `ListNode.insert_after`?

    It's **O(1)**. Always requires the fixed number of operations, as long as
    you execute it on node, so you don't need to traverse an entire list just to
    do it. Otherwise it would be **O(n)**.

2.  What is the runtime complexity of `ListNode.insert_before`?

    It's **O(1)**. Always requires the fixed number of operations, as long as
    you execute it on node, so you don't need to traverse an entire list just to
    do it. Otherwise it would be **O(n)**.

3.  What is the runtime complexity of `ListNode.delete`?

    It's **O(1)**. Always requires the fixed number of operations, as long as
    you execute it on node, so you don't need to traverse an entire list just to
    do it. Otherwise it would be **O(n)**.

4.  What is the runtime complexity of `DoublyLinkedList.add_to_head`?

    It's **O(1)**. Always requires the fixed number of operations, as long as
    you execute it on node, so you don't need to traverse an entire list just to
    do it. Otherwise it would be **O(n)**.

5.  What is the runtime complexity of `DoublyLinkedList.remove_from_head`?

    It's **O(1)**. Always requires the fixed number of operations, as long as
    you execute it on node, so you don't need to traverse an entire list just to
    do it. Otherwise it would be **O(n)**.

6.  What is the runtime complexity of `DoublyLinkedList.add_to_tail`?

    It's **O(1)**. Always requires the fixed number of operations, as long as
    you execute it on node, so you don't need to traverse an entire list just to
    do it. Otherwise it would be **O(n)**.

7.  What is the runtime complexity of `DoublyLinkedList.remove_from_tail`?

    It's **O(1)**. Always requires the fixed number of operations, as long as
    you execute it on node, so you don't need to traverse an entire list just to
    do it. Otherwise it would be **O(n)**.

8.  What is the runtime complexity of `DoublyLinkedList.move_to_front`?

    It's **O(1)**. Always requires the fixed number of operations, as long as
    you execute it on node, so you don't need to traverse an entire list just to
    do it. Otherwise it would be **O(n)**.

9.  What is the runtime complexity of `DoublyLinkedList.move_to_end`?

    It's **O(1)**. Always requires the fixed number of operations, as long as
    you execute it on node, so you don't need to traverse an entire list just to
    do it. Otherwise it would be **O(n)**.

10. What is the runtime complexity of `DoublyLinkedList.delete`?

    It's **O(1)**. Always requires the fixed number of operations, as long as
    you execute it on node, so you don't need to traverse an entire list just to
    do it. Otherwise it would be **O(n)**.

    **a)** Compare the runtime of the doubly linked list's `delete` method with
    the worst-case runtime of the JS `Array.splice` method. Which method
    generally performs better?

    Single deletion from a linked list or a doubly linked list is **O(1)** while
    `Array.splice` worst case is O(n) when it needs to copy n-1 elements to a
    new array.
