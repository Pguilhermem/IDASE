import threading

def worker(barrier):
    print('Trabalhador iniciado')
    barrier.wait()
    print('Trabalhador continuando')

barrier = threading.Barrier(3)

for i in range(3):
    t = threading.Thread(target=worker, args=(barrier,))
    t.start()