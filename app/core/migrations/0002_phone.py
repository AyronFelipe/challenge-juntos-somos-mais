# Generated by Django 3.2 on 2021-04-25 15:08

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('type', models.IntegerField(choices=[(1, 'cell'), (2, 'land')], verbose_name='Type')),
                ('number', models.CharField(max_length=14, verbose_name='Phone number')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='phones', to='accounts.user')),
            ],
            options={
                'verbose_name': 'Phone',
                'verbose_name_plural': 'Phones',
            },
        ),
    ]
