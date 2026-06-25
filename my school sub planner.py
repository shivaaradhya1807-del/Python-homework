print("====School subject planner====")

student1=("Harry" ,10 ,"Math")
student2=("Hanna" ,10 ,"english")
student3=("Jennie" ,10 ,"SS")
student4=("Lisa" ,10 ,"science")

print(student1)
print(student2)
print(student3)
print(student4)

monday = {"Math", "Science", "English"}
tuesday = {"Math", "SS", "Biology"}

monday.add("art")
print("Monday after adding art:", monday)

print("Monday :-",monday)
print("Tuesday :-",tuesday)

print("Common subjects :",(monday & tuesday ))
print("Both:-",(monday|tuesday))


