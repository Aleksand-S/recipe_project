# Generated by Django 2.2.8 on 2020-01-28 10:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_recipe', '0004_auto_20200128_0855'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecipeIngredientQuantityUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(null=True)),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_recipe.Ingredient')),
            ],
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='units',
        ),
        migrations.AlterField(
            model_name='recipe',
            name='categories',
            field=models.ManyToManyField(to='app_recipe.Category'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='cuisines',
            field=models.ManyToManyField(to='app_recipe.Cuisine'),
        ),
        # migrations.AlterField(
        #     model_name='recipe',
        #     name='ingredients',
        #     field=models.ManyToManyField(through='app_recipe.RecipeIngredientQuantityUnit', to='app_recipe.Ingredient'),
        # ),
        migrations.AddField(
            model_name='recipeingredientquantityunit',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_recipe.Recipe'),
        ),
        migrations.AddField(
            model_name='recipeingredientquantityunit',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_recipe.Unit'),
        ),
    ]
