from django.db import models
from django.contrib.auth.models import User

# Employee Details
class EmployeeDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=15)
    address = models.TextField()
    date_of_birth = models.DateField()
    second_mobile_number = models.CharField(max_length=15, blank=True, null=True)
    aadhar_card_copy = models.FileField(upload_to='aadhar/')
    pan_card_copy = models.FileField(upload_to='pan/')
    college_mark_sheet = models.FileField(upload_to='college_marks/')
    employee_photo = models.ImageField(upload_to='Profile')
    twelfth_mark_sheet = models.FileField(upload_to='12th_marks/')
    tenth_mark_sheet = models.FileField(upload_to='10th_marks/')
    is_trainee = models.BooleanField(default=False)
    is_team_member = models.BooleanField(default=False)
    is_team_leader = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_admin_assistant = models.BooleanField(default=False)

    def __str__(self):
        return self.name

# Team
class Team(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=50)
    leader = models.ForeignKey(EmployeeDetail, on_delete=models.SET_NULL, null=True, related_name='leader_of')
    members = models.ManyToManyField(EmployeeDetail, related_name='teams')

    def __str__(self):
        return self.name

# Client Details
class ClientDetail(models.Model):
    name = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.name

# Task Sheet
class TaskSheet(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    assigned_to = models.ForeignKey(EmployeeDetail, on_delete=models.CASCADE)
    assigned_by = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    due_date = models.DateField()

    def __str__(self):
        return self.title

# Employee Roles
class EmployeeRole(models.Model):
    role_name = models.CharField(max_length=255)
    description = models.TextField()
    employees = models.ManyToManyField(EmployeeDetail, related_name='roles')

    def __str__(self):
        return self.role_name
