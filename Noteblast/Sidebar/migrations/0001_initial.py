# Generated by Django 5.1.7 on 2025-03-27 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SideBar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AllNotes', models.CharField(max_length=200)),
                ('NewNotes', models.CharField(max_length=100)),
                ('Trash', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Trash',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NewNotes', models.CharField(max_length=100)),
            ],
        ),
    ]
