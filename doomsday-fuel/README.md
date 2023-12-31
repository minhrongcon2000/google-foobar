# Doomsday Fuel

Making fuel for the LAMBCHOP's reactor core is a tricky process because of the exotic matter involved. It starts as raw ore, then during processing, begins randomly changing between forms, eventually reaching a stable form. There may be multiple stable forms that a sample could ultimately reach, not all of which are useful as fuel.

Commander Lambda has tasked you to help the scientists increase fuel creation efficiency by predicting the end state of a given ore sample. You have carefully studied the different structures that the ore can take and which transitions it undergoes. It appears that, while random, the probability of each structure transforming is fixed. That is, each time the ore is in 1 state, it has the same probabilities of entering the next state (which might be the same state). You have recorded the observed transitions in a matrix. The others in the lab have hypothesized more exotic forms that the ore can become, but you haven't seen all of them.

Write a function solution(m) that takes an array of array of nonnegative ints representing how many times that state has gone to the next state and return an array of ints for each terminal state giving the exact probabilities of each terminal state, represented as the numerator for each state, then the denominator for all of them at the end and in simplest form. The matrix is at most 10 by 10. It is guaranteed that no matter which state the ore is in, there is a path from that state to a terminal state. That is, the processing will always eventually end in a stable state. The ore starts in state 0. The denominator will fit within a signed 32-bit integer during the calculation, as long as the fraction is simplified regularly.

For example, consider the matrix m:

```bash
[
[0,1,0,0,0,1], # s0, the initial state, goes to s1 and s5 with equal probability
[4,0,0,3,2,0], # s1 can become s0, s3, or s4, but with different probabilities
[0,0,0,0,0,0], # s2 is terminal, and unreachable (never observed in practice)
[0,0,0,0,0,0], # s3 is terminal
[0,0,0,0,0,0], # s4 is terminal
[0,0,0,0,0,0], # s5 is terminal
]
```

So, we can consider different paths to terminal states, such as:

```bash
s0 -> s1 -> s3
s0 -> s1 -> s0 -> s1 -> s0 -> s1 -> s4
s0 -> s1 -> s0 -> s5
```

Tracing the probabilities of each, we find that

- s2 has probability 0
- s3 has probability 3/14
- s4 has probability 1/7
- s5 has probability 9/14

So, putting that together, and making a common denominator, gives an answer in the form of [s2.numerator, s3.numerator, s4.numerator, s5.numerator, denominator] which is [0, 3, 2, 9, 14].

(I forgot to copy the test cases, but the problem should be clarified enough!)

<details>
    <summary>Hint 1</summary>
    This is Markov chain.
</details>

<details>
    <summary>Hint 2</summary>
    You are allowed to google, this is absorbing markov chain, so the solution is fairly complex.
</details>

<details>
    <summary>Solution</summary>

This problem is a typical absorbing markov chain problem. If you have math knowledge before, or do a little bit of Google search on this keyword, it shold give you a solution resembling [here](https://brilliant.org/wiki/absorbing-markov-chains/). I think the most difficult part is to calculate the inverse matrix accurately up to fractional level. In Linear Algebra, the formula for calculating inverse matrix analytically is mentioned [here](https://en.wikipedia.org/wiki/Invertible_matrix#Methods_of_matrix_inversion)

Space complexity: $O(N^2)$
Time complexity: $O(N^3)$, for calculating inverse matrix
</details>
