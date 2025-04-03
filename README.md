<img src="que.png" alt="Que" width="320"/>
A python queue implementation where the length of the name determines the capacity of the queue

## NEW ##
Now comes with OUT OF THE BOX support for up queues of up to 10 elements!

### Usage ###
```
from que import *

# 3 element queueue

q = Queueue()
q.enqueue("a")
q.enqueue("b")
q.enqueue("c")
print(q)  # <Queueue (3/3): ['a', 'b', 'c']>
q.enqueue("d")  # raises OverflowError

# Going to need like 8 here, lets make it big

q = Queueueueueueueue()
q.enqueue("a")
q.enqueue("b")
q.enqueue("c")
q.enqueue("d")
q.enqueue("e")
q.enqueue("f")
q.enqueue("g")
q.enqueue("h")
print(q)  # <Queueue (8/8): ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']>
```
