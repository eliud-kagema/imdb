# Generated by Django 2.2.5 on 2019-09-14 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=140)),
                ('description', models.TextField(max_length=10000)),
                ('image', models.ImageField(upload_to='movies')),
                ('category', models.CharField(choices=[('A', 'ACTION'), ('D', 'DRAMA'), ('C', 'COMEDY'), ('R', 'ROMANCE')], max_length=1)),
                ('language', models.CharField(choices=[('EN', 'ENGLISH'), ('GR', 'GERMAN')], max_length=2)),
                ('status', models.CharField(choices=[('RA', 'RECENTLY ADDED'), ('MW', 'MOST WATCHED'), ('TR', 'TOP RATED')], max_length=2)),
                ('cast', models.CharField(max_length=100)),
                ('rating', models.CharField(choices=[('NR', 'Not Rated'), ('G', 'General Audiences'), ('PG', 'Parental Audiences'), ('R', 'Restricted')], max_length=2)),
                ('year_of_prodcution', models.DateField()),
                ('views_count', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ('-year_of_prodcution', 'title'),
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=140)),
                ('lname', models.CharField(max_length=140)),
            ],
            options={
                'ordering': ('fname', 'lname'),
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='movie.Movie')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='movie.Person')),
            ],
            options={
                'unique_together': {('movie', 'person', 'name')},
            },
        ),
        migrations.CreateModel(
            name='MovieLinks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('D', 'Download'), ('W', 'Watch')], max_length=1)),
                ('link', models.URLField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_watch_link', to='movie.Movie')),
            ],
            options={
                'verbose_name': 'Movie Links',
                'verbose_name_plural': 'Movie Links',
            },
        ),
        migrations.AddField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(blank=True, null=True, related_name='acting_credits', through='movie.Role', to='movie.Person'),
        ),
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='directed', to='movie.Person'),
        ),
        migrations.AddField(
            model_name='movie',
            name='writers',
            field=models.ManyToManyField(blank=True, null=True, related_name='writing_credits', to='movie.Person'),
        ),
    ]
