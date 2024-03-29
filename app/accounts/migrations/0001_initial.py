# Generated by Django 3.2 on 2021-04-25 14:17

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('type', models.IntegerField(choices=[(1, 'special'), (2, 'normal'), (3, 'laborious')], verbose_name='Type')),
                ('gender', models.CharField(max_length=1, verbose_name='Gender')),
                ('birthday', models.DateTimeField(verbose_name='Birthday')),
                ('nationality', models.CharField(max_length=2, verbose_name='Nationality')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('registered', models.DateTimeField(verbose_name='Birthday')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('title', models.CharField(max_length=10, verbose_name='Title')),
                ('first', models.CharField(max_length=50, verbose_name='First Name')),
                ('last', models.CharField(max_length=50, verbose_name='Last Name')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='name_user', to='accounts.user')),
            ],
            options={
                'verbose_name': 'Name',
                'verbose_name_plural': 'Names',
            },
        ),
    ]
