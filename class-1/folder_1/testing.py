import psutil 
import logging

logging.basicConfig(
    level=logging.INFO,
    filename="cpu_usage.log",
    format="%(asctime)s | %(levelname)s | %(message)s"
)

SECONDS = []
LIMIT = 6
def main():


    try:
        while True:
            logging.debug("CPU READING STARTS")
            cpu = psutil.cpu_percent(interval=1)

            SECONDS.append(cpu)
            if len(SECONDS) > LIMIT:
                SECONDS.pop(0)
            if len(SECONDS) == LIMIT:
                avr = sum(SECONDS)/LIMIT
                if cpu > avr :
                    logging.warning(f"percent usage:{cpu} %")
                else:
                    logging.info(f"percent usage:{cpu} %")
    
                '''with open ("yosef.txt","a") as file:
                    file.write(f"percent usage:{cpu} %\n")'''
 
    except KeyboardInterrupt:
        print("shut down")

if __name__ == "__main__":

    main()