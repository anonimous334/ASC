from threading import current_thread, enumerate, Event, Thread


class Master(Thread):
    def __init__(self, max_work, work_available, result_available):
        Thread.__init__(self, name="Master")
        self.max_work = max_work
        self.work_available = work_available
        self.result_available = result_available

    def set_worker(self, worker):
        self.worker = worker

    def run(self):
        for i in range(self.max_work):
            self.work = i
            self.work_available.set()
            self.result_available.wait()
            self.result_available.clear()
            if self.get_work() + 1 != self.worker.get_result():
                print("oops")
            print("%d -> %d" % (self.work, self.worker.get_result()))

    def get_work(self):
        print("get work with self " + str(self) + " from thread " + str(current_thread()) + "\n")
        return self.work


class Worker(Thread):
    def __init__(self, terminate, work_available, result_available):
        Thread.__init__(self, name="Worker")
        self.terminate = terminate
        self.work_available = work_available
        self.result_available = result_available

    def set_master(self, master):
        self.master = master

    def run(self):
        while True:
            self.work_available.wait()
            self.work_available.clear()
            if terminate.is_set(): break
            self.result = self.master.get_work() + 1
            self.result_available.set()

    def get_result(self):
        print("get result with self " + str(self) + " from thread " + str(current_thread()) + "\n")
        return self.result


if __name__ == "__main__":
    terminate = Event()
    work_available = Event()
    result_available = Event()

    w = Worker(terminate, work_available, result_available)
    m = Master(10, work_available, result_available)
    w.set_master(m)
    m.set_worker(w)
    w.start()
    m.start()

    
    m.join()

    terminate.set()
    work_available.set()
    w.join()

    print(enumerate())
