from scheduler import *

TEST1_SCHEDULE_FILE_PATH = "test1.xml"
TEST2_SCHEDULE_FILE_PATH = "test2.xml"
test_files = [TEST1_SCHEDULE_FILE_PATH, TEST2_SCHEDULE_FILE_PATH]


plants_schedule = Scheduler(test_files)
#plants_schedule.printSchedule()
print(plants_schedule.is_active("Pelargonia"))
print(plants_schedule.is_active("Surfinia"))

print("done!")
