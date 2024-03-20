# Generated by Django 5.0.3 on 2024-03-20 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='название')),
                ('descrition', models.TextField(verbose_name='описпние')),
                ('image', models.ImageField(upload_to='img/post/', verbose_name='фото')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='дата')),
            ],
        ),
    ]
