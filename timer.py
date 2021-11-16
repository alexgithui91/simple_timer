import time
import sys

start_time = time.time()
secs = 0
mins = 0

while True:
    try:
        sys.stdout.write(
            "\r{mins} Minutes {secs} Seconds".format(mins=mins, secs=secs)
        )

        sys.stdout.flush()

        time.sleep(1)

        secs = int(time.time() - start_time) - mins * 60

        if secs >= 60:
            mins += 1
            secs = 0

    except (KeyboardInterrupt):
        break
