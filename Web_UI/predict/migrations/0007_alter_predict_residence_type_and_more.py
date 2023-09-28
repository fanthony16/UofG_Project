# Generated by Django 4.2.4 on 2023-08-31 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("predict", "0006_alter_predict_gender"),
    ]

    operations = [
        migrations.AlterField(
            model_name="predict",
            name="Residence_type",
            field=models.CharField(
                choices=[("Rural", "Rural"), ("Urban", "Urban")], max_length=15
            ),
        ),
        migrations.AlterField(
            model_name="predict",
            name="ever_married",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No")], max_length=3
            ),
        ),
        migrations.AlterField(
            model_name="predict",
            name="gender",
            field=models.CharField(
                choices=[("male", "MALE"), ("female", "FEMALE")], max_length=20
            ),
        ),
        migrations.AlterField(
            model_name="predict",
            name="smoking_status",
            field=models.CharField(
                choices=[
                    ("never smoked", "Never Smoked"),
                    ("formerly smoked", "Formerly Smoked"),
                    ("smokes", "Smokes"),
                    ("Unknown", "Unknown"),
                ],
                max_length=30,
            ),
        ),
        migrations.AlterField(
            model_name="predict",
            name="work_type",
            field=models.CharField(
                choices=[
                    ("children", "Children"),
                    ("Govt_job", "Government Job"),
                    ("Never_worked", "Never Worked"),
                    ("Private", "Private"),
                    ("Self-employed", "Self Employed"),
                ],
                max_length=15,
            ),
        ),
    ]
