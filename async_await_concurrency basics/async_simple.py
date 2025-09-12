"""
Problem:
Write two async functions:
1. task1() - prints "Task 1 running"
2. task2() - prints "Task 2 running"
Run them together using asyncio.
"""

import asyncio

async def task1():
    print("Task 1 running")
    await asyncio.sleep(1)
    print("Task 1 done")

async def task2():
    print("Task 2 running")
    await asyncio.sleep(1)
    print("Task 2 done")

async def main():
    await asyncio.gather(task1(), task2())
    # await task1()
    # await task2()

if __name__ == "__main__":
    asyncio.run(main())
