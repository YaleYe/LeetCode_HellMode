import collections


def floodFill(image,sr,sc,newColor):

    visited = set()
    oldColor = image[sr][sc]
    queue = collections.deque([ (sr,sc) ])

    while queue:
        sr,sc = queue.popleft()
        point = str(sr) + "_" +str(sc)
        if sr < 0 or sc < 0 or sr >= len(image) or sc >= len(image[0]) or image[sr][sc] != oldColor or point in visited:
            continue

        image[sr][sc] = newColor
        visited.add(point)

        queue.append((sr-1,sc))
        queue.append((sr+1,sc))
        queue.append((sr,sc+1))
        queue.append((sr,sc-1))

    print(queue)
    print(image)


image = [[0,0,0],[0,1,1]]
sr = 1
sc = 1
newColor = 1

floodFill(image,sr,sc,newColor)