
"""
deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
"""

from collections import deque

queue = deque(("A","B","C"))
print(queue)
queue.append("D")
print(queue)
queue.appendleft("E")
print(queue)
queue.pop()
print(queue)
queue.popleft()
print(queue)