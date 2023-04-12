# Generated by Django 4.2 on 2023-04-12 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0005_initial_categroy'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='category',
            constraint=models.UniqueConstraint(fields=('name', 'group'), name='unique_category_name_group'),
        ),
    ]