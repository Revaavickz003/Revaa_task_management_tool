from django.db import models
from django.contrib.auth.models import User

    
class ProductTable(models.Model):
    Product_Name = models.CharField(max_length=25)
    creaded_by =  models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=255, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return self.Product_Name
    
class ProjectCategories(models.Model):
    category_name = models.CharField(max_length=255)
    creaded_by =  models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=255, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return self.category_name

# Files Created
def lead_and_customer_companylogo(instance, org_name):
    return f'Leads and Customer/{instance.org_name}/{org_name}'

# Generate Customer ID
def generate_customer_id():
    last_customer = CustomerTable.objects.order_by('-id').first()
    if last_customer:
        last_id = int(last_customer.customer_id[7:]) 
        new_id = last_id + 1
    else:
        new_id = 1
    return f'RDSCUS{new_id:04d}'

# Client details
class CustomerTable(models.Model):
    FRESH = 'Fresh'
    CALL_BACK = 'Call Back'
    DO_NOT_DISTURB = 'Do Not Disturb'
    FOLLOW_UP = 'Follow up'
    PROPOSED = 'Proposed'
    HOLD = 'Hold'
    CLOSED = 'Closed'
    STATUS_CHOICES = [
        (FRESH, 'Fresh'),
        (CALL_BACK, 'Call Back'),
        (DO_NOT_DISTURB, 'Do Not Disturb'),
        (FOLLOW_UP, 'Follow up'),
        (PROPOSED, 'Proposed'),
        (HOLD, 'Hold'),
        (CLOSED, 'Closed'),
    ]

    HIGH = 'High'
    MEDIUM = 'Medium'
    LOW = 'Low'
    PRIORITY_CHOICES = [
        (HIGH, 'High'),
        (MEDIUM, 'Medium'),
        (LOW, 'Low'),
    ]

    ONE_TIME = 'One Time'
    RECURRING = 'Recurring'
    BUSINESS_TYPE_CHOICES = [
        (ONE_TIME, 'One Time'),
        (RECURRING, 'Recurring'),
    ]

    CREATIVE = 'Creative'
    DIGITAL_MARKETTING = 'Digital Marketing'
    DEVELOPMENT = 'Development'
    CLIENT_RELATIONSHIP = 'Client Relationship'
    PROJECT_CATEGORIES = [
        (CREATIVE, 'Creative'),
        (DIGITAL_MARKETTING, 'Digital Marketing'),
        (DEVELOPMENT, 'Development'),
        (CLIENT_RELATIONSHIP, 'Client Relationship'),
    ]

    customer_id = models.CharField(max_length=10, default=generate_customer_id, unique=True)
    client_name = models.CharField(max_length=20)
    client_number = models.IntegerField()
    org_name = models.CharField(max_length=30)
    org_img = models.ImageField(upload_to= lead_and_customer_companylogo, null=True, blank=True)
    products = models.ForeignKey(ProductTable, on_delete=models.SET_NULL, related_name='Product_table', null=True)
    end_of_date = models.DateField()
    priority = models.CharField(choices=PRIORITY_CHOICES, max_length=10)
    project_categories = models.ForeignKey(ProjectCategories, on_delete=models.SET_NULL, related_name='Project_categories', null=True)
    mail_id = models.EmailField(max_length=50, null=True, blank=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=15)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='custoner_created', null=True)
    created_date = models.DateField(auto_now_add=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='customer_updated_by', null=True)
    updated_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.org_name

# Employee Details
class EmployeeDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=10, unique=True, blank=True, null=True)
    name = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=15)
    address = models.TextField()
    date_of_birth = models.DateField()
    second_mobile_number = models.CharField(max_length=15, blank=True, null=True)
    aadhar_card_copy = models.FileField(upload_to='aadhar/', blank=True, null=True)
    pan_card_copy = models.FileField(upload_to='pan/', blank=True, null=True)
    college_mark_sheet = models.FileField(upload_to='college_marks/', blank=True, null=True)
    employee_photo = models.ImageField(upload_to='Profile', blank=True, null=True)
    twelfth_mark_sheet = models.FileField(upload_to='12th_marks/', blank=True, null=True)
    tenth_mark_sheet = models.FileField(upload_to='10th_marks/', blank=True, null=True)
    blood_group = models.CharField(max_length=5, blank=True, null=True)
    is_trainee = models.BooleanField(default=False)
    is_team_member = models.BooleanField(default=False)
    is_team_leader = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_admin_assistant = models.BooleanField(default=False)

    # Deportment
    creative = models.BooleanField(default=False)
    digital_marketin = models.BooleanField(default=False)
    development = models.BooleanField(default=False)
    client_relationship = models.BooleanField(default=False)

    # Role
    Graphic_designer = models.BooleanField(default=False)
    Video_Editing = models.BooleanField(default=False)
    Social_Media_Management = models.BooleanField(default=False)
    Content_Creation = models.BooleanField(default=False)
    Search_Engine_Optimization = models.BooleanField(default=False)
    Contant_Writing = models.BooleanField(default=False)
    Webside_Development = models.BooleanField(default=False)
    Software_Development = models.BooleanField(default=False)
    App_Development = models.BooleanField(default=False)
    Testing = models.BooleanField(default=False)
    Account_Manager = models.BooleanField(default=False)
    Admin = models.BooleanField(default=False)

    # Basic Informations
    creaded_by =  models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=255, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)



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

