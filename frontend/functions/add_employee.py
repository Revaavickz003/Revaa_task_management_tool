from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from frontend.models import *
import datetime as dt
from datetime import datetime
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
import json
from collections import defaultdict

@login_required(login_url='login')
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

@login_required(login_url='login')
def showemployee(request, epk):
    employee = get_object_or_404(EmployeeDetail, pk=epk)
    enddate = dt.datetime.now().date()
    startdate = enddate - dt.timedelta(days=6)
    monthly_report_startdate = enddate - dt.timedelta(days=28)
    employee_tasks = TaskSheet.objects.filter(assigned_to=employee, start_date_time__range=[startdate, enddate])
    monthly_tasks = TaskSheet.objects.filter(assigned_to=employee, start_date_time__range=[monthly_report_startdate, enddate])

    if request.method == 'POST':
        enddate_str = request.POST.get('enddate')
        startdate_str = request.POST.get('startdate')
        startdate = datetime.strptime(startdate_str, '%Y-%m-%d').date()
        enddate = datetime.strptime(enddate_str, '%Y-%m-%d').date()
        employee_tasks = TaskSheet.objects.filter(assigned_to=employee, start_date_time__range=[startdate, enddate])

    total_min = 0
    total_hrs = 0

    tasks_by_team_and_project = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: {"count": 0, "minutes": 0, "hours": 0, "pk": None})))
    weekly_data = defaultdict(lambda: defaultdict(int))

    for task in employee_tasks:
        team_name = task.project.team.name
        project_name = task.project.project_name
        task_type_name = task.task_type.name
        project_pk = task.project.pk

        task_timing = tasktimeing.objects.filter(task=task)
        total_minutes = sum(t.working_minutes or 0 for t in task_timing)
        total_hours = sum(t.working_hours or 0 for t in task_timing)

        total_min += total_minutes
        total_hrs += total_hours

        tasks_by_team_and_project[team_name][project_name]["pk"] = project_pk
        tasks_by_team_and_project[team_name][project_name][task_type_name]["count"] += 1
        tasks_by_team_and_project[team_name][project_name][task_type_name]["minutes"] += total_minutes
        tasks_by_team_and_project[team_name][project_name][task_type_name]["hours"] += total_hours

    for monthly_task in monthly_tasks:
        # Calculate weekly data
        task_date = monthly_task.start_date_time.date()
        week_number = (enddate - task_date).days // 7
        if week_number < 4:
            week_label = f"Week {4 - week_number}"
            weekly_data[week_label][task_date] += 1

    # Convert the aggregated tasks to JSON format
    tasks_json_compatible = {team: {project: {"pk": projects["pk"], "tasks": {task_type: {"count": task_details["count"], "minutes": task_details["minutes"], "hours": task_details["hours"], "pk": task_details["pk"]} for task_type, task_details in projects.items() if task_type != "pk"}} for project, projects in projects.items()} for team, projects in tasks_by_team_and_project.items()}
    tasks_json = json.dumps(tasks_json_compatible)

    # Prepare data for Chart.js
    weeks = sorted(weekly_data.keys())
    labels = sorted(set(date for week in weeks for date in weekly_data[week].keys()))
    datasets = [
        {
            "label": week,
            "data": [weekly_data[week].get(date, 0) for date in labels],
            "borderColor": f"rgba({255 - 40*i}, 99, 132, 1)",
            "borderWidth": 0.5,
            "fill": True,
            "lineTension": 0.4
        } for i, week in enumerate(weeks)
    ]

    context = {
        'teams_page': 'active',
        'team_members' : Team.objects.get(members=employee).members.exclude(pk=employee.pk),
        'employee': employee,
        'startdate': monthly_report_startdate,
        'enddate': enddate,
        'tasks': employee_tasks,
        'tasks_json': tasks_json,
        'datasets': json.dumps(datasets),
        'labels': json.dumps([date.strftime("%d-%m-%Y") for date in labels]),
        'total_min': total_min,
        'total_hrs': total_hrs,
    }
    return render(request, 'tmt-tool/employee_details.html', context)

