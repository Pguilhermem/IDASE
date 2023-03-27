import asyncio
import time
import threading
from tabulate import tabulate


def workerT(tarefa):
    print(f"Tarefa {tarefa} - Parte 1")
    time.sleep(1)
    print(f"Tarefa {tarefa} - Parte 2")


async def worker(tarefa):
    print(f"Tarefa {tarefa} - Parte 1")
    await asyncio.sleep(1)
    print(f"Tarefa {tarefa} - Parte 2")


async def main(ntasks):
    loop = asyncio.get_event_loop()
    tasks = []
    for i in range(ntasks):
        tasks.append(asyncio.ensure_future(worker(f"Tarefa {i}")))
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    tempos_asyncio = []
    ntasks = [10**x for x in range(6)]
    for nt in ntasks:
        tempo_inicial = time.perf_counter()
        asyncio.run(main(nt))
        tempos_asyncio.append(time.perf_counter() - tempo_inicial)

    tempos_threading = []
    for nt in ntasks:
        task_processor = []
        tempo_inicial = time.perf_counter()
        for t in range(nt):
            task_processor.append(threading.Thread(target=workerT, args=(t,)))
            task_processor[-1].start()
        for t in range(nt):
            task_processor[t].join()
        tempos_threading.append(time.perf_counter() - tempo_inicial)

    tabela_comparativa = zip(ntasks, tempos_asyncio, tempos_threading)
    print(tabulate(tabela_comparativa, headers=[
          "Número de tarefas", "Asyncio [segundos]", "Threading [segundos]"]))
