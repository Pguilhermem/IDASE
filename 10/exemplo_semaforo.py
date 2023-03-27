import threading
import time

sem = threading.Semaphore(3)


def worker():
    time.sleep(1)
    sem.acquire()
    print('Iniciando a thread', threading.current_thread().name)
    time.sleep(1)
    sem.release()


for i in range(10):
    t = threading.Thread(target=worker, name=f'Thread {i}')
    t.start()
