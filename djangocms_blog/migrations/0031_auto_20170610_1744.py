# Generated by Django 1.10.5 on 2017-06-10 12:14

import sortedm2m.fields
from django.db import migrations
from sortedm2m.operations import AlterSortedManyToManyField


class Migration(migrations.Migration):

    dependencies = [
        ("djangocms_blog", "0030_auto_20170509_1831"),
    ]

    operations = [
        AlterSortedManyToManyField(
            model_name="post",
            name="related",
            field=sortedm2m.fields.SortedManyToManyField(
                blank=True, help_text=None, to="djangocms_blog.Post", verbose_name="Related Posts"
            ),
        ),
    ]