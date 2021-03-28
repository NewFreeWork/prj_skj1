# Generated by Django 3.1.6 on 2021-03-07 12:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('prj1_app', '0006_auto_20210307_2123'),
    ]

    operations = [
        migrations.CreateModel(
            name='prj1_BlogAuthor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(help_text='Enter your bio details here.', max_length=400)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['user', 'bio'],
            },
        ),
        migrations.CreateModel(
            name='prj1_Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(help_text='Enter you blog text here.', max_length=2000)),
                ('publish', models.BooleanField(default=True)),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='prj1_app.prj1_blogauthor')),
            ],
            options={
                'ordering': ['-post_date'],
            },
        ),
    ]