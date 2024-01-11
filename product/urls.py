from django.urls import path
from .views import (
    ListProductView,
    ProductDetaileView,
    DeleteProductView,
    UpdeteProductView,
    CreateProduct
)

urlpatterns = [
    path('', ListProductView.as_view(), name='home'),
    path(
        'product-detail/<int:pk>/',
        ProductDetaileView.as_view(),
        name='product_detail'
    ),
    path(
        'product-delete/<int:pk>/',
        DeleteProductView.as_view(),
        name='delete_product'
    ),
    path(
        'product-update/<int:pk>',
        UpdeteProductView.as_view(),
        name='updete_product'
    ),
    path(
        'product-create/',
        CreateProduct.as_view(),
        name='create_product'
    )
]
