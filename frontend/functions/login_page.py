from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login
# from django.contrib.auth.decorators import login_required, authenticate
# from django.views.decorators.csrf import csrf_protect


def login_view(request):
    if request.method == 'POST':
        email = request.POST['emailaddress']
        password = request.POST['password']
        # user = authenticate(request, email=email, password=password)

        return redirect('home')
    
    return render(request, 'tmt-tool/login_page.html')
