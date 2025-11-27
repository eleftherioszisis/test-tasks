import sys
from time import sleep


def print_cgroup_limits():
    try:
        # Memory limit
        with open("/sys/fs/cgroup/memory/memory.limit_in_bytes") as f:
            memory_bytes = int(f.read().strip())
            print(f"Memory limit: {memory_bytes // (1024**2)} MB", file=sys.stderr)
        
        # CPU limit
        with open("/sys/fs/cgroup/cpu/cpu.cfs_quota_us") as f:
            quota = int(f.read().strip())
        with open("/sys/fs/cgroup/cpu/cpu.cfs_period_us") as f:
            period = int(f.read().strip())
        
        if quota > 0:
            cpu_cores = quota / period
            print(f"CPU limit: {cpu_cores:.2f} cores", file=sys.stderr)
        else:
            print("CPU limit: unlimited", file=sys.stderr)
            
    except Exception as e:
        print(f"Failed to read cgroup limits: {e}", file=sys.stderr)


if __name__ == "__main__":

    print_cgroup_limits()

    data = []
    for i in range(1, 11):
        # Allocate chunks (e.g., 10 MB each)
        data.append("X" * 500_000_000)
        print(f"Allocated another {i * 500}MB")

    print("Job completed")
