import time
import random

fastest_time = 100

for attempt in range(5):
    print("get ready...")

    wait_time = random.randint(2, 5)
    time.sleep(wait_time)

    print("GO!")
    start_time = time.monotonic()

    input()

    end_time = time.monotonic()

    reaction_time = end_time - start_time

    print("your reaction time was", reaction_time, "seconds")

    if reaction_time < fastest_time:
        fastest_time = reaction_time

print("your fastest reaction time was", fastest_time, "seconds")