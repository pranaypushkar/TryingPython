import threading

class MyThread(threading.Thread):
	def __init__(self, threadID, name, counter):
		threading.Thread.__init__(self)
			self.threadID = threadID
			self.name = name
			self.counter = counter
	def run(self):
		print("Starting", self.name)
		thradLock.acquire()
		print_time(self.name, self.counter, 5)
		thradLock.release()
		
thradLock = threading.Lock()

#code not complete
#def print_time(ThreadName, delay, counter):
#	while counter:
#		time.sleep(delay)
#		print("%s : %s"  )


thr1 = MyThread(1, "Thr 1", 1)
thr2 = MyThread(2, "Thr 2", 2)
thr1.start()
thr2.start()