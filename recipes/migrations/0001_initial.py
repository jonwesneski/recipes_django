# Generated by Django 2.0.6 on 2018-06-20 01:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmarks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('url', models.CharField(max_length=255)),
                ('created', models.DateTimeField()),
                ('modified', models.DateTimeField()),
            ],
            options={
                'db_table': 'bookmarks',
            },
        ),
        migrations.CreateModel(
            name='Recipes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('ingredients', models.TextField()),
                ('instructions', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('created', models.DateTimeField(blank=True, null=True)),
                ('modified', models.DateTimeField()),
            ],
            options={
                'db_table': 'recipes',
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('created', models.DateTimeField(blank=True, null=True)),
                ('modified', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'tags',
            },
        ),
        migrations.CreateModel(
            name='RecipesTags',
            fields=[
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='recipes.Recipes')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, to='recipes.Tags')),
            ],
            options={
                'db_table': 'recipes_tags',
            },
        ),
        migrations.AlterUniqueTogether(
            name='recipestags',
            unique_together={('recipe', 'tag')},
        ),
    ]
