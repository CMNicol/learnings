"""Define methods which return coroutines that can be awaited or gathered."""
import asyncio
import typing


# Define methods using the async keyword to have them return coroutines.
async def generate_coro_one() -> asyncio.coroutine:
    print("Start coro_one.")
    await asyncio.sleep(2)
    print("End coro_one.")
    return "Returned from coro_one"


async def generate_coro_two() -> asyncio.coroutine:
    print("Start coro_two.")
    await asyncio.sleep(1)
    print("Mid coro_two.")
    await asyncio.sleep(1)
    print("End coro_two.")
    return "Returned from coro_two"


async def gather_the_coros(coros: typing.List[asyncio.coroutine]) -> asyncio.coroutine:
    gatherings = await asyncio.gather(*coros)
    return gatherings


coros = [gen_coro() for gen_coro in [generate_coro_one, generate_coro_two]]
gatherings = gather_the_coros(coros)
coro_returns = asyncio.run(gatherings)

for coro_return in coro_returns:
    print(coro_return)
