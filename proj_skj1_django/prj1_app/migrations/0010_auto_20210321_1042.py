# Generated by Django 3.1.6 on 2021-03-21 01:42

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('prj1_app', '0009_file_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='prj1_blog',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='prj1_blog',
            name='description',
            field=models.TextField(help_text='Enter you blog text here.', max_length=60000),
        ),
    ]
