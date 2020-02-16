import pandas as pd
import datetime
import sys
import os
import xml.etree.ElementTree as et


class Scheduler():

    def __init__(self, filepath):
        print("Scheduler starting...")
        self.filepath = filepath
        self.readScheduleFile()
        print("Schedule file set to: ", self.filepath)
        
    def __exit__(self, exc_type, exc_value, traceback):
        print("Scheduler closing...")
    
    def changeScheduleFile(self,filepath):
        self.filepath = filepath
        print("Schedule file changed to: ", self.filepath)

    def readScheduleFile(self):
        print("Importing schedule file...")
        self.tree = et.parse(self.filepath)
        self.root = self.tree.getroot()       
    
    def isActive(self, tag):

        now = datetime.datetime.now()
        print(now)
        
        return True

    def printSchedule(self):
        i=0
        time_arr = []
        temp_dict = {"hour": 0, "min": 0, "sec": 0, "dur": 0}
        print("Current schedule is: ")
        print(self.root)
        for plant in self.root:
            print(plant.tag, plant.attrib)
            for period in plant:
                print(period.tag, period.attrib)
                for days in period:
                    print(i, days.tag, days.attrib)
                    i+=1
                    for hours in days:
                        print(hours.tag, hours.text)
                        temp_dict["hour"] = hours.text
            #print(temp_dict)
            print("------------------------Next plant-----------------------")
        print("------------------------Second part-----------------------")

        for period in self.root.iter("period"):
            print(period.tag, period.attrib)
        
        for weekday in self.root.iter("weekday"):
            print(weekday.tag, weekday.attrib)
            # temp_dict["hour"] = int(weekday.find("hour").text)
            # temp_dict["min"] = int(weekday.find("minute").text)
            # temp_dict["sec"] = int(weekday.find("second").text)
            # temp_dict["dur"] = weekday.find("duration").text #todo duration parsing
            #time_arr.append(temp_dict) 
        #print(time_arr)
        #for period in self.root.iter(period.iter):
        #    print(period.attrib)
        #print(self.tree.items())
        #print(self.root.tag)
        #print(self.root.items())
        #print(self.root.keys())


#scheduler1 = Scheduler()

#if __name__ == '__main__':
#        scheduler1.printSchedule()