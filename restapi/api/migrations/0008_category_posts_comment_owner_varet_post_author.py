# Generated by Django 4.1.3 on 2022-11-13 17:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0007_remove_category_posts'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='posts',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='categorie', to='api.post'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Varet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.IntegerField()),
                ('content', models.CharField(max_length=255)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='got', to=settings.AUTH_USER_MODEL)),
                ('posts', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='api.post')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ManyToManyField(related_name='comm', through='api.Varet', to=settings.AUTH_USER_MODEL),
        ),
    ]