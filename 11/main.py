import asyncio


async def tarefa():
    print("Um")
    await asyncio.sleep(1)
    print("Dois")


async def main():
    await asyncio.gather(tarefa(), tarefa(), tarefa())

if __name__ == "__main__":
    import time
    tempo_inicial = time.perf_counter()
    asyncio.run(main())
    tempo_gasto = time.perf_counter() - tempo_inicial
    print(f"Programa executado em {tempo_gasto:0.2f} segundos.")
