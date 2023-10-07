# Please Pass the Coded Messages

You need to pass a message to the bunny workers, but to avoid detection, the code you agreed to use is... obscure, to say the least. The bunnies are given food on standard-issue plates that are stamped with the numbers 0-9 for easier sorting, and you need to combine sets of plates to create the numbers in the code. The signal that a number is part of the code is that it is divisible by 3. You can do smaller numbers like 15 and 45 easily, but bigger numbers like 144 and 414 are a little trickier. Write a program to help yourself quickly create large numbers for use in the code, given a limited number of plates to work with.

You have L, a list containing some digits (0 to 9). Write a function solution(L) which finds the largest number that can be made from some or all of these digits and is divisible by 3. If it is not possible to make such a number, return 0 as the solution. L will contain anywhere from 1 to 9 digits. The same digit may appear multiple times in the list, but each element in the list may only be used once.

## Languages

To provide a Java solution, edit Solution.java
To provide a Python solution, edit solution.py

## Test cases

Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

### Java cases

Input:

```java
Solution.solution({3, 1, 4, 1})
```

Output:

```bash
4311
```

Input:

```java
Solution.solution({3, 1, 4, 1, 5, 9})
```

Output:

```bash
94311
```

### Python cases

Input:

```python
solution.solution([3, 1, 4, 1])
```

Output:

```bash
4311
```

Input:

```python
solution.solution([3, 1, 4, 1, 5, 9])
```

Output:

```bash
94311
```

<details>
    <summary>Hint 1</summary>
    Basically this means find the longest subsequence whose sum is divisible by 3
</details>

<details>
    <summary>Hint 2</summary>
    Reverse hint 1, find the minimum number of elements whose removal results in a set with sum divisible by 3
</details>

<details>
    <summary>Solution</summary>
    Let s be the sum of all elements modulo 3. What we could do is to count the frequency of each digit from 0 to 9. If s mod 3 = 0, then the entire set is the longest set. If s mod 3 = 1, then we just need to decrease the frequency of digits 1, 4, 7 by 1 and form the largest number from there. If these frequencies are 0, then we decreases the frequency of 2, 5, 8 by 2. The other case is similar
</details>
