# Data Structure and Algorithm

## Practice
- [LeetCode](https://leetcode.com) 

## BigO
- worst case
- choose dominant terms 
- ![GrowthRate](static/GrowthRate.png)
- ![SizeTable](static/SizeTable.png)


## Abstract Data Type
- collection of data
- set of operations on that data

### Linear 
- ordered
- can add or remove into particular position
#### Stack
- Last-in & First-out (LIFO) 
- Operations :
  - push(onTop)
  - pop(theFirst)
  - peek(theLast)
  - isEmpty()
  - size()
- Implementation :
    ```
    class Stack:
        def __init__(self):
            self.items = []

        def push(self, item):
            self.items.append(item)

        def pop(self):
            return self.items.pop() if self.items else None

        def peek(self):
            return self.items[-1] if self.items else None

        def is_empty(self):
            return len(self.items) == 0
    ```
- BigO :
  - push/pop :  O(1)
- ![StackOrder](static/StackOrder.png)
- Application :
  - Checking for Balanced Braces
  - Bracket Matching ![BracketMatching](static/BracketMatching.png)
  - Postfix Calcultion ![PostfixCalcultion](static/PostfixCalcultion.png)


#### Queue
- ordered collection of items
- First-in, First-out (FIFO)
- Operations :
  - enqueue(toLast)
  - dequeue(theFirst)
  - peek()
  - isEmpty()
  - size()
- Implementation :
    ```
    class SimpleQueue:
        def __init__(self):
            self.queue = []

        def enqueue(self, item):
            self.queue.append(item)

        def dequeue(self):
            if not self.is_empty():
                return self.queue.pop(0)
            raise IndexError("Dequeue from empty queue")

        def is_empty(self):
            return len(self.queue) == 0

        def size(self):
            return len(self.queue)
    ``` 
- Hot Potato
![HotPotato](static/HotPotato.png) 
    ```
    def hot_potato(players, num_passes):
        while len(players) > 1:
            for _ in range(num_passes):
                players.push(players.dequeue())  
            eliminated = players.dequeue()
        return players.peek()
    ```
- Circular Queue : ![CircularQueue](static/CircularQueue.png)
  - ![CircularQueueEnq](static/CircularQueueEnq.png)
  - ![CircularQueueDeq](static/CircularQueueDeq.png)
  ```
  class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def enqueue(self, item):
        if self.is_full():
            return
        if self.is_empty():
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
        item = self.queue[self.front]
        if self.front == self.rear:  # Queue has only one element
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return item

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[self.front]
  ```
- Round Robin Scheduler
  ![RoundRobinScheduler](static/RoundRobinScheduler.png) 
    ```
    class Process:
        def __init__(self, name, burst_time):
            self.name = name
            self.burst_time = burst_time
            self.remaining_time = burst_time


    def round_robin(processes, time_quantum):
        # time quantum refers to the fixed amount of time that each process is allowed to run 
        time = 0
        # tracking execution time
        
        queue = CircularQueue(len(processes))
        for process in processes:
            queue.enqueue(process)

        while not queue.is_empty():
            current_process = queue.dequeue()
            if current_process.remaining_time > time_quantum:
                time += time_quantum
                # simulate execution for time_quantum
                current_process.remaining_time -= time_quantum 
                queue.enqueue(current_process)
            else:
                time += current_process.remaining_time
                # simulate finishing execution
                current_process.remaining_time = 0
    ```

#### Stack vs Queue

| Stack | Queue |
|----------|----------|
| LIFO    | FIFO   |
| Good for Py List    | Bad for Py List   |
| push(), pop(), peek() : O(1)    | enqueue()(Py List):O(n), enqueue()(Circular) dequeue(), peek() : O(1)   |


#### Deque
- ordered collection 
- added or removed on both front or back
- does not require LIFO or FIFO orderings
- ![Deque](static/Deque.png)
- Operations :
  - add_front()
  - add_rear()
  - remove_front()
  - remove_rear()
  - isEmpty()
  - size()
- BigO :
  - front : O(1)
  - rear : O(n)
- Application :
  - Palindrome Checker :
    - radar
    - deed
    ```
    def is_palindrome(s):
        cleaned_str = ''.join(s.split()).lower()
        char_deque = deque(cleaned_str)

        while len(char_deque) > 1:
            if char_deque.remove_front() != char_deque.remove_rear():
                return False
        return True
    ```
#### Linked List
- Head = First Node
- Tail = Node with no next Node
- Reference variables can be used to implement the data structure known as a linked list
- Each reference in a linked list is a reference to the next node in the list
- Any element in a list can be accessed directly; however, you must traverse a linked list to access a particular node
- Items can be inserted into and deleted from a reference- based linked list without shifting data

- Operations:
  - add()
  - remove()
  - search()
  - is_empty()
  - size()

- Implementation :
    ``` 
    class Node:

    def __init__(self, init_data):
            self.data = init_data
            self.next = None
            
    def get_data(self): 
        return self.data
        
    def get_next(self):
        return self.next
        
        
    def set_data(self, new_data):
        self.data = newdata
        
    def set_next(self, new_next):
        self.next = new_next
    ```
- Node Insert :
![NodeInsert](static/NodeInsert.png)
    ```
    def insert(head, new_node, position):
    if position == 0:
        new_node.next = head
        return new_node
        
    current = head
    previous = None
    for i in range(position):
        if current is None:
            break
        previous = current
        current = current.next

    new_node.next = current
    previous.next = new_node
        
    return head
    ```
- Node Delete :
![NodeDelete](static/NodeDelete.png)
    ```
    def delete(head, value):
        if head is None:
            return head
        
        if head.value == value:
            return head.next
        
        current = head
        
        while current.next is not None:
            if current.next.value == value:
                current.next = current.next.next
                return head
            current = current.next
        
        return head
    ```
- Traversal :
    ```
    curr = self.head
    while curr != None:
    print(curr.get_data())
    curr = curr.get_next()
    ```

- Node Search :
    ```
    curr = self.head
    while curr != None:
    if curr.get_data() == item: 
        return True
    else:
        curr = curr.get_next()
    return False
    ```

- Size :
    ```
    def size():
        curr = self.head
        count = 0
        while curr != None:
            count = count + 1
            curr = curr.get_next()
        return count
        
    # cached
    def __init__():
        self.count = 0
        
    def insert/delete()
        .....
        self.count++/--
    ```

- BigO :
![LinkedListBigO](static/LinkedListBigO.png)


- Ordered List :
- Implementation :
    ```
    def insert(self, item):
        new_node = Node(item)
        current = self.head
        previous = None
        stop = False

        while current is not None and not stop:
            if current.get_data() > item:
                stop = True
            else:
                previous = current
                current = current.get_next()
        
        if previous is None:  # Insert at the head
            new_node.set_next(self.head)
            self.head = new_node
        else:  # Insert in the middle or end
            new_node.set_next(current)
            previous.set_next(new_node
        
    def search(self, item):
        current = self.head
        while current is not None:
            if current.get_data() == item:
                return True
            elif current.get_data() > item:
                return False
            current = current.get_next()
        return False
    ```


- Unordered vs Ordered :
  - Sorted in terms of characteristics
  - add != insert ![UnorederedVSOrderedBigO](static/UnorederedVSOrderedBigO.png) 

##### Singly Linked List
  - Head, also Tail referencing to last Node
  - Useful for queue-like structure, e.g. a waiting list

- Implementation : 
    ```
    def add_to_tail(node):
        if count <= 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        
        self.count += 1
        
    def remove_tail():    
        prev = self.head
        while (prev.get_next() != self.tail):
            prev = prev.get_next()
        prev.set_next(None)
        self.tail = prev
        self.count -= 1
        
    def remove_head():
        self.head = self.head.get_next()
        if self.head == None:
            self.tail = None
        self.count -= 1
    ```
- BigO : 
  ![SinglyLinkedListBigO](Singlystatic/LinkedListBigO.png)


##### Doubly Linked List
- data
- prev node
- next node

- Operations :
    ![DoublyLinkedListOps](static/DoublyLinkedListOps.png)

- Implementation :
  - insert:
    - case1 : empty list
    - case2 : at the beginning of the list
    - case3 : at the end of the list
  ```
    class NodeDLL:
        def __init__(self, init_data, next_node=None, prev_node=None):
            self.data = init_data
            self.next = next_node
            self.prev = prev_node

        def get_data(self):
            return self.data

        def get_prev(self):
            return self.prev

        def get_next(self):
            return self.next

        def set_data(self, new_data):
            self.data = new_data

        def set_next(self, new_next):
            self.next = new_next

        def set_prev(self, new_prev):
            self.prev = new_prev


    class DoublyLinkedList:
        def __init__(self):
            self.head = None
            self.tail = None

        def append(self, new_data):
            new_node = NodeDLL(new_data)
            if not self.head:
                self.head = new_node
                self.tail = new_node
            else:
                self.tail.set_next(new_node)
                new_node.set_prev(self.tail)
                self.tail = new_node

        def prepend(self, new_data):
            new_node = NodeDLL(new_data)
            if not self.head:
                self.head = new_node
                self.tail = new_node
            else:
                new_node.set_next(self.head)
                self.head.set_prev(new_node)
                self.head = new_node

        def delete(self, node):
            if not node:
                return
            if node == self.head:
                self.head = node.get_next()
                if self.head:
                    self.head.set_prev(None)
            elif node == self.tail:
                self.tail = node.get_prev()
                if self.tail:
                    self.tail.set_next(None)
            else:
                prev_node = node.get_prev()
                next_node = node.get_next()
                if prev_node:
                    prev_node.set_next(next_node)
                if next_node:
                    next_node.set_prev(prev_node)

        def display_forward(self):
            current = self.head
            while current:
                print(current.get_data(), end=' ')
                current = current.get_next()
            print()

        def display_backward(self):
            current = self.tail
            while current:
                print(current.get_data(), end=' ')
                current = current.get_prev()
            print()
    ```

##### Circular Doubly Linked List
- dummy head
- prev node of dummy head = last node
- next of the last node 
- Structure :
    ![CircularDoublyLinkedListSimple](static/CircularDoublyLinkedListSimple.png)
    ![CircularDoublyLinkedList](static/CircularDoublyLinkedList.png)
    ![CircularDoublyLinkedListEmpty](static/CircularDoublyLinkedListEmpty.png)
    
- BigO :
  ![CircularDoublyLinkedListBigO](CircularDoublystatic/LinkedListBigO.png)

##### Circular Doubly Linked List Without Dummy
- less one node, bit more memory and simpler
- but insert/remove on empty must be careful
![CircularDoublyLinkedListNoDum](static/CircularDoublyLinkedListNoDum.png)


### Tree
- Abstract model of hierachical structure
- Parent-Child relation
- Efficient O(logn)
- Efficiency depends on height


- Terminology :
- ![TreeTerms](static/TreeTerms.png)
  - Root: node without parent (A)
  - Internal node: node with at least one child (A, B, C, F)
  - External node (leaf): node wit children (E, I, J, K, G, H, D)
  - Ancestors of a node: parent, grandparent, grand-grandparent, etc.
  - Depth of node: no. of ancestors
  - Height of a tree: max depth of any node (3)
  - Descendant of a node: child, grandchild,grand-grandchild etc.
  - Subtree: tree consisting of a node and its descendants
- Traversal
  - A traversal (tree walk) visits the nodes of a tree in a systematic manner
  - ![TreeTraversal](static/TreeTraversal.png)
  - Preorder :
    - In a preorder traversal, a node visited before its descendants
    ```
        def preOrder(root):
            visit(root)
            for child in root:
                preOrder(child)
    ```
    - Application : print a structured document
  - Postorder :
    - In a postorder traversal, a node is visited after its descendants
    ```
        def postOrder(root):
            for child in root:
                postOrder(child)
            visit(root)
    ```
#### Binary Tree
- max no. of children = 2
- ordered child
- left child + right child
- Properties node(n), exnode(e), innode(i), height(h):
  - e = i + 1
  - n = 2e - 1
  - h <= i
  - h <= (n-1)/2
  - e <= 2^h
  - h >= lo2ge
  - h >= lo2g(n+1) - 1
- Applications:
  - arithmetic 
  - expressions decision 
  - processes searching
- Traversal 
  - In-Order : Produces a sorted order of values.
  - Pre-Order : Useful for copying the tree.
  - Post-Order : Useful for deleting the tree.
- Implementation :
    - Inorder :
    - This function visits the left subtree, then the current node, and finally the right subtree. This results in a sorted order for a BST.
        ```
        def inOrder(root):
            result.extend(inOrder(root.left))
            visit(root)
            result.extend(inOrder(root.right))
        ```

    - Insertion ：
        ```
        def insert(root, value):
            if root is None:
                return TreeNode(value)
            
            if value < root.value:
                root.left = insert(root.left, value)
            elif value > root.value:
                root.right = insert(root.right, value)
            
            return root
        ```

    -  Deletion :
        ```
        def delete(root, value):
            if root is None:
                return root

            if value < root.value:
                root.left = delete(root.left, value)
            elif value > root.value:
                root.right = delete(root.right, value)
            else:
                # Node with only one child or no child
                if root.left is None:
                    return root.right
                elif root.right is None:
                    return root.left
                
                # Node with two children: Get the inorder successor (smallest in the right subtree)
                min_larger_node = find_min(root.right)
                root.value = min_larger_node.value
                root.right = delete(root.right, min_larger_node.value)

            return root

        def find_min(node):
            current = node
            while current.left is not None:
                current = current.left
            return current
        ```

- BigO :
    
    | Operation      | Balanced BST | Unbalanced BST |
    |----------------|--------------|-----------------|
    | Search         | O(log n)     | O(n)            |
    | Insertion      | O(log n)     | O(n)            |
    | Deletion       | O(log n)     | O(n)            |
    | Traversal      | O(n)         | O(n)            |
    | Space (Recursive)| O(log n)   | O(n)            |


### Graph



## Algorithmn

### Design
- Divide and Conquer :
    - Description: This technique involves dividing a problem into smaller subproblems, solving each subproblem independently, and then combining their solutions to solve the original problem.
    - Examples: Merge sort, quicksort, binary search, and the Fast Fourier Transform (FFT).
- Dynamic Programming
    - Description: This approach solves problems by breaking them down into simpler overlapping subproblems and storing the results of these subproblems to avoid redundant computations.
    - Examples: Fibonacci sequence, knapsack problem, and shortest path problems (like Dijkstra’s and Bellman-Ford).
- Greedy Algorithms
    - Description: Greedy algorithms build a solution piece by piece, always choosing the next piece that offers the most immediate benefit. They do not always produce the optimal solution but can be efficient for certain problems.
    - Examples: Prim’s and Kruskal’s algorithms for minimum spanning trees, Huffman coding, and activity selection.
- Backtracking
    - Description: This technique involves building a solution incrementally and abandoning solutions as soon as it determines that they cannot lead to a valid complete solution. It is often used in constraint satisfaction problems.
    - Examples: N-Queens problem, Sudoku solver, and permutations of a set.
- Brute Force
    - Description: A straightforward approach that tries all possible solutions to find the best one. This method is often simple to implement but can be inefficient for large inputs.
    - Examples: Traveling salesman problem (TSP) using exhaustive search, and finding all combinations of a set.
- Branch and Bound
    - Description: This search algorithm systematically explores all possible solutions while pruning branches that cannot yield better solutions than the best found so far. It is often used in optimization problems.
    - Examples: Integer programming and traveling salesman problem.
- Randomized Algorithms
    - Description: These algorithms make random choices in their logic to achieve good average-case performance. They are often simpler and faster than deterministic algorithms for specific problems.
    - Examples: Randomized quicksort and Monte Carlo methods.
- Graph Algorithms
    - Description: Techniques specifically designed to solve problems related to graphs, including traversal, shortest paths, and minimum spanning trees.
    - Examples: Depth-first search (DFS), breadth-first search (BFS), Dijkstra’s algorithm, and Kruskal’s algorithm.
- Sorting Algorithms
    - Description: Various methods for arranging data in a particular order.
    - Examples: Quicksort, mergesort, heapsort, and bubblesort.
- Searching Algorithms
    - Description: Techniques for finding an element in a data structure.
    - Examples: Binary search (for sorted arrays) and linear search.
- Heuristic Methods
    - Description: Techniques that find satisfactory solutions for complex problems more quickly when classic methods are too slow. Often used in optimization and search problems.
    - Examples: Genetic algorithms and simulated annealing.

### Recursive
- 4 Keys
  - How to define samller problem of same type
  - How can each call dinimish size
  - What case of problem can be base case
  - Can you reach base case
- Base Case
  - value for which perform no calls.
  - every recursive chain MUST reach base case.
- Recurvsive Call
  - each call solve an IDENTITICAL and SMALLER problem.
  - should be defined so that it towards base case, no problem smaller than base case is allowed.
- Vizualization: ![RecursiveTrace](static/RecursiveTrace.png)
#### Binary Search
- ![BinarySearch](static/BinarySearch.png)
- BigO logn : ![BinarySearchBigO](static/BinarySearchBigO.png)

#### Type 
- Head Recursion: ![RecursionHead](static/RecursionHead.png)
- Tail Recursion: ![RecursionTail](static/RecursionTail.png)
- More : [geeksforgeeks types of recursions](https://www.geeksforgeeks.org/types-of-recursions/)

#### Fibonacci Sequence
![FibonacciCase](static/FibonacciCase.png)
```
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
```
- BigO : O(n) (make n recursive calls)


![FibonacciTree](static/FibonacciTree.png)
- BigO :
  - Time Complexity: O(n) (Cached) / O(n^2)
  - Space Complexity: O(n) (Cached) / O(n) (due to the recursion stack)
#### Power Function

![PowerFunction](static/PowerFunction.png)
- Intuition :
  -  b^100 = b^50 * b^50
  -  b^101 = b * b^50 * b^50
-  Definition :
   -  n = 0 -> b^n = 1  
   -  n > 0 && = even -> b^n/2 * b^n/2
   -  n > 0 && = odd -> b * b^n/2 * b^n/2
- Implementation :
  - recursive :
    ```
    def power(x, n):
        if n == 0:
            return 1  # Base case: x^0 = 1
        elif n < 0:
            return 1 / power(x, -n)  
        elif n % 2 == 0:
            half_power = power(x, n // 2)  
            return half_power * half_power  
            half_power = power(x, (n - 1) // 2)  
            return x * half_power * half_power  
    ```
  -  recursive simple :
        ```
        def power_recursive(x, n):
            if n == 0:
                return 1  # Base case: x^0 = 1
            elif n < 0:
                return 1 / power_recursive(x, -n) 
            else:
                return x * power_recursive(x, n - 1)
        ``` 
  - iterative  :
    ```
    def power_iterative(x, n):
        result = 1
        for _ in range(n):
            result *= x
        return result
    ```
    
- BigO :
  - Time Complexity: O(logn) / O(n) (re. simple) 
  - Space Complexity: O(logn) / O(n) (re. simple) / O(1) (iterative)

#### Hanoi Tower

```
def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    hanoi(n - 1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    hanoi(n - 1, auxiliary, target, source)
```
![HanoiTowerTree](static/HanoiTowerTree.png)
![HanoiTower](static/HanoiTower.gif)
- Step : 2^n - 1
- BigO : 
  - Time Complexity: O(2^n)
  - Space Complexity: O(n)



### Sorting
- compare function:
  ```
    def cmp(a, b):
        if a > b:
            t = a
            a = b
            b = t
        return a, b
  ```
#### Bubble Sort
![BubbleSort](static/BubbleSort.png)
  -  Number of pass-throughs (steps) = number of elements - 1 
  -  After m iterations, the rightmost m elements are sorted into their correct place
  - Largest elements tend to ‘bubble-up’ to the right
  - Implementation :
    ```
    def bubble_sort(arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                arr[j], arr[j+1] = cmp(arr[j],arr[j+1])
        return arr
    ```
  - BigO : n2 ( triangle-like, N(N - 1)/2 )
  - Implementation of early exit for optimizing : 
    ```
    def bubble_sort(arr):
        n = len(arr)
        for i in range(n):
            swapped = False
            for j in range(0, n-i-1):
                arr[j], arr[j+1] = cmp(arr[j],arr[j+1])
                swapped = True
            if not swapped:
                break
        return arr
    ```
#### Parallel Odd Even Sort 
![ParallelOddEvenSort](static/ParallelOddEvenSort.png)
- parallel processing
- good for smaller sequences
- Implementation :
    ```
    def odd_even_sort(arr):
        n = len(arr)
        sorted = False

        while not sorted:
            sorted = True

            for i in range(1, n - 1, 2):
                arr[j], arr[j+1] = cmp(arr[j],arr[j+1])
                sorted = False
                    
            for i in range(0, n - 1, 2):
                arr[j], arr[j+1] = cmp(arr[j],arr[j+1])
                sorted = False

        return arr
    ```
    
#### Selection Sort
![SelectionSort](static/SelectionSort.png)
- One swap per pass -> less swaps (O(n))
- Implementation :
    ```
    def selection_sort(arr):
        n = len(arr)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_index]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
        return arr

    ```
- BigO: n2 (N(N - 1)/2)


#### Insertion Sort
![InsertionSort](static/InsertionSort.gif)
- Implementation :
    ```
    def insertion_sort(arr):
        n = len(arr)
        for i in range(1, n):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr
    ```


- BigO: n2 (N(N - 1)/2)
- Average: O(n2)/2
- Best case: O(n)


#### Shell Sort
- Insertion sort has fewer comparisons than Selection sort 
- Selection sort has fewer moves‐swaps than Insertion sort 
- => IDEA: compare/shift non‐neighbouring elements

- On average shell sort has fewer comparisons than Selection sort and Bubble sort, 
- and fewer moves than Insertion sort
- Shell sort is based on the Insertion sort algorithm,
- => BUT: instead of shifting elements many times by one step, it makes larger moves

- Implementation :
  - Divide the list into lots of smaller sublists
  - i gap to i sublists
  - Each of which is sorted using an insertion sort
  - Then repeat sorting with reduced gap (=> fewer, but larger sublists) until gap is 1
    ![ShellSort](static/ShellSort.gif)
    ```
    # dual
    def insertion_sort_with_gap(arr, gap):
        n = len(arr)
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp

    def shell_sort(arr):
        n = len(arr)
        gap = n // 2
        while gap > 0:
            insertion_sort_with_gap(arr, gap)
            gap //= 2
        return arr
    
    # single
    def shell_sort(arr):
        n = len(arr)
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                temp = arr[i]
                j = i
                while j >= gap and arr[j - gap] > temp:
                    arr[j] = arr[j - gap]
                    j -= gap
                arr[j] = temp
            gap //= 2
        return arr
    ```
- Gap :
  -  A default option for gap sizes is 2 ‐1, i.e. [..., 31, 15, 7, 3,1]
  - Research in the optimal gap sequence is ongoing
  - A often quoted empirical derived gap sequence is [701, 301, 132, 57, 23, 10, 4, 1]
- BigO:
  - Worst Case: O(n2)
  - Average Case: O(n3/2)
  - Best Case: O(nlogn)
  - Improved Gap Sequences: O(nlo2gn) (Using more sophisticated gap sequences, such as the Hibbard or Sedgewick sequences)

#### Merge Sort
- Recursive
- Base case : empty / one item
- Cut the list in half
- Sort each half
- Merge the two sorted halves

- Implementation :
    - ![MergeSort](static/MergeSort.gif)
    - ![MergeSortDebug](static/MergeSortDebug.png)
    - ![MergeSortTree](static/MergeSortTree.png)
    ```
    def merge_sort(arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]

            merge_sort(left_half)
            merge_sort(right_half)

            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                arr[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1

        return arr
    ```
- BigO :
  - O(nlogn)
  - The time for sorting a list of size 1 is constant, i.e. T(1)=1
  - The time for sorting a list of size n is the time of sorting the two
halves plus the time for merging, i.e. T(n) = 2*T(n/2)+n
  - Can prove: T(n) = n + n log n

#### Summary
![MergeSortBigO](static/MergeSortBigO.png)

- Radix sort was invented in the late 1800s for physically sorting punched cards for the US census. It’s still used today in software because it’s very fast on numeric and string data.
- Merge sort appears to have been invented by John von Neumann to validate his stored-program computer model (the von Neumann architecture). It works well as a sorting algorithm for low-memory computers processing data that’s streamed through the machine, hence its popularity in the 1960s and 1970s. And it’s a great testbed for divide-and-conquer techniques, making it popular in algorithms classes.
- Insertion sort seems to have been around forever. Even though it’s slow in the worst case, it’s fantastic on small inputs and mostly-sorted data and is used as a building block in other fast sorting algorithms.
- Quicksort was invented in 1961. It plays excellently with processor caches, hence its continued popularity.
- Sorting networks were studied extensively many years back. They’re still useful as building blocks in theoretical proof-of-concept algorithms like signature sort.
- Timsort was invented for Python and was designed to sort practical, real-world sequences faster than other sorts by taking advantage of common distributions and patterns.
- Introsort was invented as a practical way to harness the speed of quicksort without its worst-case behavior.
- Shellsort was invented over fifty years ago and was practical on the computers of its age. Probing its theoretical limits was a difficult mathematical problem for folks who studied it back then.
- Thorup and Yao’s O(n sqrt(log log n))-time integer sorting algorithm was designed to probe the theoretical limits of efficient algorithms using word-level parallelism.
- Cycle sort derives from the study of permutations in group theory and is designed to minimize the number of memory writes made when sorting the list.
- Heapsort is noteworthy for being in-place and yet fast in practice. It’s based on the idea of implicitly representing a nontrivial data structure.


### Searching
- ? exist
- ? location
- ? how many match
- multiple time to search in a single collection


- Application 
  - parsing strings (searching characters)
  - database queries (records filtering)
  - finding files on disk

#### Linear Search
- Go through all items and check if any equals the key
- needs to go through all elements in the worst case
- implements an early exit

- Implementation : 
    ```
    single
    def linear_search(arr, target):
        for index, value in enumerate(arr):
            if value == target:
                return index
        return -1
    
    # multiple
    def linear_search_multiple(arr, target):
        indices = []
        for index, value in enumerate(arr):
            if value == target:
                indices.append(index)
        return indices
    ```
- BigO :
  - Worst case : O(n)
  - Average : O(n)/2
  - Best : O(1)
  
- Linear Search Sorted :
    ```
    def linear_search_sorted(arr, target):
        for index, value in enumerate(arr):
            if value == target:
                return index
            if value > target: 
                break
        return -1
    ```

#### Binary Search
- Perform on sorted list
- Method of choice when it comes to searching

- Implementation :
    ```
    # Sorted List
    def binary_search_list(arr, target):
        left, right = 0, len(arr) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return -1
    ```
    ![static/BinarySearch.gif](static/BinarySearch.gif)
    ```
    class TreeNode:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

        def insert_bst(root, value):
            if root is None:
                return TreeNode(value)
            if value < root.value:
                root.left = insert_bst(root.left, value)
            else:
                root.right = insert_bst(root.right, value)
            return root

        def binary_search_bst(root, target):
            if root is None:
                return None
            if root.value == target:
                return root
            elif target < root.value:
                return binary_search_bst(root.left, target)
            else:
                return binary_search_bst(root.right, target)

    ```
    
- BigO : O(logn)
- List need less overhead and memory, Tree has faster insert/delete (O(nlog) < O(n))
