
import time

# Get the current time
current_time = time.time()
print("Current time (in seconds since epoch):", current_time)

# Formatting time
local_time = time.localtime(current_time)
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
print("Formatted local time:", formatted_time)

# Sleep for 2 seconds
print("Sleeping for 2 seconds...")
time.sleep(2)
print("Awake now!")

# Calculating elapsed time
start_time = time.time()
for _ in range(1000000):
    pass  # Empty loop
end_time = time.time()
print(f"Time taken for the loop: {end_time - start_time} seconds")
