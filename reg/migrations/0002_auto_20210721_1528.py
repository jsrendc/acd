# Generated by Django 3.0.8 on 2021-07-21 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='act',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='persona',
            name='tipo',
            field=models.CharField(default='', max_length=20),
        ),
    ]
