"""
https://leetcode.com/problems/friend-circles/

547. Friend Circles

There are N students in a class. 
Some of them are friends, while some are not. 
Their friendship is transitive in nature. 
For example, if A is a direct friend of B, and B is a direct friend of C, 
then A is an indirect friend of C. 
And we defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class. 
If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. 
And you have to output the total number of friend circles among all the students.

Example 1:

Input: 
[[1,1,0],
 [1,1,0],
 [0,0,1]]
Output: 2
Explanation:The 0th and 1st students are direct friends, so they are in a friend circle. 
The 2nd student himself is in a friend circle. So return 2.
 

Example 2:

Input: 
[[1,1,0],
 [1,1,1],
 [0,1,1]]
Output: 1
Explanation:The 0th and 1st students are direct friends, 
the 1st and 2nd students are direct friends, 
so the 0th and 2nd students are indirect friends. 
All of them are in the same friend circle, so return 1.
 

Constraints:

1 <= N <= 200
M[i][i] == 1
M[i][j] == M[j][i]

Solution

建图
对于每一个学生用dfs遍历所有和他连接的同学
每次遍历前判断当前学生是不是被访问过，没访问过则circle += 1

"""

import collections
from typing import List


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        if not M:
            return 0
        graph = collections.defaultdict(list)
        n = len(M)
        for i in range(n):
            for j in range(n):
                if M[i][j] == 1:
                    graph[i].append(j)
                    graph[j].append(i)
        visited = set()
        count = 0
        for i in range(n):
            if i not in visited:
                count += 1
                self.dfs(i, visited, graph)
        return count

    def dfs(self, u, visited, graph):
        for v in graph[u]:
            if v not in visited:
                visited.add(v)
                self.dfs(v, visited, graph)
        return
