# Generated by Django 2.2.8 on 2021-11-16 13:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pyscada", "0086_auto_20211115_1612"),
    ]

    operations = [
        migrations.CreateModel(
            name="ExtendedCalculatedVariable",
            fields=[],
            options={
                "verbose_name": "Calculated Variable",
                "verbose_name_plural": "Calculated Variable",
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("pyscada.variable",),
        ),
        migrations.AlterField(
            model_name="periodicfield",
            name="start_from",
            field=models.DateTimeField(
                default=datetime.datetime(2021, 11, 16, 0, 0, tzinfo=datetime.timezone.utc),
                help_text="Calculate from this DateTime and then each period_factor*period",
            ),
        ),
        migrations.AlterField(
            model_name="periodicfield",
            name="type",
            field=models.SmallIntegerField(
                choices=[
                    (0, "min"),
                    (1, "max"),
                    (2, "total"),
                    (3, "difference"),
                    (4, "difference percent"),
                    (5, "delta"),
                    (6, "mean"),
                    (7, "first"),
                    (8, "last"),
                    (9, "count"),
                    (10, "count value"),
                    (11, "range"),
                    (12, "step"),
                    (13, "change count"),
                    (14, "distinct count"),
                ],
                help_text="Min: Minimum value of a field<br>Max: Maximum value of a field<br>Total: Sum of all values in a field<br>Difference: Difference between first and last value of a field<br>Difference percent: Percentage change between first and last value of a field<br>Delta: Cumulative change in value, only counts increments<br>Mean: Mean value of all values in a field<br>First: First value in a field<br>Last: Last value in a field<br>Count: Number of values in a field<br>Count value: Number of a value in a field<br>Range: Difference between maximum and minimum values of a field<br>Step: Minimal interval between values of a field<br>Change count: Number of times the field’s value changes<br>Distinct count: Number of unique values in a field",
            ),
        ),
    ]
