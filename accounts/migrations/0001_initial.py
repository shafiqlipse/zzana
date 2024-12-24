# Generated by Django 5.1.4 on 2024-12-16 04:37

import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_school', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_tech', models.BooleanField(default=False)),
                ('is_accounts', models.BooleanField(default=False)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='profile_images/')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155)),
                ('c_type', models.CharField(choices=[('Academic', 'Academic'), ('Student Behavior ', 'Student Behavior '), ('School Policies', 'School Policies'), (' Safety Concerns', ' Safety Concerns'), ('Special Educational Needs', 'Special Educational Needs'), ('Staff Conduct', 'Staff Conduct'), ('Administrative', 'Administrative'), ('Other', 'Other')], max_length=40)),
                ('complainer', models.CharField(max_length=155)),
                ('person', models.CharField(choices=[('Parent', 'Parent'), ('Student ', 'Student'), ('staff member', 'staff member'), (' Teacher', ' Teacher'), ('  community member', '  community member'), ('  Other', '  Other')], max_length=40)),
                ('date_recorded', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField()),
                ('recorder', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('expires_at', models.DateTimeField(blank=True, null=True)),
                ('attachment', models.FileField(blank=True, null=True, upload_to='noticeboard/attachments/')),
                ('status', models.CharField(choices=[('Draft', 'Draft'), ('Published', 'Published')], default='Draft', max_length=10)),
                ('priority', models.CharField(choices=[('Low', 'Low'), ('Normal', 'Normal'), ('High', 'High'), ('Urgent', 'Urgent')], default='Normal', max_length=10)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullnames', models.CharField(max_length=155)),
                ('date_recorded', models.DateTimeField(auto_now_add=True)),
                ('date_visited', models.DateField()),
                ('time_in', models.TimeField()),
                ('time_out', models.TimeField()),
                ('id_type', models.CharField(choices=[('National ID', 'National ID'), ('Driving Permit', 'Driving Permit'), ('Passport', 'Passport'), ('School ID', 'School ID'), ('Company ID', 'Company ID'), ('Other', 'Other')], default='National ID', max_length=155)),
                ('id_number', models.CharField(max_length=155, unique=True)),
                ('purpose', models.CharField(max_length=155)),
                ('contact', models.CharField(max_length=155, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('office', models.CharField(max_length=155)),
                ('description', models.TextField()),
                ('parcel', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=10)),
                ('recorder', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='NoticeReadStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_read', models.BooleanField(default=False)),
                ('read_at', models.DateTimeField(blank=True, null=True)),
                ('notice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.notice')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'notice')},
            },
        ),
    ]
