import asyncio
import time
from time import sleep


async def f1():
    for i in range(5):
        print(f'f1({i})')
        # sleep(1.5)
        await asyncio.sleep(1.5)


async def f2():
    for i in range(5):
        print(f'f2({i})')
        # sleep(1)
        await asyncio.sleep(1)


async def f3():
    for i in range(10):
        print(f'f3({i})')
        # sleep(1)
        await asyncio.sleep(1.2)


async def main():
    # await asyncio.gather(
    #     f1(),
    #     f2(),
    #     f3()
    # )
    # If we run for example 100 000 tasks the time will increase to 24 seconds
    # 10 000 - 8 seconds
    await asyncio.gather(
        *[f1() for _ in range(10000)]
    )


start = time.time()
# main()
asyncio.run(main())
end = time.time()
print(end - start)
