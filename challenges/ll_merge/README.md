## Challenge Description
Write a function called mergeLists which takes two linked lists as arguments. Zip the two linked lists together into one so that the nodes alternate between the two lists and return a reference to the head of the zipped list. Try and keep additional space down to O(1). You have access to the Node class and all the properties on the Linked List class as well as the methods created in previous challenges.

## Approach & Efficiency
To approach this challenge you are going to need to create a function that takes in two values (a list1 and a list2) You then want to create a while loop. Within the while loop you are going to need to set a pointer for each of the lists. and assign them to the head of each list. You then need to make your pointer ones next and to the location of pointer 2 and then take the pointer twos next and make it the value of ones next. Then assign the pointer one and pointer two to equil ones next and twos next.

## Solution
![Merge Linked List](/assets/merge.png)