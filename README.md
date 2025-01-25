# Python_LeetCode_Problem_Solve
### Visit My LeetCode Account for more and continuous progress : [Does_Not_exist](https://leetcode.com/u/Does_Not_exist/)

# LeetCode Problem Solving Repository

Welcome to my LeetCode Problem Solving Repository! 🚀 This repository is dedicated to documenting my journey of solving algorithmic problems from [LeetCode](https://leetcode.com). Here, you'll find my solutions to various coding challenges, organized and structured for easy navigation.

## About the Repository

This repository is designed to:

- Track my progress in solving LeetCode problems.
- Serve as a reference for common algorithmic patterns and techniques.
- Share solutions for learning and collaboration.

## Repository Structure

The repository is organized by:

- **Problem Category**: Problems are grouped into categories like Arrays, Strings, Dynamic Programming, Graphs, etc.
- **Difficulty**: Each problem is labeled with its difficulty level (Easy, Medium, Hard).
- **Programming Language**: Solutions are primarily implemented in `Python` (or mention other languages if applicable).

```
leetcode-problems/
├── Arrays/
├── Strings/
├── DynamicProgramming/
├── Graphs/
└── ...
```

## File Naming Convention

Each solution file follows this format for consistency:

```
[problem-number]-[problem-title].extension
```

Example: `1-two-sum.py`

## Common Patterns for Solving Problems

Here are some common patterns and techniques used in solving LeetCode problems:

### 1. Sliding Window

Used for problems involving subarrays or substrings, typically to optimize brute-force solutions.

```python
def max_sum_subarray(nums, k):
    max_sum = float('-inf')
    window_sum = 0
    start = 0

    for end in range(len(nums)):
        window_sum += nums[end]
        if end >= k - 1:
            max_sum = max(max_sum, window_sum)
            window_sum -= nums[start]
            start += 1

    return max_sum
```

### 2. Two Pointers

Efficient for problems involving arrays or linked lists, especially for finding pairs or partitions.

```python
def two_sum(nums, target):
    nums = sorted(enumerate(nums), key=lambda x: x[1])
    left, right = 0, len(nums) - 1

    while left < right:
        total = nums[left][1] + nums[right][1]
        if total == target:
            return [nums[left][0], nums[right][0]]
        elif total < target:
            left += 1
        else:
            right -= 1
```

### 3. Binary Search

Helpful for problems where the search space can be divided, like finding elements in sorted arrays or searching for boundaries.

```python
def binary_search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
```

### 4. Dynamic Programming

Solves problems by breaking them into overlapping subproblems and storing solutions to avoid redundant computations.

```python
def fibonacci(n):
    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]
```

### 5. Depth-First Search (DFS)

Used for traversing or searching tree and graph structures.

```python
def dfs(graph, start, visited):
    visited.add(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
```

### 6. Breadth-First Search (BFS)

Great for finding the shortest path or level-order traversal in graphs or trees.

```python
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            queue.extend(graph[node] - visited)
```

### 7. Backtracking

Used for problems that involve exploring all potential solutions, such as permutations and combinations.

```python
def permute(nums):
    result = []

    def backtrack(start):
        if start == len(nums):
            result.append(nums[:])
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            backtrack(start + 1)
            nums[start], nums[i] = nums[i], nums[start]

    backtrack(0)
    return result
```

### 8. Greedy Algorithms

Optimal for problems where local optimization leads to global optimization, like interval scheduling or coin change.

```python
def coin_change(coins, amount):
    coins.sort(reverse=True)
    count = 0

    for coin in coins:
        count += amount // coin
        amount %= coin

    return count if amount == 0 else -1
```

### 9. Divide and Conquer

Breaks problems into smaller subproblems, solves them independently, and combines their results.

```python
def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])

    return merge(left, right)

def merge(left, right):
    sorted_list = []
    while left and right:
        if left[0] < right[0]:
            sorted_list.append(left.pop(0))
        else:
            sorted_list.append(right.pop(0))
    sorted_list.extend(left or right)
    return sorted_list
```

## How to Use This Repository

1. Clone the repository:

   ```bash
    [git clone https://github.com/your-username/leetcode-problems.git](https://github.com/shehab0911/Python_LeetCode_Problem_Solve.git)
   ```

2. Navigate to the desired category and problem to view the solution.

3. Learn, improve, and feel free to contribute! 🤝

## Progress Tracking

| Difficulty | Solved Problems |
| ---------- | --------------- |
| Easy       | X Problems      |
| Medium     | X Problems      |
| Hard       | X Problems      |

## Contributing

Contributions are welcome! If you have alternative solutions or optimizations, feel free to submit a pull request.

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your message here"
   ```
4. Push to your branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a pull request.

## License

This repository is licensed under the [MIT License](LICENSE). Feel free to use the code for educational and personal purposes.

---

Happy coding! 🎉 If you find this repository helpful, don't forget to give it a ⭐!



