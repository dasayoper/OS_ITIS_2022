#!/usr/bin/python3

import sys
import os
import time
import random


sleep_time = sys.argv[1]
sleep_time = int(sleep_time)
process_id = os.getpid()
parent_process_id = os.getppid()

print(f"Child [{process_id}]: I am started. PID {process_id}. Parent PID {parent_process_id}")

time.sleep(sleep_time)

print(f"Child [{process_id}]: I am ended. PID {process_id}. Parent PID {parent_process_id}")

exit_status = random.randint(0, 1)
sys.exit(exit_status)