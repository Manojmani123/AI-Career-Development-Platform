from django.contrib import admin
from .models import *

admin.site.register(UserProfile)
admin.site.register(JobRole)
admin.site.register(Skill)
admin.site.register(JobRoleSkill)
admin.site.register(LearningResource)
admin.site.register(InterviewQuestion)
admin.site.register(AdminRequest)