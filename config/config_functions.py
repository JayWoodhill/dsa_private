# functions to assist performance analysis when testing
# chatgpt code

import time
import tracemalloc
import psutil
from functools import wraps

def time_function(func):
    """
    Decorator to measure the execution time of a function.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"[TIME] Function '{func.__name__}' executed in {end_time - start_time:.6f} seconds.")
        return result
    return wrapper

def memory_function(func):
    """
    Decorator to measure the peak memory usage of a function.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        result = func(*args, **kwargs)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        print(f"[MEMORY] Function '{func.__name__}' used {peak / 10**6:.6f} MB at peak.")
        return result
    return wrapper

def cpu_usage_function(func):
    """
    Decorator to measure the CPU usage of a function.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        process = psutil.Process()
        start_cpu = process.cpu_percent(interval=None)
        result = func(*args, **kwargs)
        end_cpu = process.cpu_percent(interval=None)
        print(f"[CPU] Function '{func.__name__}' CPU usage: {end_cpu - start_cpu:.2f}%")
        return result
    return wrapper

def profile_function(func):
    """
    Decorator to profile a function's time and memory usage.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        print(f"[PROFILE] Function '{func.__name__}' executed in {end_time - start_time:.6f} seconds.")
        print(f"[PROFILE] Function '{func.__name__}' used {peak / 10**6:.6f} MB at peak.")
        return result
    return wrapper

def system_info():
    """
    Function to display system resource information.
    """
    mem = psutil.virtual_memory()
    cpu_count = psutil.cpu_count(logical=True)
    print(f"[SYSTEM] Total Memory: {mem.total / 10**9:.2f} GB")
    print(f"[SYSTEM] Available Memory: {mem.available / 10**9:.2f} GB")
    print(f"[SYSTEM] CPU Cores: {cpu_count}")
