# Generated by Django 4.2 on 2023-04-20 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BestMovies_api', '0003_movie_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='preview',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]
