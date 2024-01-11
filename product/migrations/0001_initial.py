# Generated by Django 4.2.5 on 2023-12-10 07:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название продукта')),
                ('description', models.TextField(verbose_name='Описание продукта')),
                ('price', models.IntegerField(verbose_name='Цена продукта')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, upload_to='images/')),
                ('product_obj', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prod_img', to='product.product')),
            ],
        ),
    ]