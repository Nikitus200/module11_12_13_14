import asyncio as ao

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for i in range(1, 6):
        await ao.sleep(1/float(power))
        print(f'Силач {name} поднял {i}')
    print(f'Силач {name} закончил соревнования.')

async def start_tournament():
    task_1 = ao.create_task(start_strongman('Pasha', 3))
    task_2 = ao.create_task(start_strongman('Denis', 4))
    task_3 = ao.create_task(start_strongman('Apollon', 5))
    await task_1
    await task_2
    await task_3

ao.run(start_tournament())
