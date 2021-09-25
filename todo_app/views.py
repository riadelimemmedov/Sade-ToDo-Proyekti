from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import  *

# Create your views here.
@login_required(login_url='register')#burdaki login url deki name='logindir'
def index(request):
    todos = ToDo.objects.filter(profile__user = request.user).all()#yeni giris eden istifadecinin ToDo larini cek
    
    context = {
        'todos':todos,
    }
    
    return render(request,'main/index.html',context)

@login_required(login_url='register')
def create_todo(request):
    form = CreateToDoForm(request.POST or None)
    
    if form.is_valid():
        posts = form.save(commit=False)
        posts.profile = Profile.objects.get(user=request.user)
        posts.save()
        return redirect('index')
    
    return render(request,'main/createtodo.html',{'form':form})

@login_required(login_url='register')
def delete_todo(request,id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect('index')

@login_required(login_url='register')
def yes_finish(request,id):
    todo = ToDo.objects.get(id=id)#eger Truedursa False ele
    todo.finished = False#yeni yes_finish bir defe tiklayanda tersi olur yeni false cevirilir
    todo.save()
    return redirect('index')

@login_required(login_url='register')
def no_finish(request,id):
    todo = ToDo.objects.get(id=id)
    todo.finished = True
    todo.save()
    return redirect('index')

@login_required(login_url='register')
def update_doto(request,id):#burda hemin id li ToDonu alib update edirsen ona gore id ni hemise yaz updatede
    todo = ToDo.objects.get(id=id)
    form = UpdateForm(request.POST or None,instance=todo)

    if form.is_valid():#eger formum dogrudursa if e girsin
        posts = form.save(commit=False)#yeni gelen kimi save olmasin gorunmeyen deyiskinlikler edib forma gonderdikden sonra save oluncag ona gore commit=False yazildi yeni qadagalidir
        posts.profile = Profile.objects.get(user=request.user)
        posts.save()
        return redirect('index')
    
    return render(request,'main/updatetodo.html',{'form':form})




#!Profil Islemleri

def giris(request):
    if request.method == 'POST':
        namelogin = request.POST.get('username')
        namepassword = request.POST.get('password')
        
        #authenticate o ise yarayirki formdan gelen datalar databsede movcuddur ya yox eger movcuddursa databasede giris ele bilersen
        user = authenticate(username = namelogin,password = namepassword)
        
        if user is not None:#eger bele bir istifadeci varsa,not bir inkar None iki inkar iki inkar birlikde True eleyir if de hemise true olanda isleyir ona gore if bloguna girir
            login(request,user)
            messages.add_message(request,messages.SUCCESS,'Hesab Acildi')
            return redirect('index')
        else:
            messages.add_message(request,messages.ERROR,'Xetali istifadeci Adi ve ya Sifre')
            return redirect('login')
    else:
        return render(request,'main/login.html')
    
    
def qeydiyyat(request):
    if request.method == 'POST':#eger attigimiz request POST requestdirsa onda if e gir POST olanda gorunmur urldeki datalar buda onemlidir guvenlik terefinden
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['sifretekrar']
        
        if password == repassword:
            if User.objects.filter(username = username).exists():#yeni bele bir istifadeci adi movcuddursa
                messages.add_message(request,messages.WARNING,'Bele Bir Istifadeci Adi Movcuddur')
                return redirect('register')#burdaki register url deki name='register' dir
            else:
                if User.objects.filter(email=email).exists():#eger bele bir email movcuddursa movcudlugu ise exists() ile yoxlayirig
                    messages.add_message(request,messages.WARNING,'Bele Bir Email Adi Movcuddur')
                    return redirect('register')
                else:#create yox create_user yaz hemise istifadeci qeydiyyatdan kecence cunki bir istifadeci yaradirsa adida normal olarag create_user => yeni istifadeci yarat
                    user = User.objects.create_user(username=username,password=password,email=email)
                    user.save()
                    messages.add_message(request,messages.SUCCESS,'Ugurlu Bir Sekilde Qeydiyyatdan Kecdiniz')
                    return redirect('login')
        else:#?render => tercumesi gostermek demekdir yeni html seyfesini goster return render ile
            messages.add_message(request,messages.WARNING,'Sifre Xetali')
            return redirect('register')
    else:
        return render(request,'main/register.html')

def cikis(request):
    logout(request)
    return redirect('index')

