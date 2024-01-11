from django.db import models


class Product(models.Model):
    name = models.CharField(
        verbose_name="Название продукта",
        max_length=255,
    )
    description = models.TextField(
        verbose_name="Описание продукта"
    )
    price = models.IntegerField(
        verbose_name="Цена продукта"
    )

    def __str__(self):
        # строковое представление объекта
        return str(self.id)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ['name']


class ProductImage(models.Model):
    product_obj = models.ForeignKey(
        Product, related_name="prod_img",
        on_delete=models.CASCADE,
        null=True
    )
    img = models.ImageField(
        upload_to='images/',
        blank=True
    )

    def __str__(self):
        return str(self.img)
