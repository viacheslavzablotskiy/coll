# Generated by Django 4.1.3 on 2022-11-12 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_category_post_alter_comment_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='owner',
        ),
    ]