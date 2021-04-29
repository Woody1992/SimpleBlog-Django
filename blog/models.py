from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='categories/')
    icon = models.ImageField(upload_to='categories/icons/')
    developer = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    last_version = models.CharField(max_length=20)
    website = models.URLField(max_length=250)
    description = models.TextField()

    slug = models.SlugField(max_length=200)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:category_list', args=[self.slug])


class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published', main_post=False)

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='posts/')
    # content = models.TextField()
    content = RichTextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    publish = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    slug = models.SlugField(max_length=200, unique=True)
    tags = models.ManyToManyField(Tag, related_name="post", blank=True, null=True)
    status = models.CharField(max_length=10, choices=options, default='draft')
    main_post = models.BooleanField(default=False)
    category = models.ForeignKey(
        Category,
        related_name="post",
        on_delete=models.SET_NULL,
        null=True
    )
    objects = models.Manager()  # default manager
    newmanager = NewManager()  # custom manager

    def get_absolute_url(self):
        return reverse('blog:post_single', args=[self.slug])

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title


