import asyncio


async def task1():
    print("task1 started")
    await asyncio.sleep(1)
    print("task1 ended")


async def task2():
    print("task2 started")
    await asyncio.sleep(0.5)
    print("task2 ended")


async def main():
    await asyncio.gather(task1(), task2())


asyncio.run(main())
