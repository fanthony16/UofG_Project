# Generated by Django 4.2.4 on 2023-08-31 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("predict", "0005_alter_predict_gender"),
    ]

    operations = [
        migrations.AlterField(
            model_name="predict",
            name="gender",
            field=models.CharField(
                choices=[("Male", "MALE"), ("Male", "FEMALE")], max_length=20
            ),
        ),
    ]
