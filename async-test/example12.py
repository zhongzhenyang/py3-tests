import asyncio
import time
import types


def now(): return time.time()


async def do_some_work(x):
    print('Waiting: ', x)
    await asyncio.sleep(x)
    return 'Done after {}s'.format(x)


async def main():
    coroutine1 = do_some_work(1)
    coroutine2 = do_some_work(2)
    coroutine3 = do_some_work(4)

    tasks = [
        asyncio.ensure_future(coroutine3),
        asyncio.ensure_future(coroutine2),
        asyncio.ensure_future(coroutine1),
    ]
    # print("tasks:", tasks)
    for task in asyncio.as_completed(tasks):
        # print("task:", task)
        result = await task
        print('Task ret: {}'.format(result))

start = now()

loop = asyncio.get_event_loop()
done = loop.run_until_complete(main())
print('TIME: ', now() - start)
