from django.shortcuts import render,Http404,redirect
from articles.models import Article
from django.http import Http404

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


# Create your views here.
