from .forms import *
from .models import *
from django.contrib import messages 
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required 
# Create your views here.



def index(request):
    online_user = ProfileModel.objects.filter(is_online=True)
    online_soni = ProfileModel.objects.filter(is_online=True).count()

    ctx={
        "online_user":online_user,
        'online_soni':online_soni
    }
    return render(request, 'index.html',ctx)


######### filter qilish vazifa
def project_page(request):
    project_page = ProjectModel.objects.filter(yonalish='backend').count()
    proyect = ProjectModel.objects.filter(yonalish='frontend').count()
    projectss= ProjectModel.objects.all()
    al = ProjectModel.objects.all().count()
    ctx={
        'project_page':project_page,
        'projectss':projectss,
        'proyect':proyect,
        'al':al
    }

    return render(request, 'project_page.html',ctx )


def CommentView(request,comid):
    form = CommentForm()
    comment_id = ProjectModel.objects.get(id = comid)
    if request.method == "POST":
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.project = ProjectModel.objects.get(pk=comid)
            comment.user_profile = request.user.profilemodel
            comment.user_profile_image = request.user.profilemodel.profil_image
            
            comment.save()
    
    comment_data = Comment.objects.filter(project_id = comment_id)
    commentcount= Comment.objects.filter(project_id = comment_id).count()
    # commentview = Comment.objects.get(id = comid)
    # commentview.view += 1
    # commentview.save()

    ctx={
        'form':form,
        'comment_id':comment_id,
        'comment_data':comment_data,
        'commentcount':commentcount,
        # 'commentview':commentview
    }
    return render(request, 'comment.html', ctx)


def blog(request):
    return render(request, 'blog.html')


def Userlogin(request):
    if request.POST:
        username = request.POST["UserName"]
        password = request.POST["password"]

        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'xush kelipsiz')
            return redirect('index')
        else:
            messages.error(request, 'xato username yoki passwordda')

    form = LoginForm()
    ctx = {
        "form": form,
        
    }
    return render(request, 'login.html',ctx)
    
    
def UserLogout(request):
    logout(request)
    return redirect('login')

def sign(request):
    form =SignupForm()
    if  request.method == 'POST':
        form =SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else :
            print("error")
            return redirect('sign')
    ctx = {
            'form' : form,
        }
    
    return render(request, 'sign_up.html',ctx)

@login_required()  
def Sectionview(request):
    def button(request):
        return render (request, button('/'))
    return render(request,'section.html',)

@login_required()  
def EditProfilView(request,editid):
    editprofil = ProfileModel.objects.get(id=editid)
    if request.method=="POST":
        form = ProfilForm(request.POST,  request.FILES, instance=editprofil)
        if form.is_valid():
            form.save()
            return redirect('bio')
        else:
            print('error')
    form = ProfilForm(instance=editprofil)
    ctx={
        'form':form,
        'editprofil':editprofil
    }
    
    return render(request, 'editprofil.html',ctx)
    

@login_required()  
def bioView(request):
    form = ProfilForm()
    if request.method == "POST":
        form = ProfilForm(request.POST,request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            tel_nomer = form.cleaned_data['tel_nomer']
            email = form.cleaned_data['email']
            profil_image = form.cleaned_data['profil_image']
            profile_data = ProfileModel(name=name, email=email, tel_nomer = tel_nomer , profil_image = profil_image)
            profile_data.save()
            print("salom")
            return redirect('bio')
        else:
            print('error')
            return redirect('bio')
    data = request.user.profilemodel
    ctx ={
        'form': form,
        "data":data
        # 'userd':ProfileModel.objects.get(id=id)
    }
    
    return render(request, 'bio.html', ctx)
    

@login_required() 
def projectview (request, prj_id):
    profile_id = ProfileModel.objects.get(id=prj_id)
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=profile_id)
        if form.is_valid():
            name = form.cleaned_data['name']
            price = form.cleaned_data['price']
            gitHub_link = form.cleaned_data['gitHub_link']
            project_image = form.cleaned_data['project_image']
            yonalish = form.cleaned_data['yonalish']        
            profil_data = ProjectModel(name=name,price=price,gitHub_link=gitHub_link, profil=profile_id, project_image=project_image, yonalish=yonalish)
            profil_data.save()

        else:
            print('error')
            return redirect('project')
    form = ProjectForm()
    projects = ProjectModel.objects.filter(profil_id = profile_id)
    ctx ={
        'form':form,
        'projects': projects
    }
    return render (request, 'project.html',ctx)


@login_required()
def EditProjectView(request,edit_id):
    edit_project = ProjectModel.objects.get(id=edit_id)
    if request.method=="POST":
        form = ProjectForm(request.POST, instance=edit_project)
        if form.is_valid():
            form.save()
            return redirect('project')
        else:
            print('error')
    form = ProjectForm(instance=edit_project)
    ctx={
        'form':form,
        'edit_project':edit_project
    }
    return render(request, 'edit_p.html', ctx)


@login_required()
def DeleteProjectView(request,delete_id):
    delete_project = ProjectModel.objects.get(id=delete_id)
    print(delete_project)
    if request.POST:
        delete_project.delete()
        return redirect('project')
    else:

        ctx={
            'delete_project':delete_project
        }
        return render(request, 'delete_p.html', ctx)

