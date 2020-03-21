from datetime import datetime, timedelta
import xml.etree.ElementTree as et


class Scheduler(object):

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
    
    def is_exception_by_tag(self, tag):
        exempt = False
        now = datetime.now()
        for element in self.trees:
            if element.getroot().tag == tag:
                for exception in element.iter("exception"):
                    if datetime.strptime(exception.attrib["begin"], "%Y-%m-%d %H:%M:%S") < now < datetime.strptime(exception.attrib["end"], "%Y-%m-%d %H:%M:%S"):
                        exempt = True
                        print(exception.attrib["id"])
        return exempt

    def is_active_by_tag(self, tag):
        active = False
        now = datetime.now()
        for element in self.trees:
            if element.getroot().tag == tag:
                for period in element.iter("period"):
                    if datetime.strptime(period.attrib["begin"], "%Y-%m-%d %H:%M:%S") < now < datetime.strptime(period.attrib["end"], "%Y-%m-%d %H:%M:%S") and self.is_exception_by_tag(tag) is False:
                        for weekday in period:
                            if weekday.attrib["day"] == now.strftime("%A"):
                                start_time = datetime.strptime(weekday[0].text, "%H:%M:%S")
                                duration = datetime.strptime(weekday[1].text, "%H:%M:%S")
                                end_time = start_time + timedelta(hours=duration.hour, minutes=duration.minute, seconds=duration.second)
                                if start_time.time() <= now.time() <= end_time.time():
                                    active = True
        return active

    def get_tags(self):
        tags = []
        for element in self.trees:
            tags.append(element.getroot().tag)
        return tags

    def get_tags_amount(self):
        return len(self.trees)

    def is_active_all(self):
        active_dict = {}
        now = datetime.now()
        for element in self.trees:
            active_dict.update({element.getroot().tag: False})
            for period in element.iter("period"):
                if datetime.strptime(period.attrib["begin"], "%Y-%m-%d %H:%M:%S") < now < datetime.strptime(period.attrib["end"], "%Y-%m-%d %H:%M:%S") and self.is_exception_by_tag(element.getroot().tag) is False:
                    for weekday in period:
                        if weekday.attrib["day"] == now.strftime("%A"):
                            start_time = datetime.strptime(weekday[0].text, "%H:%M:%S")
                            duration = datetime.strptime(weekday[1].text, "%H:%M:%S")
                            end_time = start_time + timedelta(hours=duration.hour, minutes=duration.minute, seconds=duration.second)
                            if start_time.time() <= now.time() <= end_time.time():
                                active_dict[element.getroot().tag] = True

        return active_dict

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

    def print_schedule_by_tag(self, tag):
        print("Current ", tag, "\'s schedule is: ")
        for element in self.trees:
            if element.getroot().tag == tag:
                print(element.getroot().tag, element.getroot().attrib)
                for period in element.iter("period"):
                    print("\t", period.tag, period.attrib)
                    for weekday in period:
                        print("\t\t", weekday.tag, weekday.attrib, weekday[0].text, weekday[1].text)
                for exception in element.iter("exception"):
                    print("\t", exception.tag, exception.attrib)

# scheduler1 = Scheduler()

# if __name__ == '__main__':
#                      print("done")
