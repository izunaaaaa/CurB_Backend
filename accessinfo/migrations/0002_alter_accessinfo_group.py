from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
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
