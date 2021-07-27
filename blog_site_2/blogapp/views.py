from django.shortcuts import render,HttpResponse,get_object_or_404,redirect
from .models import Article,Author, Comment
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .forms import RegistrationForm,PostCreationForm,AuthorForm,CommentForm

# Create your views here.
def index(request):
    post = Article.objects.all()
    article_author = get_object_or_404(Author, name=request.user.id)
    context = {
        "post": post,
        "author": article_author
    }
    return render(request, "index.html", context)


def Blog(request):
    blog_post = Article.objects.all()
    return render(request, 'blog.html',{"blog_post": blog_post})


def Blog_single(request,pid):
    post = get_object_or_404(Article, pk=pid)
    user_name = get_object_or_404(User, id=request.user.id)
    show_comment = Comment.objects.all()
    form = CommentForm(request.POST or None)
    instance = form.save(commit=False)
    instance.name = user_name
    instance.post = post
    instance.save()
    context = {
        "single": post,
        "form": form,
        "show_comment": show_comment
    }
    return render(request, 'blog-single.html', context)


def Login(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == "POST":
            user = request.POST.get("user")
            password = request.POST.get("password")
            auth = authenticate(request, password=password, username=user)
            if auth is not None:
                login(request, auth)
                return redirect('index')
    return render(request, 'login.html')


def Logout(request):
    logout(request)
    return redirect('blog')


def Register(request):
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect('login')
    return render(request, 'register.html', {"form": form})


def Profile(request):
    if request.user.is_authenticated:
        author = get_object_or_404(User, id=request.user.id)
        author_profile = Author.objects.filter(name=author.id)
        if author_profile:
            author_user = get_object_or_404(author_profile, name=request.user.id)
            author_post = Article.objects.filter(article_author = author_user.id)
        return render(request,'profile.html',{"post": author_post,"user": author_user})
    else:
        return redirect('login')


def Create_Post(request):
    if request.user.is_authenticated:
        user = get_object_or_404(Author, name=request.user.id)
        form = PostCreationForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.article_author=user
            instance.save()
            return redirect('profile')
        return render(request, 'create_post.html', {"form": form})
    else:
        return redirect('login')


def Update_Post(request,uid):
    if request.user.is_authenticated:
        user = get_object_or_404(Author, name=request.user.id)
        post = get_object_or_404(Article, id=uid)
        form = PostCreationForm(request.POST or None, request.FILES or None, instance=post)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.article_author=user
            instance.save()
            return redirect('profile')
        return render(request,'create_post.html',{"form": form})
    else:
        return redirect('login')


def Delete_Post(request,uid):
    if request.user.is_authenticated:
        post = get_object_or_404(Article, id=uid)
        post.delete()
        return redirect('profile')
    else:
        return redirect('login')


def Authors(request):
    if request.user.is_staff:
        auth = Author.objects.all()
        context = {
            "auth": auth
        }
        return render(request, 'author.html', context)
    else:
        return redirect('login')


def Create_Author(request):
    form = AuthorForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect('authors') 
    return render(request, 'Create_Author.html',{"form": form})

def Delete_Author(request,cid):
    if request.user.is_staff:
        author = get_object_or_404(Author, id=cid)
        author.delete()
        return redirect('authors')
    else:
        return redirect('login')


def Update_Author(request,cid):
    if request.user.is_staff:
        auth = get_object_or_404(Author, id=cid)
        form = AuthorForm(request.POST or None, request.FILES or None, instance=auth)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('authors')
        return render(request,'Create_Author.html',{"form": form})
    else:
        return redirect('login')


def Get_User(request):
    if request.user.is_authenticated:
        users = User.objects.all()
        return render(request, 'user.html',{"users": users})
    else:
        return redirect('login')


def Delete_User(request, nid):
    if request.user.is_staff:
        user = get_object_or_404(User, id=nid)
        user.delete()
        return redirect('get_user')
    else:
        return redirect('login')


def Update_User(request, nid):
    if request.user.is_staff:
        auth = get_object_or_404(User, id=nid)
        form = RegistrationForm(request.POST or None, instance=auth)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('get_user')
        return render(request, 'register.html',{"form": form})
    else:
        return redirect('login')