# Generated by Django 1.10.5 on 2017-07-22 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("djangocms_blog", "0029_post_related"),
    ]

    operations = [
        migrations.AlterField(
            model_name="posttranslation",
            name="slug",
            field=models.SlugField(
                allow_unicode=True, blank=True, db_index=False, max_length=255, verbose_name="slug"
            ),
        ),
    ]