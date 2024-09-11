from django.shortcuts import render, redirect
from .models import Recipe
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# @login_required(login_url='/Login/')

@login_required(login_url="/Login/")
def recipe(request):
    # yaha pe tune khali post method allow kiya hai to usko test karne ke liye postman download karna padega becuase in browser support only get method
    if request.method == "POST":
        recipe_obj = Recipe()
        data = request.POST
        recipe_image = request.FILES.get('recipe_image')  # Use request.FILES to handle file uploads
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')

        recipe_obj.recipe_image = recipe_image
        recipe_obj.recipe_name = recipe_name
        recipe_obj.recipe_description = recipe_description

        recipe_obj.save()

        return redirect('/')  # iska use karne se ham dubara recipe add kar sakte h bina refesh kiye


    queryset = Recipe.objects.all()

    if request.GET.get('search'):
        queryset = queryset.filter(recipe_name__icontains=request.GET.get('search'))

    context = {'recipes': queryset}
    return render(request, "index.html", context)
@login_required(login_url="/Login/")
def update_recipe(request,id):
    queryset = Recipe.objects.get(id=id)
    if request.method =="POST":
        data = request.POST

        recipe_image = request.FILES.get('recipe_image')  # Use request.FILES to handle file uploads
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')

        queryset.recipe_name = recipe_name
        queryset.recipe_description = recipe_description

        if recipe_image:
            queryset.recipe_image = recipe_image

        queryset.save()
        return redirect('/')

    context = {'recipe': queryset}

    return render(request, "update_recipe.html", context)

@login_required(login_url="/Login/")
def delete_recipe(request,id):
    queryset = Recipe.objects.get(id=id)
    queryset.delete()
    return redirect('/')

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.info(request, "Invalid Username.")
            return redirect('/Login/')

        user = authenticate(username=username, password=password)

        if user is None:
            messages.info(request, "Invalid Password.")
            return redirect('/Login/')
        else:
            login(request, user)
            return redirect('/')


    return render(request, 'Login.html')


def logout_page(request):
    logout(request)
    return redirect('/Login/')

def resister_page(request):

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            messages.info(request, "Username already taken.")
            return redirect('/register/')

        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username
        )

        # Set password after user creation
        user.set_password(password)
        user.save()

        messages.info(request, "Account created successfully.")
        return redirect('/register/')



    return render(request, 'register.html')

