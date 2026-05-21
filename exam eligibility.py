number_of_working_days = 200
number_of_days_present= int(input("enter the no. of  days present"))
attendence_pecentage=( number_of_days_present/ number_of_working_days)*100
print("Attendance Percentage =", attendence_pecentage, "%")


if attendence_pecentage >= 75:
    print("You can attend the exam")
else:
    print("Sorry you cannot attend the exam!")
