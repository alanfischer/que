# que
A python queue implementation where the length of the name determines the capacity of the queue

## NEW ##
Now comes with OUT OF THE BOX support for up queues of up to 10 elements!

### Usage ###
```
from que import *
q = Queueue()
q.enqueue("a")
q.enqueue("b")
q.enqueue("c")
print(q)  # <Queueue (3/3): ['a', 'b', 'c']>
q.enqueue("d")  # raises OverflowError
```
