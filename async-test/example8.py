
import asyncio
import time

async def meow(number):
    print(f'starting {number}')
    await asyncio.sleep(number)
    print(f'stopping {number}')


async def run():
    f = []
    for x in range(1, 6):
        f.append(meow(x))
    
    t1 = time.time()
    for x, y in enumerate(f):
        if x % 2 == 0:
            await y
    for x, y in enumerate(f):
        if x % 2 != 0:
            await y
    t2 = time.time()
    print("time:", t2-t1)

loop = asyncio.get_event_loop()
loop.run_until_complete(run())
