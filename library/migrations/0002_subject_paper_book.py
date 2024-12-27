# Generated by Django 5.1.4 on 2024-12-25 14:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=144)),
                ('created', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=144)),
                ('created', models.DateField(auto_now_add=True)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.subject', verbose_name='subject')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=144)),
                ('booknumber', models.CharField(max_length=50)),
                ('publisher', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
                ('description', models.TextField()),
                ('created', models.DateField(auto_now_add=True)),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.bookcategory', verbose_name='category')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.subject', verbose_name='subject')),
            ],
        ),
    ]
