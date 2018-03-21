from threading import Thread, current_thread
import time
import asyncio



def now(): return time.time()

def start_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()

async def do_some_work(x):
    print('Waiting {}'.format(x))
    await asyncio.sleep(x)
    print('do_some_work x:{}, time: {}'.format(x, time.time() - start))
    print('Done after {}s'.format(x))

def more_work(x):
    print('More work {}'.format(x))
    time.sleep(x)
    print('more_work x:{}, time: {}'.format(x, time.time() - start))
    print('Finished more work {}'.format(x))

start = now()
new_loop = asyncio.new_event_loop()
t = Thread(target=start_loop, args=(new_loop,))
t.start()
print('TIME: {}'.format(time.time() - start))

asyncio.run_coroutine_threadsafe(do_some_work(6), new_loop)
asyncio.run_coroutine_threadsafe(do_some_work(4), new_loop)
time.sleep(10)
print('TIME: {}'.format(time.time() - start))