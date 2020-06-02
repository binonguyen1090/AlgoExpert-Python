def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
    visited = [False] * len(rooms)
     visited[0] = True
      stack = [0]

       while len(stack) > 0:
            keys = stack.pop()
            for key in rooms[keys]:
                if not (visited[key]):
                    visited[key] = True
                    stack.append(key)
        return all(visited)
