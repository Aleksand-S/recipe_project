# Generated by Django 2.2.8 on 2020-01-28 20:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_recipe', '0009_auto_20200128_1346'),
    ]

    operations = [
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('step_image', models.ImageField(blank=True, upload_to='images/')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_recipe.Recipe')),
            ],
        ),
    ]
