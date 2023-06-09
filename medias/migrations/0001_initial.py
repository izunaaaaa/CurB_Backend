# Generated by Django 4.2 on 2023-04-05 06:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('feeds', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('url', models.URLField()),
                ('feed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feeds.feed')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
