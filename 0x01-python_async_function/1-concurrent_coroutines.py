#!/usr/bin/env python3

import asyncio
import random
import importlib

# Dynamically import the wait_random function from the '0-basic_async_syntax' module
basic_async_syntax = importlib.import_module('0-basic_async_syntax')
wait_random = basic_async_syntax.wait_random

async def wait_n(n: int, max_delay: int) -> list[float]:
    task_to_coroutine = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = await asyncio.gather(*task_to_coroutine)

    # manually sort the delays

    sorted_delay = []
    while delays:
        min_delay = min(delays)
        sorted_delay.append(min_delay)
        delays.remove(min_delay)
        
    return sorted_delay

# if __name__ == "__main__":
#    asyncio.run(wait_n
