from django.db import models


class GenreModel(models.Model):
    title = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'genre'
        verbose_name_plural = 'genres'


class AuthorModel(models.Model):
    name = models.CharField(max_length=60)
    birth_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'author'
        verbose_name_plural = 'authors'


class BookModel(models.Model):
    title = models.CharField(max_length=128)
    author = models.ForeignKey(AuthorModel, on_delete=models.PROTECT, related_name='books')
    genres = models.ManyToManyField(GenreModel, related_name='books')
    cover = models.ImageField(null=True, blank=True)
    isbn = models.CharField(max_length=13, unique=True, verbose_name='ISBN')
    page_count = models.IntegerField(null=True, blank=True)
    summary = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'book'
        verbose_name_plural = 'books'
