#!/usr/bin/python3

import os
import sys
import random


def run_children():
    child = os.fork()
    if child == 0:
        argument = str(random.randint(5, 10))
        os.execl("./child.py", "child.py", argument)
    print(f"Parent [{os.getpid()}]: I ran children process with PID {child}")


num_children = sys.argv[1]
num_children = int(num_children)

for i in range(0, num_children):
    run_children()

while num_children > 0:
    child_pid, status = os.wait()
    status = status / 256
    status = int(status)
    print(f"Parent[{os.getpid()}]: Child with PID {child_pid} terminated. Exit Status {status}.")
    if status == 0:
        num_children = num_children - 1
    else:
        run_children()