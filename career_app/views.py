from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import JobRole, Skill, JobRoleSkill, LearningResource,  InterviewQuestion
from django.contrib.auth.models import User



def home(request):
    return render(request, 'career_app/home.html')


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'career_app/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)

            if user.is_superuser:
                return redirect('super_admin_dashboard')
            elif user.is_staff:
                return redirect('admin_dashboard')
            else:
                return redirect('dashboard')
    else:
        form = AuthenticationForm()

    return render(request, 'career_app/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def dashboard_view(request):
    return render(request, 'career_app/dashboard.html')


@login_required
def admin_dashboard_view(request):
    if not request.user.is_staff:
        return redirect('dashboard')

    return render(request, 'career_app/admin_dashboard.html')


@login_required
def super_admin_dashboard_view(request):
    if not request.user.is_superuser:
        return redirect('dashboard')

    return render(request, 'career_app/super_admin_dashboard.html')
@login_required
def add_job_role(request):
    if not request.user.is_staff:
        return redirect('dashboard')

    if request.method == 'POST':
        role_name = request.POST.get('role_name')
        description = request.POST.get('description')

        if role_name and description:
            JobRole.objects.create(
                role_name=role_name,
                description=description
            )
            return redirect('view_job_roles')

    return render(request, 'career_app/add_job_role.html')


@login_required
def view_job_roles(request):
    if not request.user.is_staff:
        return redirect('dashboard')

    job_roles = JobRole.objects.all()

    return render(request, 'career_app/view_job_roles.html', {
        'job_roles': job_roles
    })
@login_required
def add_skill(request):
    if not request.user.is_staff:
        return redirect('dashboard')

    if request.method == 'POST':
        skill_name = request.POST.get('skill_name')

        if skill_name:
            Skill.objects.create(skill_name=skill_name)
            return redirect('view_skills')

    return render(request, 'career_app/add_skill.html')


@login_required
def view_skills(request):
    if not request.user.is_staff:
        return redirect('dashboard')

    skills = Skill.objects.all()

    return render(request, 'career_app/view_skills.html', {
        'skills': skills
    })

@login_required
def assign_skills_to_role(request):
    if not request.user.is_staff:
        return redirect('dashboard')

    job_roles = JobRole.objects.all()
    skills = Skill.objects.all()

    if request.method == 'POST':
        job_role_id = request.POST.get('job_role')
        selected_skills = request.POST.getlist('skills')

        job_role = JobRole.objects.get(id=job_role_id)

        for skill_id in selected_skills:
            skill = Skill.objects.get(id=skill_id)

            JobRoleSkill.objects.get_or_create(
                job_role=job_role,
                skill=skill
            )

        return redirect('view_role_skills')

    return render(request, 'career_app/assign_skills.html', {
        'job_roles': job_roles,
        'skills': skills
    })


@login_required
def view_role_skills(request):
    if not request.user.is_staff:
        return redirect('dashboard')

    role_skills = JobRoleSkill.objects.select_related('job_role', 'skill').all()

    return render(request, 'career_app/view_role_skills.html', {
        'role_skills': role_skills
    })
@login_required
def add_learning_resource(request):
    if not request.user.is_staff:
        return redirect('dashboard')

    skills = Skill.objects.all()

    if request.method == 'POST':
        title = request.POST.get('title')
        url = request.POST.get('url')
        skill_id = request.POST.get('skill')

        if title and url and skill_id:
            skill = Skill.objects.get(id=skill_id)
            LearningResource.objects.create(
                title=title,
                url=url,
                skill=skill
            )
            return redirect('view_learning_resources')

    return render(request, 'career_app/add_learning_resource.html', {
        'skills': skills
    })


@login_required
def view_learning_resources(request):
    if not request.user.is_staff:
        return redirect('dashboard')

    resources = LearningResource.objects.select_related('skill').all()

    return render(request, 'career_app/view_learning_resources.html', {
        'resources': resources
    })
@login_required
def add_interview_question(request):
    if not request.user.is_staff:
        return redirect('dashboard')

    job_roles = JobRole.objects.all()

    if request.method == 'POST':
        job_role_id = request.POST.get('job_role')
        question = request.POST.get('question')

        if job_role_id and question:
            job_role = JobRole.objects.get(id=job_role_id)
            InterviewQuestion.objects.create(
                job_role=job_role,
                question=question
            )
            return redirect('view_interview_questions')

    return render(request, 'career_app/add_interview_question.html', {
        'job_roles': job_roles
    })


@login_required
def view_interview_questions(request):
    if not request.user.is_staff:
        return redirect('dashboard')

    questions = InterviewQuestion.objects.select_related('job_role').all()

    return render(request, 'career_app/view_interview_questions.html', {
        'questions': questions
    })
@login_required
def super_admin_dashboard_view(request):
    if not request.user.is_superuser:
        return redirect('dashboard')

    total_users = User.objects.filter(is_staff=False, is_superuser=False).count()
    total_admins = User.objects.filter(is_staff=True, is_superuser=False).count()
    total_job_roles = JobRole.objects.count()

    return render(request, 'career_app/super_admin_dashboard.html', {
        'total_users': total_users,
        'total_admins': total_admins,
        'total_job_roles': total_job_roles,
    })
@login_required
def view_users(request):
    if not request.user.is_superuser:
        return redirect('dashboard')

    users = User.objects.filter(is_staff=False, is_superuser=False)

    return render(request, 'career_app/view_users.html', {
        'users': users
    })


@login_required
def view_admins(request):
    if not request.user.is_superuser:
        return redirect('dashboard')

    admins = User.objects.filter(is_staff=True, is_superuser=False)

    return render(request, 'career_app/view_admins.html', {
        'admins': admins
    })