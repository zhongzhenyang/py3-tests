# coding:utf-8

import asyncio


async def speak():
    print('C')
    await asyncio.sleep(3)
    return 'D'


async def run():
    will_speak = speak()
    print('A')
    print('B')
    print(await will_speak)

loop = asyncio.get_event_loop()
loop.run_until_complete(run())
