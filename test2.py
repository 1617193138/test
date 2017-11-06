#!/usr/bin/python
# -*- coding: UTF-8 -*-

class StudentInformation:
   '学生信息'
   stu_male_empCount = 0
   stu_female_empCount = 0
 
   def __init__(self, name, stu_no, class_no, gender, English, program):
      self.name = name
      self.stu_no = stu_no
      self.class_no = class_no
      self.gender = gender
      self.English = English
      self.program = program
      if gender == 'male':
         StudentInformation.stu_male_empCount += 1
      else:
         StudentInformation.stu_female_empCount += 1
   def displayStu_male_Count(self):
      print StudentInformation.stu_male_empCount

   def displayStu_female_Count(self):
      print StudentInformation.stu_female_empCount

   def displayInformation(self):
      print "Name : ", self.name,  ",Stu_no : ", "Stu_no : ", self.stu_no, ",Class_no :", self.class_no, ",Gender :", self.gender

   def speakEnglish(self):
       print self.name," 's English is",self.English

   def canprogram(self):
       print self.name," 's program is very",self.program
