import time

now = time.time()
ltm = time.localtime(now)

print(f"Time: {ltm.tm_hour}:{ltm.tm_min}:{ltm.tm_sec}")

seconds_since_epoch = int(now)
days_since_epoch = seconds_since_epoch // 86400

print(f"Days since epoch: {days_since_epoch}")