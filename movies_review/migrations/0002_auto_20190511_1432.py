# Generated by Django 2.0.13 on 2019-05-11 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies_review', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Moviess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('popularity', models.CharField(blank=True, max_length=30)),
                ('director', models.CharField(blank=True, max_length=30)),
                ('imdb_score', models.DecimalField(decimal_places=2, max_digits=10)),
                ('name', models.CharField(max_length=30)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='MoviesList',
        ),
    ]
