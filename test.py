import queue
import random
import threading
import time


def producer(q: queue.Queue):
    for i in range(10):
        item = f"item_{i}"
        q.put(item)
        print(f"生产: {item}\n", end="")
        time.sleep(random.random())
    q.put(None)


def consumer(name: str, q: queue.Queue):
    while True:
        item = q.get()
        if item is None:
            q.task_done()
            break
        print(f"{name} 消费: {item}\n", end="")
        q.task_done()


q = queue.Queue(maxsize=5)
threads = [
    threading.Thread(target=producer, args=(q,)),
    threading.Thread(target=consumer, args=("C1", q)),
    threading.Thread(target=consumer, args=("C2", q)),
]

for t in threads:
    t.start()
for t in threads:
    t.join()
