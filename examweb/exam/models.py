from django.db import models

from django.db import models

class Question(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    answerA = models.CharField(max_length=200)
    answerB = models.CharField(max_length=200)
    answerC = models.CharField(max_length=200)
    answerD = models.CharField(max_length=200)
    answerR = models.CharField(max_length=200)

    def __str__(self):
        return self.question_text

class StudentInfo(models.Model):
    account=models.CharField(max_length=20,primary_key=True)
    password=models.CharField(max_length=200)
    name=models.CharField(max_length=200)
    Sex = models.CharField(max_length=200)
    Birth = models.DateTimeField(blank=True, null=True)
    Tel = models.CharField(max_length=200)
    Email = models.CharField(max_length=200)
    Addr = models.CharField(max_length=200)
    def __str__(self):
        return self.name
class TeacherInfo(models.Model):
    account = models.CharField(max_length=200,primary_key=True)
    password = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    Sex = models.CharField(max_length=200)
    Birth = models.DateTimeField(blank=True, null=True)
    Tel = models.CharField(max_length=200)
    Email = models.CharField(max_length=200)
    Addr = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class PaperInfo(models.Model):
    PaperName=models.CharField(max_length=200)
    Teacher=models.ForeignKey(TeacherInfo, on_delete=models.CASCADE)
    Pcourse=models.ForeignKey("Course",on_delete=models.CASCADE,null=True)
    examdate = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return self.PaperName
class Course(models.Model):
    CourseName=models.CharField(max_length=200)
    def __str__(self):
        return self.CourseName
class ScoreInfo(models.Model):
    Spaperinfo=models.ForeignKey(PaperInfo,on_delete=models.CASCADE)
    Student=models.ForeignKey(StudentInfo,on_delete=models.CASCADE)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    Score=models.IntegerField()
    def __str__(self):
        return self.Student_id


