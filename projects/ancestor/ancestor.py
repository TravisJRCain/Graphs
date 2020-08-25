from collections import deque
# list container

def earliest_ancestor(ancestors, starting_node):
    cache = {}
    for i in ancestors:
        parent = i[0]
        child = i[1]
        if child not in cache:
            cache[child] = []
        cache[child].append(parent)

    queue = deque()
    queue.append([starting_node])
    length = [1, -1]
    while len(queue) > 0:
        # add current to queue
        current = queue.popleft()
        last = current[-1]
        if last not in cache:
            if len(current) > length[0]:
                length = [len(current), last]

            if len(current) == length[0] and last < length[1]:
                length = [len(current), last]

        else:
            for i in cache[last]:
                queue.append(current + [i])
        
    print("Answer:", length[1])
    return length[1]