# Generated by Django 3.1.6 on 2021-03-07 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prj1_app', '0005_prj1_blog_prj1_blogauthor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prj1_blogauthor',
            name='user',
        ),
        migrations.DeleteModel(
            name='prj1_Blog',
        ),
        migrations.DeleteModel(
            name='prj1_BlogAuthor',
        ),
    ]
