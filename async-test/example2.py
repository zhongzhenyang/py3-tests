# coding:utf-8

import asyncio
import time

async def speak():
    print('C')
    await asyncio.sleep(3)
    return 'D'


async def run():
    # will_speak = asyncio.ensure_future(speak())
    will_speak = loop.create_task(speak())
    print("will_speak done",will_speak.done())
    # await asyncio.sleep(1)
    print('A')
    await asyncio.sleep(1)
    print('B')
    await asyncio.sleep(2)
    print('run() after 2 seconds')
    print(await will_speak)
    print('E')

loop = asyncio.get_event_loop()
task = asyncio.ensure_future(run())
# task = loop.create_task(run())
print("task:", task)
time.sleep(5)
loop.run_until_complete(task)
print("task:", task)