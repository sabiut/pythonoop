"""
Polymorphisms - This is when you have the same method name but different signatures
"""


class FullTimeStaff:

    def __init__(self):
        self.working_hrs = None

    def numberOfWorkingHrs(self):
        self.working_hrs = 40

    def disPlayWorkingHrs(self):
        print("The number of working hours is", self.working_hrs)


class PartTimeStaff(FullTimeStaff):
    def numberOfWorkingHrs(self):
        self.working_hrs = 25

    def resetNumOfWorkingHrs(self):
        super().numberOfWorkingHrs()


if __name__ == '__main__':
    full_time_staff = FullTimeStaff()
    full_time_staff.numberOfWorkingHrs()
    full_time_staff.disPlayWorkingHrs()
    """ 
    Creating the child class object that invoked the method that 
    overrides the number of working hours that was define from the parent class
     """
    part_time_staff = PartTimeStaff()
    part_time_staff.numberOfWorkingHrs()
    part_time_staff.disPlayWorkingHrs()

    """ Reseting the  number of working hours"""
    part_time_staff.resetNumOfWorkingHrs()
    part_time_staff.disPlayWorkingHrs()
