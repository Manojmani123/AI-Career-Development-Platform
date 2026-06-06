from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)


class JobRole(models.Model):
    role_name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.role_name


class Skill(models.Model):
    skill_name = models.CharField(max_length=100)

    def __str__(self):
        return self.skill_name


class JobRoleSkill(models.Model):
    job_role = models.ForeignKey(JobRole, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.job_role.role_name} - {self.skill.skill_name}"

class LearningResource(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField()
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    def __str__(self):
        return self.title


class InterviewQuestion(models.Model):
    job_role = models.ForeignKey(JobRole, on_delete=models.CASCADE)
    question = models.TextField()


class AdminRequest(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()

    status_choices = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]

    status = models.CharField(
        max_length=20,
        choices=status_choices,
        default='Pending'
    )