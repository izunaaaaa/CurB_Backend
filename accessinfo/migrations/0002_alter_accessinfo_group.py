<<<<<<< HEAD
# Generated by Django 4.2 on 2023-04-20 11:49
=======
# Generated by Django 4.2 on 2023-04-20 06:00
>>>>>>> d35700b8eb456479cfd5a367b0334039a338c6e3

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
<<<<<<< HEAD

=======
>>>>>>> d35700b8eb456479cfd5a367b0334039a338c6e3
    dependencies = [
        ("groups", "0004_alter_group_name"),
        ("accessinfo", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="accessinfo",
            name="group",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="accessinfo",
                to="groups.group",
            ),
        ),
    ]
