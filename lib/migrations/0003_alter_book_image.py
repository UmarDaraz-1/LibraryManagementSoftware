# Generated by Django 4.1.1 on 2023-01-28 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lib', '0002_alter_book_author_alter_categories_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(upload_to='media'),
        ),
    ]
