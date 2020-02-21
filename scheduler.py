import pandas as pd
import datetime
import sys
import os
import xml.etree.ElementTree as et


class Scheduler():

    def __init__(self, filepaths):
        print("Scheduler starting...")
        self.files = []
        self.trees = []
        if not isinstance(filepaths, list):
            self.files = [filepaths]
        else:
            self.files = filepaths

        self.read_schedule_file()

        print("Schedule files set to:")
        for i in self.files:
            print(i)
        
    def __exit__(self, exc_type, exc_value, traceback):
        print("Scheduler closing...")
    
    def change_schedule_file(self, filepath, index):
        self.files[index] = filepath
        print("Schedule files changed to: ", self.files)

    def add_schedule_file(self, filepath):
        self.files.append(filepath)
        print("Schedule file: ", self.filepath, "added to list")

    def read_schedule_file(self):
        print("Importing and parsing schedule files...")
        for i in range(len(self.files)):
            tree = et.parse(self.files[i])
            self.trees.append(tree)
    
    def parse_xml_to_df(self, root_tag):
        for element in self.trees:
            if element.getroot().tag == root_tag:
                print(element.getroot.tag())


        #TODO
        pass

    def is_active(self, tag):
        now = datetime.datetime.now()
        for element in self.trees:
            if element.getroot().tag == tag:
                print(now, element.getroot().tag)
        #TODO: compare now to schedule
        return True

    def print_schedule(self):
        i = 0
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
                    i += 1
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
