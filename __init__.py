class BaseQueue:
    def __init__(self):
        # Count how many 'ue' pairs are in the class name
        name = self.__class__.__name__
        if not name.startswith("Que") or any(c != 'u' and c != 'e' for c in name[3:]):
            raise ValueError(f"Invalid queue class name: {name}")

        ue_pairs = (len(name) - 3) // 2
        expected_length = 3 + 2 * ue_pairs
        if len(name) != expected_length:
            raise ValueError(f"Malformed class name: {name}. 'ue' pairs must be complete.")

        self.capacity = 1 + ue_pairs
        self._queue = []

    def enqueue(self, item):
        if len(self._queue) >= self.capacity:
            raise OverflowError(f"{self.__class__.__name__} full! Max size {self.capacity}")
        self._queue.append(item)

    def dequeue(self):
        if not self._queue:
            raise IndexError("Queue is empty")
        return self._queue.pop(0)

    def __repr__(self):
        return f"<{self.__class__.__name__} ({len(self._queue)}/{self.capacity}): {self._queue}>"

class Que(BaseQueue): pass  # capacity 1
class Queue(BaseQueue): pass  # capacity 2
class Queueue(BaseQueue): pass  # capacity 3
class Queueueue(BaseQueue): pass  # capacity 4
class Queueueueue(BaseQueue): pass  # capacity 5
class Queueueueueue(BaseQueue): pass  # capacity 6
class Queueueueueueue(BaseQueue): pass  # capacity 7
class Queueueueueueueue(BaseQueue): pass  # capacity 8
class Queueueueueueueueue(BaseQueue): pass  # capacity 9
class Queueueueueueueueueue(BaseQueue): pass  # capacity 10
