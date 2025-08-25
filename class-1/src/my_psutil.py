import psutil
import time
from logger import logger

THRESHOLD = 3
SECONDS = 10

vals = []

def main():

    logger.info(f"live montring with limit of {THRESHOLD} every {SECONDS} seconds")
    try:
        while True:
            # print(f"this is the cpu-time{psutil.cpu_times_percent(interval=1)}")
            # print(f"this is the cpu %{psutil.cpu_percent(interval=1)}")
            vals.append(psutil.cpu_percent(interval=1))

            if len(vals) > SECONDS:
                vals.pop(0)
            if len(vals) == SECONDS:
                avg = sum(vals)/SECONDS
                if avg >= THRESHOLD:
                    logger.warning(f"[ALERT] CPU {avg:.1f}%  {SECONDS}s")
                    vals.clear()
    except KeyboardInterrupt:
        logger.info("the system is clossing")

if __name__ == "__main__":
    main()