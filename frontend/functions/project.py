from django.shortcuts import render
from frontend.models import ProjectCategories, CustomerTable

def projects_page(request):
    all_projects = CustomerTable.objects.all()
    all_project_categories = ProjectCategories.objects.all()
    
    # Calculate the project count for each category
    categories_with_counts = []
    for category in all_project_categories:
        project_count = CustomerTable.objects.filter(project_categories=category).count()
        categories_with_counts.append((category, project_count))
    
    context = {
        'all_projects': all_projects,
        'categories_with_counts': categories_with_counts,
    }
    
    return render(request, 'tmt-tool/project.html', context)

