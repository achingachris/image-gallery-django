from django.shortcuts import render, redirect
from .models import Category, Photo

# home page
def home_page(request):
    category = request.GET.get('category')
    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name=category)

    categories = Category.objects.all()
    context = {'categories': categories, 'photos': photos}
    return render(request, 'index.html', context)

def view_image(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'photo.html', {'photo': photo})

def add_image(request):
    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data ['category_new'] != '':
            category, created = Category.objects.get_or_create(name=data['category_new'])
        else:
            category = None

        photo = Photo.objects.create(
            category = category,
            description = data['description'],
            image=image,
        )

        return redirect('gallery')

        # test for submission on terminal
        # print('data:', data )
        # print('image:', image )
    categories = Category.objects.all()
    context = {'categories':categories,}
    return render(request, 'add.html', context)
