# Reverse an Array
<!-- Short summary or background information -->

## Challenge
**Write a function called BinarySearch which takes in 2 parameters: a sorted array and the search key. Without utilizing any of the built-in methods available to your language, return the index of the array’s element that is equal to the search key, or -1 if the element does not exist.**

## Approach & Efficiency
* First I wanted to create the function and pass in arr and key as params.
* I then would want to set the value of a 'low' variable to 0.
* As well as set the 'high' variable to the length of the array.
* I then would want to run a while loop only if the the length of the array is greater than 0.
* If the array passed is empty then return -1.
* I would then set a 'middle' variable to the sum of the high and low values divided by 2.
* I would then compare the middle value with the key value and either
    * return value if equil
    * adjust high and low values accordingly
    * or return -1 if the key doesnt exist.

## Solution
![array_binary_search](/assets/array_binary_search.png)