sr = []
def student_record(Roll_No, Student_Name, marks):
    sr.append([Roll_No, Student_Name, marks])
student_record(1, "Abhinav", 92)
student_record(2, "Prakash", 80)
student_record(3, "Stefan ", 84)
student_record(4, "Taylor ", 96)
def print_second_row():
    print(f"{sr[1][0]}          {sr[1][1]}      {sr[1][2]}")
    
print_second_row()