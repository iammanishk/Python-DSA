# Write a program that implement an exponential backoff strategy that doubles the wait time between retries, starting from 1 second but stop after 5 retries


import time 

wait_time = 1
max_retries = 5
attempts = 0

while attempts < max_retries:
    print("Attempts", attempts +1, "waiting for", wait_time, "seconds for next attempts" )
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1

