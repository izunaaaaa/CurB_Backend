# Generated by Django 4.2 on 2023-04-09 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('letterlists', '0003_remove_letterlist_message_remove_letterlist_user_and_more'),
        ('letters', '0003_remove_letter_user_letter_receiver_letter_sender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='letter',
            name='receiver',
        ),
        migrations.RemoveField(
            model_name='letter',
            name='sender',
        ),
        migrations.AddField(
            model_name='letter',
            name='list',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='letter', to='letterlists.letterlist'),
        ),
    ]
