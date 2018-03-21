import asyncio
import types
import random

@types.coroutine
def compute(x, y):
    print("Compute %s + %s ..." % (x, y))
    yield from asyncio.sleep(random.uniform(2.2, 4.5))
    return x + y

async def print_sum(x, y):
    result = await compute(x, y)
    print("%s + %s = %s" % (x, y, result))

loop = asyncio.get_event_loop()
tasks = asyncio.wait([print_sum(1, 2), print_sum(2,3), print_sum(3,4), print_sum(4,5), print_sum(5,6)])
for t in tasks:
    print(t)
print("types.GeneratorType:",type(tasks) is types.GeneratorType)
print("types.CoroutineType:", type(tasks) is types.CoroutineType)
print("types.AsyncGeneratorType:", type(tasks) is types.AsyncGeneratorType)
loop.run_until_complete(tasks)
loop.close()