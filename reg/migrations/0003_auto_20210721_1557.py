# Generated by Django 3.0.8 on 2021-07-21 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0002_auto_20210721_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='act',
            field=models.CharField(max_length=100),
        ),
    ]