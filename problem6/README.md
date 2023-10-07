# The Grandest Staircase Of Them All

With the LAMBCHOP doomsday device finished, Commander Lambda is preparing to debut on the galactic stage -- but in order to make a grand entrance, Lambda needs a grand staircase! As the Commander's personal assistant, you've been tasked with figuring out how to build the best staircase EVER.

Lambda has given you an overview of the types of bricks available, plus a budget. You can buy different amounts of the different types of bricks (for example, 3 little pink bricks, or 5 blue lace bricks). Commander Lambda wants to know how many different types of staircases can be built with each amount of bricks, so they can pick the one with the most options.

Each type of staircase should consist of 2 or more steps. No two steps are allowed to be at the same height - each step must be lower than the previous one. All steps must contain at least one brick. A step's height is classified as the total amount of bricks that make up that step.
For example, when N = 3, you have only 1 choice of how to build the staircase, with the first step having a height of 2 and the second step having a height of 1: (# indicates a brick)

```bash
#
##
21
```

When N = 4, you still only have 1 staircase choice:

```bash
#
#
##
31
```

But when N = 5, there are two ways you can build a staircase from the given bricks. The two staircases can have heights (4, 1) or (3, 2), as shown below:

```bash
#
#
#
##
41
```

```bash
#
##
##
32
```

Write a function called solution(n) that takes a positive integer n and returns the number of different staircases that can be built from exactly n bricks. n will always be at least 3 (so you can have a staircase at all), but no more than 200, because Commander Lambda's not made of money!

## Languages

To provide a Java solution, edit Solution.java
To provide a Python solution, edit solution.py

## Test cases

Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

### Java cases

Input:

```java
Solution.solution(200)
```

Output:

```bash
487067745
```

Input:

```java
Solution.solution(3)
```

Output:

```bash
1
```

### Python cases

Input:

```python
solution.solution(200)
```

Output:

```bash
487067745
```

Input:

```python
solution.solution(3)
```

Output:

```bash
1
```

<details>
    <summary>Hint 1</summary>
    This is a problem of finding the number of ways to split a number into sums of other numbers.
</details>

<details>
    <summary>Hint 2</summary>
    Let's look at it in another way. Since all operands in the addition should be smaller than the input itself, this problem could be seen as finding the number of subsets whose sum is equal to input number
</details>

<details>
    <summary>Solution</summary>
    Let s[i, j] is the number of subsets from the set {1, 2, 3, ..., i} whose sum is j. We could see that if we add i + 1 to the set {1, 2, ..., i}, you can do 2 things:
    <ul>
        <li>If i + 1 >= j, then the required subset remains the same (s[i + 1, j] = s[i, j])</li>
        <li>If i + 1 <= j, then the required subset is s[i + 1, j] = s[i, j] + s[i, j - i - 1]</li>
    </ul>
    Then, we can just apply dynamic programming to find out the solution.
</details>
