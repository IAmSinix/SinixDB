import SinixDB

import asyncio
import random

db = SinixDB.AsyncSinixDB()
db.load("AsyncData.json")

async def rand():
    return random.randint(0, 1000000000000)

async def main():
    """
    await db.set(
        key="string",
        data={
            "string": "string"
        }
    )
    await db.save()
    await db.is_json("{}")
    await db.remove(key="string")
    await db.get("string")
    """
    msg = input("Waring! This can KILL devices with little RAM! Do you want to continue?  (y / n) >>> ")
    if msg.lower() in ("n", "no"):
        quit()
    i = 0
    while True:
        try:
            await db.set(
                key=str(await rand()),
                data={
                    str(await rand()): str(await rand())
                }
            )
            i += 1
        except:
            print(
                f"{i} objects, wow!"
                )
            msg = input("Save? (y / n) >>>")
            if msg.lower() in ("n", "no"):
                quit()
            await db.save()
    
asyncio.run(main())
