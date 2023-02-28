import threading
import time

sem = threading.Semaphore(2)

def worker():
    sem.acquire()
    print('Iniciando a thread', threading.current_thread().name)
    time.sleep(1)
    sem.release()

for i in range(5):
    t = threading.Thread(target=worker, name=f'Thread {i}')
    t.start()