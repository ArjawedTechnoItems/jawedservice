from django.shortcuts import render

# Create your views here.
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        user.save()

        messages.success(request, "Account created. Complete your profile.")
        return redirect('edit_profile')

    return render(request, 'register.html')

def user_login(request):
    if request.method == "POST":
        # username = request.POST['username']
        # password = request.POST['password']
        # print(username)
        # print(password)
        # user = authenticate(request, username=username, password=password)
        email = request.POST['email']
        password = request.POST['password']

        try:
            user_obj = User.objects.get(email=email)
            user = authenticate(
                request,
                username=user_obj.username,
                password=password
            )
        except User.DoesNotExist:
            user = None
        if user:
            login(request, user)
            print("hello")
            return redirect('view_profile')
        else:
            print("hello34")
            messages.error(request, "Invalid credentials")
            return redirect('login')

    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('login')

def service(request):
    category = request.GET.get('category')

    profiles = Profile.objects.select_related('user').all()

    # 🔹 Filter by service category
    if category:
        profiles = profiles.filter(service_category=category)

    # 🔹 Pagination
    paginator = Paginator(profiles, 10)  # 5 rows per page
    page_number = request.GET.get('page')
    profiles = paginator.get_page(page_number)

    context = {
        'profiles': profiles,
        'categories': Profile.ServiceCategory.choices,
        'selected_category': category,
    }

    return render(request, 'service.html', context)

@login_required
def edit_profile(request):
    profile = Profile.objects.get(user=request.user)

    if request.method == "POST":
        profile.full_name = request.POST['full_name']
        profile.phone = request.POST['phone']
        profile.service_category = request.POST.get('service_category')
        profile.work = request.POST['work']
        profile.work_description = request.POST['work_description']
        profile.experience = request.POST['experience']
        profile.address = request.POST['address']
        profile.location = request.POST['location']

        if 'profile_pic' in request.FILES:
            profile.profile_pic = request.FILES['profile_pic']

        profile.save()
        return redirect('view_profile')

    return render(request, 'edit_profile.html', {'profile': profile})

@login_required
def view_profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'profile.html', {'profile': profile})






