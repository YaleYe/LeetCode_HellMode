def canVisitAllRooms(rooms):

    visited = set()
    visited.add(0)

    stack = []+rooms[0]

    while stack:
        key = stack.pop()

        if key not in visited:
            visited.add(key)
            stack += rooms[key]


    return len(rooms) == len(visited)


rooms = [[1,3],[3,0,1],[2],[0]]
print(canVisitAllRooms(rooms))

