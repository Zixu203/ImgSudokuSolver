# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 23:17:17 2024
@author: 梓旭
"""

from copy import deepcopy

class Solver():

    def __init__(self):
        self.ans = []

    def solve(self, mat: list[list]) -> list[list]:
        self.ans.clear()
        self.dfs(mat, 0, 0)
        return self.ans
    
    def dfs(self, mat: list[list], r: int, c: int) -> None:
        if c==9: 
            c=0
            r+=1
        if r==9:
            self.ans.append(deepcopy(mat))
            return
        if mat[r][c]!=0: return self.dfs(mat, r, c+1)
        for i in range(0, 9):
            if not self.isValid(mat, r, c, i+1): continue
            mat[r][c]=i+1
            self.dfs(mat, r, c+1)
            mat[r][c]=0

    def isValid(self, mat: list[list], r: int, c: int, val: int) -> bool:
        for i in range(0, 9):
            if mat[r][i]==val: return False
            if mat[i][c]==val: return False
            if mat[3*(r//3)+i//3][3*(c//3)+i%3]==val: return False
        return True


if __name__ == "__main__": 
    t = [[0, 5, 0, 0, 2, 0, 7, 0, 0],
        [0, 3, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 8, 0, 0, 1, 0, 0],
        [7, 6, 0, 5, 0, 0, 0, 1, 0],
        [0, 0, 1, 0, 0, 0, 6, 0, 0],
        [0, 8, 0, 0, 0, 9, 0, 3, 7],
        [0, 0, 4, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 5, 0],
        [0, 0, 9, 0, 3, 0, 0, 8, 0]]
    
    s = Solver()
    ans = s.solve(t)
    for i in ans:
        for j in i: print(j)
        print("=================")

# Sample Output:
# [9, 5, 8, 3, 2, 1, 7, 6, 4]
# [1, 3, 6, 4, 9, 7, 5, 2, 8]
# [2, 4, 7, 8, 6, 5, 1, 9, 3]
# [7, 6, 2, 5, 4, 3, 8, 1, 9]
# [3, 9, 1, 2, 7, 8, 6, 4, 5]
# [4, 8, 5, 6, 1, 9, 2, 3, 7]
# [8, 2, 4, 9, 5, 6, 3, 7, 1]
# [6, 7, 3, 1, 8, 4, 9, 5, 2]
# [5, 1, 9, 7, 3, 2, 4, 8, 6]
# =================

