from threading import Thread, current_thread
import time
import asyncio

def now(): return time.time()

def start_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()

def more_work(x):
    print('More work {}, thread ident:{}'.format(x, current_thread().ident))
    time.sleep(x)
    print('Finished more work {}'.format(x))

async def do_some_work(x):
    print('Waiting: ', x, ',thread ident:', current_thread().ident)

    await asyncio.sleep(x)
    print('x:{}, time: {}'.format(x, time.time() - start))
    return 'Done after {}s'.format(x)

start = now()
new_loop = asyncio.new_event_loop()
t = Thread(target=start_loop, args=(new_loop,))
t.start()
print('TIME1: {}'.format(time.time() - start))

new_loop.create_task(do_some_work(10))
new_loop.create_task(do_some_work(3))
new_loop.call_soon_threadsafe(more_work, 15)
# new_loop.create_task(do_some_work(10))
# new_loop.create_task(do_some_work(3))
# new_loop.call_soon_threadsafe(more_work, 3)

print('TIME2: {}'.format(time.time() - start))