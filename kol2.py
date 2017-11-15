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

#!usr/bin/python

class Subject:
	def __init__(self):
		self.scores=[]
	
	def add (self, score):
		self.scores.append(score)


class Student:
	def __init__(self, name, surname):
		self.name=name
		self.surname=surname
		self.classes=[]

	def add_class (self, class_name):
		
		self.classes.append(class_name)
	
	def add_score(self, class_name, score):
		index = self.classes.index(class_name)
		self.classes[index].add(score)

	def get_average_in_class(self, class_name):
		index = self.classes.index(class_name)
		#average=sum(self.classes[index].scores)/len(self.classes[index].scores
		#return sum(self.classes[index].scores)/len(self.classes[index].scores
		

		






if __name__=="__main__":

	maths=Subject()
	s1=Student("Jan", "Kowalski")
	s1.add_class(maths)
	s1.add_score(maths, 5)
	#print(s1.get_average_in_class(maths))
	
	

		
