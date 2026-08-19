from queue import Queue


def hotPotato(names, tosses):
    # Write code here
    q = Queue()

    for name in names:
        q.enqueue(name)
    
    while q.size() > 1:
        for n in range(tosses):
            q.enqueue(q.front())
            q.dequeue()
        q.dequeue()
        
    return q.front()
