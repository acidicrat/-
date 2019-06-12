from django.shortcuts import render,Http404,redirect
from articles.models import Article, login_form, register_form
from django.http import Http404,HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login


def archive(request):
    return render(request, 'archive.html', {"posts": Article.objects.all()})

def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist:
        raise Http404

def create_post(request):
    if not request.user.is_anonymous:
        #Здесь будет основной код
        if request.method == "POST":
            #обработать данные формы,если метод POST
            form = {
                'text': request.POST["text"],
                'title': request.POST["title"]
                }
            #в словаре form будет храниться информация,введенная пользователем
            if form["text"] and form["title"]:
                #если поля заполнены без ошибок
                if len(Article.objects.filter(title=form['title'])) > 0:
                    form['errors']= u" Ошибка уникальности статьи "
                    return render(request, 'create_post.html', {'form': form})
                else:
                    Article.objects.create(text=form["text"], title=form["title"], author=request.user)
                    article = Article.objects.get(title=form['title'])
                    return redirect('get_article', article.id)
            #перейти на страницу поста
            else:
                #если введенные данные некорректны
                form['errors']= u" НЕ ВСЕ ПОЛЯ ЗАПОЛНЕНЫ! "
                return render(request, 'create_post.html', {'form': form})
        else:
            #просто вернуть странцу с формой,если метод GET
            return render(request, 'create_post.html', {})
    else:
        raise Http404


def register_fun(request):
    error = []
    if request.method == "POST":
        form=register_form(request.POST)
        if form.is_valid():
            user = form.save()
            conpassword = form.cleaned_data.get('password')
            user = authenticate(username=user.username,
                                email=user.email,
                                password=conpassword)
            login(request, user)
            return redirect('register_fun')
        else:
            error.append("Ошбика регистрации")
    else:
        form=register_form()
    return render(request, 'register_form.html',{'form': form, 'error': error})


def login_fun(request):
    error = []
    if request.method == "POST":
        form = login_form(request.POST)
        if form.is_valid():
            if form.get_user():
                login(request, form.get_user())
                return HttpResponseRedirect('')
        else:
            #return HttpResponse('Не правильный логин или пароль')
            error.append("Ошбика логина или пароля")
    else:
        form = login_form()
    return render(request, 'autho_form.html',{'form': form, 'error': error})
            
    
    


# Create your views here.
