import asyncio
import time


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():
    task1 = asyncio.create_task(
        say_after(1, 'hello'))

    task2 = asyncio.create_task(
        say_after(2, 'world'))

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")


# asyncio.run(main())


async def nested(ma):
    for i in range(0, ma):
        await asyncio.sleep(1)
        print(i)


async def main1():
    # Schedule nested() to run soon concurrently
    # with "main()".
    task = asyncio.create_task(nested(5))
    another_task = asyncio.create_task(nested(9))
    task3 = asyncio.create_task(nested(15))

    # "task" can now be used to cancel "nested()", or
    # can simply be awaited to wait until it is complete:
    await task
    await another_task
    await task3


asyncio.run(main1())
