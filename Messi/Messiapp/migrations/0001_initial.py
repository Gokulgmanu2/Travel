# Generated by Django 5.0.3 on 2024-03-28 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=250)),
                ('img', models.ImageField(upload_to='Pics')),
                ('desc', models.TextField()),
            ],
        ),
    ]
