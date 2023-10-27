from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from website.forms import RecordForm, RegisterForm
from website.models import Record


def home(request):
    records = Record.objects.all()

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Authenticated
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You Have Been Logged')
            return redirect('home')
        else:
            messages.error(request, 'There Was An Error')
            return redirect('home')
    else: 
        return render(request, 'home.html', {'records': records})


def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Authenticated
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You Have Been Logged')
            return redirect('home')
        else:
            messages.success(request, 'There Was An Error')
            return redirect('home')
    else: 
        return render(request, 'home.html')

def logout_user(request):
    logout(request)
    messages.info(request, "You Have Been Logout")
    return redirect('home')


def register_user(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You Have Been Register!')
            return redirect('home')
    else:
        form = RegisterForm()    
    
    return render(request, 'register.html', {'form': form})


def record_user(request, pk):
    if request.user.is_authenticated:
        record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'record': record})
    else:
        messages.info(request, 'You Must Be Logged To Access This View')
        return redirect('home')
    

def delete_record(request, pk):
    if request.user.is_authenticated:
        record = Record.objects.get(id=pk)
        record.delete()
        messages.info(request, 'Record deleted successfully!')
        return redirect('home')
    else:
        messages.info(request, 'Record delet')
        return redirect('home')
    

def add_record(request):
    form = RecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':            
            if form.is_valid():
                form.save()
                messages.success(request, 'Record added successfully!')
                return redirect('home')
        else:
            return render(request, 'add_record.html', {'form': form})
    else:
        messages.info(request, 'You Must Be Logged To This View')
        return redirect('home')
    

def update_record(request, pk):
    if request.user.is_authenticated:
        record = Record.objects.get(id=pk)
        form = RecordForm(request.POST or None, instance=record)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record Updated Successfully!')
            return redirect('home')
        else:
            return render(request, 'update_record.html', {'form': form})
    else:
        messages.info(request, 'You Must Be Logged To This View')
        return redirect('home')
        