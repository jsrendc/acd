# Generated by Django 3.0.8 on 2021-07-09 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Arte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=500)),
                ('tipo', models.CharField(choices=[('B', 'Baile'), ('M', 'Música')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Baile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg', models.CharField(max_length=20)),
            ],
        ),
    ]
