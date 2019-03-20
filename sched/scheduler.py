import threading
import time

from services.singleton import singleton


@singleton
class Schedule:

    def __init__(self):
        self.keep_running = True
        self.sleep_time = 1
        self.__job_list = {}

    def __jobs(self):
        print("oh gez, i'm working")
        for _, job in self.job_list.items():
            job()

    def add_job(self, job_name, new_job):
        self.__job_list[job_name] = new_job

    def remove_job(self, job_name):
        del self.__job_list[job_name]

    def __main_loop(self):
        while self.keep_running:
            self.__jobs()
            time.sleep(self.sleep_time)
            print("Done!")

    def run(self):
        thread = threading.Thread(target=self.__main_loop)
        thread.start()
