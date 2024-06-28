from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from frontend.models import *
import datetime as dt

from django.utils.timezone import make_aware
from datetime import datetime, timedelta
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.utils.timezone import now, timedelta
from frontend.models import EmployeeDetail, TaskSheet
from frontend.serializers import TaskSheetSerializer
from rest_framework.decorators import api_view

def addemployee(request):
    if request.method == 'POST':
        # Get all values from the form
        employee_id = request.POST.get('employee_id')
        employee_photo = request.FILES.get('employee_photo')
        ename = request.POST.get('ename')
        aadhar_card_copy = request.FILES.get('AadarCardCopy')
        mobile_number = request.POST.get('mobilenumber')
        pan_card_copy = request.FILES.get('pancardcopy')
        date_of_birth = request.POST.get('dateofbirth')
        college_marksheet = request.FILES.get('collegemarksheet')
        email_id  = request.POST.get('Emailid')
        twelfth_marksheet = request.FILES.get('twelfthmarksheet')
        second_mobile_num = request.POST.get('secondmobilenum')
        blood_group = request.POST.get('blood-group')
        tenth_marksheet = request.FILES.get('tenthmarksheet')
        address = request.POST.get('Address')

        is_trainee = request.POST.get('is_trainee') == 'on'
        is_team_member = request.POST.get('is_team_member') == 'on'
        is_team_leader = request.POST.get('is_team_leader') == 'on'
        is_manager = request.POST.get('is_manager') == 'on'
        is_admin = request.POST.get('is_admin') == 'on'
        is_admin_assistant = request.POST.get('is_admin_assistant') == 'on'

        creative = request.POST.get('creative') == 'on'
        digital_marketing = request.POST.get('digital_marketing') == 'on'
        development = request.POST.get('Development') == 'on'
        client_relationship = request.POST.get('client_relationship') == 'on'

        graphic_designer = request.POST.get('graphicdesigner') == 'on'
        video_editing = request.POST.get('Videoediting') == 'on'
        smm = request.POST.get('SMM') == 'on'
        content_creation = request.POST.get('contentcreation') == 'on'
        seo = request.POST.get('SEO') == 'on'
        content_writing = request.POST.get('contantwriting') == 'on'
        website_development = request.POST.get('websidedevelopment') == 'on'
        software_development = request.POST.get('Softwaredevelopment') == 'on'
        app_development = request.POST.get('appdevelpment') == 'on'
        tester = request.POST.get('Tester') == 'on'
        account_manager = request.POST.get('Accountmanager') == 'on'
        admin = request.POST.get('Admin') == 'on'

        # Create the new EmployeeDetail object
        user = User.objects.create_user(username=email_id, email=email_id, password='password')  # Change 'password' as needed
        employee_detail = EmployeeDetail(
            employee_id = employee_id,
            user=user,
            name=ename,
            mobile_number=mobile_number,
            address=address,
            date_of_birth=date_of_birth,
            second_mobile_number=second_mobile_num,
            aadhar_card_copy=aadhar_card_copy,
            pan_card_copy=pan_card_copy,
            college_mark_sheet=college_marksheet,
            employee_photo=employee_photo,
            twelfth_mark_sheet=twelfth_marksheet,
            tenth_mark_sheet=tenth_marksheet,
            blood_group = blood_group,
            is_trainee=is_trainee,
            is_team_member=is_team_member,
            is_team_leader=is_team_leader,
            is_manager=is_manager,
            is_admin=is_admin,
            is_admin_assistant=is_admin_assistant,
            creative=creative,
            digital_marketin=digital_marketing,
            development=development,
            client_relationship=client_relationship,
            Graphic_designer=graphic_designer,
            Video_Editing=video_editing,
            Social_Media_Management=smm,
            Content_Creation=content_creation,
            Search_Engine_Optimization=seo,
            Contant_Writing=content_writing,
            Webside_Development=website_development,
            Software_Development=software_development,
            App_Development=app_development,
            Testing=tester,
            Account_Manager=account_manager,
            Admin=admin,
            creaded_by = request.user,
            created_at = dt.datetime.now()
        )
        
        employee_detail.save()
    return redirect('teams')

def showemployee(request, epk):
    employee = EmployeeDetail.objects.get(pk=epk)
    enddate = dt.datetime.now().date
    startdate = enddate - dt.timedelta(days=7)
    employee_tasks = TaskSheet.objects.filter(assigned_to=employee, start_date_time__range=[startdate, enddate])
    for employee_task in employee_tasks:
        print(employee_task.title)
    context={
        'teams_page': 'active',
        'employee':employee,
        'employee_tasks':employee_tasks,
    }
    return render(request, 'tmt-tool/employee_details.html',context)


def employee_task_data(request, epk, start_date, end_date):
    employee = get_object_or_404(EmployeeDetail, pk=epk)
    employee_tasks = TaskSheet.objects.filter(assigned_to=employee, start_date_time__range=[start_date, end_date])
    pass