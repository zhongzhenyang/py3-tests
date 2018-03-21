import asyncio


async def new_future(n):
    print('future', n)
    await asyncio.sleep(3)
    print('future done', n)
    return n


async def run():
    results = asyncio.ensure_future(new_future(1))
    print(results)  # <Task> object returned
    print(await results)  # `1` is returned
    print(results)  # <Task> is returned again
    print(await results)  # `1` is returned again

    results = new_future(2)
    print(results)  # coroutine returned
    print(await results)  # `2` is returned
    print(results)  # coroutine returned again
    print(await results)  # RuntimeError: cannopy reuse aalready awaited coroutine


loop = asyncio.get_event_loop()
loop.run_until_complete(run())
