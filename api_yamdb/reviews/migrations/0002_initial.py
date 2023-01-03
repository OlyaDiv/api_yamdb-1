# Generated by Django 3.2 on 2022-12-28 10:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор отзыва'),
        ),
        migrations.AddField(
            model_name='reviews',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.titles', verbose_name='Произведение'),
        ),
        migrations.AddField(
            model_name='comments',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор комментария'),
        ),
        migrations.AddField(
            model_name='comments',
            name='review',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.reviews', verbose_name='Отзыв'),
        ),
    ]
