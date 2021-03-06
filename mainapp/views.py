from django.shortcuts import render
from django.http import HttpResponse, request
from .models import Carousel, Mobiles

# Create your views here.
def index(request):

    c_img = Carousel.objects.all()

    mproduct = Mobiles.objects.all().filter(brand="Xiaomi")

    best_under = Mobiles.objects.all().filter(price__lte= 10000)

    under_20 = Mobiles.objects.all().filter(price__range= (10000, 20000))

    return render(request, 'index.html', {'item': c_img, 'mproduct': mproduct, 'range': range(6), 'best_under':best_under, 'under_20': under_20})

def explore_all(request):

    context = {}
    
    all_m = Mobiles.objects.all()

    f_sort = request.POST.get('sort', None)
    f_price = request.POST.get('price', None)
    f_brands = request.POST.get('brands', None)
    f_rating = request.POST.get('rating', None)
    f_search = request.POST.get('search', None)

    b_search = False
    if f_search != None:
        b_search = True

    if f_sort == 'ascending':
        sort_order = Mobiles.objects.all().order_by('mbl_name')
        return render(request, 'explore_all.html', {'all_m':sort_order, })
    elif f_sort == 'descending':
        sort_order = Mobiles.objects.all().order_by('-mbl_name')
        return render(request, 'explore_all.html', {'all_m':sort_order, })
    elif f_price == 'zero-ten':
        sort_order = Mobiles.objects.all().filter(price__lte = 10000)
        return render(request, 'explore_all.html', {'all_m':sort_order, })
    elif f_price == 'ten-twenty':
        sort_order = Mobiles.objects.all().filter(price__range = (10000, 20000))
        return render(request, 'explore_all.html', {'all_m':sort_order, })
    elif f_price == 'twenty-plus':
        sort_order = Mobiles.objects.all().filter(price__gte = 20000)
        return render(request, 'explore_all.html', {'all_m':sort_order, })
    elif f_brands == 'xiaomi':
        sort_order = Mobiles.objects.all().filter(brand = "Xiaomi")
        return render(request, 'explore_all.html', {'all_m':sort_order, })
    elif f_brands == 'apple':
        sort_order = Mobiles.objects.all().filter(brand = "Apple")
        return render(request, 'explore_all.html', {'all_m':sort_order, })
    elif f_brands == 'oneplus':
        sort_order = Mobiles.objects.all().filter(brand = "Oneplus")
        return render(request, 'explore_all.html', {'all_m':sort_order, })
    elif f_brands == 'samsung':
        sort_order = Mobiles.objects.all().filter(brand = "Samsung")
        return render(request, 'explore_all.html', {'all_m':sort_order, })
    elif f_brands == 'realme':
        sort_order = Mobiles.objects.all().filter(brand = "Realme")
        return render(request, 'explore_all.html', {'all_m':sort_order, })
    elif f_rating == 'four':
        sort_order = Mobiles.objects.all().filter(rating__gte = 4.0)
        return render(request, 'explore_all.html', {'all_m':sort_order, })
    elif f_rating == 't-f':
        sort_order = Mobiles.objects.all().filter(rating__range = (3.0, 4.0))
        return render(request, 'explore_all.html', {'all_m':sort_order, })
    elif f_rating == 't-t':
        sort_order = Mobiles.objects.all().filter(rating__range = (2.0, 3.0) )
        return render(request, 'explore_all.html', {'all_m':sort_order, })
    elif f_rating == 'two':
        sort_order = Mobiles.objects.all().filter(rating__lte = 2.0)
        return render(request, 'explore_all.html', {'all_m':sort_order, })
    elif b_search == True:
        sort_order = Mobiles.objects.all().filter(mbl_name__contains = f_search)
        return render(request, 'explore_all.html', {'all_m':sort_order, })
    


    return render(request, 'explore_all.html', {'all_m':all_m, })
    


def product(request, id):
    
    item = Mobiles.objects.all().filter(id = id)
    return render(request, 'product.html', {'item': item})
def cart(request):
    item = Mobiles.objects.all().filter(cart = True)
    return render(request, 'cart.html',{'item':item})

def orders(request):
    item = Mobiles.objects.all().filter(order = True)
    return render(request, 'orders.html',{'item':item})