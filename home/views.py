from django.shortcuts import render, HttpResponse,redirect
from .models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from blog.models import Post


# ===============================================================================================
# Html Pages
# ===============================================================================================
# Create your views here.
def home(request):
    return render(request, "home/home.html")


def about(request):
    return render(request, "home/about.html")
    # return HttpResponse("this is about")


def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        content = request.POST["content"]
        # print(name, email, phone, content)

        if len(name) < 2 or len(email) < 3 or len(phone) < 10 or len(content) < 4:
            messages.error(request, "please fill the form correctly")
        else:
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "your messages has successfully sent")
    return render(request, "home/contact.html")
    # return HttpResponse("this is contact")


def search(request):
    query = request.GET["query"]
    if len(query)>78:
        allPosts=Post.objects.none()
    else:
        # allPosts = Post.objects.all()
        allPostsTitle = Post.objects.filter(title__icontains=query)
        allPostsContent = Post.objects.filter(content__icontains=query)
        allPosts=allPostsTitle.union(allPostsContent)
        
    if allPosts.count()==0:
        messages.warning(request, "No search results found. Please refine your query.")
    params = {"allPosts": allPosts, "query": query}
    return render(request, "home/search.html", params)

    # return HttpResponse("this is search")
    
    
    
# ===============================================================================================
# Authentication Apis    
# ===============================================================================================
# sign up
# ===============================================================================================
    
def handleSignup(request):
    if request.method == "POST":
        username = request.POST["username"]
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        pass1 = request.POST["pass1"]
        pass2 = request.POST["pass2"]
    
        # checks for errorneous input
        if len(username)>10:
            messages.error(request,"Username must be under 10 characters")
            return redirect("home")
        if not username.isalnum():
            messages.error(request,"Username should only contain letters and numbers")
            return redirect("home")
        
        if pass1 != pass2:
            messages.error(request,"Password do not matched")
            return redirect("home")
        
        # create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()

        messages.success(request, "Your account has been created successfully")
        return redirect("home")

    else:
        return HttpResponse("404 - Not Found")


# ====================================================================================================================================
# log in    
# ====================================================================================================================================
    
def handleLogIn(request):
    if request.method == "POST":
        loginusername = request.POST["loginusername"]
        loginpassword = request.POST["loginpassword"]

        user = authenticate(username=loginusername, password=loginpassword)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("home")     

        else:
            messages.error(request, "Invalid Credentials, please try again")
            return redirect("home")

    return HttpResponse("404 - Not Found")


# ====================================================================================================================================
# log out
# ====================================================================================================================================

def handleLogOut(request):
    logout(request)
    messages.error(request, "Successfully Logged Out")
    return redirect("home")
 
    return HttpResponse("handleLogOut")