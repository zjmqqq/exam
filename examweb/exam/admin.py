from django.contrib import admin
from .models import Question,StudentInfo,TeacherInfo,ScoreInfo,Course,PaperInfo
admin.site.register(Question)
admin.site.register(StudentInfo)
admin.site.register(TeacherInfo)
admin.site.register(Course)
admin.site.register(ScoreInfo)
admin.site.register(PaperInfo)
