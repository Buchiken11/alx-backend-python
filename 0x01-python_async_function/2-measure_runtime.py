#!/usr/bin/env python3

import importlib
import asyncio
import random
import time


concurrent_coroutines = importlib.import_module('1-concurrent_coroutines').wait_n

async def measure_time(n: int, max_delay: int):
    start_time = time.time()
    await wait_n(n, max_delay)
    end_time = time.time()
    total_time = end_time - start_time
    return total-time
