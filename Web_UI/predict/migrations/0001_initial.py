# Generated by Django 4.2.4 on 2023-08-31 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Predict",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("gender", models.CharField(max_length=20)),
                ("age", models.IntegerField()),
                ("hypertension", models.BooleanField(default=False)),
                ("heart_disease", models.BooleanField(default=False)),
                ("ever_married", models.CharField(max_length=3)),
                ("work_type", models.CharField(max_length=15)),
                ("Residence_type", models.CharField(max_length=15)),
                ("avg_glucose_level", models.IntegerField()),
                ("bmi", models.DecimalField(decimal_places=2, max_digits=4)),
                ("smoking_status", models.CharField(max_length=10)),
                ("stroke", models.BooleanField(default=False)),
            ],
        ),
    ]