# Generated by Django 3.0.6 on 2020-07-06 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='about_the_author',
            field=models.TextField(max_length=250),
        ),
    ]