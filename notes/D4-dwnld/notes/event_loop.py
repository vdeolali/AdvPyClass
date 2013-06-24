''' Demonstrate event-loop basics
    and gain an insight in popular tools like Twisted, Tornado, Diesel, sched, ...

    Show-off callbacks and patterns of using them.

    Heaps -- find the next scheduled event

    
'''

from heapq import heappush, heappop
from collections import namedtuple
from pprint import pprint
from time import time, sleep

ScheduledEvent = namedtuple('ScheduledEvent',
                    ['event_time', 'task'])

events = []

def add_task(event_time, task):
    heappush(events, ScheduledEvent(event_time, task))

def event_loop():
    try:
        while events:
            while events[0].event_time > time():
                sleep(0.1)
            curr_event = heappop(events)
            curr_event.task()
    except KeyboardInterrupt:
        pass
        
#####################################################

def show_ten():
    print 10

def show_two():
    print 2

def show_goodbye():
    print 'Adios'

def show_welcome():
    print 'hello'
    add_task(time() + 1.5, show_goodbye)
    
def show_three_repeatedly():
    print 3
    add_task(time() + 1, show_three_repeatedly)

def run_n_times(func, interval, n):
    for i in range(n):
        add_task(time() + i * interval, func)

add_task(time() + 5, show_ten)
add_task(time() + 2, show_two)
add_task(time(), show_three_repeatedly)
run_n_times(show_welcome, 2.5, 10)
event_loop()

