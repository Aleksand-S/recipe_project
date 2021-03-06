# Generated by Django 2.2.8 on 2020-01-27 22:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_recipe', '0002_recipe'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Cuisine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuisine_name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_name', models.CharField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='recipe',
            name='cooking_time',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='number_of_persons',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='recipe_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='categories',
            field=models.ManyToManyField(to='app_recipe.Category'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='cuisines',
            field=models.ManyToManyField(to='app_recipe.Cuisine'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='units',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_recipe.Unit'),
        ),
    ]
