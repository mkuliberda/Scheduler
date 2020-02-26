from datetime import datetime, timedelta
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
    
    def is_exception(self, tag):
        #TODO
        return False

    def is_active(self, tag):
        now = datetime.now()
        activate = False
        for element in self.trees:
            if element.getroot().tag == tag:
                for period in element.iter("period"):
                    if now > datetime.strptime(period.attrib["begin"], "%Y-%m-%d %H:%M:%S") and now < datetime.strptime(period.attrib["end"], "%Y-%m-%d %H:%M:%S") and self.is_exception(tag) is False:
                        for weekday in period:
                            if weekday.attrib["day"] == now.strftime("%A"):
                                start_time = datetime.strptime(weekday[0].text, "%H:%M:%S")
                                duration = datetime.strptime(weekday[1].text, "%H:%M:%S")
                                end_time = start_time + timedelta(hours=duration.hour, minutes=duration.minute, seconds=duration.second)
                                if now.time() >= start_time.time() and now.time() <= end_time.time():
                                    activate = True
                                    #print(start_time, duration, end_time)
                                    #print(weekday.tag, weekday.attrib, weekday[0].text, weekday[1].text)

        return activate

    def print_full_schedule(self):
        print("Current schedule is: ")
        for element in self.trees:
            print(element.getroot().tag, element.getroot().attrib)
            for period in element.iter("period"):
                print("\t", period.tag, period.attrib)
                for weekday in period:
                    print("\t\t", weekday.tag, weekday.attrib, weekday[0].text, weekday[1].text)
            for exception in element.iter("exception"):
                print("\t", exception.tag, exception.attrib)
            #print("------------------------Next schedule-----------------------")
    


        # for element in self.root:
        #     print(plant.tag, plant.attrib)
        #     for period in plant:
        #         print(period.tag, period.attrib)
        #         for days in period:
        #             print(i, days.tag, days.attrib)
        #             i += 1
        #             for hours in days:
        #                 print(hours.tag, hours.text)
        #                 temp_dict["hour"] = hours.text
        # print("------------------------Next file-----------------------")

        # for period in self.root.iter("period"):
        #     print(period.tag, period.attrib)
        
        # for weekday in self.root.iter("weekday"):
        #     print(weekday.tag, weekday.attrib)
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

# if __name__ == '__main__':
#                      print("done")
