# Implement a Queue using two Stacks.

## Author: Terrell Douglas and Anastasia Lebedeva

## Challenge
Create a brand new PseudoQueue class. This PseudoQueue class will implement our standard queue interface (enqueue(value), dequeue()), but will internally only utilize 2 Stack objects.

### Example Input ---> Output:
**enqueue(value)**
Input: </br>
[10]->[15]->[20] </br>
Arg: </br>
5 </br>
Output: </br>
[5]->[10]->[15]->[20] </br>

Input: </br>
Empty </br>
Arg: </br>
5 </br>
Output: </br>
[5]->[ </br>

**dequeue()** </br>
Input: </br>
[5]->[10]->[15]->[20] </br>

Output: </br>
20 </br>

Internal State: </br>
[5]->[10]->[15]) </br>


## Solution
![Whiteboard Solution](/asset/queue_and_stacks.png)