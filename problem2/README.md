# Don't Get Volunteered

As a henchman on Commander Lambda's space station, you're expected to be resourceful, smart, and a quick thinker. It's not easy building a doomsday device and ordering the bunnies around at the same time, after all! In order to make sure that everyone is sufficiently quick-witted, Commander Lambda has installed new flooring outside the henchman dormitories. It looks like a chessboard, and every morning and evening you have to solve a new movement puzzle in order to cross the floor. That would be fine if you got to be the rook or the queen, but instead, you have to be the knight. Worse, if you take too much time solving the puzzle, you get "volunteered" as a test subject for the LAMBCHOP doomsday device!

To help yourself get to and from your bunk every day, write a function called solution(src, dest) which takes in two parameters: the source square, on which you start, and the destination square, which is where you need to land to solve the puzzle.  The function should return an integer representing the smallest number of moves it will take for you to travel from the source square to the destination square using a chess knight's moves (that is, two squares in any direction immediately followed by one square perpendicular to that direction, or vice versa, in an "L" shape).  Both the source and destination squares will be an integer between 0 and 63, inclusive, and are numbered like the example chessboard below:

```bash
-------------------------
| 0| 1| 2| 3| 4| 5| 6| 7|
-------------------------
| 8| 9|10|11|12|13|14|15|
-------------------------
|16|17|18|19|20|21|22|23|
-------------------------
|24|25|26|27|28|29|30|31|
-------------------------
|32|33|34|35|36|37|38|39|
-------------------------
|40|41|42|43|44|45|46|47|
-------------------------
|48|49|50|51|52|53|54|55|
-------------------------
|56|57|58|59|60|61|62|63|
-------------------------
```

## Languages

To provide a Python solution, edit solution.py
To provide a Java solution, edit Solution.java

### Test cases

Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

### Python cases

Input:

```python
solution.solution(0, 1)
```

Output:

```bash
3
```

Input:

```python
solution.solution(19, 36)
```

Output:

```bash
1
```

### Java cases

Input:

```java
Solution.solution(19, 36)
```

Output:

```bash
1
```

Input:

```java
Solution.solution(0, 1)
```

Output:

```bash
3
```

<details>
    <summary>Hint 1</summary>
    Knight move can form a graph data structure. Your job is to find the shortest path between 2 nodes.
</details>

<details>
    <summary>Hint 2</summary>
    Should you use DFS or should you use BFS?
</details>

<details>
    <summary>Solution</summary>
    This is the famous problem `Knight's Tour`. The only difference is that you need to find the shortest path between 2 nodes instead of finding Halmington path, So you need to traverse the knight's movement graph, but which method to traverse? DFS is very likely to take the longest path while BFS is likely to take the shortest path. Hence, you need to implement DFS to traverse knight's movement graph.

    Time complexity: O(1) (since the chessboard size is known; otherwise, it would be O(n^2))
    Space complexity: O(1) (same reason as above, O(n^2) when chessboard is unknown) 
</details>
