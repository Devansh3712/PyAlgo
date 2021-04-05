'''
module for implementation of
Prim's Minimum Spanning Tree
'''

import sys

class Graph:

    def __init__(self, vertices: int):

        self.v      = vertices
        self.graph  = [[0 for column in range (vertices)] for row in range (vertices)]

    def min_key(self, key: list, mst_set: list):

        min = sys.maxsize

        for i in range (self.v):

            if (key[i] < min and mst_set[i] == False):

                min         = key[i]
                min_index   = i

        return min_index

    def prim_mst(self):

        key         = [sys.maxsize] * self.v
        parent      = [None] * self.v
        key[0]      = 0
        mst_set     = [False] * self.v
        parent[0]   = -1

        for i in range (self.v):

            u = self.min_key(key, mst_set)
            mst_set[u] = True

            for j in range (self.v):

                if (self.graph[u][j] > 0 and mst_set[j] == False and key[j] > self.graph[u][j]):

                    key[j] = self.graph[u][j]
                    parent[j] = u

        result = {}

        for i in range (1, self.v):

            result[(parent[i], i)] = self.graph[i][parent[i]]

        return result

'''
PyAlgo
Devansh Singh, 2021
'''