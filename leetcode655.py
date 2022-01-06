import collections


def printTree(root):

    deque = collections.deque([root,0])
    answer = []
    while deque:
        node,level = deque.popleft()
        answer[level].append()