# Generated by Django 4.2 on 2023-04-20 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BestMovies_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField()),
                ('description', models.TextField()),
                ('release_date', models.DateTimeField()),
            ],
        ),
        migrations.DeleteModel(
            name='BestMovies',
        ),
    ]