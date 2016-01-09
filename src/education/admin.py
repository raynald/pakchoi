from django.contrib import admin
from models import Order, Subject, Teacher, Student, City, District, Level, Rating, Grade,\
    Problem, Answer

class SubjectAdmin(admin.ModelAdmin):
    pass

class TeacherAdmin(admin.ModelAdmin):
    pass

class StudentAdmin(admin.ModelAdmin):
    pass

class CityAdmin(admin.ModelAdmin):
    pass

class DistrictAdmin(admin.ModelAdmin):
    pass

class LevelAdmin(admin.ModelAdmin):
    pass

class RatingAdmin(admin.ModelAdmin):
    pass

class GradeAdmin(admin.ModelAdmin):
    pass

class ProblemAdmin(admin.ModelAdmin):
    pass

class AnswerAdmin(admin.ModelAdmin):
    pass

class OrderAdmin(admin.ModelAdmin):
    pass


admin.site.register(Subject, SubjectAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(Level, LevelAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(Grade, GradeAdmin)
admin.site.register(Problem, ProblemAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Order, OrderAdmin)
