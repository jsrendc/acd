# Generated by Django 3.0.8 on 2021-07-21 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0003_auto_20210721_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='act',
            field=models.IntegerField(default=0),
        ),
    ]
