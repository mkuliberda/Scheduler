import pandas as py
import time
import sys
import os
import datetime
import xml


class Scheduler():

    def __init__(self):
        print("Scheduler starting...")
        
    def __exit__(self, exc_type, exc_value, traceback):
        print('Scheduler closing...')

    def importFile(self):
        print("importFile")

    def printSchedule(self):
        print("printSchedule")


scheduler1 = Scheduler()

if __name__ == '__main__':
        scheduler1.printSchedule()