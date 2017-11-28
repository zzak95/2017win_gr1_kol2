# Class diary
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
# The default interface for interaction should be python interpreter.
# Please, use your imagination and create more functionalities.
# Your project should be able to handle entire school.
# If you have enough courage and time, try storing (reading/writing)
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface.

import json

class ClassDiary:
    def __init__(self):
        self.students=[]
        self.classes_count=0

    def add_student(self, name):
            self.students.append({"name and surname":name, "attendance":0, "math":[], "polish":[], "history":[],
                                  "physics":[], "chemistry":[], "english":[]})


    def add_score(self, name, class_name, score):
        for st in self.students:
            if st.get("name and surname")==name:
                st[class_name].append(score)

    def get_average_in_class(self,name,class_name):
        for st in self.students:
            if st.get("name and surname")==name:
                return sum(st[class_name])/len(st[class_name])

    def get_total_average(self, name):
        result=0
        for key in self.students[0]:
            if key != "name and surname" and key != "attendance":
                result=result + self.get_average_in_class(name, key)
        return result/(len(self.students[0])-2)

    def attendance(self):
        for st in self.students:
           answ=input(st["name and surname"])
           if answ != 1  and  answ != 0:
            st["attendance"]+=int(answ)
           else: break
        self.classes_count = self.classes_count+1

    def get_total_attendance(self, name):
        for st in self.students:
            if st.get("name and surname") == name:
                return st["attendance"]/self.classes_count

    def write_class_data(self, file_name):
        with open(file_name,'w') as f1:
            json.dump(self.students, f1)
        f1.close()


if __name__=="__main__":

    class1=ClassDiary()
    class1.add_student("Jan Kowalski")
    class1.add_score("Jan Kowalski","math",5)
    class1.add_score("Jan Kowalski", "math", 4)

    print("math average: ", class1.get_average_in_class("Jan Kowalski", "math"))

    class1.add_score("Jan Kowalski", "polish", 5)
    class1.add_score("Jan Kowalski", "history", 4)
    class1.add_score("Jan Kowalski", "physics", 3)
    class1.add_score("Jan Kowalski", "chemistry", 5)
    class1.add_score("Jan Kowalski", "english", 4)

  
    print("total average: ", class1.get_total_average("Jan Kowalski"))

    class1.add_student("Anna Nowak")
    class1.attendance()
    class1.attendance()
    print("total attendance: ", class1.get_total_attendance("Jan Kowalski"))
    class1.write_class_data("class_1.json")


