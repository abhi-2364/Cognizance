sr = []
def student_record(Roll_No, Student_Name, marks):
    sr.append([Roll_No, Student_Name, marks])
student_record(1, "Abhinav", 92)
student_record(2, "Prakash", 80)
student_record(3, "Stefan ", 84)
student_record(4, "Taylor ", 96)
def list():
    if(len(sr) != 0):
        print("Roll_No   Student_Name      Marks")
    for i in sr:
        print(f"{i[0]}         {i[1]}            {i[2]}")
 
list()