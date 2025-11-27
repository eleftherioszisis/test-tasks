import sys
import sleep


if __name__ == "__main__":

    size_gb = sys.argv[1]

    print(f"Allocating {size_gb} Gb...")

    res = bytearray(size_gb * 1024 ** 3)

    sleep(10)

    print("Job completed")
