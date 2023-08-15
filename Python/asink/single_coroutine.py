"""Define methods which return coroutines that can be awaited or gathered."""
import asyncio


# Define a method using the async keyword to have it return a coroutine.
async def generate_coro_one() -> asyncio.coroutine:
    print("Start coro_one.")
    await asyncio.sleep(2)
    print("End coro_one.")
    return "This is what will be returned when the coroutine is given to asyncio.run"


# Execute the generate_coro_one to get a coroutine object, run this using asyncio.run.
coro_one = generate_coro_one()
something = asyncio.run(coro_one)
print(something)
