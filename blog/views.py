from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from django.http import JsonResponse

from .models import Post, Category


def home(request):
    all_posts = Post.newmanager.all()
    main = Post.objects.filter(status='published', main_post=True).order_by('-created_at')[0:1]

    return render(request, 'base.html', {'posts': all_posts, 'main': main})


def post_single(request, post):
    post = get_object_or_404(Post, slug=post, status='published')

    return render(request, 'blog/single.html', {'post': post})


def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    post = Post.newmanager.filter(category=category)

    return render(request, 'blog/category.html', {'category': category, 'posts': post})


def search_results(request):
    if request.is_ajax():
        res = None
        post = request.POST.get('post')
        qs = Post.objects.filter(status='published', title__icontains=post)
        if len(qs) > 0 and len(post) > 0:
            data = []
            for pos in qs:
                item = {
                    'slug': pos.slug,
                    'title': pos.title,
                    'category': pos.category.name,
                    'created_at': pos.created_at,
                    'image': str(pos.image.url),
                    'category_slug': 'news/' + pos.category.slug,
                }
                data.append(item)
            res = data
        else:
            res = 'No results found...'
        return JsonResponse({'data': res})

    return JsonResponse({})


def posts_all(request):
    all_posts = Post.newmanager.all()

    return render(request, 'blog/news.html', {'posts': all_posts})
