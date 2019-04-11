from collections import deque

# Deque stand for "double ended queue" - great for O(1) when popping items off and onto list
# list is O(n) because it may have to realloc
myDeque = deque([4,7,2,67,3,344,22])
print(myDeque.popleft())
myDeque.appendleft('new var')
print(myDeque)
