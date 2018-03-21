# coding:utf-8

import asyncio
import time

now = lambda : time.time()

async def meow(number):
    print(f'starting {number}')
    await asyncio.sleep(number)
    print(f'stopping {number}')
    return number


async def run():
    f = []
    for x in range(1, 6):
        f.append(meow(x))
        # f.append(loop.create_task(meow(x)))
    t1 = now()
    done, pending = await asyncio.wait(f)
    print("done:", done)
    print("pending:", pending)
    for task in done:
        print("task result:", task.result())
    # x = await asyncio.gather(* f)
    # print(x)
    t2 = now()
    print("time:", t2-t1)

loop = asyncio.get_event_loop()
loop.run_until_complete(run())