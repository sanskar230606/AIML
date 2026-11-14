
from collections import defaultdict, deque

# BFS
def BFS(graph, start, goal):
    visited = []
    queue = deque([start])
    visited.append(start)
    result = []

    while queue:
        print("Queue:", list(queue))

        node = queue.popleft()
        result.append(node)

        print("Traversal:", result)
        print("----------------------------")

        if node == goal:
            print("Goal found!")
            break

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

    if goal in result:
        print("\nGoal found!")
    else:
        print("\nGoal not reachable!")

    print("Final BFS:", result)


# DFS
def DFS(graph, start, goal):
    visited = []
    stack = [start]
    result = []

    while stack:
        print("Stack:", stack)

        node = stack.pop()

        if node not in visited:
            visited.append(node)
            result.append(node)

            print("Traversal:", result)
            print("----------------------------")

            if node == goal:
                break

            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

    if goal in result:
        print("\nGoal found!")
    else:
        print("\nGoal not reachable!")

    print("Final DFS:", result)


# Creating graph
graph = defaultdict(list)

n = int(input("Enter number of edges: "))

for i in range(n):
    u, v = input("Enter edge (u v): ").split()
    graph[u].append(v)
    graph[v].append(u)

start = input("Enter the starting node: ")
goal = input("enter goal")
print("\n1. BFS")
print("2. DFS")

choice = input("Enter your choice: ")

if choice == '1':
    BFS(graph, start,goal)
elif choice == '2':
    DFS(graph, start,goal)
else:
    print("Invalid choice")
