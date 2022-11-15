# Generated by Django 4.1.2 on 2022-10-30 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("property", "0002_alter_property_street_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="company",
            field=models.CharField(max_length=100, verbose_name="company"),
        ),
        migrations.AlterField(
            model_name="project",
            name="dates",
            field=models.DateTimeField(blank=True, null=True, verbose_name="dates"),
        ),
        migrations.AlterField(
            model_name="project",
            name="location",
            field=models.CharField(max_length=100, verbose_name="location"),
        ),
        migrations.AlterField(
            model_name="project",
            name="size_project",
            field=models.SmallIntegerField(verbose_name="size_project"),
        ),
        migrations.AlterField(
            model_name="project",
            name="street",
            field=models.CharField(max_length=100, verbose_name="street"),
        ),
        migrations.AlterField(
            model_name="project",
            name="street_number",
            field=models.CharField(max_length=100, verbose_name="street_number"),
        ),
        migrations.AlterField(
            model_name="project",
            name="type_project",
            field=models.CharField(max_length=100, verbose_name="type_project"),
        ),
        migrations.AlterField(
            model_name="project",
            name="value",
            field=models.FloatField(verbose_name="value"),
        ),
        migrations.AlterField(
            model_name="property",
            name="floor",
            field=models.SmallIntegerField(verbose_name="floor"),
        ),
        migrations.AlterField(
            model_name="property",
            name="location",
            field=models.CharField(max_length=100, verbose_name="location"),
        ),
        migrations.AlterField(
            model_name="property",
            name="price",
            field=models.FloatField(verbose_name="price"),
        ),
        migrations.AlterField(
            model_name="property",
            name="property_type",
            field=models.CharField(max_length=100, verbose_name="property_type"),
        ),
        migrations.AlterField(
            model_name="property",
            name="room",
            field=models.SmallIntegerField(verbose_name="room"),
        ),
        migrations.AlterField(
            model_name="property",
            name="square_meter",
            field=models.SmallIntegerField(verbose_name="square_meter"),
        ),
        migrations.AlterField(
            model_name="property",
            name="street",
            field=models.CharField(max_length=100, verbose_name="street"),
        ),
        migrations.AlterField(
            model_name="property",
            name="street_number",
            field=models.SmallIntegerField(
                max_length=100, verbose_name="street_number"
            ),
        ),
    ]