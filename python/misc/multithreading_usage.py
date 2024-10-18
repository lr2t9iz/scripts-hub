import threading
import time

# Define a class that simulates work that can be done in parallel
class Worker:
    def __init__(self, name):
        self.name = name

    def do_work(self):
        for i in range(2):
            print(f"{self.name} is working: iteration {i+1}")
            time.sleep(10)  # Simulate work time

# Create a function that starts a thread with a worker
def start_worker(worker_name):
    worker = Worker(worker_name)
    worker.do_work()

if __name__ == "__main__":
    # Create two threads to work in parallel
    thread1 = threading.Thread(target=start_worker, args=("Worker 1",))
    thread2 = threading.Thread(target=start_worker, args=("Worker 2",))

    # Start the threads
    thread1.start()
    thread2.start()

    # Wait for both threads to finish
    thread1.join()
    thread2.join()

    print("All workers have finished their work.")
