# Generated by Django 4.2 on 2023-04-19 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("comments", "0007_alter_comment_user_recomment"),
        ("likes", "0005_commentlike_recomment_alter_commentlike_comment_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="commentlike",
            name="comment",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="commentlike",
                to="comments.comment",
            ),
        ),
        migrations.AlterField(
            model_name="commentlike",
            name="recomment",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="recommentlike",
                to="comments.recomment",
            ),
        ),
    ]
