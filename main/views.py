from main.decorators import allowed_users, unauthenticated_user
from main.models import Category, Formation
from main.forms import CategoryForm, CreateUserForm, FormationForm
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
# Create your views here.
# inscription 
@unauthenticated_user
def registration(request):
    form = CreateUserForm()
    if request.method == 'POST' :
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('login')
            
    context ={'form' : form}
    return render(request, 'main/registration.html' , context)

#login page 
@unauthenticated_user
def loginpage (request) :
  
        if request.method == 'POST' :
            username = request.POST.get('username') 
            password = request.POST.get('password') 
            user = authenticate(request , username = username , password = password)
            if user is not None :
                login(request , user)
                return redirect ('home')
            else:
                messages = "username or password is incorect"
                context = {'message' : messages} 
                return render(request , 'main/login.html' , context )
        return render(request , 'main/login.html' )

#logout page 
def logoutpage(request):
    logout(request)
    return redirect('login') 

#page d'accuiel just pour les admins 
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def home_page(request):
    formations = Formation.objects.all() 
    nb = Formation.objects.count() 
    context = {'formations' : formations , 'nb' : nb}
    return render(request , 'main/home.html' , context)

#page d'accueil pour tout les visiteurs 
def home_utilisateur(request) :
    formations = Formation.objects.all() 
    category = Category.objects.all() 
    context = {'formations' : formations , 'categorys' : category}
    return render(request , 'main/home_utilisateur.html' , context)

#page de creation de formation
@allowed_users(allowed_roles=['admin'])
@login_required(login_url='login')
def create_formation(request):
    form = FormationForm(request.FILES)
    if request.method == 'POST':
        form = FormationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save() 
            return redirect('/home')
    context ={'f':form}
    return render(request , 'main/FormationForm.html' , context)

#modification de formation 
@allowed_users(allowed_roles=['admin'])
@login_required(login_url='login')
def update_formation (request,pk):
    formation = Formation.objects.get(id=pk) 
    form = FormationForm(instance=formation )
    if request.method == 'POST' :
        form = FormationForm(request.POST , request.FILES , instance= formation )
        if form.is_valid():
            form.save()
            return redirect('/home') 
    context ={'f':form}
    return render(request , 'main/FormationForm.html' , context)

#supprision de formation 
@allowed_users(allowed_roles=['admin'])
@login_required(login_url='login')
def delete_formation (request,pk) :
    formation = Formation.objects.get(id=pk) 
    if request.method == 'POST' :
        formation.delete() 
        return redirect('/home')
    context ={'f':formation}
    return render(request , 'main/delete_formation.html' , context)

#detail de formation 
@allowed_users(allowed_roles=['admin'])
@login_required(login_url='login')
def details_formation(request,pk):
    formation = Formation.objects.get(id=pk) 
    context = {'f':formation}
    return render (request, 'main/details_formation.html' , context )

#creation de category 
@allowed_users(allowed_roles=['admin'])
@login_required(login_url='login')
def create_category(request):
    form = CategoryForm() 
    if request.method == 'POST':
        form = CategoryForm(request.POST) 
        if form.is_valid():
            form.save() 
            return redirect('/home') 
    context ={'f':form} 
    return render(request, 'main/CategoryForm.html' , context)

#liste par category 
def lister_parcat(request,pk) : 
    cat = Category.objects.get(id = pk)
    formations = Formation.objects.filter(category = cat)
    context = { 'formations' : formations , 'c' : cat}
    return render(request , 'main/listeparcategory.html' ,context)


#recherche de formation par nom 
def search_formation(request):
    if request.method == 'POST' :
        search = request.POST['search'] 
        formations = Formation.objects.filter(name__contains  = search)
        context = {'formations': formations,'search' :search}
        return render(request, 'main/recherchecat.html',context )
    else:
        return render(request, 'main/recherchecat.html' )


#detail de formation pour les visiteur 
def detail_formation(request,pk):
    formation = Formation.objects.get(id=pk) 
    context = {'f':formation}
    return render (request, 'main/det_formation.html' , context )

