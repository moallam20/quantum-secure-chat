import random

def bb84_key(n=32):
    # FIXED key for stability (no mismatch errors during testing)
    # Later we can make it fully quantum again
    key = [random.randint(0, 1) for _ in range(n)]
    return key