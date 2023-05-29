from django.shortcuts import render, get_object_or_404
from .models import (Categories, Subcategories,
                     Product, ProductImage,
                     Size, Fabric,
                     Cart, CartItem, ProductForMainPage)


def index(request):
    categories = Categories.objects.all()
    products = Product.objects.all()
    products_six = ProductForMainPage.objects.all()
    return render(request, 'main/index.html', {'products': products, 'products_six': products_six, 'categories': categories })


# def catalog(request):
#     # if request.method == "GET":
#     #     request_category = request.GET.get("category")
#     #     request_subcategory = request.GET.get("subcategory")
#     #     if request.GET.get("category"):
#     #         if request_category == "Стільці":
#     #             products = Product.objects.filter(category=2)
#     #         elif request_category == "Столи":
#     #             products = Product.objects.filter(category=3)
#     #         elif request_category == "Лампи":
#     #             products = Product.objects.filter(category=4)
#     #         elif request_category == "Ліжка":
#     #             products = Product.objects.filter(category=5)
#     #         elif request_category == "Дивани":
#     #             products = Product.objects.filter(category=6)
#     #         else:
#     #             products = Product.objects.all()
#     #
#     #     if request.GET.get("subcategory"):
#     #         if request_subcategory == "Домашні":
#     #             products = Product.objects.filter(subcategory=2)
#     #         if request_subcategory == "Офісні":
#     #             products = Product.objects.filter(subcategory=3)
#     #         if request_subcategory == "Всі товари":
#     #             products = Product.objects.all()
#     categories = Categories.objects.all()
#     products = Product.objects.filter(category=request.GET.get("category"))
#     print(request.GET.get("category"))
#     subcategories = Subcategories.objects.all()
#     return render(request, 'main/catalog.html', {'products': products, 'categories': categories, 'subcategories': subcategories})


def category(request, category_id):
    categories = Categories.objects.all()
    products = Product.objects.filter(category__product__id=category_id)
    print(request.GET.get("category"))
    subcategories = Subcategories.objects.all()
    return render(request, 'main/catalog.html', {'products': products, 'categories': categories, 'subcategories': subcategories})


def product(request, product_real_id):
    categories = Categories.objects.all()
    main_product = Product.objects.get(id=product_real_id)
    main_product_images = ProductImage.objects.filter(product__id=product_real_id)
    print(main_product_images)
    products = Product.objects.all()
    print(products)
    return render(request, 'main/product.html', {'head_product': main_product, 'categories': categories, 'products': products, 'head_product_images': main_product_images})


def cart(request):
    products = Product.objects.all()
    categories = Categories.objects.all()
    return render(request, 'main/cart.html', {'categories': categories, 'products': products})

def catalog(request):
    products = Product.objects.all()
    if request.method == "GET":
        request_category = request.GET.get("category")
        request_subcategory = request.GET.get("subcategory")
        print('request_subcategory  ', request_subcategory)
        print(request.GET)
        if request_category != '1':
            if request.GET.get("category"):
                products = Product.objects.filter(category=request_category)
        if request_subcategory != '1':
            if request.GET.get("subcategory"):
                products = Product.objects.filter(subcategory=request_subcategory)
    categories = Categories.objects.all()
    subcategories = Subcategories.objects.all()
    return render(request, 'main/catalog.html',
                  {'products': products, 'categories': categories, 'subcategories': subcategories})

    #
    # if request.method == "GET":
    #     request_category = request.GET.get("category")
    #     request_subcategory = request.GET.get("subcategory")
    #     if request.GET.get("category"):
    #         if request_category == "2":
    #             products = Product.objects.filter(category=2)
    #         elif request_category == "3":
    #             products = Product.objects.filter(category=3)
    #         elif request_category == "4":
    #             products = Product.objects.filter(category=4)
    #         elif request_category == "5":
    #             products = Product.objects.filter(category=5)
    #         elif request_category == "6":
    #             products = Product.objects.filter(category=6)
    #         else:
    #             products = Product.objects.all()
    #
    #     if request.GET.get("subcategory"):
    #         if request_subcategory == "2":
    #             products = Product.objects.filter(subcategory=2)
    #         if request_subcategory == "3":
    #             products = Product.objects.filter(subcategory=3)
    #         if request_subcategory == "1":
    #             products = Product.objects.all()