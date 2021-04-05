"""
module for implementation
of convex hull algorithm
"""

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y
  
def Left_index(points: int): 

    min_num = 0

    for i in range(1, len(points)):

        if (points[i].x < points[min_num].x):
            min_num = i

        elif (points[i].x == points[min_num].x):

            if (points[i].y > points[min_num].y):
                min_num = i

    return min_num
  
def orientation(p, q, r): 

    val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)

    if (val == 0):
        return 0

    elif (val > 0):
        return 1

    else:
        return 2
  
def convex_hull(points: list, n: int):

    """
    finding the convex hull of a given
    set of points using jarvis
    algorithm
    """ 

    if (n < 3):
        return

    l       = Left_index(points)
    hull    = []
    p       = l 
    q       = 0
    result  = []

    while (True): 

        hull.append(p)
        q = (p + 1) % n

        for i in range(n):

            if (orientation(points[p], points[i], points[q]) == 2):
                q = i

        p = q

        if (p == l): 
            break

    for each in hull:
        result.append((points[each].x, points[each].y))

    return result

"""
PyAlgo
Devansh Singh, 2021
"""
