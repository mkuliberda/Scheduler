import pandas as pd
import time
import sys
import os
import datetime
import xml.etree.ElementTree as et


class Scheduler():

    def __init__(self,_filepath):
        print("Scheduler starting...")
        self.filepath = _filepath
        print("Schedule file set to: ", self.filepath)
        
    def __exit__(self, exc_type, exc_value, traceback):
        print('Scheduler closing...')
    
    def changeScheduleFilePath(self,_filepath):
        self.filepath = _filepath
        print("Schedule file changed to: ", self.filepath)

    def readScheduleFile(self):
        print("importing schedule file...")
    
    def isActive(self):
        return True

    def printSchedule(self):
        print("current schedule is: ")


#scheduler1 = Scheduler()

#if __name__ == '__main__':
#        scheduler1.printSchedule()