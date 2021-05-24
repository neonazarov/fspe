from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from books.models import BookModel


def index(request):
    q = request.GET.get('q')

    if q:
        data = BookModel.objects.filter(Q(title__icontains=q) | Q(author__name__icontains=q)).order_by('-pk')
    else:
        data = BookModel.objects.all()

    context = {
        'data': data
    }
    return render(request, 'index.html', context)


def detail(request, pk=5):
    # try:
    #     book = BookModel.objects.get(pk=pk)
    # except BookModel.DoesNotExist:
    #     raise Http404

    book = get_object_or_404(BookModel, pk=pk)

    context = {
        'book': book
    }
    return render(request, 'detail.html', context)
