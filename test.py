from scheduler import *

TEST_SCHEDULE_FILE_PATH = "test.xml"

plants_schedule = Scheduler(TEST_SCHEDULE_FILE_PATH)
plants_schedule.printSchedule()
print (plants_schedule.isActive("Pelargonia"))

print("done!")