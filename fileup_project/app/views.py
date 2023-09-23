from django.shortcuts import render,HttpResponse,redirect
from .forms import RegistrationForm,uploadForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .models import Upload
# Create your views here.
@login_required(login_url='/login')
def home(request):
    titles=Upload.objects.filter(author=request.user,title__isnull=False)
    user_files = Upload.objects.filter(author=request.user,Upload_File__isnull=False)
    user_images = Upload.objects.filter(author=request.user, Upload_Image__isnull=False)
    return render(request, 'main/home.html', {'user_files': user_files,'user_images': user_images,'title':titles})
def success(request):
    return render(request,'main/sucess.html')
@login_required(login_url='/login')
def upload_post(request):
    if request.method == 'POST':
        form = uploadForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author= request.user
            post.save()
            return redirect('/success')
    else:
            form=uploadForm()
    return render(request,'main/upload_file.html',{'form':form})    

def register(request):
    if request.method=='POST':
        form=RegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('/home')
    else:
        form=RegistrationForm()
    return render(request,'registration/register.html',{'form':form})       