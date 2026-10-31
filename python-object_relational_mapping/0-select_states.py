#!/usr/bin/env python3
"""Coroutine loop 10 times, each time waiting 1 second and yielding a random number."""

import random
import asyncio
import typing


async def async_generator() -> typing.AsyncGenerator[float, None]:
    """Yields 10 random numbers between 0 and 10 with a 1-second delay."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
