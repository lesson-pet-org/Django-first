from django.shortcuts import render, redirect

from .forms import ProductForm, ProductImageForm

from django.views.generic import (
    View,
)

from .models import Product


class ListProductView(View):
    def get(self, request):
        products = Product.objects.all()
        context = {
            'list_product': products
        }
        return render(request, 'index.html', context)


class ProductDetaileView(View):
    def get(self, request, *args, **kwargs):
        product = Product.objects.get(id=kwargs.get('pk'))
        context = {
            'product': product,
            'product_name': product.name
        }
        return render(request, 'product_detail.html', context)


class DeleteProductView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'product_delete.html')

    def post(self, request, *args, **kwargs):
        Product.objects.get(id=kwargs.get('pk')).delete()
        return redirect('home')


class UpdeteProductView(View):
    def get(self, request, *args, **kwargs):
        product = Product.objects.get(id=kwargs['pk'])
        image_product_obj = product.prod_img.all()[0]
        product_form = ProductForm(
            initial={
                'name': product.name,
                'description': product.description,
                'price': product.price
            }
        )
        product_form_img = ProductImageForm(
            initial={
                'img': image_product_obj.img
            }
        )
        context = {
            'form': product_form,
            'product': product,
            'image_product_form': product_form_img
        }
        return render(request, 'product_update.html', context)

    def post(self, request, *args, **kwargs):
        product = Product.objects.get(id=kwargs['pk'])
        product_form = ProductForm(request.POST, request.FILES)
        product_form_img = ProductImageForm(request.POST, request.FILES)
        image_product_obj = product.prod_img.all()[0]
        if product_form.is_valid():
            product.name = product_form.cleaned_data['name']
            product.description = product_form.cleaned_data['description']
            product.price = product_form.cleaned_data['price']
            product.save()
            if product_form_img.is_valid():
                image_product_obj.img = product_form_img.cleaned_data['img']
                image_product_obj.save()
                return redirect('home')



class CreateProduct(View):
    def get(self, request):
        product_form = ProductForm()
        product_form_img = ProductImageForm()
        # данные которые передаются в шаблон с помощью словаря
        context = {
            'form': product_form,
            'form_img': product_form_img
        }
        return render(request, 'create_product.html', context)

    def post(self, request, *args, **kwargs):
        product_form = ProductForm(request.POST, request.FILES)
        product_form_img = ProductImageForm(request.POST, request.FILES)
        if product_form.is_valid():
            # save preproduct
            prod_obj = product_form.save(commit=False)
            prod_obj.name = product_form.cleaned_data['name']
            prod_obj.description = product_form.cleaned_data['description']
            prod_obj.price = product_form.cleaned_data['price']
            prod_obj.save()
            if product_form_img.is_valid():
                product_obj_img = product_form_img.save(commit=False)
                product_obj_img.img = product_form_img.cleaned_data['img']
                product_obj_img.product_obj = prod_obj
                product_obj_img.save()
                return redirect('home')