from threading import Thread
import sys


class MyThread(Thread):
    def __init__(self, param):
        Thread.__init__(self)
        self.param = param

    def run(self):
        print("Hello, I'm %s and I received the number %d\n" %(self.name, self.param))


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Usage: python %s <number-of-threads>" % sys.argv[0])
        sys.exit(0)

    num_threads = int(sys.argv[1])

    threads = []

    import random
    random.seed(0)

    for i in range(num_threads):
        threads.append(MyThread(random.randint(0, 1000)))
        threads[-1].start()
    for t in threads:
        t.join()

