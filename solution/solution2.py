from collections import defaultdict
from heapq import heappush, heappop
from math import inf
from typing import List

class Solution:
    def minimumCostFrom(self, sourceChar):
        """
        Find the shortest paths from the source character to all other characters.

        Args:
            sourceChar (str): The source character.

        Returns:
            dict: A dictionary of shortest distances from the source character to all other characters.
        """
        bests = defaultdict(int)
        seenCost = defaultdict(lambda: inf)
        seenCost[sourceChar] = 0
        frontier = [(0, sourceChar)]
        while frontier:
            reachCost, current = heappop(frontier)
            if current in bests:
                continue
            bests[current] = reachCost
            for d, edgeCost in self.edges[current].items():
                totalCost = reachCost + edgeCost
                if totalCost < seenCost[d]:
                    heappush(frontier, (totalCost, d))
                    seenCost[d] = totalCost
        return bests

    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        """
        Find the minimum cost to transform the source string into the target string.

        Args:
            source (str): The source string.
            target (str): The target string.
            original (List[str]): The original characters.
            changed (List[str]): The changed characters.
            cost (List[int]): The costs of changing characters.

        Returns:
            int: The minimum cost to transform the source string into the target string.
        """
        self.edges = defaultdict(dict)
        for s, d, c in zip(original, changed, cost):
            if d not in self.edges[s] or c < self.edges[s][d]:
                self.edges[s][d] = c

        bests = defaultdict(dict)
        totalCost = 0
        for s, t in zip(source, target):
            if s != t:
                if t in bests[s]:
                    totalCost += bests[s][t]
                elif bests[s]:
                    return -1
                else:
                    best = self.minimumCostFrom(s)
                    bests[s] = best
                    if t in best:
                        totalCost += best[t]
                    else:
                        return -1
        return totalCost