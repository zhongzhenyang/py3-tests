# coding:utf-8

import asyncio


async def meow(number):
    print(f'starting {number}')
    await asyncio.sleep(number)
    print(f'stopping {number}')
    return number


async def run():
    # notice how we assign each coroutine to a variable
    a = meow(1)
    b = meow(2)
    c = meow(3)
    d = meow(4)
    e = meow(5)
    
    # print("a:", a)
    # fut = asyncio.gather(*[a,b,c,d,e], return_exceptions=True)
    # print("fut:", fut)
    # await fut
    # for result in fut.result():
    #     print("result:", result)
    # then we can decide which order we wish our coroutines to execute
    await c
    await a
    await e
    await b
    await d


loop = asyncio.get_event_loop()
loop.run_until_complete(run())
