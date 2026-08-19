from queue import Queue


def maxWindowSum(a, k):
    # Write code here
    num_list = a
    window = k
    q = Queue()

    result = []

    for num in num_list:
        q.enqueue(num)

    while q.size() >= window:
        result.append(sum(q.items[0:window]))
        q.dequeue()
    

    return max(result)
